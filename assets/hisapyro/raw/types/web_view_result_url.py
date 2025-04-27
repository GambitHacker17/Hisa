
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebViewResultUrl (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","url"]

    ID =0xc14557c 
    QUALNAME ="types.WebViewResultUrl"

    def __init__ (self ,*,query_id :int ,url :str )->None :
        self .query_id =query_id 
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebViewResultUrl":

        query_id =Long .read (b )

        url =String .read (b )

        return WebViewResultUrl (query_id =query_id ,url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .query_id ))

        b .write (String (self .url ))

        return b .getvalue ()
