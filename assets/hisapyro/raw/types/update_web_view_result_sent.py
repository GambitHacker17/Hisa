
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateWebViewResultSent (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id"]

    ID =0x1592b79d 
    QUALNAME ="types.UpdateWebViewResultSent"

    def __init__ (self ,*,query_id :int )->None :
        self .query_id =query_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateWebViewResultSent":

        query_id =Long .read (b )

        return UpdateWebViewResultSent (query_id =query_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .query_id ))

        return b .getvalue ()
