
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AcceptCall (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","g_b","protocol"]

    ID =0x3bd2b4a0 
    QUALNAME ="functions.phone.AcceptCall"

    def __init__ (self ,*,peer :"raw.base.InputPhoneCall",g_b :bytes ,protocol :"raw.base.PhoneCallProtocol")->None :
        self .peer =peer 
        self .g_b =g_b 
        self .protocol =protocol 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AcceptCall":

        peer =TLObject .read (b )

        g_b =Bytes .read (b )

        protocol =TLObject .read (b )

        return AcceptCall (peer =peer ,g_b =g_b ,protocol =protocol )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Bytes (self .g_b ))

        b .write (self .protocol .write ())

        return b .getvalue ()
