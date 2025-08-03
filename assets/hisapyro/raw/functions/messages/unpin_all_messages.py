
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UnpinAllMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","top_msg_id"]

    ID =0xee22b9a8 
    QUALNAME ="functions.messages.UnpinAllMessages"

    def __init__ (self ,*,peer :"raw.base.InputPeer",top_msg_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UnpinAllMessages":

        flags =Int .read (b )

        peer =TLObject .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        return UnpinAllMessages (peer =peer ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        return b .getvalue ()
