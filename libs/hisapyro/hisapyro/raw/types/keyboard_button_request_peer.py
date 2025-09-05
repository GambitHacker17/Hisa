
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonRequestPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["text","button_id","peer_type"]

    ID =0xd0b468c 
    QUALNAME ="types.KeyboardButtonRequestPeer"

    def __init__ (self ,*,text :str ,button_id :int ,peer_type :"raw.base.RequestPeerType")->None :
        self .text =text 
        self .button_id =button_id 
        self .peer_type =peer_type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonRequestPeer":

        text =String .read (b )

        button_id =Int .read (b )

        peer_type =TLObject .read (b )

        return KeyboardButtonRequestPeer (text =text ,button_id =button_id ,peer_type =peer_type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (Int (self .button_id ))

        b .write (self .peer_type .write ())

        return b .getvalue ()
