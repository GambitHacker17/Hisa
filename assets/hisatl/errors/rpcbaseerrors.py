from ..tl import functions 

_NESTS_QUERY =(
functions .InvokeAfterMsgRequest ,
functions .InvokeAfterMsgsRequest ,
functions .InitConnectionRequest ,
functions .InvokeWithLayerRequest ,
functions .InvokeWithoutUpdatesRequest ,
functions .InvokeWithMessagesRangeRequest ,
functions .InvokeWithTakeoutRequest ,
)

class RPCError (Exception ):
    """"""
    code =None 
    message =None 

    def __init__ (self ,request ,message ,code =None ):
        super ().__init__ ('RPCError {}: {}{}'.format (
        code or self .code ,message ,self ._fmt_request (request )))

        self .request =request 
        self .code =code 
        self .message =message 

    @staticmethod 
    def _fmt_request (request ):
        n =0 
        reason =''
        while isinstance (request ,_NESTS_QUERY ):
            n +=1 
            reason +=request .__class__ .__name__ +'('
            request =request .query 
        reason +=request .__class__ .__name__ +')'*n 

        return ' (caused by {})'.format (reason )

    def __reduce__ (self ):
        return type (self ),(self .request ,self .message ,self .code )

class InvalidDCError (RPCError ):
    """"""
    code =303 
    message ='ERROR_SEE_OTHER'

class BadRequestError (RPCError ):
    """"""
    code =400 
    message ='BAD_REQUEST'

class UnauthorizedError (RPCError ):
    """"""
    code =401 
    message ='UNAUTHORIZED'

class ForbiddenError (RPCError ):
    """"""
    code =403 
    message ='FORBIDDEN'

class NotFoundError (RPCError ):
    """"""
    code =404 
    message ='NOT_FOUND'

class AuthKeyError (RPCError ):
    """"""
    code =406 
    message ='AUTH_KEY'

class FloodError (RPCError ):
    """"""
    code =420 
    message ='FLOOD'

class ServerError (RPCError ):
    """"""
    code =500 
    message ='INTERNAL'

class TimedOutError (RPCError ):
    """"""
    code =503 
    message ='Timeout'

BotTimeout =TimedOutError 

base_errors ={x .code :x for x in (
InvalidDCError ,BadRequestError ,UnauthorizedError ,ForbiddenError ,
NotFoundError ,AuthKeyError ,FloodError ,ServerError ,TimedOutError 
)}
