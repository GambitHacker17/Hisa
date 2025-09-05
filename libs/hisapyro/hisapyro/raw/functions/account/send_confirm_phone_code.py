
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendConfirmPhoneCode (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","settings"]

    ID =0x1b3faa88 
    QUALNAME ="functions.account.SendConfirmPhoneCode"

    def __init__ (self ,*,hash :str ,settings :"raw.base.CodeSettings")->None :
        self .hash =hash 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendConfirmPhoneCode":

        hash =String .read (b )

        settings =TLObject .read (b )

        return SendConfirmPhoneCode (hash =hash ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .hash ))

        b .write (self .settings .write ())

        return b .getvalue ()
