
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetScheduledHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","hash"]

    ID =0xf516760b 
    QUALNAME ="functions.messages.GetScheduledHistory"

    def __init__ (self ,*,peer :"raw.base.InputPeer",hash :int )->None :
        self .peer =peer 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetScheduledHistory":

        peer =TLObject .read (b )

        hash =Long .read (b )

        return GetScheduledHistory (peer =peer ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Long (self .hash ))

        return b .getvalue ()
