
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetRecentLocations (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","limit","hash"]

    ID =0x702a40e0 
    QUALNAME ="functions.messages.GetRecentLocations"

    def __init__ (self ,*,peer :"raw.base.InputPeer",limit :int ,hash :int )->None :
        self .peer =peer 
        self .limit =limit 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetRecentLocations":

        peer =TLObject .read (b )

        limit =Int .read (b )

        hash =Long .read (b )

        return GetRecentLocations (peer =peer ,limit =limit ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .limit ))

        b .write (Long (self .hash ))

        return b .getvalue ()
