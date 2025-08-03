
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePrivacy (TLObject ):
    """"""

    __slots__ :List [str ]=["key","rules"]

    ID =0xee3b272a 
    QUALNAME ="types.UpdatePrivacy"

    def __init__ (self ,*,key :"raw.base.PrivacyKey",rules :List ["raw.base.PrivacyRule"])->None :
        self .key =key 
        self .rules =rules 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePrivacy":

        key =TLObject .read (b )

        rules =TLObject .read (b )

        return UpdatePrivacy (key =key ,rules =rules )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .key .write ())

        b .write (Vector (self .rules ))

        return b .getvalue ()
