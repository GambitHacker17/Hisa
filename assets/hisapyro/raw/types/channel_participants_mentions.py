
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipantsMentions (TLObject ):
    """"""

    __slots__ :List [str ]=["q","top_msg_id"]

    ID =0xe04b5ceb 
    QUALNAME ="types.ChannelParticipantsMentions"

    def __init__ (self ,*,q :Optional [str ]=None ,top_msg_id :Optional [int ]=None )->None :
        self .q =q 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipantsMentions":

        flags =Int .read (b )

        q =String .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<1 )else None 
        return ChannelParticipantsMentions (q =q ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .q is not None else 0 
        flags |=(1 <<1 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        if self .q is not None :
            b .write (String (self .q ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        return b .getvalue ()
