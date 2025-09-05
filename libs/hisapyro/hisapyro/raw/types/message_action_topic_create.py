
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionTopicCreate (TLObject ):
    """"""

    __slots__ :List [str ]=["title","icon_color","icon_emoji_id"]

    ID =0xd999256 
    QUALNAME ="types.MessageActionTopicCreate"

    def __init__ (self ,*,title :str ,icon_color :int ,icon_emoji_id :Optional [int ]=None )->None :
        self .title =title 
        self .icon_color =icon_color 
        self .icon_emoji_id =icon_emoji_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionTopicCreate":

        flags =Int .read (b )

        title =String .read (b )

        icon_color =Int .read (b )

        icon_emoji_id =Long .read (b )if flags &(1 <<0 )else None 
        return MessageActionTopicCreate (title =title ,icon_color =icon_color ,icon_emoji_id =icon_emoji_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .icon_emoji_id is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .title ))

        b .write (Int (self .icon_color ))

        if self .icon_emoji_id is not None :
            b .write (Long (self .icon_emoji_id ))

        return b .getvalue ()
