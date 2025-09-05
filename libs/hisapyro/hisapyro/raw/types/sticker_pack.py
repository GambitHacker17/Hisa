
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StickerPack (TLObject ):
    """"""

    __slots__ :List [str ]=["emoticon","documents"]

    ID =0x12b299d4 
    QUALNAME ="types.StickerPack"

    def __init__ (self ,*,emoticon :str ,documents :List [int ])->None :
        self .emoticon =emoticon 
        self .documents =documents 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StickerPack":

        emoticon =String .read (b )

        documents =TLObject .read (b ,Long )

        return StickerPack (emoticon =emoticon ,documents =documents )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .emoticon ))

        b .write (Vector (self .documents ,Long ))

        return b .getvalue ()
