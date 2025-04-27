
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetFullUser (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0xb60f5918 
    QUALNAME ="functions.users.GetFullUser"

    def __init__ (self ,*,id :"raw.base.InputUser")->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetFullUser":

        id =TLObject .read (b )

        return GetFullUser (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .id .write ())

        return b .getvalue ()
