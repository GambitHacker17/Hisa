""""""
import asyncio 
import functools 
import inspect 

from .import events ,errors ,utils ,connection ,helpers 
from .client .account import _TakeoutClient 
from .client .telegramclient import TelegramClient 
from .tl import types ,functions ,custom 
from .tl .custom import (
Draft ,Dialog ,MessageButton ,Forward ,Button ,
Message ,InlineResult ,Conversation 
)
from .tl .custom .chatgetter import ChatGetter 
from .tl .custom .sendergetter import SenderGetter 

def _syncify_wrap (t ,method_name ):
    method =getattr (t ,method_name )

    @functools .wraps (method )
    def syncified (*args ,**kwargs ):
        coro =method (*args ,**kwargs )
        loop =helpers .get_running_loop ()
        if loop .is_running ():
            return coro 
        else :
            return loop .run_until_complete (coro )

    setattr (syncified ,'__tl.sync',method )
    setattr (t ,method_name ,syncified )

def syncify (*types ):
    """"""

    for t in types :
        for name in dir (t ):
            if not name .startswith ('_')or name =='__call__':
                if inspect .iscoroutinefunction (getattr (t ,name )):
                    _syncify_wrap (t ,name )

syncify (TelegramClient ,_TakeoutClient ,Draft ,Dialog ,MessageButton ,
ChatGetter ,SenderGetter ,Forward ,Message ,InlineResult ,Conversation )

_syncify_wrap (Conversation ,'_get_result')

__all__ =[
'TelegramClient','Button',
'types','functions','custom','errors',
'events','utils','connection'
]
