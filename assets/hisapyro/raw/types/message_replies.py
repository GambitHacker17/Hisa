
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageReplies (TLObject ):
    """"""

    __slots__ :List [str ]=["replies","replies_pts","comments","recent_repliers","channel_id","max_id","read_max_id"]

    ID =0x83d60fc2 
    QUALNAME ="types.MessageReplies"

    def __init__ (self ,*,replies :int ,replies_pts :int ,comments :Optional [bool ]=None ,recent_repliers :Optional [List ["raw.base.Peer"]]=None ,channel_id :Optional [int ]=None ,max_id :Optional [int ]=None ,read_max_id :Optional [int ]=None )->None :
        self .replies =replies 
        self .replies_pts =replies_pts 
        self .comments =comments 
        self .recent_repliers =recent_repliers 
        self .channel_id =channel_id 
        self .max_id =max_id 
        self .read_max_id =read_max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageReplies":

        flags =Int .read (b )

        comments =True if flags &(1 <<0 )else False 
        replies =Int .read (b )

        replies_pts =Int .read (b )

        recent_repliers =TLObject .read (b )if flags &(1 <<1 )else []

        channel_id =Long .read (b )if flags &(1 <<0 )else None 
        max_id =Int .read (b )if flags &(1 <<2 )else None 
        read_max_id =Int .read (b )if flags &(1 <<3 )else None 
        return MessageReplies (replies =replies ,replies_pts =replies_pts ,comments =comments ,recent_repliers =recent_repliers ,channel_id =channel_id ,max_id =max_id ,read_max_id =read_max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .comments else 0 
        flags |=(1 <<1 )if self .recent_repliers else 0 
        flags |=(1 <<0 )if self .channel_id is not None else 0 
        flags |=(1 <<2 )if self .max_id is not None else 0 
        flags |=(1 <<3 )if self .read_max_id is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .replies ))

        b .write (Int (self .replies_pts ))

        if self .recent_repliers is not None :
            b .write (Vector (self .recent_repliers ))

        if self .channel_id is not None :
            b .write (Long (self .channel_id ))

        if self .max_id is not None :
            b .write (Int (self .max_id ))

        if self .read_max_id is not None :
            b .write (Int (self .read_max_id ))

        return b .getvalue ()
