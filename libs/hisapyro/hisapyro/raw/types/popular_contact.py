
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PopularContact (TLObject ):
    """"""

    __slots__ :List [str ]=["client_id","importers"]

    ID =0x5ce14175 
    QUALNAME ="types.PopularContact"

    def __init__ (self ,*,client_id :int ,importers :int )->None :
        self .client_id =client_id 
        self .importers =importers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PopularContact":

        client_id =Long .read (b )

        importers =Int .read (b )

        return PopularContact (client_id =client_id ,importers =importers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .client_id ))

        b .write (Int (self .importers ))

        return b .getvalue ()
