
from typing import Callable 

import hisapyro 
from hisapyro .filters import Filter 

class OnCallbackQuery :
    def on_callback_query (
    self =None ,
    filters =None ,
    group :int =0 
    )->Callable :
        """"""

        def decorator (func :Callable )->Callable :
            if isinstance (self ,hisapyro .Client ):
                self .add_handler (hisapyro .handlers .CallbackQueryHandler (func ,filters ),group )
            elif isinstance (self ,Filter )or self is None :
                if not hasattr (func ,"handlers"):
                    func .handlers =[]

                func .handlers .append (
                (
                hisapyro .handlers .CallbackQueryHandler (func ,self ),
                group if filters is None else filters 
                )
                )

            return func 

        return decorator 
