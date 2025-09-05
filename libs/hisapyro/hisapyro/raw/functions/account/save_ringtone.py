
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveRingtone (TLObject ):
    """"""

    __slots__ :List [str ]=["id","unsave"]

    ID =0x3dea5b03 
    QUALNAME ="functions.account.SaveRingtone"

    def __init__ (self ,*,id :"raw.base.InputDocument",unsave :bool )->None :
        self .id =id 
        self .unsave =unsave 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveRingtone":

        id =TLObject .read (b )

        unsave =Bool .read (b )

        return SaveRingtone (id =id ,unsave =unsave )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .id .write ())

        b .write (Bool (self .unsave ))

        return b .getvalue ()
