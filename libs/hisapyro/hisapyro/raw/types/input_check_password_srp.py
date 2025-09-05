
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputCheckPasswordSRP (TLObject ):
    """"""

    __slots__ :List [str ]=["srp_id","A","M1"]

    ID =0xd27ff082 
    QUALNAME ="types.InputCheckPasswordSRP"

    def __init__ (self ,*,srp_id :int ,A :bytes ,M1 :bytes )->None :
        self .srp_id =srp_id 
        self .A =A 
        self .M1 =M1 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputCheckPasswordSRP":

        srp_id =Long .read (b )

        A =Bytes .read (b )

        M1 =Bytes .read (b )

        return InputCheckPasswordSRP (srp_id =srp_id ,A =A ,M1 =M1 )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .srp_id ))

        b .write (Bytes (self .A ))

        b .write (Bytes (self .M1 ))

        return b .getvalue ()
