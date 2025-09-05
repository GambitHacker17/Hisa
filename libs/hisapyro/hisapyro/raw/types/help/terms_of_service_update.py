
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TermsOfServiceUpdate (TLObject ):
    """"""

    __slots__ :List [str ]=["expires","terms_of_service"]

    ID =0x28ecf961 
    QUALNAME ="types.help.TermsOfServiceUpdate"

    def __init__ (self ,*,expires :int ,terms_of_service :"raw.base.help.TermsOfService")->None :
        self .expires =expires 
        self .terms_of_service =terms_of_service 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TermsOfServiceUpdate":

        expires =Int .read (b )

        terms_of_service =TLObject .read (b )

        return TermsOfServiceUpdate (expires =expires ,terms_of_service =terms_of_service )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .expires ))

        b .write (self .terms_of_service .write ())

        return b .getvalue ()
