
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Country (TLObject ):
    """"""

    __slots__ :List [str ]=["iso2","default_name","country_codes","hidden","name"]

    ID =0xc3878e23 
    QUALNAME ="types.help.Country"

    def __init__ (self ,*,iso2 :str ,default_name :str ,country_codes :List ["raw.base.help.CountryCode"],hidden :Optional [bool ]=None ,name :Optional [str ]=None )->None :
        self .iso2 =iso2 
        self .default_name =default_name 
        self .country_codes =country_codes 
        self .hidden =hidden 
        self .name =name 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Country":

        flags =Int .read (b )

        hidden =True if flags &(1 <<0 )else False 
        iso2 =String .read (b )

        default_name =String .read (b )

        name =String .read (b )if flags &(1 <<1 )else None 
        country_codes =TLObject .read (b )

        return Country (iso2 =iso2 ,default_name =default_name ,country_codes =country_codes ,hidden =hidden ,name =name )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .hidden else 0 
        flags |=(1 <<1 )if self .name is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .iso2 ))

        b .write (String (self .default_name ))

        if self .name is not None :
            b .write (String (self .name ))

        b .write (Vector (self .country_codes ))

        return b .getvalue ()
