
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageReplyHeader (TLObject ):
    """"""

    __slots__ :List [str ]=["reply_to_msg_id","reply_to_scheduled","forum_topic","reply_to_peer_id","reply_to_top_id"]

    ID =0xa6d57763 
    QUALNAME ="types.MessageReplyHeader"

    def __init__ (self ,*,reply_to_msg_id :int ,reply_to_scheduled :Optional [bool ]=None ,forum_topic :Optional [bool ]=None ,reply_to_peer_id :"raw.base.Peer"=None ,reply_to_top_id :Optional [int ]=None )->None :
        self .reply_to_msg_id =reply_to_msg_id 
        self .reply_to_scheduled =reply_to_scheduled 
        self .forum_topic =forum_topic 
        self .reply_to_peer_id =reply_to_peer_id 
        self .reply_to_top_id =reply_to_top_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageReplyHeader":

        flags =Int .read (b )

        reply_to_scheduled =True if flags &(1 <<2 )else False 
        forum_topic =True if flags &(1 <<3 )else False 
        reply_to_msg_id =Int .read (b )

        reply_to_peer_id =TLObject .read (b )if flags &(1 <<0 )else None 

        reply_to_top_id =Int .read (b )if flags &(1 <<1 )else None 
        return MessageReplyHeader (reply_to_msg_id =reply_to_msg_id ,reply_to_scheduled =reply_to_scheduled ,forum_topic =forum_topic ,reply_to_peer_id =reply_to_peer_id ,reply_to_top_id =reply_to_top_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .reply_to_scheduled else 0 
        flags |=(1 <<3 )if self .forum_topic else 0 
        flags |=(1 <<0 )if self .reply_to_peer_id is not None else 0 
        flags |=(1 <<1 )if self .reply_to_top_id is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .reply_to_msg_id ))

        if self .reply_to_peer_id is not None :
            b .write (self .reply_to_peer_id .write ())

        if self .reply_to_top_id is not None :
            b .write (Int (self .reply_to_top_id ))

        return b .getvalue ()
