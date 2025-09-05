
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputNotifyForumTopic (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","top_msg_id"]

    ID =0x5c467992 
    QUALNAME ="types.InputNotifyForumTopic"

    def __init__ (self ,*,peer :"raw.base.InputPeer",top_msg_id :int )->None :
        self .peer =peer 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputNotifyForumTopic":

        peer =TLObject .read (b )

        top_msg_id =Int .read (b )

        return InputNotifyForumTopic (peer =peer ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .top_msg_id ))

        return b .getvalue ()
