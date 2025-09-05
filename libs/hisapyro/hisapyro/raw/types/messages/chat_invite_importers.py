
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatInviteImporters (TLObject ):
    """"""

    __slots__ :List [str ]=["count","importers","users"]

    ID =0x81b6b00a 
    QUALNAME ="types.messages.ChatInviteImporters"

    def __init__ (self ,*,count :int ,importers :List ["raw.base.ChatInviteImporter"],users :List ["raw.base.User"])->None :
        self .count =count 
        self .importers =importers 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatInviteImporters":

        count =Int .read (b )

        importers =TLObject .read (b )

        users =TLObject .read (b )

        return ChatInviteImporters (count =count ,importers =importers ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .count ))

        b .write (Vector (self .importers ))

        b .write (Vector (self .users ))

        return b .getvalue ()
