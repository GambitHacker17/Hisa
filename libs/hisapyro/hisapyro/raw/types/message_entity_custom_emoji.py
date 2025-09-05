
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityCustomEmoji (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length","document_id"]

    ID =0xc8cf05f8 
    QUALNAME ="types.MessageEntityCustomEmoji"

    def __init__ (self ,*,offset :int ,length :int ,document_id :int )->None :
        self .offset =offset 
        self .length =length 
        self .document_id =document_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityCustomEmoji":

        offset =Int .read (b )

        length =Int .read (b )

        document_id =Long .read (b )

        return MessageEntityCustomEmoji (offset =offset ,length =length ,document_id =document_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        b .write (Long (self .document_id ))

        return b .getvalue ()
