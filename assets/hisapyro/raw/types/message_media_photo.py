
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaPhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["spoiler","photo","ttl_seconds"]

    ID =0x695150d7 
    QUALNAME ="types.MessageMediaPhoto"

    def __init__ (self ,*,spoiler :Optional [bool ]=None ,photo :"raw.base.Photo"=None ,ttl_seconds :Optional [int ]=None )->None :
        self .spoiler =spoiler 
        self .photo =photo 
        self .ttl_seconds =ttl_seconds 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaPhoto":

        flags =Int .read (b )

        spoiler =True if flags &(1 <<3 )else False 
        photo =TLObject .read (b )if flags &(1 <<0 )else None 

        ttl_seconds =Int .read (b )if flags &(1 <<2 )else None 
        return MessageMediaPhoto (spoiler =spoiler ,photo =photo ,ttl_seconds =ttl_seconds )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .spoiler else 0 
        flags |=(1 <<0 )if self .photo is not None else 0 
        flags |=(1 <<2 )if self .ttl_seconds is not None else 0 
        b .write (Int (flags ))

        if self .photo is not None :
            b .write (self .photo .write ())

        if self .ttl_seconds is not None :
            b .write (Int (self .ttl_seconds ))

        return b .getvalue ()
