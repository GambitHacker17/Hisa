
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Message (TLObject ):
    """"""

    __slots__ :List [str ]=["id","peer_id","date","message","out","mentioned","media_unread","silent","post","from_scheduled","legacy","edit_hide","pinned","noforwards","from_id","fwd_from","via_bot_id","reply_to","media","reply_markup","entities","views","forwards","replies","edit_date","post_author","grouped_id","reactions","restriction_reason","ttl_period"]

    ID =0x38116ee0 
    QUALNAME ="types.Message"

    def __init__ (self ,*,id :int ,peer_id :"raw.base.Peer",date :int ,message :str ,out :Optional [bool ]=None ,mentioned :Optional [bool ]=None ,media_unread :Optional [bool ]=None ,silent :Optional [bool ]=None ,post :Optional [bool ]=None ,from_scheduled :Optional [bool ]=None ,legacy :Optional [bool ]=None ,edit_hide :Optional [bool ]=None ,pinned :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,from_id :"raw.base.Peer"=None ,fwd_from :"raw.base.MessageFwdHeader"=None ,via_bot_id :Optional [int ]=None ,reply_to :"raw.base.MessageReplyHeader"=None ,media :"raw.base.MessageMedia"=None ,reply_markup :"raw.base.ReplyMarkup"=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,views :Optional [int ]=None ,forwards :Optional [int ]=None ,replies :"raw.base.MessageReplies"=None ,edit_date :Optional [int ]=None ,post_author :Optional [str ]=None ,grouped_id :Optional [int ]=None ,reactions :"raw.base.MessageReactions"=None ,restriction_reason :Optional [List ["raw.base.RestrictionReason"]]=None ,ttl_period :Optional [int ]=None )->None :
        self .id =id 
        self .peer_id =peer_id 
        self .date =date 
        self .message =message 
        self .out =out 
        self .mentioned =mentioned 
        self .media_unread =media_unread 
        self .silent =silent 
        self .post =post 
        self .from_scheduled =from_scheduled 
        self .legacy =legacy 
        self .edit_hide =edit_hide 
        self .pinned =pinned 
        self .noforwards =noforwards 
        self .from_id =from_id 
        self .fwd_from =fwd_from 
        self .via_bot_id =via_bot_id 
        self .reply_to =reply_to 
        self .media =media 
        self .reply_markup =reply_markup 
        self .entities =entities 
        self .views =views 
        self .forwards =forwards 
        self .replies =replies 
        self .edit_date =edit_date 
        self .post_author =post_author 
        self .grouped_id =grouped_id 
        self .reactions =reactions 
        self .restriction_reason =restriction_reason 
        self .ttl_period =ttl_period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Message":

        flags =Int .read (b )

        out =True if flags &(1 <<1 )else False 
        mentioned =True if flags &(1 <<4 )else False 
        media_unread =True if flags &(1 <<5 )else False 
        silent =True if flags &(1 <<13 )else False 
        post =True if flags &(1 <<14 )else False 
        from_scheduled =True if flags &(1 <<18 )else False 
        legacy =True if flags &(1 <<19 )else False 
        edit_hide =True if flags &(1 <<21 )else False 
        pinned =True if flags &(1 <<24 )else False 
        noforwards =True if flags &(1 <<26 )else False 
        id =Int .read (b )

        from_id =TLObject .read (b )if flags &(1 <<8 )else None 

        peer_id =TLObject .read (b )

        fwd_from =TLObject .read (b )if flags &(1 <<2 )else None 

        via_bot_id =Long .read (b )if flags &(1 <<11 )else None 
        reply_to =TLObject .read (b )if flags &(1 <<3 )else None 

        date =Int .read (b )

        message =String .read (b )

        media =TLObject .read (b )if flags &(1 <<9 )else None 

        reply_markup =TLObject .read (b )if flags &(1 <<6 )else None 

        entities =TLObject .read (b )if flags &(1 <<7 )else []

        views =Int .read (b )if flags &(1 <<10 )else None 
        forwards =Int .read (b )if flags &(1 <<10 )else None 
        replies =TLObject .read (b )if flags &(1 <<23 )else None 

        edit_date =Int .read (b )if flags &(1 <<15 )else None 
        post_author =String .read (b )if flags &(1 <<16 )else None 
        grouped_id =Long .read (b )if flags &(1 <<17 )else None 
        reactions =TLObject .read (b )if flags &(1 <<20 )else None 

        restriction_reason =TLObject .read (b )if flags &(1 <<22 )else []

        ttl_period =Int .read (b )if flags &(1 <<25 )else None 
        return Message (id =id ,peer_id =peer_id ,date =date ,message =message ,out =out ,mentioned =mentioned ,media_unread =media_unread ,silent =silent ,post =post ,from_scheduled =from_scheduled ,legacy =legacy ,edit_hide =edit_hide ,pinned =pinned ,noforwards =noforwards ,from_id =from_id ,fwd_from =fwd_from ,via_bot_id =via_bot_id ,reply_to =reply_to ,media =media ,reply_markup =reply_markup ,entities =entities ,views =views ,forwards =forwards ,replies =replies ,edit_date =edit_date ,post_author =post_author ,grouped_id =grouped_id ,reactions =reactions ,restriction_reason =restriction_reason ,ttl_period =ttl_period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .out else 0 
        flags |=(1 <<4 )if self .mentioned else 0 
        flags |=(1 <<5 )if self .media_unread else 0 
        flags |=(1 <<13 )if self .silent else 0 
        flags |=(1 <<14 )if self .post else 0 
        flags |=(1 <<18 )if self .from_scheduled else 0 
        flags |=(1 <<19 )if self .legacy else 0 
        flags |=(1 <<21 )if self .edit_hide else 0 
        flags |=(1 <<24 )if self .pinned else 0 
        flags |=(1 <<26 )if self .noforwards else 0 
        flags |=(1 <<8 )if self .from_id is not None else 0 
        flags |=(1 <<2 )if self .fwd_from is not None else 0 
        flags |=(1 <<11 )if self .via_bot_id is not None else 0 
        flags |=(1 <<3 )if self .reply_to is not None else 0 
        flags |=(1 <<9 )if self .media is not None else 0 
        flags |=(1 <<6 )if self .reply_markup is not None else 0 
        flags |=(1 <<7 )if self .entities else 0 
        flags |=(1 <<10 )if self .views is not None else 0 
        flags |=(1 <<10 )if self .forwards is not None else 0 
        flags |=(1 <<23 )if self .replies is not None else 0 
        flags |=(1 <<15 )if self .edit_date is not None else 0 
        flags |=(1 <<16 )if self .post_author is not None else 0 
        flags |=(1 <<17 )if self .grouped_id is not None else 0 
        flags |=(1 <<20 )if self .reactions is not None else 0 
        flags |=(1 <<22 )if self .restriction_reason else 0 
        flags |=(1 <<25 )if self .ttl_period is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        if self .from_id is not None :
            b .write (self .from_id .write ())

        b .write (self .peer_id .write ())

        if self .fwd_from is not None :
            b .write (self .fwd_from .write ())

        if self .via_bot_id is not None :
            b .write (Long (self .via_bot_id ))

        if self .reply_to is not None :
            b .write (self .reply_to .write ())

        b .write (Int (self .date ))

        b .write (String (self .message ))

        if self .media is not None :
            b .write (self .media .write ())

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .views is not None :
            b .write (Int (self .views ))

        if self .forwards is not None :
            b .write (Int (self .forwards ))

        if self .replies is not None :
            b .write (self .replies .write ())

        if self .edit_date is not None :
            b .write (Int (self .edit_date ))

        if self .post_author is not None :
            b .write (String (self .post_author ))

        if self .grouped_id is not None :
            b .write (Long (self .grouped_id ))

        if self .reactions is not None :
            b .write (self .reactions .write ())

        if self .restriction_reason is not None :
            b .write (Vector (self .restriction_reason ))

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        return b .getvalue ()
