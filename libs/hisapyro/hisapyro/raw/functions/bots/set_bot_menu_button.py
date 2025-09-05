
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetBotMenuButton (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","button"]

    ID =0x4504d54f 
    QUALNAME ="functions.bots.SetBotMenuButton"

    def __init__ (self ,*,user_id :"raw.base.InputUser",button :"raw.base.BotMenuButton")->None :
        self .user_id =user_id 
        self .button =button 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetBotMenuButton":

        user_id =TLObject .read (b )

        button =TLObject .read (b )

        return SetBotMenuButton (user_id =user_id ,button =button )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .user_id .write ())

        b .write (self .button .write ())

        return b .getvalue ()
