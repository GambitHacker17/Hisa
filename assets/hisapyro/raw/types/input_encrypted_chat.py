
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputEncryptedChat (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","access_hash"]

    ID =0xf141b5e1 
    QUALNAME ="types.InputEncryptedChat"

    def __init__ (self ,*,chat_id :int ,access_hash :int )->None :
        self .chat_id =chat_id 
        self .access_hash =access_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputEncryptedChat":

        chat_id =Int .read (b )

        access_hash =Long .read (b )

        return InputEncryptedChat (chat_id =chat_id ,access_hash =access_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .chat_id ))

        b .write (Long (self .access_hash ))

        return b .getvalue ()
