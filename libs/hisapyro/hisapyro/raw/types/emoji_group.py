
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiGroup (TLObject ):
    """"""

    __slots__ :List [str ]=["title","icon_emoji_id","emoticons"]

    ID =0x7a9abda9 
    QUALNAME ="types.EmojiGroup"

    def __init__ (self ,*,title :str ,icon_emoji_id :int ,emoticons :List [str ])->None :
        self .title =title 
        self .icon_emoji_id =icon_emoji_id 
        self .emoticons =emoticons 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiGroup":

        title =String .read (b )

        icon_emoji_id =Long .read (b )

        emoticons =TLObject .read (b ,String )

        return EmojiGroup (title =title ,icon_emoji_id =icon_emoji_id ,emoticons =emoticons )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .title ))

        b .write (Long (self .icon_emoji_id ))

        b .write (Vector (self .emoticons ,String ))

        return b .getvalue ()
