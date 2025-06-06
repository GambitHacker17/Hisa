
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateEncryptedMessagesRead (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","max_date","date"]

    ID =0x38fe25b7 
    QUALNAME ="types.UpdateEncryptedMessagesRead"

    def __init__ (self ,*,chat_id :int ,max_date :int ,date :int )->None :
        self .chat_id =chat_id 
        self .max_date =max_date 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateEncryptedMessagesRead":

        chat_id =Int .read (b )

        max_date =Int .read (b )

        date =Int .read (b )

        return UpdateEncryptedMessagesRead (chat_id =chat_id ,max_date =max_date ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .chat_id ))

        b .write (Int (self .max_date ))

        b .write (Int (self .date ))

        return b .getvalue ()
