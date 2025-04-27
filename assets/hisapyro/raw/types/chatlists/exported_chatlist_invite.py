
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedChatlistInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["filter","invite"]

    ID =0x10e6e3a6 
    QUALNAME ="types.chatlists.ExportedChatlistInvite"

    def __init__ (self ,*,filter :"raw.base.DialogFilter",invite :"raw.base.ExportedChatlistInvite")->None :
        self .filter =filter 
        self .invite =invite 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedChatlistInvite":

        filter =TLObject .read (b )

        invite =TLObject .read (b )

        return ExportedChatlistInvite (filter =filter ,invite =invite )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .filter .write ())

        b .write (self .invite .write ())

        return b .getvalue ()
