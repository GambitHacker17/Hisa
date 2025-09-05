
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendVote (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","options"]

    ID =0x10ea6184 
    QUALNAME ="functions.messages.SendVote"

    def __init__ (self ,*,peer :"raw.base.InputPeer",msg_id :int ,options :List [bytes ])->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .options =options 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendVote":

        peer =TLObject .read (b )

        msg_id =Int .read (b )

        options =TLObject .read (b ,Bytes )

        return SendVote (peer =peer ,msg_id =msg_id ,options =options )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .msg_id ))

        b .write (Vector (self .options ,Bytes ))

        return b .getvalue ()
