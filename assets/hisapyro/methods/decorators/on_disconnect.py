
from typing import Callable 

import hisapyro 

class OnDisconnect :
    def on_disconnect (self =None )->Callable :
        """"""

        def decorator (func :Callable )->Callable :
            if isinstance (self ,hisapyro .Client ):
                self .add_handler (hisapyro .handlers .DisconnectHandler (func ))
            else :
                if not hasattr (func ,"handlers"):
                    func .handlers =[]

                func .handlers .append ((hisapyro .handlers .DisconnectHandler (func ),0 ))

            return func 

        return decorator 
