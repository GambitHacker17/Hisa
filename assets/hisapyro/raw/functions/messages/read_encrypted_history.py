
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReadEncryptedHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","max_date"]

    ID =0x7f4b690a 
    QUALNAME ="functions.messages.ReadEncryptedHistory"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat",max_date :int )->None :
        self .peer =peer 
        self .max_date =max_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReadEncryptedHistory":

        peer =TLObject .read (b )

        max_date =Int .read (b )

        return ReadEncryptedHistory (peer =peer ,max_date =max_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .max_date ))

        return b .getvalue ()
