
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotAppShortName (TLObject ):
    """"""

    __slots__ :List [str ]=["bot_id","short_name"]

    ID =0x908c0407 
    QUALNAME ="types.InputBotAppShortName"

    def __init__ (self ,*,bot_id :"raw.base.InputUser",short_name :str )->None :
        self .bot_id =bot_id 
        self .short_name =short_name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotAppShortName":

        bot_id =TLObject .read (b )

        short_name =String .read (b )

        return InputBotAppShortName (bot_id =bot_id ,short_name =short_name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .bot_id .write ())

        b .write (String (self .short_name ))

        return b .getvalue ()
