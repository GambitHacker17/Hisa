
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UploadMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","media"]

    ID =0x519bc2b1 
    QUALNAME ="functions.messages.UploadMedia"

    def __init__ (self ,*,peer :"raw.base.InputPeer",media :"raw.base.InputMedia")->None :
        self .peer =peer 
        self .media =media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UploadMedia":

        peer =TLObject .read (b )

        media =TLObject .read (b )

        return UploadMedia (peer =peer ,media =media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .media .write ())

        return b .getvalue ()
