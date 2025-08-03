
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ShippingOption (TLObject ):
    """"""

    __slots__ :List [str ]=["id","title","prices"]

    ID =0xb6213cdf 
    QUALNAME ="types.ShippingOption"

    def __init__ (self ,*,id :str ,title :str ,prices :List ["raw.base.LabeledPrice"])->None :
        self .id =id 
        self .title =title 
        self .prices =prices 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ShippingOption":

        id =String .read (b )

        title =String .read (b )

        prices =TLObject .read (b )

        return ShippingOption (id =id ,title =title ,prices =prices )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .id ))

        b .write (String (self .title ))

        b .write (Vector (self .prices ))

        return b .getvalue ()
