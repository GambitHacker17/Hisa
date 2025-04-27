
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaDocument (TLObject ):
    """"""

    __slots__ :List [str ]=["nopremium","spoiler","document","ttl_seconds"]

    ID =0x9cb070d7 
    QUALNAME ="types.MessageMediaDocument"

    def __init__ (self ,*,nopremium :Optional [bool ]=None ,spoiler :Optional [bool ]=None ,document :"raw.base.Document"=None ,ttl_seconds :Optional [int ]=None )->None :
        self .nopremium =nopremium 
        self .spoiler =spoiler 
        self .document =document 
        self .ttl_seconds =ttl_seconds 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaDocument":

        flags =Int .read (b )

        nopremium =True if flags &(1 <<3 )else False 
        spoiler =True if flags &(1 <<4 )else False 
        document =TLObject .read (b )if flags &(1 <<0 )else None 

        ttl_seconds =Int .read (b )if flags &(1 <<2 )else None 
        return MessageMediaDocument (nopremium =nopremium ,spoiler =spoiler ,document =document ,ttl_seconds =ttl_seconds )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .nopremium else 0 
        flags |=(1 <<4 )if self .spoiler else 0 
        flags |=(1 <<0 )if self .document is not None else 0 
        flags |=(1 <<2 )if self .ttl_seconds is not None else 0 
        b .write (Int (flags ))

        if self .document is not None :
            b .write (self .document .write ())

        if self .ttl_seconds is not None :
            b .write (Int (self .ttl_seconds ))

        return b .getvalue ()
