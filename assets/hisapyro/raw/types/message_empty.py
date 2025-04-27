
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["id","peer_id"]

    ID =0x90a6ca84 
    QUALNAME ="types.MessageEmpty"

    def __init__ (self ,*,id :int ,peer_id :"raw.base.Peer"=None )->None :
        self .id =id 
        self .peer_id =peer_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEmpty":

        flags =Int .read (b )

        id =Int .read (b )

        peer_id =TLObject .read (b )if flags &(1 <<0 )else None 

        return MessageEmpty (id =id ,peer_id =peer_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .peer_id is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        if self .peer_id is not None :
            b .write (self .peer_id .write ())

        return b .getvalue ()
