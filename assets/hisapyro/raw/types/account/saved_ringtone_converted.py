
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SavedRingtoneConverted (TLObject ):
    """"""

    __slots__ :List [str ]=["document"]

    ID =0x1f307eb7 
    QUALNAME ="types.account.SavedRingtoneConverted"

    def __init__ (self ,*,document :"raw.base.Document")->None :
        self .document =document 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SavedRingtoneConverted":

        document =TLObject .read (b )

        return SavedRingtoneConverted (document =document )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .document .write ())

        return b .getvalue ()
