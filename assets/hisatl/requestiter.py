import abc 
import asyncio 
import time 

from .import helpers 

class RequestIter (abc .ABC ):
    """"""
    def __init__ (self ,client ,limit ,*,reverse =False ,wait_time =None ,**kwargs ):
        self .client =client 
        self .reverse =reverse 
        self .wait_time =wait_time 
        self .kwargs =kwargs 
        self .limit =max (float ('inf')if limit is None else limit ,0 )
        self .left =self .limit 
        self .buffer =None 
        self .index =0 
        self .total =None 
        self .last_load =0 

    async def _init (self ,**kwargs ):
        """"""

    async def __anext__ (self ):
        if self .buffer is None :
            self .buffer =[]
            if await self ._init (**self .kwargs ):
                self .left =len (self .buffer )

        if self .left <=0 :
            raise StopAsyncIteration 

        if self .index ==len (self .buffer ):

            if self .wait_time :
                await asyncio .sleep (
                self .wait_time -(time .time ()-self .last_load )
                )
                self .last_load =time .time ()

            self .index =0 
            self .buffer =[]
            if await self ._load_next_chunk ():
                self .left =len (self .buffer )

        if not self .buffer :
            raise StopAsyncIteration 

        result =self .buffer [self .index ]
        self .left -=1 
        self .index +=1 
        return result 

    def __next__ (self ):
        try :
            return self .client .loop .run_until_complete (self .__anext__ ())
        except StopAsyncIteration :
            raise StopIteration 

    def __aiter__ (self ):
        self .buffer =None 
        self .index =0 
        self .last_load =0 
        self .left =self .limit 
        return self 

    def __iter__ (self ):
        if self .client .loop .is_running ():
            raise RuntimeError (
            'You must use "async for" if the event loop '
            'is running (i.e. you are inside an "async def")'
            )

        return self .__aiter__ ()

    async def collect (self ):
        """"""
        result =helpers .TotalList ()
        async for message in self :
            result .append (message )

        result .total =self .total 
        return result 

    @abc .abstractmethod 
    async def _load_next_chunk (self ):
        """"""
        raise NotImplementedError 

    def __reversed__ (self ):
        self .reverse =not self .reverse 
        return self 
