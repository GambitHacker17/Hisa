import asyncio 
import functools 
import inspect 
import itertools 
import time 

from .chatgetter import ChatGetter 
from ...import helpers ,utils ,errors 

_EDIT_COLLISION_DELTA =0.001 

def _checks_cancelled (f ):
    @functools .wraps (f )
    def wrapper (self ,*args ,**kwargs ):
        if self ._cancelled :
            raise asyncio .CancelledError ('The conversation was cancelled before')

        return f (self ,*args ,**kwargs )
    return wrapper 

class Conversation (ChatGetter ):
    """"""
    _id_counter =0 
    _custom_counter =0 

    def __init__ (self ,client ,input_chat ,
    *,timeout ,total_timeout ,max_messages ,
    exclusive ,replies_are_responses ):

        ChatGetter .__init__ (self ,input_chat =input_chat )

        self ._id =Conversation ._id_counter 
        Conversation ._id_counter +=1 

        self ._client =client 
        self ._timeout =timeout 
        self ._total_timeout =total_timeout 
        self ._total_due =None 

        self ._outgoing =set ()
        self ._last_outgoing =0 
        self ._incoming =[]
        self ._last_incoming =0 
        self ._max_incoming =max_messages 
        self ._last_read =None 
        self ._custom ={}

        self ._pending_responses ={}
        self ._pending_replies ={}
        self ._pending_edits ={}
        self ._pending_reads ={}

        self ._exclusive =exclusive 
        self ._cancelled =False 

        self ._response_indices ={}
        if replies_are_responses :
            self ._reply_indices =self ._response_indices 
        else :
            self ._reply_indices ={}

        self ._edit_dates ={}

    @_checks_cancelled 
    async def send_message (self ,*args ,**kwargs ):
        """"""
        sent =await self ._client .send_message (
        self ._input_chat ,*args ,**kwargs )

        ms =sent if isinstance (sent ,list )else (sent ,)
        self ._outgoing .update (m .id for m in ms )
        self ._last_outgoing =ms [-1 ].id 
        return sent 

    @_checks_cancelled 
    async def send_file (self ,*args ,**kwargs ):
        """"""
        sent =await self ._client .send_file (
        self ._input_chat ,*args ,**kwargs )

        ms =sent if isinstance (sent ,list )else (sent ,)
        self ._outgoing .update (m .id for m in ms )
        self ._last_outgoing =ms [-1 ].id 
        return sent 

    @_checks_cancelled 
    def mark_read (self ,message =None ):
        """"""
        if message is None :
            if self ._incoming :
                message =self ._incoming [-1 ].id 
            else :
                message =0 
        elif not isinstance (message ,int ):
            message =message .id 

        return self ._client .send_read_acknowledge (
        self ._input_chat ,max_id =message )

    def get_response (self ,message =None ,*,timeout =None ):
        """"""
        return self ._get_message (
        message ,self ._response_indices ,self ._pending_responses ,timeout ,
        lambda x ,y :True 
        )

    def get_reply (self ,message =None ,*,timeout =None ):
        """"""
        return self ._get_message (
        message ,self ._reply_indices ,self ._pending_replies ,timeout ,
        lambda x ,y :x .reply_to and x .reply_to .reply_to_msg_id ==y 
        )

    def _get_message (
    self ,target_message ,indices ,pending ,timeout ,condition ):
        """"""
        start_time =time .time ()
        target_id =self ._get_message_id (target_message )

        if target_id not in indices :
            for i ,incoming in enumerate (self ._incoming ):
                if incoming .id >target_id :
                    indices [target_id ]=i 
                    break 
            else :
                indices [target_id ]=len (self ._incoming )

        future =self ._client .loop .create_future ()

        last_idx =indices [target_id ]
        if last_idx <len (self ._incoming ):
            incoming =self ._incoming [last_idx ]
            if condition (incoming ,target_id ):
                indices [target_id ]+=1 
                future .set_result (incoming )
                return future 

        pending [target_id ]=future 
        return self ._get_result (future ,start_time ,timeout ,pending ,target_id )

    def get_edit (self ,message =None ,*,timeout =None ):
        """"""
        start_time =time .time ()
        target_id =self ._get_message_id (message )

        target_date =self ._edit_dates .get (target_id ,0 )
        earliest_edit =min (
        (x for x in self ._incoming 
        if x .edit_date 
        and x .id >target_id 
        and x .edit_date .timestamp ()>target_date 
        ),
        key =lambda x :x .edit_date .timestamp (),
        default =None 
        )

        future =self ._client .loop .create_future ()
        if earliest_edit and earliest_edit .edit_date .timestamp ()>target_date :
            self ._edit_dates [target_id ]=earliest_edit .edit_date .timestamp ()
            future .set_result (earliest_edit )
            return future 

        self ._pending_edits [target_id ]=future 
        return self ._get_result (future ,start_time ,timeout ,self ._pending_edits ,target_id )

    def wait_read (self ,message =None ,*,timeout =None ):
        """"""
        start_time =time .time ()
        future =self ._client .loop .create_future ()
        target_id =self ._get_message_id (message )

        if self ._last_read is None :
            self ._last_read =target_id -1 

        if self ._last_read >=target_id :
            return 

        self ._pending_reads [target_id ]=future 
        return self ._get_result (future ,start_time ,timeout ,self ._pending_reads ,target_id )

    async def wait_event (self ,event ,*,timeout =None ):
        """"""
        start_time =time .time ()
        if isinstance (event ,type ):
            event =event ()

        await event .resolve (self ._client )

        counter =Conversation ._custom_counter 
        Conversation ._custom_counter +=1 

        future =self ._client .loop .create_future ()
        self ._custom [counter ]=(event ,future )
        try :
            return await self ._get_result (future ,start_time ,timeout ,self ._custom ,counter )
        finally :

            self ._custom .pop (counter ,None )

    async def _check_custom (self ,built ):
        for key ,(ev ,fut )in list (self ._custom .items ()):
            ev_type =type (ev )
            inst =built [ev_type ]

            if inst :
                filter =ev .filter (inst )
                if inspect .isawaitable (filter ):
                    filter =await filter 

                if filter :
                    fut .set_result (inst )
                    del self ._custom [key ]

    def _on_new_message (self ,response ):
        response =response .message 
        if response .chat_id !=self .chat_id or response .out :
            return 

        if len (self ._incoming )==self ._max_incoming :
            self ._cancel_all (ValueError ('Too many incoming messages'))
            return 

        self ._incoming .append (response )

        for msg_id ,future in list (self ._pending_responses .items ()):
            self ._response_indices [msg_id ]=len (self ._incoming )
            future .set_result (response )
            del self ._pending_responses [msg_id ]

        for msg_id ,future in list (self ._pending_replies .items ()):
            if response .reply_to and msg_id ==response .reply_to .reply_to_msg_id :
                self ._reply_indices [msg_id ]=len (self ._incoming )
                future .set_result (response )
                del self ._pending_replies [msg_id ]

    def _on_edit (self ,message ):
        message =message .message 
        if message .chat_id !=self .chat_id or message .out :
            return 

        for i ,m in enumerate (self ._incoming ):
            if m .id ==message .id :
                self ._incoming [i ]=message 
                break 

        for msg_id ,future in list (self ._pending_edits .items ()):
            if msg_id <message .id :
                edit_ts =message .edit_date .timestamp ()

                if edit_ts <=self ._edit_dates .get (msg_id ,0 ):
                    self ._edit_dates [msg_id ]+=_EDIT_COLLISION_DELTA 
                else :
                    self ._edit_dates [msg_id ]=message .edit_date .timestamp ()

                future .set_result (message )
                del self ._pending_edits [msg_id ]

    def _on_read (self ,event ):
        if event .chat_id !=self .chat_id or event .inbox :
            return 

        self ._last_read =event .max_id 

        for msg_id ,pending in list (self ._pending_reads .items ()):
            if msg_id >=self ._last_read :
                pending .set_result (True )
                del self ._pending_reads [msg_id ]

    def _get_message_id (self ,message ):
        if message is not None :
            return message if isinstance (message ,int )else message .id 
        elif self ._last_outgoing :
            return self ._last_outgoing 
        else :
            raise ValueError ('No message was sent previously')

    @_checks_cancelled 
    def _get_result (self ,future ,start_time ,timeout ,pending ,target_id ):
        due =self ._total_due 
        if timeout is None :
            timeout =self ._timeout 

        if timeout is not None :
            due =min (due ,start_time +timeout )

        return asyncio .wait_for (
        future ,
        timeout =None if due ==float ('inf')else due -time .time ()
        )

    def _cancel_all (self ,exception =None ):
        self ._cancelled =True 
        for pending in itertools .chain (
        self ._pending_responses .values (),
        self ._pending_replies .values (),
        self ._pending_edits .values ()):
            if exception :
                pending .set_exception (exception )
            else :
                pending .cancel ()

        for _ ,fut in self ._custom .values ():
            if exception :
                fut .set_exception (exception )
            else :
                fut .cancel ()

    async def __aenter__ (self ):
        self ._input_chat =await self ._client .get_input_entity (self ._input_chat )

        self ._chat_peer =utils .get_peer (self ._input_chat )

        chat_id =utils .get_peer_id (self ._chat_peer )
        conv_set =self ._client ._conversations [chat_id ]
        if self ._exclusive and conv_set :
            raise errors .AlreadyInConversationError ()

        conv_set .add (self )
        self ._cancelled =False 

        self ._last_outgoing =0 
        self ._last_incoming =0 
        for d in (
        self ._outgoing ,self ._incoming ,
        self ._pending_responses ,self ._pending_replies ,
        self ._pending_edits ,self ._response_indices ,
        self ._reply_indices ,self ._edit_dates ,self ._custom ):
            d .clear ()

        if self ._total_timeout :
            self ._total_due =time .time ()+self ._total_timeout 
        else :
            self ._total_due =float ('inf')

        return self 

    def cancel (self ):
        """"""
        self ._cancel_all ()

    async def cancel_all (self ):
        """"""
        chat_id =await self ._client .get_peer_id (self ._input_chat )
        for conv in self ._client ._conversations [chat_id ]:
            conv .cancel ()

    async def __aexit__ (self ,exc_type ,exc_val ,exc_tb ):
        chat_id =utils .get_peer_id (self ._chat_peer )
        conv_set =self ._client ._conversations [chat_id ]
        conv_set .discard (self )
        if not conv_set :
            del self ._client ._conversations [chat_id ]

        self ._cancel_all ()

    __enter__ =helpers ._sync_enter 
    __exit__ =helpers ._sync_exit 
