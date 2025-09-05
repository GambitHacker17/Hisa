
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JoinChatlistUpdates (TLObject ):
    """"""

    __slots__ :List [str ]=["chatlist","peers"]

    ID =0xe089f8f5 
    QUALNAME ="functions.chatlists.JoinChatlistUpdates"

    def __init__ (self ,*,chatlist :"raw.base.InputChatlist",peers :List ["raw.base.InputPeer"])->None :
        self .chatlist =chatlist 
        self .peers =peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JoinChatlistUpdates":

        chatlist =TLObject .read (b )

        peers =TLObject .read (b )

        return JoinChatlistUpdates (chatlist =chatlist ,peers =peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chatlist .write ())

        b .write (Vector (self .peers ))

        return b .getvalue ()
