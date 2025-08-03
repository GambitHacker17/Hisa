
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotWebhookJSONQuery (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","data","timeout"]

    ID =0x9b9240a6 
    QUALNAME ="types.UpdateBotWebhookJSONQuery"

    def __init__ (self ,*,query_id :int ,data :"raw.base.DataJSON",timeout :int )->None :
        self .query_id =query_id 
        self .data =data 
        self .timeout =timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotWebhookJSONQuery":

        query_id =Long .read (b )

        data =TLObject .read (b )

        timeout =Int .read (b )

        return UpdateBotWebhookJSONQuery (query_id =query_id ,data =data ,timeout =timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .query_id ))

        b .write (self .data .write ())

        b .write (Int (self .timeout ))

        return b .getvalue ()
