
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditBanned (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","participant","banned_rights"]

    ID =0x96e6cd81 
    QUALNAME ="functions.channels.EditBanned"

    def __init__ (self ,*,channel :"raw.base.InputChannel",participant :"raw.base.InputPeer",banned_rights :"raw.base.ChatBannedRights")->None :
        self .channel =channel 
        self .participant =participant 
        self .banned_rights =banned_rights 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditBanned":

        channel =TLObject .read (b )

        participant =TLObject .read (b )

        banned_rights =TLObject .read (b )

        return EditBanned (channel =channel ,participant =participant ,banned_rights =banned_rights )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .participant .write ())

        b .write (self .banned_rights .write ())

        return b .getvalue ()
