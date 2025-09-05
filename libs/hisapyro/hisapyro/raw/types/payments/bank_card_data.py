
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BankCardData (TLObject ):
    """"""

    __slots__ :List [str ]=["title","open_urls"]

    ID =0x3e24e573 
    QUALNAME ="types.payments.BankCardData"

    def __init__ (self ,*,title :str ,open_urls :List ["raw.base.BankCardOpenUrl"])->None :
        self .title =title 
        self .open_urls =open_urls 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BankCardData":

        title =String .read (b )

        open_urls =TLObject .read (b )

        return BankCardData (title =title ,open_urls =open_urls )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .title ))

        b .write (Vector (self .open_urls ))

        return b .getvalue ()
