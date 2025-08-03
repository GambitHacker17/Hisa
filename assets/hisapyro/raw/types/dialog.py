
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Dialog (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","top_message","read_inbox_max_id","read_outbox_max_id","unread_count","unread_mentions_count","unread_reactions_count","notify_settings","pinned","unread_mark","pts","draft","folder_id","ttl_period"]

    ID =0xd58a08c6 
    QUALNAME ="types.Dialog"

    def __init__ (self ,*,peer :"raw.base.Peer",top_message :int ,read_inbox_max_id :int ,read_outbox_max_id :int ,unread_count :int ,unread_mentions_count :int ,unread_reactions_count :int ,notify_settings :"raw.base.PeerNotifySettings",pinned :Optional [bool ]=None ,unread_mark :Optional [bool ]=None ,pts :Optional [int ]=None ,draft :"raw.base.DraftMessage"=None ,folder_id :Optional [int ]=None ,ttl_period :Optional [int ]=None )->None :
        self .peer =peer 
        self .top_message =top_message 
        self .read_inbox_max_id =read_inbox_max_id 
        self .read_outbox_max_id =read_outbox_max_id 
        self .unread_count =unread_count 
        self .unread_mentions_count =unread_mentions_count 
        self .unread_reactions_count =unread_reactions_count 
        self .notify_settings =notify_settings 
        self .pinned =pinned 
        self .unread_mark =unread_mark 
        self .pts =pts 
        self .draft =draft 
        self .folder_id =folder_id 
        self .ttl_period =ttl_period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Dialog":

        flags =Int .read (b )

        pinned =True if flags &(1 <<2 )else False 
        unread_mark =True if flags &(1 <<3 )else False 
        peer =TLObject .read (b )

        top_message =Int .read (b )

        read_inbox_max_id =Int .read (b )

        read_outbox_max_id =Int .read (b )

        unread_count =Int .read (b )

        unread_mentions_count =Int .read (b )

        unread_reactions_count =Int .read (b )

        notify_settings =TLObject .read (b )

        pts =Int .read (b )if flags &(1 <<0 )else None 
        draft =TLObject .read (b )if flags &(1 <<1 )else None 

        folder_id =Int .read (b )if flags &(1 <<4 )else None 
        ttl_period =Int .read (b )if flags &(1 <<5 )else None 
        return Dialog (peer =peer ,top_message =top_message ,read_inbox_max_id =read_inbox_max_id ,read_outbox_max_id =read_outbox_max_id ,unread_count =unread_count ,unread_mentions_count =unread_mentions_count ,unread_reactions_count =unread_reactions_count ,notify_settings =notify_settings ,pinned =pinned ,unread_mark =unread_mark ,pts =pts ,draft =draft ,folder_id =folder_id ,ttl_period =ttl_period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .pinned else 0 
        flags |=(1 <<3 )if self .unread_mark else 0 
        flags |=(1 <<0 )if self .pts is not None else 0 
        flags |=(1 <<1 )if self .draft is not None else 0 
        flags |=(1 <<4 )if self .folder_id is not None else 0 
        flags |=(1 <<5 )if self .ttl_period is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .top_message ))

        b .write (Int (self .read_inbox_max_id ))

        b .write (Int (self .read_outbox_max_id ))

        b .write (Int (self .unread_count ))

        b .write (Int (self .unread_mentions_count ))

        b .write (Int (self .unread_reactions_count ))

        b .write (self .notify_settings .write ())

        if self .pts is not None :
            b .write (Int (self .pts ))

        if self .draft is not None :
            b .write (self .draft .write ())

        if self .folder_id is not None :
            b .write (Int (self .folder_id ))

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        return b .getvalue ()
