
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportLoginToken (TLObject ):
    """"""

    __slots__ :List [str ]=["api_id","api_hash","except_ids"]

    ID =0xb7e085fe 
    QUALNAME ="functions.auth.ExportLoginToken"

    def __init__ (self ,*,api_id :int ,api_hash :str ,except_ids :List [int ])->None :
        self .api_id =api_id 
        self .api_hash =api_hash 
        self .except_ids =except_ids 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportLoginToken":

        api_id =Int .read (b )

        api_hash =String .read (b )

        except_ids =TLObject .read (b ,Long )

        return ExportLoginToken (api_id =api_id ,api_hash =api_hash ,except_ids =except_ids )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .api_id ))

        b .write (String (self .api_hash ))

        b .write (Vector (self .except_ids ,Long ))

        return b .getvalue ()
