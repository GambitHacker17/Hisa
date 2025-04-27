
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestFirebaseSms (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","phone_code_hash","safety_net_token","ios_push_secret"]

    ID =0x89464b50 
    QUALNAME ="functions.auth.RequestFirebaseSms"

    def __init__ (self ,*,phone_number :str ,phone_code_hash :str ,safety_net_token :Optional [str ]=None ,ios_push_secret :Optional [str ]=None )->None :
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .safety_net_token =safety_net_token 
        self .ios_push_secret =ios_push_secret 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestFirebaseSms":

        flags =Int .read (b )

        phone_number =String .read (b )

        phone_code_hash =String .read (b )

        safety_net_token =String .read (b )if flags &(1 <<0 )else None 
        ios_push_secret =String .read (b )if flags &(1 <<1 )else None 
        return RequestFirebaseSms (phone_number =phone_number ,phone_code_hash =phone_code_hash ,safety_net_token =safety_net_token ,ios_push_secret =ios_push_secret )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .safety_net_token is not None else 0 
        flags |=(1 <<1 )if self .ios_push_secret is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .phone_number ))

        b .write (String (self .phone_code_hash ))

        if self .safety_net_token is not None :
            b .write (String (self .safety_net_token ))

        if self .ios_push_secret is not None :
            b .write (String (self .ios_push_secret ))

        return b .getvalue ()
