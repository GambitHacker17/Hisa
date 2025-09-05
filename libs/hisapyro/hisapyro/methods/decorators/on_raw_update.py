
from typing import Callable 

import hisapyro 

class OnRawUpdate :
    def on_raw_update (
    self =None ,
    group :int =0 
    )->Callable :
        """"""

        def decorator (func :Callable )->Callable :
            if isinstance (self ,hisapyro .Client ):
                self .add_handler (hisapyro .handlers .RawUpdateHandler (func ),group )
            else :
                if not hasattr (func ,"handlers"):
                    func .handlers =[]

                func .handlers .append (
                (
                hisapyro .handlers .RawUpdateHandler (func ),
                group 
                )
                )

            return func 

        return decorator 
