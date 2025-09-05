
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputBotInlineMessageID (TLObject ):
    """"""

    __slots__ :List [str ]=["dc_id","id","access_hash"]

    ID =0x890c3d89 
    QUALNAME ="types.InputBotInlineMessageID"

    def __init__ (self ,*,dc_id :int ,id :int ,access_hash :int )->None :
        self .dc_id =dc_id 
        self .id =id 
        self .access_hash =access_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputBotInlineMessageID":

        dc_id =Int .read (b )

        id =Long .read (b )

        access_hash =Long .read (b )

        return InputBotInlineMessageID (dc_id =dc_id ,id =id ,access_hash =access_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .dc_id ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        return b .getvalue ()
