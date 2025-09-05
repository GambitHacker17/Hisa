
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PeerBlocked (TLObject ):
    """"""

    __slots__ :List [str ]=["peer_id","date"]

    ID =0xe8fd8014 
    QUALNAME ="types.PeerBlocked"

    def __init__ (self ,*,peer_id :"raw.base.Peer",date :int )->None :
        self .peer_id =peer_id 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PeerBlocked":

        peer_id =TLObject .read (b )

        date =Int .read (b )

        return PeerBlocked (peer_id =peer_id ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer_id .write ())

        b .write (Int (self .date ))

        return b .getvalue ()
