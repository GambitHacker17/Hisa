
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotInlineMessageID64 (TLObject ):
    """"""

    __slots__ :List [str ]=["dc_id","owner_id","id","access_hash"]

    ID =0xb6d915d7 
    QUALNAME ="types.InputBotInlineMessageID64"

    def __init__ (self ,*,dc_id :int ,owner_id :int ,id :int ,access_hash :int )->None :
        self .dc_id =dc_id 
        self .owner_id =owner_id 
        self .id =id 
        self .access_hash =access_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotInlineMessageID64":

        dc_id =Int .read (b )

        owner_id =Long .read (b )

        id =Int .read (b )

        access_hash =Long .read (b )

        return InputBotInlineMessageID64 (dc_id =dc_id ,owner_id =owner_id ,id =id ,access_hash =access_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .dc_id ))

        b .write (Long (self .owner_id ))

        b .write (Int (self .id ))

        b .write (Long (self .access_hash ))

        return b .getvalue ()
