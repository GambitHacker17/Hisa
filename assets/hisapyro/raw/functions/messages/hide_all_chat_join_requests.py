
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HideAllChatJoinRequests (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","approved","link"]

    ID =0xe085f4ea 
    QUALNAME ="functions.messages.HideAllChatJoinRequests"

    def __init__ (self ,*,peer :"raw.base.InputPeer",approved :Optional [bool ]=None ,link :Optional [str ]=None )->None :
        self .peer =peer 
        self .approved =approved 
        self .link =link 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HideAllChatJoinRequests":

        flags =Int .read (b )

        approved =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        link =String .read (b )if flags &(1 <<1 )else None 
        return HideAllChatJoinRequests (peer =peer ,approved =approved ,link =link )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .approved else 0 
        flags |=(1 <<1 )if self .link is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .link is not None :
            b .write (String (self .link ))

        return b .getvalue ()
