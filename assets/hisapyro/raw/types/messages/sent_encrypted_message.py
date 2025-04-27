
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentEncryptedMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["date"]

    ID =0x560f8935 
    QUALNAME ="types.messages.SentEncryptedMessage"

    def __init__ (self ,*,date :int )->None :
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentEncryptedMessage":

        date =Int .read (b )

        return SentEncryptedMessage (date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .date ))

        return b .getvalue ()
