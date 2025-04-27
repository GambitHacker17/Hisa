
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Found (TLObject ):
    """"""

    __slots__ :List [str ]=["my_results","results","chats","users"]

    ID =0xb3134d9d 
    QUALNAME ="types.contacts.Found"

    def __init__ (self ,*,my_results :List ["raw.base.Peer"],results :List ["raw.base.Peer"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .my_results =my_results 
        self .results =results 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Found":

        my_results =TLObject .read (b )

        results =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return Found (my_results =my_results ,results =results ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .my_results ))

        b .write (Vector (self .results ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
