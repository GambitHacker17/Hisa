
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateReadHistoryOutbox (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","max_id","pts","pts_count"]

    ID =0x2f2f21bf 
    QUALNAME ="types.UpdateReadHistoryOutbox"

    def __init__ (self ,*,peer :"raw.base.Peer",max_id :int ,pts :int ,pts_count :int )->None :
        self .peer =peer 
        self .max_id =max_id 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateReadHistoryOutbox":

        peer =TLObject .read (b )

        max_id =Int .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateReadHistoryOutbox (peer =peer ,max_id =max_id ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .max_id ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
