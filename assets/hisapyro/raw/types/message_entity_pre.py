
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityPre (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length","language"]

    ID =0x73924be0 
    QUALNAME ="types.MessageEntityPre"

    def __init__ (self ,*,offset :int ,length :int ,language :str )->None :
        self .offset =offset 
        self .length =length 
        self .language =language 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityPre":

        offset =Int .read (b )

        length =Int .read (b )

        language =String .read (b )

        return MessageEntityPre (offset =offset ,length =length ,language =language )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        b .write (String (self .language ))

        return b .getvalue ()
