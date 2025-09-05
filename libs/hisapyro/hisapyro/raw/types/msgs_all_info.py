
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MsgsAllInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_ids","info"]

    ID =0x8cc0d131 
    QUALNAME ="types.MsgsAllInfo"

    def __init__ (self ,*,msg_ids :List [int ],info :str )->None :
        self .msg_ids =msg_ids 
        self .info =info 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MsgsAllInfo":

        msg_ids =TLObject .read (b ,Long )

        info =String .read (b )

        return MsgsAllInfo (msg_ids =msg_ids ,info =info )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .msg_ids ,Long ))

        b .write (String (self .info ))

        return b .getvalue ()
