
from ..rpc_error import RPCError 

class ServiceUnavailable (RPCError ):
    """"""
    CODE =503 
    """"""
    NAME =__doc__ 

class ApiCallError (ServiceUnavailable ):
    """"""
    ID ="ApiCallError"
    """"""
    MESSAGE =__doc__ 

class Timeout (ServiceUnavailable ):
    """"""
    ID ="Timeout"
    """"""
    MESSAGE =__doc__ 

