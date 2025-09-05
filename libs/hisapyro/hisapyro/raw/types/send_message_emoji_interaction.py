
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendMessageEmojiInteraction (TLObject ):
    """"""

    __slots__ :List [str ]=["emoticon","msg_id","interaction"]

    ID =0x25972bcb 
    QUALNAME ="types.SendMessageEmojiInteraction"

    def __init__ (self ,*,emoticon :str ,msg_id :int ,interaction :"raw.base.DataJSON")->None :
        self .emoticon =emoticon 
        self .msg_id =msg_id 
        self .interaction =interaction 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendMessageEmojiInteraction":

        emoticon =String .read (b )

        msg_id =Int .read (b )

        interaction =TLObject .read (b )

        return SendMessageEmojiInteraction (emoticon =emoticon ,msg_id =msg_id ,interaction =interaction )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .emoticon ))

        b .write (Int (self .msg_id ))

        b .write (self .interaction .write ())

        return b .getvalue ()
