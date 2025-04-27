
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AutoSaveSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["users_settings","chats_settings","broadcasts_settings","exceptions","chats","users"]

    ID =0x4c3e069d 
    QUALNAME ="types.account.AutoSaveSettings"

    def __init__ (self ,*,users_settings :"raw.base.AutoSaveSettings",chats_settings :"raw.base.AutoSaveSettings",broadcasts_settings :"raw.base.AutoSaveSettings",exceptions :List ["raw.base.AutoSaveException"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .users_settings =users_settings 
        self .chats_settings =chats_settings 
        self .broadcasts_settings =broadcasts_settings 
        self .exceptions =exceptions 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AutoSaveSettings":

        users_settings =TLObject .read (b )

        chats_settings =TLObject .read (b )

        broadcasts_settings =TLObject .read (b )

        exceptions =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return AutoSaveSettings (users_settings =users_settings ,chats_settings =chats_settings ,broadcasts_settings =broadcasts_settings ,exceptions =exceptions ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .users_settings .write ())

        b .write (self .chats_settings .write ())

        b .write (self .broadcasts_settings .write ())

        b .write (Vector (self .exceptions ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
