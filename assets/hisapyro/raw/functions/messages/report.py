
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Report (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","reason","message"]

    ID =0x8953ab4e 
    QUALNAME ="functions.messages.Report"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :List [int ],reason :"raw.base.ReportReason",message :str )->None :
        self .peer =peer 
        self .id =id 
        self .reason =reason 
        self .message =message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Report":

        peer =TLObject .read (b )

        id =TLObject .read (b ,Int )

        reason =TLObject .read (b )

        message =String .read (b )

        return Report (peer =peer ,id =id ,reason =reason ,message =message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Vector (self .id ,Int ))

        b .write (self .reason .write ())

        b .write (String (self .message ))

        return b .getvalue ()
