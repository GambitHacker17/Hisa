
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetChatlistUpdates (TLObject ):
    """"""

    __slots__ :List [str ]=["chatlist"]

    ID =0x89419521 
    QUALNAME ="functions.chatlists.GetChatlistUpdates"

    def __init__ (self ,*,chatlist :"raw.base.InputChatlist")->None :
        self .chatlist =chatlist 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetChatlistUpdates":

        chatlist =TLObject .read (b )

        return GetChatlistUpdates (chatlist =chatlist )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chatlist .write ())

        return b .getvalue ()
