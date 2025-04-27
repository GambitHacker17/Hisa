
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendCode (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","api_id","api_hash","settings"]

    ID =0xa677244f 
    QUALNAME ="functions.auth.SendCode"

    def __init__ (self ,*,phone_number :str ,api_id :int ,api_hash :str ,settings :"raw.base.CodeSettings")->None :
        self .phone_number =phone_number 
        self .api_id =api_id 
        self .api_hash =api_hash 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendCode":

        phone_number =String .read (b )

        api_id =Int .read (b )

        api_hash =String .read (b )

        settings =TLObject .read (b )

        return SendCode (phone_number =phone_number ,api_id =api_id ,api_hash =api_hash ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (Int (self .api_id ))

        b .write (String (self .api_hash ))

        b .write (self .settings .write ())

        return b .getvalue ()
