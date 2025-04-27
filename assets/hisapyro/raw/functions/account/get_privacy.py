
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetPrivacy (TLObject ):
    """"""

    __slots__ :List [str ]=["key"]

    ID =0xdadbc950 
    QUALNAME ="functions.account.GetPrivacy"

    def __init__ (self ,*,key :"raw.base.InputPrivacyKey")->None :
        self .key =key 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetPrivacy":

        key =TLObject .read (b )

        return GetPrivacy (key =key )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .key .write ())

        return b .getvalue ()
