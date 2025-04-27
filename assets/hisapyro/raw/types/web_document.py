
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebDocument (TLObject ):
    """"""

    __slots__ :List [str ]=["url","access_hash","size","mime_type","attributes"]

    ID =0x1c570ed1 
    QUALNAME ="types.WebDocument"

    def __init__ (self ,*,url :str ,access_hash :int ,size :int ,mime_type :str ,attributes :List ["raw.base.DocumentAttribute"])->None :
        self .url =url 
        self .access_hash =access_hash 
        self .size =size 
        self .mime_type =mime_type 
        self .attributes =attributes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebDocument":

        url =String .read (b )

        access_hash =Long .read (b )

        size =Int .read (b )

        mime_type =String .read (b )

        attributes =TLObject .read (b )

        return WebDocument (url =url ,access_hash =access_hash ,size =size ,mime_type =mime_type ,attributes =attributes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .size ))

        b .write (String (self .mime_type ))

        b .write (Vector (self .attributes ))

        return b .getvalue ()
