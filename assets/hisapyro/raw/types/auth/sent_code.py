
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCode (TLObject ):
    """"""

    __slots__ :List [str ]=["type","phone_code_hash","next_type","timeout"]

    ID =0x5e002502 
    QUALNAME ="types.auth.SentCode"

    def __init__ (self ,*,type :"raw.base.auth.SentCodeType",phone_code_hash :str ,next_type :"raw.base.auth.CodeType"=None ,timeout :Optional [int ]=None )->None :
        self .type =type 
        self .phone_code_hash =phone_code_hash 
        self .next_type =next_type 
        self .timeout =timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCode":

        flags =Int .read (b )

        type =TLObject .read (b )

        phone_code_hash =String .read (b )

        next_type =TLObject .read (b )if flags &(1 <<1 )else None 

        timeout =Int .read (b )if flags &(1 <<2 )else None 
        return SentCode (type =type ,phone_code_hash =phone_code_hash ,next_type =next_type ,timeout =timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .next_type is not None else 0 
        flags |=(1 <<2 )if self .timeout is not None else 0 
        b .write (Int (flags ))

        b .write (self .type .write ())

        b .write (String (self .phone_code_hash ))

        if self .next_type is not None :
            b .write (self .next_type .write ())

        if self .timeout is not None :
            b .write (Int (self .timeout ))

        return b .getvalue ()
