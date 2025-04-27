
import hisapyro 
from hisapyro .handlers import DisconnectHandler 
from hisapyro .handlers .handler import Handler 

class RemoveHandler :
    def remove_handler (
    self :"hisapyro.Client",
    handler :"Handler",
    group :int =0 
    ):
        """"""
        if isinstance (handler ,DisconnectHandler ):
            self .disconnect_handler =None 
        else :
            self .dispatcher .remove_handler (handler ,group )
