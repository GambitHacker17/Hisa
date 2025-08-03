
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportedChatlistInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["title","url","peers"]

    ID =0xc5181ac 
    QUALNAME ="types.ExportedChatlistInvite"

    def __init__ (self ,*,title :str ,url :str ,peers :List ["raw.base.Peer"])->None :
        self .title =title 
        self .url =url 
        self .peers =peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportedChatlistInvite":

        flags =Int .read (b )

        title =String .read (b )

        url =String .read (b )

        peers =TLObject .read (b )

        return ExportedChatlistInvite (title =title ,url =url ,peers =peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 

        b .write (Int (flags ))

        b .write (String (self .title ))

        b .write (String (self .url ))

        b .write (Vector (self .peers ))

        return b .getvalue ()
