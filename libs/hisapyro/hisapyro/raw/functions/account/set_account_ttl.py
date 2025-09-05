
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetAccountTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["ttl"]

    ID =0x2442485e 
    QUALNAME ="functions.account.SetAccountTTL"

    def __init__ (self ,*,ttl :"raw.base.AccountDaysTTL")->None :
        self .ttl =ttl 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetAccountTTL":

        ttl =TLObject .read (b )

        return SetAccountTTL (ttl =ttl )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .ttl .write ())

        return b .getvalue ()
