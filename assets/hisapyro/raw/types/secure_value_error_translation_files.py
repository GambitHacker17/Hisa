
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureValueErrorTranslationFiles (TLObject ):
    """"""

    __slots__ :List [str ]=["type","file_hash","text"]

    ID =0x34636dd8 
    QUALNAME ="types.SecureValueErrorTranslationFiles"

    def __init__ (self ,*,type :"raw.base.SecureValueType",file_hash :List [bytes ],text :str )->None :
        self .type =type 
        self .file_hash =file_hash 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureValueErrorTranslationFiles":

        type =TLObject .read (b )

        file_hash =TLObject .read (b ,Bytes )

        text =String .read (b )

        return SecureValueErrorTranslationFiles (type =type ,file_hash =file_hash ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .type .write ())

        b .write (Vector (self .file_hash ,Bytes ))

        b .write (String (self .text ))

        return b .getvalue ()
