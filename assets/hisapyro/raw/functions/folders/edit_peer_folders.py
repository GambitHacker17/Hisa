
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditPeerFolders (TLObject ):
    """"""

    __slots__ :List [str ]=["folder_peers"]

    ID =0x6847d0ab 
    QUALNAME ="functions.folders.EditPeerFolders"

    def __init__ (self ,*,folder_peers :List ["raw.base.InputFolderPeer"])->None :
        self .folder_peers =folder_peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditPeerFolders":

        folder_peers =TLObject .read (b )

        return EditPeerFolders (folder_peers =folder_peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .folder_peers ))

        return b .getvalue ()
