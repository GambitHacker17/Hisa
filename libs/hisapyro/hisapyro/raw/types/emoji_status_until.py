
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiStatusUntil (TLObject ):
    """"""

    __slots__ :List [str ]=["document_id","until"]

    ID =0xfa30a8c7 
    QUALNAME ="types.EmojiStatusUntil"

    def __init__ (self ,*,document_id :int ,until :int )->None :
        self .document_id =document_id 
        self .until =until 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiStatusUntil":

        document_id =Long .read (b )

        until =Int .read (b )

        return EmojiStatusUntil (document_id =document_id ,until =until )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .document_id ))

        b .write (Int (self .until ))

        return b .getvalue ()
