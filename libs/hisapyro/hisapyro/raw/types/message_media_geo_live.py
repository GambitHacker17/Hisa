
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaGeoLive (TLObject ):
    """"""

    __slots__ :List [str ]=["geo","period","heading","proximity_notification_radius"]

    ID =0xb940c666 
    QUALNAME ="types.MessageMediaGeoLive"

    def __init__ (self ,*,geo :"raw.base.GeoPoint",period :int ,heading :Optional [int ]=None ,proximity_notification_radius :Optional [int ]=None )->None :
        self .geo =geo 
        self .period =period 
        self .heading =heading 
        self .proximity_notification_radius =proximity_notification_radius 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaGeoLive":

        flags =Int .read (b )

        geo =TLObject .read (b )

        heading =Int .read (b )if flags &(1 <<0 )else None 
        period =Int .read (b )

        proximity_notification_radius =Int .read (b )if flags &(1 <<1 )else None 
        return MessageMediaGeoLive (geo =geo ,period =period ,heading =heading ,proximity_notification_radius =proximity_notification_radius )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .heading is not None else 0 
        flags |=(1 <<1 )if self .proximity_notification_radius is not None else 0 
        b .write (Int (flags ))

        b .write (self .geo .write ())

        if self .heading is not None :
            b .write (Int (self .heading ))

        b .write (Int (self .period ))

        if self .proximity_notification_radius is not None :
            b .write (Int (self .proximity_notification_radius ))

        return b .getvalue ()
