
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPaymentCredentials (TLObject ):
    """"""

    __slots__ :List [str ]=["data","save"]

    ID =0x3417d728 
    QUALNAME ="types.InputPaymentCredentials"

    def __init__ (self ,*,data :"raw.base.DataJSON",save :Optional [bool ]=None )->None :
        self .data =data 
        self .save =save 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPaymentCredentials":

        flags =Int .read (b )

        save =True if flags &(1 <<0 )else False 
        data =TLObject .read (b )

        return InputPaymentCredentials (data =data ,save =save )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .save else 0 
        b .write (Int (flags ))

        b .write (self .data .write ())

        return b .getvalue ()
