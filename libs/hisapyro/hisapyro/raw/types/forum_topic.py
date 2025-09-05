
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ForumTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["id","date","title","icon_color","top_message","read_inbox_max_id","read_outbox_max_id","unread_count","unread_mentions_count","unread_reactions_count","from_id","notify_settings","my","closed","pinned","short","hidden","icon_emoji_id","draft"]

    ID =0x71701da9 
    QUALNAME ="types.ForumTopic"

    def __init__ (self ,*,id :int ,date :int ,title :str ,icon_color :int ,top_message :int ,read_inbox_max_id :int ,read_outbox_max_id :int ,unread_count :int ,unread_mentions_count :int ,unread_reactions_count :int ,from_id :"raw.base.Peer",notify_settings :"raw.base.PeerNotifySettings",my :Optional [bool ]=None ,closed :Optional [bool ]=None ,pinned :Optional [bool ]=None ,short :Optional [bool ]=None ,hidden :Optional [bool ]=None ,icon_emoji_id :Optional [int ]=None ,draft :"raw.base.DraftMessage"=None )->None :
        self .id =id 
        self .date =date 
        self .title =title 
        self .icon_color =icon_color 
        self .top_message =top_message 
        self .read_inbox_max_id =read_inbox_max_id 
        self .read_outbox_max_id =read_outbox_max_id 
        self .unread_count =unread_count 
        self .unread_mentions_count =unread_mentions_count 
        self .unread_reactions_count =unread_reactions_count 
        self .from_id =from_id 
        self .notify_settings =notify_settings 
        self .my =my 
        self .closed =closed 
        self .pinned =pinned 
        self .short =short 
        self .hidden =hidden 
        self .icon_emoji_id =icon_emoji_id 
        self .draft =draft 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ForumTopic":

        flags =Int .read (b )

        my =True if flags &(1 <<1 )else False 
        closed =True if flags &(1 <<2 )else False 
        pinned =True if flags &(1 <<3 )else False 
        short =True if flags &(1 <<5 )else False 
        hidden =True if flags &(1 <<6 )else False 
        id =Int .read (b )

        date =Int .read (b )

        title =String .read (b )

        icon_color =Int .read (b )

        icon_emoji_id =Long .read (b )if flags &(1 <<0 )else None 
        top_message =Int .read (b )

        read_inbox_max_id =Int .read (b )

        read_outbox_max_id =Int .read (b )

        unread_count =Int .read (b )

        unread_mentions_count =Int .read (b )

        unread_reactions_count =Int .read (b )

        from_id =TLObject .read (b )

        notify_settings =TLObject .read (b )

        draft =TLObject .read (b )if flags &(1 <<4 )else None 

        return ForumTopic (id =id ,date =date ,title =title ,icon_color =icon_color ,top_message =top_message ,read_inbox_max_id =read_inbox_max_id ,read_outbox_max_id =read_outbox_max_id ,unread_count =unread_count ,unread_mentions_count =unread_mentions_count ,unread_reactions_count =unread_reactions_count ,from_id =from_id ,notify_settings =notify_settings ,my =my ,closed =closed ,pinned =pinned ,short =short ,hidden =hidden ,icon_emoji_id =icon_emoji_id ,draft =draft )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .my else 0 
        flags |=(1 <<2 )if self .closed else 0 
        flags |=(1 <<3 )if self .pinned else 0 
        flags |=(1 <<5 )if self .short else 0 
        flags |=(1 <<6 )if self .hidden else 0 
        flags |=(1 <<0 )if self .icon_emoji_id is not None else 0 
        flags |=(1 <<4 )if self .draft is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        b .write (Int (self .date ))

        b .write (String (self .title ))

        b .write (Int (self .icon_color ))

        if self .icon_emoji_id is not None :
            b .write (Long (self .icon_emoji_id ))

        b .write (Int (self .top_message ))

        b .write (Int (self .read_inbox_max_id ))

        b .write (Int (self .read_outbox_max_id ))

        b .write (Int (self .unread_count ))

        b .write (Int (self .unread_mentions_count ))

        b .write (Int (self .unread_reactions_count ))

        b .write (self .from_id .write ())

        b .write (self .notify_settings .write ())

        if self .draft is not None :
            b .write (self .draft .write ())

        return b .getvalue ()
