
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MigrateChat (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id"]

    ID =0xa2875319 
    QUALNAME ="functions.messages.MigrateChat"

    def __init__ (self ,*,chat_id :int )->None :
        self .chat_id =chat_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MigrateChat":

        chat_id =Long .read (b )

        return MigrateChat (chat_id =chat_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        return b .getvalue ()
