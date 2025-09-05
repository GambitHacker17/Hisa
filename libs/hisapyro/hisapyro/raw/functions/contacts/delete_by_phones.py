
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteByPhones (TLObject ):
    """"""

    __slots__ :List [str ]=["phones"]

    ID =0x1013fd9e 
    QUALNAME ="functions.contacts.DeleteByPhones"

    def __init__ (self ,*,phones :List [str ])->None :
        self .phones =phones 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteByPhones":

        phones =TLObject .read (b ,String )

        return DeleteByPhones (phones =phones )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .phones ,String ))

        return b .getvalue ()
