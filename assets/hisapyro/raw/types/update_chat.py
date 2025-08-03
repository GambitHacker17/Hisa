
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChat (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id"]

    ID =0xf89a6a4e 
    QUALNAME ="types.UpdateChat"

    def __init__ (self ,*,chat_id :int )->None :
        self .chat_id =chat_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChat":

        chat_id =Long .read (b )

        return UpdateChat (chat_id =chat_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        return b .getvalue ()
