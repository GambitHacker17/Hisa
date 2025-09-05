
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotMenuButton (TLObject ):
    """"""

    __slots__ :List [str ]=["bot_id","button"]

    ID =0x14b85813 
    QUALNAME ="types.UpdateBotMenuButton"

    def __init__ (self ,*,bot_id :int ,button :"raw.base.BotMenuButton")->None :
        self .bot_id =bot_id 
        self .button =button 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotMenuButton":

        bot_id =Long .read (b )

        button =TLObject .read (b )

        return UpdateBotMenuButton (bot_id =bot_id ,button =button )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .bot_id ))

        b .write (self .button .write ())

        return b .getvalue ()
