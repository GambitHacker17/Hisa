
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputChannel (TLObject ):
    """"""

    __slots__ :List [str ]=["channel_id","access_hash"]

    ID =0xf35aec28 
    QUALNAME ="types.InputChannel"

    def __init__ (self ,*,channel_id :int ,access_hash :int )->None :
        self .channel_id =channel_id 
        self .access_hash =access_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputChannel":

        channel_id =Long .read (b )

        access_hash =Long .read (b )

        return InputChannel (channel_id =channel_id ,access_hash =access_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .channel_id ))

        b .write (Long (self .access_hash ))

        return b .getvalue ()
