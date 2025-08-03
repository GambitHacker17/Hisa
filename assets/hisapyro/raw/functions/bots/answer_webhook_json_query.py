
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AnswerWebhookJSONQuery (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","data"]

    ID =0xe6213f4d 
    QUALNAME ="functions.bots.AnswerWebhookJSONQuery"

    def __init__ (self ,*,query_id :int ,data :"raw.base.DataJSON")->None :
        self .query_id =query_id 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AnswerWebhookJSONQuery":

        query_id =Long .read (b )

        data =TLObject .read (b )

        return AnswerWebhookJSONQuery (query_id =query_id ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .query_id ))

        b .write (self .data .write ())

        return b .getvalue ()
