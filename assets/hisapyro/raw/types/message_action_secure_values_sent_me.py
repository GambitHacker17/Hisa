
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionSecureValuesSentMe (TLObject ):
    """"""

    __slots__ :List [str ]=["values","credentials"]

    ID =0x1b287353 
    QUALNAME ="types.MessageActionSecureValuesSentMe"

    def __init__ (self ,*,values :List ["raw.base.SecureValue"],credentials :"raw.base.SecureCredentialsEncrypted")->None :
        self .values =values 
        self .credentials =credentials 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionSecureValuesSentMe":

        values =TLObject .read (b )

        credentials =TLObject .read (b )

        return MessageActionSecureValuesSentMe (values =values ,credentials =credentials )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .values ))

        b .write (self .credentials .write ())

        return b .getvalue ()
