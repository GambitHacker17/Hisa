
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBotsBot (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","users"]

    ID =0x93bf667f 
    QUALNAME ="types.AttachMenuBotsBot"

    def __init__ (self ,*,bot :"raw.base.AttachMenuBot",users :List ["raw.base.User"])->None :
        self .bot =bot 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBotsBot":

        bot =TLObject .read (b )

        users =TLObject .read (b )

        return AttachMenuBotsBot (bot =bot ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .bot .write ())

        b .write (Vector (self .users ))

        return b .getvalue ()
