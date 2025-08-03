
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePeerSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","settings"]

    ID =0x6a7e7366 
    QUALNAME ="types.UpdatePeerSettings"

    def __init__ (self ,*,peer :"raw.base.Peer",settings :"raw.base.PeerSettings")->None :
        self .peer =peer 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePeerSettings":

        peer =TLObject .read (b )

        settings =TLObject .read (b )

        return UpdatePeerSettings (peer =peer ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .settings .write ())

        return b .getvalue ()
