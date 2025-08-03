
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DialogFilterChatlist (TLObject ):
    """"""

    __slots__ :List [str ]=["id","title","pinned_peers","include_peers","has_my_invites","emoticon"]

    ID =0xd64a04a8 
    QUALNAME ="types.DialogFilterChatlist"

    def __init__ (self ,*,id :int ,title :str ,pinned_peers :List ["raw.base.InputPeer"],include_peers :List ["raw.base.InputPeer"],has_my_invites :Optional [bool ]=None ,emoticon :Optional [str ]=None )->None :
        self .id =id 
        self .title =title 
        self .pinned_peers =pinned_peers 
        self .include_peers =include_peers 
        self .has_my_invites =has_my_invites 
        self .emoticon =emoticon 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DialogFilterChatlist":

        flags =Int .read (b )

        has_my_invites =True if flags &(1 <<26 )else False 
        id =Int .read (b )

        title =String .read (b )

        emoticon =String .read (b )if flags &(1 <<25 )else None 
        pinned_peers =TLObject .read (b )

        include_peers =TLObject .read (b )

        return DialogFilterChatlist (id =id ,title =title ,pinned_peers =pinned_peers ,include_peers =include_peers ,has_my_invites =has_my_invites ,emoticon =emoticon )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<26 )if self .has_my_invites else 0 
        flags |=(1 <<25 )if self .emoticon is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        b .write (String (self .title ))

        if self .emoticon is not None :
            b .write (String (self .emoticon ))

        b .write (Vector (self .pinned_peers ))

        b .write (Vector (self .include_peers ))

        return b .getvalue ()
