
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReportEncryptedSpam (TLObject ):
    """"""

    __slots__ :List [str ]=["peer"]

    ID =0x4b0c8c0f 
    QUALNAME ="functions.messages.ReportEncryptedSpam"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat")->None :
        self .peer =peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReportEncryptedSpam":

        peer =TLObject .read (b )

        return ReportEncryptedSpam (peer =peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        return b .getvalue ()
