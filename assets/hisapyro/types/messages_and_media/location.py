
import hisapyro 

from hisapyro import raw 
from ..object import Object 

class Location (Object ):
    """"""

    def __init__ (
    self ,
    *,
    client :"hisapyro.Client"=None ,
    longitude :float ,
    latitude :float 
    ):
        super ().__init__ (client )

        self .longitude =longitude 
        self .latitude =latitude 

    @staticmethod 
    def _parse (client ,geo_point :"raw.types.GeoPoint")->"Location":
        if isinstance (geo_point ,raw .types .GeoPoint ):
            return Location (
            longitude =geo_point .long ,
            latitude =geo_point .lat ,
            client =client 
            )
