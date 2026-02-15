""""""
from .tlmessage import TLMessage 
from .gzippacked import GzipPacked 
from .messagecontainer import MessageContainer 
from .rpcresult import RpcResult 

core_objects ={x .CONSTRUCTOR_ID :x for x in (
GzipPacked ,MessageContainer ,RpcResult 
)}
