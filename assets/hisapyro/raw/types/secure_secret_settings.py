
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureSecretSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["secure_algo","secure_secret","secure_secret_id"]

    ID =0x1527bcac 
    QUALNAME ="types.SecureSecretSettings"

    def __init__ (self ,*,secure_algo :"raw.base.SecurePasswordKdfAlgo",secure_secret :bytes ,secure_secret_id :int )->None :
        self .secure_algo =secure_algo 
        self .secure_secret =secure_secret 
        self .secure_secret_id =secure_secret_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureSecretSettings":

        secure_algo =TLObject .read (b )

        secure_secret =Bytes .read (b )

        secure_secret_id =Long .read (b )

        return SecureSecretSettings (secure_algo =secure_algo ,secure_secret =secure_secret ,secure_secret_id =secure_secret_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .secure_algo .write ())

        b .write (Bytes (self .secure_secret ))

        b .write (Long (self .secure_secret_id ))

        return b .getvalue ()
