
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateFolderPeers (TLObject ):
    """"""

    __slots__ :List [str ]=["folder_peers","pts","pts_count"]

    ID =0x19360dc0 
    QUALNAME ="types.UpdateFolderPeers"

    def __init__ (self ,*,folder_peers :List ["raw.base.FolderPeer"],pts :int ,pts_count :int )->None :
        self .folder_peers =folder_peers 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateFolderPeers":

        folder_peers =TLObject .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateFolderPeers (folder_peers =folder_peers ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .folder_peers ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
