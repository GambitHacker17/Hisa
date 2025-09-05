
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditForumTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","topic_id","title","icon_emoji_id","closed","hidden"]

    ID =0xf4dfa185 
    QUALNAME ="functions.channels.EditForumTopic"

    def __init__ (self ,*,channel :"raw.base.InputChannel",topic_id :int ,title :Optional [str ]=None ,icon_emoji_id :Optional [int ]=None ,closed :Optional [bool ]=None ,hidden :Optional [bool ]=None )->None :
        self .channel =channel 
        self .topic_id =topic_id 
        self .title =title 
        self .icon_emoji_id =icon_emoji_id 
        self .closed =closed 
        self .hidden =hidden 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditForumTopic":

        flags =Int .read (b )

        channel =TLObject .read (b )

        topic_id =Int .read (b )

        title =String .read (b )if flags &(1 <<0 )else None 
        icon_emoji_id =Long .read (b )if flags &(1 <<1 )else None 
        closed =Bool .read (b )if flags &(1 <<2 )else None 
        hidden =Bool .read (b )if flags &(1 <<3 )else None 
        return EditForumTopic (channel =channel ,topic_id =topic_id ,title =title ,icon_emoji_id =icon_emoji_id ,closed =closed ,hidden =hidden )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .title is not None else 0 
        flags |=(1 <<1 )if self .icon_emoji_id is not None else 0 
        flags |=(1 <<2 )if self .closed is not None else 0 
        flags |=(1 <<3 )if self .hidden is not None else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        b .write (Int (self .topic_id ))

        if self .title is not None :
            b .write (String (self .title ))

        if self .icon_emoji_id is not None :
            b .write (Long (self .icon_emoji_id ))

        if self .closed is not None :
            b .write (Bool (self .closed ))

        if self .hidden is not None :
            b .write (Bool (self .hidden ))

        return b .getvalue ()
