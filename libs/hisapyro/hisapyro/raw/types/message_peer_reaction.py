
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessagePeerReaction (TLObject ):
    """"""

    __slots__ :List [str ]=["peer_id","date","reaction","big","unread"]

    ID =0x8c79b63c 
    QUALNAME ="types.MessagePeerReaction"

    def __init__ (self ,*,peer_id :"raw.base.Peer",date :int ,reaction :"raw.base.Reaction",big :Optional [bool ]=None ,unread :Optional [bool ]=None )->None :
        self .peer_id =peer_id 
        self .date =date 
        self .reaction =reaction 
        self .big =big 
        self .unread =unread 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessagePeerReaction":

        flags =Int .read (b )

        big =True if flags &(1 <<0 )else False 
        unread =True if flags &(1 <<1 )else False 
        peer_id =TLObject .read (b )

        date =Int .read (b )

        reaction =TLObject .read (b )

        return MessagePeerReaction (peer_id =peer_id ,date =date ,reaction =reaction ,big =big ,unread =unread )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .big else 0 
        flags |=(1 <<1 )if self .unread else 0 
        b .write (Int (flags ))

        b .write (self .peer_id .write ())

        b .write (Int (self .date ))

        b .write (self .reaction .write ())

        return b .getvalue ()
