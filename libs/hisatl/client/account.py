import functools 
import inspect 
import typing 

from .users import _NOT_A_REQUEST 
from ..import helpers ,utils 
from ..tl import functions ,TLRequest 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

class _TakeoutClient :
    """"""
    __PROXY_INTERFACE =('__enter__','__exit__','__aenter__','__aexit__')

    def __init__ (self ,finalize ,client ,request ):

        self .__finalize =finalize 
        self .__client =client 
        self .__request =request 
        self .__success =None 

    @property 
    def success (self ):
        return self .__success 

    @success .setter 
    def success (self ,value ):
        self .__success =value 

    async def __aenter__ (self ):

        client =self .__client 
        if client .session .takeout_id is None :
            client .session .takeout_id =(await client (self .__request )).id 
        elif self .__request is not None :
            raise ValueError ("Can't send a takeout request while another "
            "takeout for the current session still not been finished yet.")
        return self 

    async def __aexit__ (self ,exc_type ,exc_value ,traceback ):
        if self .__success is None and self .__finalize :
            self .__success =exc_type is None 

        if self .__success is not None :
            result =await self (functions .account .FinishTakeoutSessionRequest (
            self .__success ))
            if not result :
                raise ValueError ("Failed to finish the takeout.")
            self .session .takeout_id =None 

    __enter__ =helpers ._sync_enter 
    __exit__ =helpers ._sync_exit 

    async def __call__ (self ,request ,ordered =False ):
        takeout_id =self .__client .session .takeout_id 
        if takeout_id is None :
            raise ValueError ('Takeout mode has not been initialized '
            '(are you calling outside of "with"?)')

        single =not utils .is_list_like (request )
        requests =((request ,)if single else request )
        wrapped =[]
        for r in requests :
            if not isinstance (r ,TLRequest ):
                raise _NOT_A_REQUEST ()
            await r .resolve (self ,utils )
            wrapped .append (functions .InvokeWithTakeoutRequest (takeout_id ,r ))

        return await self .__client (
        wrapped [0 ]if single else wrapped ,ordered =ordered )

    def __getattribute__ (self ,name ):

        if name .startswith ('__')and name not in type (self ).__PROXY_INTERFACE :
            raise AttributeError 

        return super ().__getattribute__ (name )

    def __getattr__ (self ,name ):
        value =getattr (self .__client ,name )
        if inspect .ismethod (value ):

            return functools .partial (
            getattr (self .__client .__class__ ,name ),self )

        return value 

    def __setattr__ (self ,name ,value ):
        if name .startswith ('_{}__'.format (type (self ).__name__ .lstrip ('_'))):

            return super ().__setattr__ (name ,value )
        return setattr (self .__client ,name ,value )

class AccountMethods :
    def takeout (
    self :'TelegramClient',
    finalize :bool =True ,
    *,
    contacts :bool =None ,
    users :bool =None ,
    chats :bool =None ,
    megagroups :bool =None ,
    channels :bool =None ,
    files :bool =None ,
    max_file_size :bool =None )->'TelegramClient':
        """"""
        request_kwargs =dict (
        contacts =contacts ,
        message_users =users ,
        message_chats =chats ,
        message_megagroups =megagroups ,
        message_channels =channels ,
        files =files ,
        file_max_size =max_file_size 
        )
        arg_specified =(arg is not None for arg in request_kwargs .values ())

        if self .session .takeout_id is None or any (arg_specified ):
            request =functions .account .InitTakeoutSessionRequest (
            **request_kwargs )
        else :
            request =None 

        return _TakeoutClient (finalize ,self ,request )

    async def end_takeout (self :'TelegramClient',success :bool )->bool :
        """"""
        try :
            async with _TakeoutClient (True ,self ,None )as takeout :
                takeout .success =success 
        except ValueError :
            return False 
        return True 
