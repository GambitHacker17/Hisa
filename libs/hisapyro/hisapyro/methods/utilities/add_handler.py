
import hisapyro 
from hisapyro .handlers import DisconnectHandler 
from hisapyro .handlers .handler import Handler 

class AddHandler :
    def add_handler (
    self :"hisapyro.Client",
    handler :"Handler",
    group :int =0 
    ):
        """"""
        if isinstance (handler ,DisconnectHandler ):
            self .disconnect_handler =handler .callback 
        else :
            self .dispatcher .add_handler (handler ,group )

        return handler ,group 
