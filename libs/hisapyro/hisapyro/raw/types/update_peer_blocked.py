
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePeerBlocked (TLObject ):
    """"""

    __slots__ :List [str ]=["peer_id","blocked"]

    ID =0x246a4b22 
    QUALNAME ="types.UpdatePeerBlocked"

    def __init__ (self ,*,peer_id :"raw.base.Peer",blocked :bool )->None :
        self .peer_id =peer_id 
        self .blocked =blocked 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePeerBlocked":

        peer_id =TLObject .read (b )

        blocked =Bool .read (b )

        return UpdatePeerBlocked (peer_id =peer_id ,blocked =blocked )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer_id .write ())

        b .write (Bool (self .blocked ))

        return b .getvalue ()
