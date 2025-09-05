
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureCredentialsEncrypted (TLObject ):
    """"""

    __slots__ :List [str ]=["data","hash","secret"]

    ID =0x33f0ea47 
    QUALNAME ="types.SecureCredentialsEncrypted"

    def __init__ (self ,*,data :bytes ,hash :bytes ,secret :bytes )->None :
        self .data =data 
        self .hash =hash 
        self .secret =secret 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureCredentialsEncrypted":

        data =Bytes .read (b )

        hash =Bytes .read (b )

        secret =Bytes .read (b )

        return SecureCredentialsEncrypted (data =data ,hash =hash ,secret =secret )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Bytes (self .data ))

        b .write (Bytes (self .hash ))

        b .write (Bytes (self .secret ))

        return b .getvalue ()
