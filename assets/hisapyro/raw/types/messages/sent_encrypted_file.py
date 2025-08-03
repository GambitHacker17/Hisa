
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentEncryptedFile (TLObject ):
    """"""

    __slots__ :List [str ]=["date","file"]

    ID =0x9493ff32 
    QUALNAME ="types.messages.SentEncryptedFile"

    def __init__ (self ,*,date :int ,file :"raw.base.EncryptedFile")->None :
        self .date =date 
        self .file =file 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentEncryptedFile":

        date =Int .read (b )

        file =TLObject .read (b )

        return SentEncryptedFile (date =date ,file =file )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .date ))

        b .write (self .file .write ())

        return b .getvalue ()
