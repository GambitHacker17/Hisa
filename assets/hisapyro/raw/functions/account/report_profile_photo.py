
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReportProfilePhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","photo_id","reason","message"]

    ID =0xfa8cc6f5 
    QUALNAME ="functions.account.ReportProfilePhoto"

    def __init__ (self ,*,peer :"raw.base.InputPeer",photo_id :"raw.base.InputPhoto",reason :"raw.base.ReportReason",message :str )->None :
        self .peer =peer 
        self .photo_id =photo_id 
        self .reason =reason 
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReportProfilePhoto":

        peer =TLObject .read (b )

        photo_id =TLObject .read (b )

        reason =TLObject .read (b )

        message =String .read (b )

        return ReportProfilePhoto (peer =peer ,photo_id =photo_id ,reason =reason ,message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .photo_id .write ())

        b .write (self .reason .write ())

        b .write (String (self .message ))

        return b .getvalue ()
