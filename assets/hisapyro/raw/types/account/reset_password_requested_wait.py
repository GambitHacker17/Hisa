
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ResetPasswordRequestedWait (TLObject ):
    """"""

    __slots__ :List [str ]=["until_date"]

    ID =0xe9effc7d 
    QUALNAME ="types.account.ResetPasswordRequestedWait"

    def __init__ (self ,*,until_date :int )->None :
        self .until_date =until_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ResetPasswordRequestedWait":

        until_date =Int .read (b )

        return ResetPasswordRequestedWait (until_date =until_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .until_date ))

        return b .getvalue ()
