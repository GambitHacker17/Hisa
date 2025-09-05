
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPeerChannelFromMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","channel_id"]

    ID =0xbd2a0840 
    QUALNAME ="types.InputPeerChannelFromMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",msg_id :int ,channel_id :int )->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .channel_id =channel_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPeerChannelFromMessage":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        channel_id =Long .read (b )

        return InputPeerChannelFromMessage (peer =peer ,msg_id =msg_id ,channel_id =channel_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        b .write (Long (self .channel_id ))

        return b .getvalue ()
