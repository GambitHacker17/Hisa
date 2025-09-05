
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerKeyword (TLObject ):
    """"""

    __slots__ :List [str ]=["document_id","keyword"]

    ID =0xfcfeb29c 
    QUALNAME ="types.StickerKeyword"

    def __init__ (self ,*,document_id :int ,keyword :List [str ])->None :
        self .document_id =document_id 
        self .keyword =keyword 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerKeyword":

        document_id =Long .read (b )

        keyword =TLObject .read (b ,String )

        return StickerKeyword (document_id =document_id ,keyword =keyword )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .document_id ))

        b .write (Vector (self .keyword ,String ))

        return b .getvalue ()
