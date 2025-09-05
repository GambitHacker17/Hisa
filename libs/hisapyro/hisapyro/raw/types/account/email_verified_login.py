
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmailVerifiedLogin (TLObject ):
    """"""

    __slots__ :List [str ]=["email","sent_code"]

    ID =0xe1bb0d61 
    QUALNAME ="types.account.EmailVerifiedLogin"

    def __init__ (self ,*,email :str ,sent_code :"raw.base.auth.SentCode")->None :
        self .email =email 
        self .sent_code =sent_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmailVerifiedLogin":

        email =String .read (b )

        sent_code =TLObject .read (b )

        return EmailVerifiedLogin (email =email ,sent_code =sent_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .email ))

        b .write (self .sent_code .write ())

        return b .getvalue ()
