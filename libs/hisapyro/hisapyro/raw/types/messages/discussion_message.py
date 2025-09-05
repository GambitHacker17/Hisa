
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DiscussionMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["messages","unread_count","chats","users","max_id","read_inbox_max_id","read_outbox_max_id"]

    ID =0xa6341782 
    QUALNAME ="types.messages.DiscussionMessage"

    def __init__ (self ,*,messages :List ["raw.base.Message"],unread_count :int ,chats :List ["raw.base.Chat"],users :List ["raw.base.User"],max_id :Optional [int ]=None ,read_inbox_max_id :Optional [int ]=None ,read_outbox_max_id :Optional [int ]=None )->None :
        self .messages =messages 
        self .unread_count =unread_count 
        self .chats =chats 
        self .users =users 
        self .max_id =max_id 
        self .read_inbox_max_id =read_inbox_max_id 
        self .read_outbox_max_id =read_outbox_max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DiscussionMessage":

        flags =Int .read (b )

        messages =TLObject .read (b )

        max_id =Int .read (b )if flags &(1 <<0 )else None 
        read_inbox_max_id =Int .read (b )if flags &(1 <<1 )else None 
        read_outbox_max_id =Int .read (b )if flags &(1 <<2 )else None 
        unread_count =Int .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return DiscussionMessage (messages =messages ,unread_count =unread_count ,chats =chats ,users =users ,max_id =max_id ,read_inbox_max_id =read_inbox_max_id ,read_outbox_max_id =read_outbox_max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .max_id is not None else 0 
        flags |=(1 <<1 )if self .read_inbox_max_id is not None else 0 
        flags |=(1 <<2 )if self .read_outbox_max_id is not None else 0 
        b .write (Int (flags ))

        b .write (Vector (self .messages ))

        if self .max_id is not None :
            b .write (Int (self .max_id ))

        if self .read_inbox_max_id is not None :
            b .write (Int (self .read_inbox_max_id ))

        if self .read_outbox_max_id is not None :
            b .write (Int (self .read_outbox_max_id ))

        b .write (Int (self .unread_count ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
