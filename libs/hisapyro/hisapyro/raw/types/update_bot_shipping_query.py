
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotShippingQuery (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","user_id","payload","shipping_address"]

    ID =0xb5aefd7d 
    QUALNAME ="types.UpdateBotShippingQuery"

    def __init__ (self ,*,query_id :int ,user_id :int ,payload :bytes ,shipping_address :"raw.base.PostAddress")->None :
        self .query_id =query_id 
        self .user_id =user_id 
        self .payload =payload 
        self .shipping_address =shipping_address 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotShippingQuery":

        query_id =Long .read (b )

        user_id =Long .read (b )

        payload =Bytes .read (b )

        shipping_address =TLObject .read (b )

        return UpdateBotShippingQuery (query_id =query_id ,user_id =user_id ,payload =payload ,shipping_address =shipping_address )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .query_id ))

        b .write (Long (self .user_id ))

        b .write (Bytes (self .payload ))

        b .write (self .shipping_address .write ())

        return b .getvalue ()
