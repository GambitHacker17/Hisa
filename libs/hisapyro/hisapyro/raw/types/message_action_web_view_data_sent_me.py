
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionWebViewDataSentMe (TLObject ):
    """"""

    __slots__ :List [str ]=["text","data"]

    ID =0x47dd8079 
    QUALNAME ="types.MessageActionWebViewDataSentMe"

    def __init__ (self ,*,text :str ,data :str )->None :
        self .text =text 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionWebViewDataSentMe":

        text =String .read (b )

        data =String .read (b )

        return MessageActionWebViewDataSentMe (text =text ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (String (self .data ))

        return b .getvalue ()
