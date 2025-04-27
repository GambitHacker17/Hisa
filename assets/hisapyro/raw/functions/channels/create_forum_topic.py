
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CreateForumTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","title","random_id","icon_color","icon_emoji_id","send_as"]

    ID =0xf40c0224 
    QUALNAME ="functions.channels.CreateForumTopic"

    def __init__ (self ,*,channel :"raw.base.InputChannel",title :str ,random_id :int ,icon_color :Optional [int ]=None ,icon_emoji_id :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .channel =channel 
        self .title =title 
        self .random_id =random_id 
        self .icon_color =icon_color 
        self .icon_emoji_id =icon_emoji_id 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CreateForumTopic":

        flags =Int .read (b )

        channel =TLObject .read (b )

        title =String .read (b )

        icon_color =Int .read (b )if flags &(1 <<0 )else None 
        icon_emoji_id =Long .read (b )if flags &(1 <<3 )else None 
        random_id =Long .read (b )

        send_as =TLObject .read (b )if flags &(1 <<2 )else None 

        return CreateForumTopic (channel =channel ,title =title ,random_id =random_id ,icon_color =icon_color ,icon_emoji_id =icon_emoji_id ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .icon_color is not None else 0 
        flags |=(1 <<3 )if self .icon_emoji_id is not None else 0 
        flags |=(1 <<2 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        b .write (String (self .title ))

        if self .icon_color is not None :
            b .write (Int (self .icon_color ))

        if self .icon_emoji_id is not None :
            b .write (Long (self .icon_emoji_id ))

        b .write (Long (self .random_id ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
