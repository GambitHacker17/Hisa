
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateChatDefaultBannedRights (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","default_banned_rights","version"]

    ID =0x54c01850 
    QUALNAME ="types.UpdateChatDefaultBannedRights"

    def __init__ (self ,*,peer :"raw.base.Peer",default_banned_rights :"raw.base.ChatBannedRights",version :int )->None :
        self .peer =peer 
        self .default_banned_rights =default_banned_rights 
        self .version =version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateChatDefaultBannedRights":

        peer =TLObject .read (b )

        default_banned_rights =TLObject .read (b )

        version =Int .read (b )

        return UpdateChatDefaultBannedRights (peer =peer ,default_banned_rights =default_banned_rights ,version =version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .default_banned_rights .write ())

        b .write (Int (self .version ))

        return b .getvalue ()
