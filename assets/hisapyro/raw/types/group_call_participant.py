
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCallParticipant (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","date","source","muted","left","can_self_unmute","just_joined","versioned","min","muted_by_you","volume_by_admin","is_self","video_joined","active_date","volume","about","raise_hand_rating","video","presentation"]

    ID =0xeba636fe 
    QUALNAME ="types.GroupCallParticipant"

    def __init__ (self ,*,peer :"raw.base.Peer",date :int ,source :int ,muted :Optional [bool ]=None ,left :Optional [bool ]=None ,can_self_unmute :Optional [bool ]=None ,just_joined :Optional [bool ]=None ,versioned :Optional [bool ]=None ,min :Optional [bool ]=None ,muted_by_you :Optional [bool ]=None ,volume_by_admin :Optional [bool ]=None ,is_self :Optional [bool ]=None ,video_joined :Optional [bool ]=None ,active_date :Optional [int ]=None ,volume :Optional [int ]=None ,about :Optional [str ]=None ,raise_hand_rating :Optional [int ]=None ,video :"raw.base.GroupCallParticipantVideo"=None ,presentation :"raw.base.GroupCallParticipantVideo"=None )->None :
        self .peer =peer 
        self .date =date 
        self .source =source 
        self .muted =muted 
        self .left =left 
        self .can_self_unmute =can_self_unmute 
        self .just_joined =just_joined 
        self .versioned =versioned 
        self .min =min 
        self .muted_by_you =muted_by_you 
        self .volume_by_admin =volume_by_admin 
        self .is_self =is_self 
        self .video_joined =video_joined 
        self .active_date =active_date 
        self .volume =volume 
        self .about =about 
        self .raise_hand_rating =raise_hand_rating 
        self .video =video 
        self .presentation =presentation 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCallParticipant":

        flags =Int .read (b )

        muted =True if flags &(1 <<0 )else False 
        left =True if flags &(1 <<1 )else False 
        can_self_unmute =True if flags &(1 <<2 )else False 
        just_joined =True if flags &(1 <<4 )else False 
        versioned =True if flags &(1 <<5 )else False 
        min =True if flags &(1 <<8 )else False 
        muted_by_you =True if flags &(1 <<9 )else False 
        volume_by_admin =True if flags &(1 <<10 )else False 
        is_self =True if flags &(1 <<12 )else False 
        video_joined =True if flags &(1 <<15 )else False 
        peer =TLObject .read (b )

        date =Int .read (b )

        active_date =Int .read (b )if flags &(1 <<3 )else None 
        source =Int .read (b )

        volume =Int .read (b )if flags &(1 <<7 )else None 
        about =String .read (b )if flags &(1 <<11 )else None 
        raise_hand_rating =Long .read (b )if flags &(1 <<13 )else None 
        video =TLObject .read (b )if flags &(1 <<6 )else None 

        presentation =TLObject .read (b )if flags &(1 <<14 )else None 

        return GroupCallParticipant (peer =peer ,date =date ,source =source ,muted =muted ,left =left ,can_self_unmute =can_self_unmute ,just_joined =just_joined ,versioned =versioned ,min =min ,muted_by_you =muted_by_you ,volume_by_admin =volume_by_admin ,is_self =is_self ,video_joined =video_joined ,active_date =active_date ,volume =volume ,about =about ,raise_hand_rating =raise_hand_rating ,video =video ,presentation =presentation )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .muted else 0 
        flags |=(1 <<1 )if self .left else 0 
        flags |=(1 <<2 )if self .can_self_unmute else 0 
        flags |=(1 <<4 )if self .just_joined else 0 
        flags |=(1 <<5 )if self .versioned else 0 
        flags |=(1 <<8 )if self .min else 0 
        flags |=(1 <<9 )if self .muted_by_you else 0 
        flags |=(1 <<10 )if self .volume_by_admin else 0 
        flags |=(1 <<12 )if self .is_self else 0 
        flags |=(1 <<15 )if self .video_joined else 0 
        flags |=(1 <<3 )if self .active_date is not None else 0 
        flags |=(1 <<7 )if self .volume is not None else 0 
        flags |=(1 <<11 )if self .about is not None else 0 
        flags |=(1 <<13 )if self .raise_hand_rating is not None else 0 
        flags |=(1 <<6 )if self .video is not None else 0 
        flags |=(1 <<14 )if self .presentation is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .date ))

        if self .active_date is not None :
            b .write (Int (self .active_date ))

        b .write (Int (self .source ))

        if self .volume is not None :
            b .write (Int (self .volume ))

        if self .about is not None :
            b .write (String (self .about ))

        if self .raise_hand_rating is not None :
            b .write (Long (self .raise_hand_rating ))

        if self .video is not None :
            b .write (self .video .write ())

        if self .presentation is not None :
            b .write (self .presentation .write ())

        return b .getvalue ()
