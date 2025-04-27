
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateReadHistoryInbox (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","max_id","still_unread_count","pts","pts_count","folder_id"]

    ID =0x9c974fdf 
    QUALNAME ="types.UpdateReadHistoryInbox"

    def __init__ (self ,*,peer :"raw.base.Peer",max_id :int ,still_unread_count :int ,pts :int ,pts_count :int ,folder_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .max_id =max_id 
        self .still_unread_count =still_unread_count 
        self .pts =pts 
        self .pts_count =pts_count 
        self .folder_id =folder_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateReadHistoryInbox":

        flags =Int .read (b )

        folder_id =Int .read (b )if flags &(1 <<0 )else None 
        peer =TLObject .read (b )

        max_id =Int .read (b )

        still_unread_count =Int .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateReadHistoryInbox (peer =peer ,max_id =max_id ,still_unread_count =still_unread_count ,pts =pts ,pts_count =pts_count ,folder_id =folder_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .folder_id is not None else 0 
        b .write (Int (flags ))

        if self .folder_id is not None :
            b .write (Int (self .folder_id ))

        b .write (self .peer .write ())

        b .write (Int (self .max_id ))

        b .write (Int (self .still_unread_count ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
