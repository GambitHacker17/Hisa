
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TopPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","rating"]

    ID =0xedcdc05b 
    QUALNAME ="types.TopPeer"

    def __init__ (self ,*,peer :"raw.base.Peer",rating :float )->None :
        self .peer =peer 
        self .rating =rating 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TopPeer":

        peer =TLObject .read (b )

        rating =Double .read (b )

        return TopPeer (peer =peer ,rating =rating )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Double (self .rating ))

        return b .getvalue ()
