
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetDiscussionMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id"]

    ID =0x446972fd 
    QUALNAME ="functions.messages.GetDiscussionMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",msg_id :int )->None :
        self .peer =peer 
        self .msg_id =msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetDiscussionMessage":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        return GetDiscussionMessage (peer =peer ,msg_id =msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        return b .getvalue ()
