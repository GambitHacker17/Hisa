
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetBotMenuButton (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id"]

    ID =0x9c60eb28 
    QUALNAME ="functions.bots.GetBotMenuButton"

    def __init__ (self ,*,user_id :"raw.base.InputUser")->None :
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetBotMenuButton":

        user_id =TLObject .read (b )

        return GetBotMenuButton (user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .user_id .write ())

        return b .getvalue ()
