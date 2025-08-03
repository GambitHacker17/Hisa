
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBots (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","bots","users"]

    ID =0x3c4301c0 
    QUALNAME ="types.AttachMenuBots"

    def __init__ (self ,*,hash :int ,bots :List ["raw.base.AttachMenuBot"],users :List ["raw.base.User"])->None :
        self .hash =hash 
        self .bots =bots 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBots":

        hash =Long .read (b )

        bots =TLObject .read (b )

        users =TLObject .read (b )

        return AttachMenuBots (hash =hash ,bots =bots ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .bots ))

        b .write (Vector (self .users ))

        return b .getvalue ()
