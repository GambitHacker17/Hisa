
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPhoneContact (TLObject ):
    """"""

    __slots__ :List [str ]=["client_id","phone","first_name","last_name"]

    ID =0xf392b7f4 
    QUALNAME ="types.InputPhoneContact"

    def __init__ (self ,*,client_id :int ,phone :str ,first_name :str ,last_name :str )->None :
        self .client_id =client_id 
        self .phone =phone 
        self .first_name =first_name 
        self .last_name =last_name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPhoneContact":

        client_id =Long .read (b )

        phone =String .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        return InputPhoneContact (client_id =client_id ,phone =phone ,first_name =first_name ,last_name =last_name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .client_id ))

        b .write (String (self .phone ))

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        return b .getvalue ()
