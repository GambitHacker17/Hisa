
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ImportedContact (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","client_id"]

    ID =0xc13e3c50 
    QUALNAME ="types.ImportedContact"

    def __init__ (self ,*,user_id :int ,client_id :int )->None :
        self .user_id =user_id 
        self .client_id =client_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ImportedContact":

        user_id =Long .read (b )

        client_id =Long .read (b )

        return ImportedContact (user_id =user_id ,client_id =client_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (Long (self .client_id ))

        return b .getvalue ()
