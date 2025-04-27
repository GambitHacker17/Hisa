
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SentCodeTypeFragmentSms (TLObject ):
    """"""

    __slots__ :List [str ]=["url","length"]

    ID =0xd9565c39 
    QUALNAME ="types.auth.SentCodeTypeFragmentSms"

    def __init__ (self ,*,url :str ,length :int )->None :
        self .url =url 
        self .length =length 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SentCodeTypeFragmentSms":

        url =String .read (b )

        length =Int .read (b )

        return SentCodeTypeFragmentSms (url =url ,length =length )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Int (self .length ))

        return b .getvalue ()
