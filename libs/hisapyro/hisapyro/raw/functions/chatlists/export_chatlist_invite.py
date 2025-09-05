
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportChatlistInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["chatlist","title","peers"]

    ID =0x8472478e 
    QUALNAME ="functions.chatlists.ExportChatlistInvite"

    def __init__ (self ,*,chatlist :"raw.base.InputChatlist",title :str ,peers :List ["raw.base.InputPeer"])->None :
        self .chatlist =chatlist 
        self .title =title 
        self .peers =peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportChatlistInvite":

        chatlist =TLObject .read (b )

        title =String .read (b )

        peers =TLObject .read (b )

        return ExportChatlistInvite (chatlist =chatlist ,title =title ,peers =peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .chatlist .write ())

        b .write (String (self .title ))

        b .write (Vector (self .peers ))

        return b .getvalue ()
