
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DismissSuggestion (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","suggestion"]

    ID =0xf50dbaa1 
    QUALNAME ="functions.help.DismissSuggestion"

    def __init__ (self ,*,peer :"raw.base.InputPeer",suggestion :str )->None :
        self .peer =peer 
        self .suggestion =suggestion 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DismissSuggestion":

        peer =TLObject .read (b )

        suggestion =String .read (b )

        return DismissSuggestion (peer =peer ,suggestion =suggestion )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (String (self .suggestion ))

        return b .getvalue ()
