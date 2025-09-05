
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SavedGifs (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","gifs"]

    ID =0x84a02a0d 
    QUALNAME ="types.messages.SavedGifs"

    def __init__ (self ,*,hash :int ,gifs :List ["raw.base.Document"])->None :
        self .hash =hash 
        self .gifs =gifs 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SavedGifs":

        hash =Long .read (b )

        gifs =TLObject .read (b )

        return SavedGifs (hash =hash ,gifs =gifs )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .gifs ))

        return b .getvalue ()
