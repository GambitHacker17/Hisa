
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LeaveChatlist (TLObject ):
    """"""

    __slots__ :List [str ]=["chatlist","peers"]

    ID =0x74fae13a 
    QUALNAME ="functions.chatlists.LeaveChatlist"

    def __init__ (self ,*,chatlist :"raw.base.InputChatlist",peers :List ["raw.base.InputPeer"])->None :
        self .chatlist =chatlist 
        self .peers =peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LeaveChatlist":

        chatlist =TLObject .read (b )

        peers =TLObject .read (b )

        return LeaveChatlist (chatlist =chatlist ,peers =peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chatlist .write ())

        b .write (Vector (self .peers ))

        return b .getvalue ()
