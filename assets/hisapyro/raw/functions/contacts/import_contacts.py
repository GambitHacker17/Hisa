
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportContacts (TLObject ):
    """"""

    __slots__ :List [str ]=["contacts"]

    ID =0x2c800be5 
    QUALNAME ="functions.contacts.ImportContacts"

    def __init__ (self ,*,contacts :List ["raw.base.InputContact"])->None :
        self .contacts =contacts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportContacts":

        contacts =TLObject .read (b )

        return ImportContacts (contacts =contacts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .contacts ))

        return b .getvalue ()
