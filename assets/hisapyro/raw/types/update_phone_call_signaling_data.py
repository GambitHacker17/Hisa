
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePhoneCallSignalingData (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_call_id","data"]

    ID =0x2661bf09 
    QUALNAME ="types.UpdatePhoneCallSignalingData"

    def __init__ (self ,*,phone_call_id :int ,data :bytes )->None :
        self .phone_call_id =phone_call_id 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePhoneCallSignalingData":

        phone_call_id =Long .read (b )

        data =Bytes .read (b )

        return UpdatePhoneCallSignalingData (phone_call_id =phone_call_id ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .phone_call_id ))

        b .write (Bytes (self .data ))

        return b .getvalue ()
