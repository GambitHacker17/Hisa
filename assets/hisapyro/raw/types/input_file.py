
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputFile (TLObject ):
    """"""

    __slots__ :List [str ]=["id","parts","name","md5_checksum"]

    ID =0xf52ff27f 
    QUALNAME ="types.InputFile"

    def __init__ (self ,*,id :int ,parts :int ,name :str ,md5_checksum :str )->None :
        self .id =id 
        self .parts =parts 
        self .name =name 
        self .md5_checksum =md5_checksum 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputFile":

        id =Long .read (b )

        parts =Int .read (b )

        name =String .read (b )

        md5_checksum =String .read (b )

        return InputFile (id =id ,parts =parts ,name =name ,md5_checksum =md5_checksum )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        b .write (Int (self .parts ))

        b .write (String (self .name ))

        b .write (String (self .md5_checksum ))

        return b .getvalue ()
