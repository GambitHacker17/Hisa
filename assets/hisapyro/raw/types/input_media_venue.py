
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaVenue (TLObject ):
    """"""

    __slots__ :List [str ]=["geo_point","title","address","provider","venue_id","venue_type"]

    ID =0xc13d1c11 
    QUALNAME ="types.InputMediaVenue"

    def __init__ (self ,*,geo_point :"raw.base.InputGeoPoint",title :str ,address :str ,provider :str ,venue_id :str ,venue_type :str )->None :
        self .geo_point =geo_point 
        self .title =title 
        self .address =address 
        self .provider =provider 
        self .venue_id =venue_id 
        self .venue_type =venue_type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaVenue":

        geo_point =TLObject .read (b )

        title =String .read (b )

        address =String .read (b )

        provider =String .read (b )

        venue_id =String .read (b )

        venue_type =String .read (b )

        return InputMediaVenue (geo_point =geo_point ,title =title ,address =address ,provider =provider ,venue_id =venue_id ,venue_type =venue_type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .geo_point .write ())

        b .write (String (self .title ))

        b .write (String (self .address ))

        b .write (String (self .provider ))

        b .write (String (self .venue_id ))

        b .write (String (self .venue_type ))

        return b .getvalue ()
