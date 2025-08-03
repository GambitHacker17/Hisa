
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","participants_count","unmuted_video_limit","version","join_muted","can_change_join_muted","join_date_asc","schedule_start_subscribed","can_start_video","record_video_active","rtmp_stream","listeners_hidden","title","stream_dc_id","record_start_date","schedule_date","unmuted_video_count"]

    ID =0xd597650c 
    QUALNAME ="types.GroupCall"

    def __init__ (self ,*,id :int ,access_hash :int ,participants_count :int ,unmuted_video_limit :int ,version :int ,join_muted :Optional [bool ]=None ,can_change_join_muted :Optional [bool ]=None ,join_date_asc :Optional [bool ]=None ,schedule_start_subscribed :Optional [bool ]=None ,can_start_video :Optional [bool ]=None ,record_video_active :Optional [bool ]=None ,rtmp_stream :Optional [bool ]=None ,listeners_hidden :Optional [bool ]=None ,title :Optional [str ]=None ,stream_dc_id :Optional [int ]=None ,record_start_date :Optional [int ]=None ,schedule_date :Optional [int ]=None ,unmuted_video_count :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .participants_count =participants_count 
        self .unmuted_video_limit =unmuted_video_limit 
        self .version =version 
        self .join_muted =join_muted 
        self .can_change_join_muted =can_change_join_muted 
        self .join_date_asc =join_date_asc 
        self .schedule_start_subscribed =schedule_start_subscribed 
        self .can_start_video =can_start_video 
        self .record_video_active =record_video_active 
        self .rtmp_stream =rtmp_stream 
        self .listeners_hidden =listeners_hidden 
        self .title =title 
        self .stream_dc_id =stream_dc_id 
        self .record_start_date =record_start_date 
        self .schedule_date =schedule_date 
        self .unmuted_video_count =unmuted_video_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCall":

        flags =Int .read (b )

        join_muted =True if flags &(1 <<1 )else False 
        can_change_join_muted =True if flags &(1 <<2 )else False 
        join_date_asc =True if flags &(1 <<6 )else False 
        schedule_start_subscribed =True if flags &(1 <<8 )else False 
        can_start_video =True if flags &(1 <<9 )else False 
        record_video_active =True if flags &(1 <<11 )else False 
        rtmp_stream =True if flags &(1 <<12 )else False 
        listeners_hidden =True if flags &(1 <<13 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        participants_count =Int .read (b )

        title =String .read (b )if flags &(1 <<3 )else None 
        stream_dc_id =Int .read (b )if flags &(1 <<4 )else None 
        record_start_date =Int .read (b )if flags &(1 <<5 )else None 
        schedule_date =Int .read (b )if flags &(1 <<7 )else None 
        unmuted_video_count =Int .read (b )if flags &(1 <<10 )else None 
        unmuted_video_limit =Int .read (b )

        version =Int .read (b )

        return GroupCall (id =id ,access_hash =access_hash ,participants_count =participants_count ,unmuted_video_limit =unmuted_video_limit ,version =version ,join_muted =join_muted ,can_change_join_muted =can_change_join_muted ,join_date_asc =join_date_asc ,schedule_start_subscribed =schedule_start_subscribed ,can_start_video =can_start_video ,record_video_active =record_video_active ,rtmp_stream =rtmp_stream ,listeners_hidden =listeners_hidden ,title =title ,stream_dc_id =stream_dc_id ,record_start_date =record_start_date ,schedule_date =schedule_date ,unmuted_video_count =unmuted_video_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .join_muted else 0 
        flags |=(1 <<2 )if self .can_change_join_muted else 0 
        flags |=(1 <<6 )if self .join_date_asc else 0 
        flags |=(1 <<8 )if self .schedule_start_subscribed else 0 
        flags |=(1 <<9 )if self .can_start_video else 0 
        flags |=(1 <<11 )if self .record_video_active else 0 
        flags |=(1 <<12 )if self .rtmp_stream else 0 
        flags |=(1 <<13 )if self .listeners_hidden else 0 
        flags |=(1 <<3 )if self .title is not None else 0 
        flags |=(1 <<4 )if self .stream_dc_id is not None else 0 
        flags |=(1 <<5 )if self .record_start_date is not None else 0 
        flags |=(1 <<7 )if self .schedule_date is not None else 0 
        flags |=(1 <<10 )if self .unmuted_video_count is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .participants_count ))

        if self .title is not None :
            b .write (String (self .title ))

        if self .stream_dc_id is not None :
            b .write (Int (self .stream_dc_id ))

        if self .record_start_date is not None :
            b .write (Int (self .record_start_date ))

        if self .schedule_date is not None :
            b .write (Int (self .schedule_date ))

        if self .unmuted_video_count is not None :
            b .write (Int (self .unmuted_video_count ))

        b .write (Int (self .unmuted_video_limit ))

        b .write (Int (self .version ))

        return b .getvalue ()
