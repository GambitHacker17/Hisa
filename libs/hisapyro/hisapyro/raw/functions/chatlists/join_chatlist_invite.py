
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JoinChatlistInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["slug","peers"]

    ID =0xa6b1e39a 
    QUALNAME ="functions.chatlists.JoinChatlistInvite"

    def __init__ (self ,*,slug :str ,peers :List ["raw.base.InputPeer"])->None :
        self .slug =slug 
        self .peers =peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JoinChatlistInvite":

        slug =String .read (b )

        peers =TLObject .read (b )

        return JoinChatlistInvite (slug =slug ,peers =peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .slug ))

        b .write (Vector (self .peers ))

        return b .getvalue ()
