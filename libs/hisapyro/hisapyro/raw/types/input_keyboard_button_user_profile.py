
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputKeyboardButtonUserProfile (TLObject ):
    """"""

    __slots__ :List [str ]=["text","user_id"]

    ID =0xe988037b 
    QUALNAME ="types.InputKeyboardButtonUserProfile"

    def __init__ (self ,*,text :str ,user_id :"raw.base.InputUser")->None :
        self .text =text 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputKeyboardButtonUserProfile":

        text =String .read (b )

        user_id =TLObject .read (b )

        return InputKeyboardButtonUserProfile (text =text ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (self .user_id .write ())

        return b .getvalue ()
