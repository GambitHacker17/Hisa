
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendSignalingData (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","data"]

    ID =0xff7a9383 
    QUALNAME ="functions.phone.SendSignalingData"

    def __init__ (self ,*,peer :"raw.base.InputPhoneCall",data :bytes )->None :
        self .peer =peer 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendSignalingData":

        peer =TLObject .read (b )

        data =Bytes .read (b )

        return SendSignalingData (peer =peer ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Bytes (self .data ))

        return b .getvalue ()
