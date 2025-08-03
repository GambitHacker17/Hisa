
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePeerHistoryTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","ttl_period"]

    ID =0xbb9bb9a5 
    QUALNAME ="types.UpdatePeerHistoryTTL"

    def __init__ (self ,*,peer :"raw.base.Peer",ttl_period :Optional [int ]=None )->None :
        self .peer =peer 
        self .ttl_period =ttl_period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePeerHistoryTTL":

        flags =Int .read (b )

        peer =TLObject .read (b )

        ttl_period =Int .read (b )if flags &(1 <<0 )else None 
        return UpdatePeerHistoryTTL (peer =peer ,ttl_period =ttl_period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .ttl_period is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        return b .getvalue ()
