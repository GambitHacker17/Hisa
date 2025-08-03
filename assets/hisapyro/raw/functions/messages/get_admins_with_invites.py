
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAdminsWithInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["peer"]

    ID =0x3920e6ef 
    QUALNAME ="functions.messages.GetAdminsWithInvites"

    def __init__ (self ,*,peer :"raw.base.InputPeer")->None :
        self .peer =peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAdminsWithInvites":

        peer =TLObject .read (b )

        return GetAdminsWithInvites (peer =peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        return b .getvalue ()
