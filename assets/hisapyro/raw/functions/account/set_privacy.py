
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetPrivacy (TLObject ):
    """"""

    __slots__ :List [str ]=["key","rules"]

    ID =0xc9f81ce8 
    QUALNAME ="functions.account.SetPrivacy"

    def __init__ (self ,*,key :"raw.base.InputPrivacyKey",rules :List ["raw.base.InputPrivacyRule"])->None :
        self .key =key 
        self .rules =rules 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetPrivacy":

        key =TLObject .read (b )

        rules =TLObject .read (b )

        return SetPrivacy (key =key ,rules =rules )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .key .write ())

        b .write (Vector (self .rules ))

        return b .getvalue ()
