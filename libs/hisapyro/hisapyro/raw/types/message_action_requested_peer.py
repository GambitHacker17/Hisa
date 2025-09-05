
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionRequestedPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["button_id","peer"]

    ID =0xfe77345d 
    QUALNAME ="types.MessageActionRequestedPeer"

    def __init__ (self ,*,button_id :int ,peer :"raw.base.Peer")->None :
        self .button_id =button_id 
        self .peer =peer 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionRequestedPeer":

        button_id =Int .read (b )

        peer =TLObject .read (b )

        return MessageActionRequestedPeer (button_id =button_id ,peer =peer )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .button_id ))

        b .write (self .peer .write ())

        return b .getvalue ()
