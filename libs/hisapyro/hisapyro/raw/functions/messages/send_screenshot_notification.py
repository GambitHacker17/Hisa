
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendScreenshotNotification (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","reply_to_msg_id","random_id"]

    ID =0xc97df020 
    QUALNAME ="functions.messages.SendScreenshotNotification"

    def __init__ (self ,*,peer :"raw.base.InputPeer",reply_to_msg_id :int ,random_id :int )->None :
        self .peer =peer 
        self .reply_to_msg_id =reply_to_msg_id 
        self .random_id =random_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendScreenshotNotification":

        peer =TLObject .read (b )

        reply_to_msg_id =Int .read (b )

        random_id =Long .read (b )

        return SendScreenshotNotification (peer =peer ,reply_to_msg_id =reply_to_msg_id ,random_id =random_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .reply_to_msg_id ))

        b .write (Long (self .random_id ))

        return b .getvalue ()
