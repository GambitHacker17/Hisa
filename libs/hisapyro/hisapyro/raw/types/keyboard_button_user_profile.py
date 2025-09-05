
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonUserProfile (TLObject ):
    """"""

    __slots__ :List [str ]=["text","user_id"]

    ID =0x308660c1 
    QUALNAME ="types.KeyboardButtonUserProfile"

    def __init__ (self ,*,text :str ,user_id :int )->None :
        self .text =text 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonUserProfile":

        text =String .read (b )

        user_id =Long .read (b )

        return KeyboardButtonUserProfile (text =text ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
