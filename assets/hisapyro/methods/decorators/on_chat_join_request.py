
from typing import Callable 

import hisapyro 
from hisapyro .filters import Filter 

class OnChatJoinRequest :
    def on_chat_join_request (
    self =None ,
    filters =None ,
    group :int =0 
    )->Callable :
        """"""

        def decorator (func :Callable )->Callable :
            if isinstance (self ,hisapyro .Client ):
                self .add_handler (hisapyro .handlers .ChatJoinRequestHandler (func ,filters ),group )
            elif isinstance (self ,Filter )or self is None :
                if not hasattr (func ,"handlers"):
                    func .handlers =[]

                func .handlers .append (
                (
                hisapyro .handlers .ChatJoinRequestHandler (func ,self ),
                group if filters is None else filters 
                )
                )

            return func 

        return decorator 
