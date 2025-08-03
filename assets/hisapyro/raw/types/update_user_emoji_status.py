
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateUserEmojiStatus (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","emoji_status"]

    ID =0x28373599 
    QUALNAME ="types.UpdateUserEmojiStatus"

    def __init__ (self ,*,user_id :int ,emoji_status :"raw.base.EmojiStatus")->None :
        self .user_id =user_id 
        self .emoji_status =emoji_status 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateUserEmojiStatus":

        user_id =Long .read (b )

        emoji_status =TLObject .read (b )

        return UpdateUserEmojiStatus (user_id =user_id ,emoji_status =emoji_status )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .user_id ))

        b .write (self .emoji_status .write ())

        return b .getvalue ()
