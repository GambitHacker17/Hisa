
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DialogFilterSuggested (TLObject ):
    """"""

    __slots__ :List [str ]=["filter","description"]

    ID =0x77744d4a 
    QUALNAME ="types.DialogFilterSuggested"

    def __init__ (self ,*,filter :"raw.base.DialogFilter",description :str )->None :
        self .filter =filter 
        self .description =description 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DialogFilterSuggested":

        filter =TLObject .read (b )

        description =String .read (b )

        return DialogFilterSuggested (filter =filter ,description =description )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .filter .write ())

        b .write (String (self .description ))

        return b .getvalue ()
