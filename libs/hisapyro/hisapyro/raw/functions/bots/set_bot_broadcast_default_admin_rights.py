
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetBotBroadcastDefaultAdminRights (TLObject ):
    """"""

    __slots__ :List [str ]=["admin_rights"]

    ID =0x788464e1 
    QUALNAME ="functions.bots.SetBotBroadcastDefaultAdminRights"

    def __init__ (self ,*,admin_rights :"raw.base.ChatAdminRights")->None :
        self .admin_rights =admin_rights 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetBotBroadcastDefaultAdminRights":

        admin_rights =TLObject .read (b )

        return SetBotBroadcastDefaultAdminRights (admin_rights =admin_rights )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .admin_rights .write ())

        return b .getvalue ()
