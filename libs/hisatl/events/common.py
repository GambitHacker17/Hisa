import abc 
import asyncio 
import warnings 

from ..import utils 
from ..tl import TLObject ,types 
from ..tl .custom .chatgetter import ChatGetter 

async def _into_id_set (client ,chats ):
    """"""
    if chats is None :
        return None 

    if not utils .is_list_like (chats ):
        chats =(chats ,)

    result =set ()
    for chat in chats :
        if isinstance (chat ,int ):
            if chat <0 :
                result .add (chat )
            else :
                result .update ({
                utils .get_peer_id (types .PeerUser (chat )),
                utils .get_peer_id (types .PeerChat (chat )),
                utils .get_peer_id (types .PeerChannel (chat )),
                })
        elif isinstance (chat ,TLObject )and chat .SUBCLASS_OF_ID ==0x2d45687 :

            result .add (utils .get_peer_id (chat ))
        else :
            chat =await client .get_input_entity (chat )
            if isinstance (chat ,types .InputPeerSelf ):
                chat =await client .get_me (input_peer =True )
            result .add (utils .get_peer_id (chat ))

    return result 

class EventBuilder (abc .ABC ):
    """"""
    def __init__ (self ,chats =None ,*,blacklist_chats =False ,func =None ):
        self .chats =chats 
        self .blacklist_chats =bool (blacklist_chats )
        self .resolved =False 
        self .func =func 
        self ._resolve_lock =None 

    @classmethod 
    @abc .abstractmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        """"""

    async def resolve (self ,client ):
        """"""
        if self .resolved :
            return 

        if not self ._resolve_lock :
            self ._resolve_lock =asyncio .Lock ()

        async with self ._resolve_lock :
            if not self .resolved :
                await self ._resolve (client )
                self .resolved =True 

    async def _resolve (self ,client ):
        self .chats =await _into_id_set (client ,self .chats )

    def filter (self ,event ):
        """"""
        if not self .resolved :
            return 

        if self .chats is not None :

            inside =event .chat_id in self .chats 
            if inside ==self .blacklist_chats :

                return 

        if not self .func :
            return True 

        return self .func (event )

class EventCommon (ChatGetter ,abc .ABC ):
    """"""
    _event_name ='Event'

    def __init__ (self ,chat_peer =None ,msg_id =None ,broadcast =None ):
        super ().__init__ (chat_peer ,broadcast =broadcast )
        self ._entities ={}
        self ._client =None 
        self ._message_id =msg_id 
        self .original_update =None 

    def _set_client (self ,client ):
        """"""
        self ._client =client 
        if self ._chat_peer :
            self ._chat ,self ._input_chat =utils ._get_entity_pair (
            self .chat_id ,self ._entities ,client ._entity_cache )
        else :
            self ._chat =self ._input_chat =None 

    @property 
    def client (self ):
        """"""
        return self ._client 

    def __str__ (self ):
        return TLObject .pretty_format (self .to_dict ())

    def stringify (self ):
        return TLObject .pretty_format (self .to_dict (),indent =0 )

    def to_dict (self ):
        d ={k :v for k ,v in self .__dict__ .items ()if k [0 ]!='_'}
        d ['_']=self ._event_name 
        return d 

def name_inner_event (cls ):
    """"""
    if hasattr (cls ,'Event'):
        cls .Event ._event_name ='{}.Event'.format (cls .__name__ )
    else :
        warnings .warn ('Class {} does not have a inner Event'.format (cls ))
    return cls 
