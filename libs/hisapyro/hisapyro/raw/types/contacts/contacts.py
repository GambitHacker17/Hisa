
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Contacts (TLObject ):
    """"""

    __slots__ :List [str ]=["contacts","saved_count","users"]

    ID =0xeae87e42 
    QUALNAME ="types.contacts.Contacts"

    def __init__ (self ,*,contacts :List ["raw.base.Contact"],saved_count :int ,users :List ["raw.base.User"])->None :
        self .contacts =contacts 
        self .saved_count =saved_count 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Contacts":

        contacts =TLObject .read (b )

        saved_count =Int .read (b )

        users =TLObject .read (b )

        return Contacts (contacts =contacts ,saved_count =saved_count ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .contacts ))

        b .write (Int (self .saved_count ))

        b .write (Vector (self .users ))

        return b .getvalue ()
