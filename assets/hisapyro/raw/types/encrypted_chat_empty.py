
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EncryptedChatEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0xab7ec0a0 
    QUALNAME ="types.EncryptedChatEmpty"

    def __init__ (self ,*,id :int )->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EncryptedChatEmpty":

        id =Int .read (b )

        return EncryptedChatEmpty (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .id ))

        return b .getvalue ()
