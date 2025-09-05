
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditChatDefaultBannedRights (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","banned_rights"]

    ID =0xa5866b41 
    QUALNAME ="functions.messages.EditChatDefaultBannedRights"

    def __init__ (self ,*,peer :"raw.base.InputPeer",banned_rights :"raw.base.ChatBannedRights")->None :
        self .peer =peer 
        self .banned_rights =banned_rights 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditChatDefaultBannedRights":

        peer =TLObject .read (b )

        banned_rights =TLObject .read (b )

        return EditChatDefaultBannedRights (peer =peer ,banned_rights =banned_rights )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .banned_rights .write ())

        return b .getvalue ()
