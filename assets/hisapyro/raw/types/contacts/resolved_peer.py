
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ResolvedPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","chats","users"]

    ID =0x7f077ad9 
    QUALNAME ="types.contacts.ResolvedPeer"

    def __init__ (self ,*,peer :"raw.base.Peer",chats :List ["raw.base.Chat"],users :List ["raw.base.User"])->None :
        self .peer =peer 
        self .chats =chats 
        self .users =users 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ResolvedPeer":

        peer =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ResolvedPeer (peer =peer ,chats =chats ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
