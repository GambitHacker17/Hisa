
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionChannelMigrateFrom (TLObject ):
    """"""

    __slots__ :List [str ]=["title","chat_id"]

    ID =0xea3948e9 
    QUALNAME ="types.MessageActionChannelMigrateFrom"

    def __init__ (self ,*,title :str ,chat_id :int )->None :
        self .title =title 
        self .chat_id =chat_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionChannelMigrateFrom":

        title =String .read (b )

        chat_id =Long .read (b )

        return MessageActionChannelMigrateFrom (title =title ,chat_id =chat_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .title ))

        b .write (Long (self .chat_id ))

        return b .getvalue ()
