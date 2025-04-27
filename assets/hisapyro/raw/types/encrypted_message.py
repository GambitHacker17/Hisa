
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EncryptedMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["random_id","chat_id","date","bytes","file"]

    ID =0xed18c118 
    QUALNAME ="types.EncryptedMessage"

    def __init__ (self ,*,random_id :int ,chat_id :int ,date :int ,bytes :bytes ,file :"raw.base.EncryptedFile")->None :
        self .random_id =random_id 
        self .chat_id =chat_id 
        self .date =date 
        self .bytes =bytes 
        self .file =file 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EncryptedMessage":

        random_id =Long .read (b )

        chat_id =Int .read (b )

        date =Int .read (b )

        bytes =Bytes .read (b )

        file =TLObject .read (b )

        return EncryptedMessage (random_id =random_id ,chat_id =chat_id ,date =date ,bytes =bytes ,file =file )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .random_id ))

        b .write (Int (self .chat_id ))

        b .write (Int (self .date ))

        b .write (Bytes (self .bytes ))

        b .write (self .file .write ())

        return b .getvalue ()
