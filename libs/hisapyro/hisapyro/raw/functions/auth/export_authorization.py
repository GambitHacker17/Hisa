
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportAuthorization (TLObject ):
    """"""

    __slots__ :List [str ]=["dc_id"]

    ID =0xe5bfffcd 
    QUALNAME ="functions.auth.ExportAuthorization"

    def __init__ (self ,*,dc_id :int )->None :
        self .dc_id =dc_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportAuthorization":

        dc_id =Int .read (b )

        return ExportAuthorization (dc_id =dc_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .dc_id ))

        return b .getvalue ()
