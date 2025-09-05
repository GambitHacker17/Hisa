
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BotCommand (TLObject ):
    """"""

    __slots__ :List [str ]=["command","description"]

    ID =0xc27ac8c7 
    QUALNAME ="types.BotCommand"

    def __init__ (self ,*,command :str ,description :str )->None :
        self .command =command 
        self .description =description 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BotCommand":

        command =String .read (b )

        description =String .read (b )

        return BotCommand (command =command ,description =description )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .command ))

        b .write (String (self .description ))

        return b .getvalue ()
