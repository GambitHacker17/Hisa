
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ResetTopPeerRating (TLObject ):
    """"""

    __slots__ :List [str ]=["category","peer"]

    ID =0x1ae373ac 
    QUALNAME ="functions.contacts.ResetTopPeerRating"

    def __init__ (self ,*,category :"raw.base.TopPeerCategory",peer :"raw.base.InputPeer")->None :
        self .category =category 
        self .peer =peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ResetTopPeerRating":

        category =TLObject .read (b )

        peer =TLObject .read (b )

        return ResetTopPeerRating (category =category ,peer =peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .category .write ())

        b .write (self .peer .write ())

        return b .getvalue ()
