
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaGeo (TLObject ):
    """"""

    __slots__ :List [str ]=["geo"]

    ID =0x56e0d474 
    QUALNAME ="types.MessageMediaGeo"

    def __init__ (self ,*,geo :"raw.base.GeoPoint")->None :
        self .geo =geo 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaGeo":

        geo =TLObject .read (b )

        return MessageMediaGeo (geo =geo )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .geo .write ())

        return b .getvalue ()
