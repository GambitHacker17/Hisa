
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateMessageExtendedMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","extended_media"]

    ID =0x5a73a98c 
    QUALNAME ="types.UpdateMessageExtendedMedia"

    def __init__ (self ,*,peer :"raw.base.Peer",msg_id :int ,extended_media :"raw.base.MessageExtendedMedia")->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .extended_media =extended_media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateMessageExtendedMedia":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        extended_media =TLObject .read (b )

        return UpdateMessageExtendedMedia (peer =peer ,msg_id =msg_id ,extended_media =extended_media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        b .write (self .extended_media .write ())

        return b .getvalue ()
