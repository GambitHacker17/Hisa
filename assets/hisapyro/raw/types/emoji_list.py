
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiList (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","document_id"]

    ID =0x7a1e11d1 
    QUALNAME ="types.EmojiList"

    def __init__ (self ,*,hash :int ,document_id :List [int ])->None :
        self .hash =hash 
        self .document_id =document_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiList":

        hash =Long .read (b )

        document_id =TLObject .read (b ,Long )

        return EmojiList (hash =hash ,document_id =document_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .document_id ,Long ))

        return b .getvalue ()
