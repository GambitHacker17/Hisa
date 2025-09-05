
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class FolderPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","folder_id"]

    ID =0xe9baa668 
    QUALNAME ="types.FolderPeer"

    def __init__ (self ,*,peer :"raw.base.Peer",folder_id :int )->None :
        self .peer =peer 
        self .folder_id =folder_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"FolderPeer":

        peer =TLObject .read (b )

        folder_id =Int .read (b )

        return FolderPeer (peer =peer ,folder_id =folder_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .folder_id ))

        return b .getvalue ()
