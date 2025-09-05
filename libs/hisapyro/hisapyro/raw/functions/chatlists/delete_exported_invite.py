
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteExportedInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["chatlist","slug"]

    ID =0x719c5c5e 
    QUALNAME ="functions.chatlists.DeleteExportedInvite"

    def __init__ (self ,*,chatlist :"raw.base.InputChatlist",slug :str )->None :
        self .chatlist =chatlist 
        self .slug =slug 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteExportedInvite":

        chatlist =TLObject .read (b )

        slug =String .read (b )

        return DeleteExportedInvite (chatlist =chatlist ,slug =slug )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chatlist .write ())

        b .write (String (self .slug ))

        return b .getvalue ()
