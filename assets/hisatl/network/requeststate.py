import asyncio 

class RequestState :
    """"""
    __slots__ =('container_id','msg_id','request','data','future','after')

    def __init__ (self ,request ,after =None ):
        self .container_id =None 
        self .msg_id =None 
        self .request =request 
        self .data =bytes (request )
        self .future =asyncio .Future ()
        self .after =after 
