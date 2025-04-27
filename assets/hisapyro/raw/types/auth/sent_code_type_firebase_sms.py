
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCodeTypeFirebaseSms (TLObject ):
    """"""

    __slots__ :List [str ]=["length","nonce","receipt","push_timeout"]

    ID =0xe57b1432 
    QUALNAME ="types.auth.SentCodeTypeFirebaseSms"

    def __init__ (self ,*,length :int ,nonce :Optional [bytes ]=None ,receipt :Optional [str ]=None ,push_timeout :Optional [int ]=None )->None :
        self .length =length 
        self .nonce =nonce 
        self .receipt =receipt 
        self .push_timeout =push_timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCodeTypeFirebaseSms":

        flags =Int .read (b )

        nonce =Bytes .read (b )if flags &(1 <<0 )else None 
        receipt =String .read (b )if flags &(1 <<1 )else None 
        push_timeout =Int .read (b )if flags &(1 <<1 )else None 
        length =Int .read (b )

        return SentCodeTypeFirebaseSms (length =length ,nonce =nonce ,receipt =receipt ,push_timeout =push_timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .nonce is not None else 0 
        flags |=(1 <<1 )if self .receipt is not None else 0 
        flags |=(1 <<1 )if self .push_timeout is not None else 0 
        b .write (Int (flags ))

        if self .nonce is not None :
            b .write (Bytes (self .nonce ))

        if self .receipt is not None :
            b .write (String (self .receipt ))

        if self .push_timeout is not None :
            b .write (Int (self .push_timeout ))

        b .write (Int (self .length ))

        return b .getvalue ()
