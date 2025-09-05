
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SavedRingtones (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","ringtones"]

    ID =0xc1e92cc5 
    QUALNAME ="types.account.SavedRingtones"

    def __init__ (self ,*,hash :int ,ringtones :List ["raw.base.Document"])->None :
        self .hash =hash 
        self .ringtones =ringtones 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SavedRingtones":

        hash =Long .read (b )

        ringtones =TLObject .read (b )

        return SavedRingtones (hash =hash ,ringtones =ringtones )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .hash ))

        b .write (Vector (self .ringtones ))

        return b .getvalue ()
