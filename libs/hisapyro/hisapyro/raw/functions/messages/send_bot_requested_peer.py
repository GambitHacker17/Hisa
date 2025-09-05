
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendBotRequestedPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","button_id","requested_peer"]

    ID =0xfe38d01b 
    QUALNAME ="functions.messages.SendBotRequestedPeer"

    def __init__ (self ,*,peer :"raw.base.InputPeer",msg_id :int ,button_id :int ,requested_peer :"raw.base.InputPeer")->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .button_id =button_id 
        self .requested_peer =requested_peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendBotRequestedPeer":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        button_id =Int .read (b )

        requested_peer =TLObject .read (b )

        return SendBotRequestedPeer (peer =peer ,msg_id =msg_id ,button_id =button_id ,requested_peer =requested_peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        b .write (Int (self .button_id ))

        b .write (self .requested_peer .write ())

        return b .getvalue ()
