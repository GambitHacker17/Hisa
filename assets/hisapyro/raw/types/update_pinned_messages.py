
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePinnedMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","messages","pts","pts_count","pinned"]

    ID =0xed85eab5 
    QUALNAME ="types.UpdatePinnedMessages"

    def __init__ (self ,*,peer :"raw.base.Peer",messages :List [int ],pts :int ,pts_count :int ,pinned :Optional [bool ]=None )->None :
        self .peer =peer 
        self .messages =messages 
        self .pts =pts 
        self .pts_count =pts_count 
        self .pinned =pinned 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePinnedMessages":

        flags =Int .read (b )

        pinned =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        messages =TLObject .read (b ,Int )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdatePinnedMessages (peer =peer ,messages =messages ,pts =pts ,pts_count =pts_count ,pinned =pinned )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pinned else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Vector (self .messages ,Int ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
