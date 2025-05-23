
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PostAddress (TLObject ):
    """"""

    __slots__ :List [str ]=["street_line1","street_line2","city","state","country_iso2","post_code"]

    ID =0x1e8caaeb 
    QUALNAME ="types.PostAddress"

    def __init__ (self ,*,street_line1 :str ,street_line2 :str ,city :str ,state :str ,country_iso2 :str ,post_code :str )->None :
        self .street_line1 =street_line1 
        self .street_line2 =street_line2 
        self .city =city 
        self .state =state 
        self .country_iso2 =country_iso2 
        self .post_code =post_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PostAddress":

        street_line1 =String .read (b )

        street_line2 =String .read (b )

        city =String .read (b )

        state =String .read (b )

        country_iso2 =String .read (b )

        post_code =String .read (b )

        return PostAddress (street_line1 =street_line1 ,street_line2 =street_line2 ,city =city ,state =state ,country_iso2 =country_iso2 ,post_code =post_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .street_line1 ))

        b .write (String (self .street_line2 ))

        b .write (String (self .city ))

        b .write (String (self .state ))

        b .write (String (self .country_iso2 ))

        b .write (String (self .post_code ))

        return b .getvalue ()
