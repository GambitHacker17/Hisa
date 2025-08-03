
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureValueErrorData (TLObject ):
    """"""

    __slots__ :List [str ]=["type","data_hash","field","text"]

    ID =0xe8a40bd9 
    QUALNAME ="types.SecureValueErrorData"

    def __init__ (self ,*,type :"raw.base.SecureValueType",data_hash :bytes ,field :str ,text :str )->None :
        self .type =type 
        self .data_hash =data_hash 
        self .field =field 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureValueErrorData":

        type =TLObject .read (b )

        data_hash =Bytes .read (b )

        field =String .read (b )

        text =String .read (b )

        return SecureValueErrorData (type =type ,data_hash =data_hash ,field =field ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .type .write ())

        b .write (Bytes (self .data_hash ))

        b .write (String (self .field ))

        b .write (String (self .text ))

        return b .getvalue ()
