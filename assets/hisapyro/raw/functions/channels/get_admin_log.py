
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetAdminLog (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","q","max_id","min_id","limit","events_filter","admins"]

    ID =0x33ddf480 
    QUALNAME ="functions.channels.GetAdminLog"

    def __init__ (self ,*,channel :"raw.base.InputChannel",q :str ,max_id :int ,min_id :int ,limit :int ,events_filter :"raw.base.ChannelAdminLogEventsFilter"=None ,admins :Optional [List ["raw.base.InputUser"]]=None )->None :
        self .channel =channel 
        self .q =q 
        self .max_id =max_id 
        self .min_id =min_id 
        self .limit =limit 
        self .events_filter =events_filter 
        self .admins =admins 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetAdminLog":

        flags =Int .read (b )

        channel =TLObject .read (b )

        q =String .read (b )

        events_filter =TLObject .read (b )if flags &(1 <<0 )else None 

        admins =TLObject .read (b )if flags &(1 <<1 )else []

        max_id =Long .read (b )

        min_id =Long .read (b )

        limit =Int .read (b )

        return GetAdminLog (channel =channel ,q =q ,max_id =max_id ,min_id =min_id ,limit =limit ,events_filter =events_filter ,admins =admins )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .events_filter is not None else 0 
        flags |=(1 <<1 )if self .admins else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        b .write (String (self .q ))

        if self .events_filter is not None :
            b .write (self .events_filter .write ())

        if self .admins is not None :
            b .write (Vector (self .admins ))

        b .write (Long (self .max_id ))

        b .write (Long (self .min_id ))

        b .write (Int (self .limit ))

        return b .getvalue ()
