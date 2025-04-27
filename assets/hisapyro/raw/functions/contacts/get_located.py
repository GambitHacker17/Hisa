
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetLocated (TLObject ):
    """"""

    __slots__ :List [str ]=["geo_point","background","self_expires"]

    ID =0xd348bc44 
    QUALNAME ="functions.contacts.GetLocated"

    def __init__ (self ,*,geo_point :"raw.base.InputGeoPoint",background :Optional [bool ]=None ,self_expires :Optional [int ]=None )->None :
        self .geo_point =geo_point 
        self .background =background 
        self .self_expires =self_expires 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetLocated":

        flags =Int .read (b )

        background =True if flags &(1 <<1 )else False 
        geo_point =TLObject .read (b )

        self_expires =Int .read (b )if flags &(1 <<0 )else None 
        return GetLocated (geo_point =geo_point ,background =background ,self_expires =self_expires )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .background else 0 
        flags |=(1 <<0 )if self .self_expires is not None else 0 
        b .write (Int (flags ))

        b .write (self .geo_point .write ())

        if self .self_expires is not None :
            b .write (Int (self .self_expires ))

        return b .getvalue ()
