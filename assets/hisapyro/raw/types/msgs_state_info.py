
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MsgsStateInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["req_msg_id","info"]

    ID =0x04deb57d 
    QUALNAME ="types.MsgsStateInfo"

    def __init__ (self ,*,req_msg_id :int ,info :str )->None :
        self .req_msg_id =req_msg_id 
        self .info =info 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MsgsStateInfo":

        req_msg_id =Long .read (b )

        info =String .read (b )

        return MsgsStateInfo (req_msg_id =req_msg_id ,info =info )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .req_msg_id ))

        b .write (String (self .info ))

        return b .getvalue ()
