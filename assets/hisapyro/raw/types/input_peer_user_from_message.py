
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPeerUserFromMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","user_id"]

    ID =0xa87b0a1c 
    QUALNAME ="types.InputPeerUserFromMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",msg_id :int ,user_id :int )->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPeerUserFromMessage":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        user_id =Long .read (b )

        return InputPeerUserFromMessage (peer =peer ,msg_id =msg_id ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
