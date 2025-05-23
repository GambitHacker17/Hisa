
import hisapyro 
from hisapyro import raw 
from hisapyro import types 
from ..object import Object 

class Venue (Object ):
    """"""

    def __init__ (
    self ,
    *,
    client :"hisapyro.Client"=None ,
    location :"types.Location",
    title :str ,
    address :str ,
    foursquare_id :str =None ,
    foursquare_type :str =None 
    ):
        super ().__init__ (client )

        self .location =location 
        self .title =title 
        self .address =address 
        self .foursquare_id =foursquare_id 
        self .foursquare_type =foursquare_type 

    @staticmethod 
    def _parse (client ,venue :"raw.types.MessageMediaVenue"):
        return Venue (
        location =types .Location ._parse (client ,venue .geo ),
        title =venue .title ,
        address =venue .address ,
        foursquare_id =venue .venue_id or None ,
        foursquare_type =venue .venue_type ,
        client =client 
        )
