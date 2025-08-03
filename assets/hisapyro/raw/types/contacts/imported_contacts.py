
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportedContacts (TLObject ):
    """"""

    __slots__ :List [str ]=["imported","popular_invites","retry_contacts","users"]

    ID =0x77d01c3b 
    QUALNAME ="types.contacts.ImportedContacts"

    def __init__ (self ,*,imported :List ["raw.base.ImportedContact"],popular_invites :List ["raw.base.PopularContact"],retry_contacts :List [int ],users :List ["raw.base.User"])->None :
        self .imported =imported 
        self .popular_invites =popular_invites 
        self .retry_contacts =retry_contacts 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportedContacts":

        imported =TLObject .read (b )

        popular_invites =TLObject .read (b )

        retry_contacts =TLObject .read (b ,Long )

        users =TLObject .read (b )

        return ImportedContacts (imported =imported ,popular_invites =popular_invites ,retry_contacts =retry_contacts ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .imported ))

        b .write (Vector (self .popular_invites ))

        b .write (Vector (self .retry_contacts ,Long ))

        b .write (Vector (self .users ))

        return b .getvalue ()
