
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetGroupCallJoinAs (TLObject ):
    """"""

    __slots__ :List [str ]=["peer"]

    ID =0xef7c213a 
    QUALNAME ="functions.phone.GetGroupCallJoinAs"

    def __init__ (self ,*,peer :"raw.base.InputPeer")->None :
        self .peer =peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetGroupCallJoinAs":

        peer =TLObject .read (b )

        return GetGroupCallJoinAs (peer =peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        return b .getvalue ()
