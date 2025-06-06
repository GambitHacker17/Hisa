
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveSecureValue (TLObject ):
    """"""

    __slots__ :List [str ]=["value","secure_secret_id"]

    ID =0x899fe31d 
    QUALNAME ="functions.account.SaveSecureValue"

    def __init__ (self ,*,value :"raw.base.InputSecureValue",secure_secret_id :int )->None :
        self .value =value 
        self .secure_secret_id =secure_secret_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveSecureValue":

        value =TLObject .read (b )

        secure_secret_id =Long .read (b )

        return SaveSecureValue (value =value ,secure_secret_id =secure_secret_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .value .write ())

        b .write (Long (self .secure_secret_id ))

        return b .getvalue ()
