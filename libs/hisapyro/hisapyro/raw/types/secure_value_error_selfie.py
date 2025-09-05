
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureValueErrorSelfie (TLObject ):
    """"""

    __slots__ :List [str ]=["type","file_hash","text"]

    ID =0xe537ced6 
    QUALNAME ="types.SecureValueErrorSelfie"

    def __init__ (self ,*,type :"raw.base.SecureValueType",file_hash :bytes ,text :str )->None :
        self .type =type 
        self .file_hash =file_hash 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureValueErrorSelfie":

        type =TLObject .read (b )

        file_hash =Bytes .read (b )

        text =String .read (b )

        return SecureValueErrorSelfie (type =type ,file_hash =file_hash ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .type .write ())

        b .write (Bytes (self .file_hash ))

        b .write (String (self .text ))

        return b .getvalue ()
