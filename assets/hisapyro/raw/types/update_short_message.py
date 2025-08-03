
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateShortMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["id","user_id","message","pts","pts_count","date","out","mentioned","media_unread","silent","fwd_from","via_bot_id","reply_to","entities","ttl_period"]

    ID =0x313bc7f8 
    QUALNAME ="types.UpdateShortMessage"

    def __init__ (self ,*,id :int ,user_id :int ,message :str ,pts :int ,pts_count :int ,date :int ,out :Optional [bool ]=None ,mentioned :Optional [bool ]=None ,media_unread :Optional [bool ]=None ,silent :Optional [bool ]=None ,fwd_from :"raw.base.MessageFwdHeader"=None ,via_bot_id :Optional [int ]=None ,reply_to :"raw.base.MessageReplyHeader"=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,ttl_period :Optional [int ]=None )->None :
        self .id =id 
        self .user_id =user_id 
        self .message =message 
        self .pts =pts 
        self .pts_count =pts_count 
        self .date =date 
        self .out =out 
        self .mentioned =mentioned 
        self .media_unread =media_unread 
        self .silent =silent 
        self .fwd_from =fwd_from 
        self .via_bot_id =via_bot_id 
        self .reply_to =reply_to 
        self .entities =entities 
        self .ttl_period =ttl_period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateShortMessage":

        flags =Int .read (b )

        out =True if flags &(1 <<1 )else False 
        mentioned =True if flags &(1 <<4 )else False 
        media_unread =True if flags &(1 <<5 )else False 
        silent =True if flags &(1 <<13 )else False 
        id =Int .read (b )

        user_id =Long .read (b )

        message =String .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        date =Int .read (b )

        fwd_from =TLObject .read (b )if flags &(1 <<2 )else None 

        via_bot_id =Long .read (b )if flags &(1 <<11 )else None 
        reply_to =TLObject .read (b )if flags &(1 <<3 )else None 

        entities =TLObject .read (b )if flags &(1 <<7 )else []

        ttl_period =Int .read (b )if flags &(1 <<25 )else None 
        return UpdateShortMessage (id =id ,user_id =user_id ,message =message ,pts =pts ,pts_count =pts_count ,date =date ,out =out ,mentioned =mentioned ,media_unread =media_unread ,silent =silent ,fwd_from =fwd_from ,via_bot_id =via_bot_id ,reply_to =reply_to ,entities =entities ,ttl_period =ttl_period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .out else 0 
        flags |=(1 <<4 )if self .mentioned else 0 
        flags |=(1 <<5 )if self .media_unread else 0 
        flags |=(1 <<13 )if self .silent else 0 
        flags |=(1 <<2 )if self .fwd_from is not None else 0 
        flags |=(1 <<11 )if self .via_bot_id is not None else 0 
        flags |=(1 <<3 )if self .reply_to is not None else 0 
        flags |=(1 <<7 )if self .entities else 0 
        flags |=(1 <<25 )if self .ttl_period is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        b .write (Long (self .user_id ))

        b .write (String (self .message ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        b .write (Int (self .date ))

        if self .fwd_from is not None :
            b .write (self .fwd_from .write ())

        if self .via_bot_id is not None :
            b .write (Long (self .via_bot_id ))

        if self .reply_to is not None :
            b .write (self .reply_to .write ())

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        return b .getvalue ()
