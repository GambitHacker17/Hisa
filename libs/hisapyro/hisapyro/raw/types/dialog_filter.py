
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DialogFilter (TLObject ):
    """"""

    __slots__ :List [str ]=["id","title","pinned_peers","include_peers","exclude_peers","contacts","non_contacts","groups","broadcasts","bots","exclude_muted","exclude_read","exclude_archived","emoticon"]

    ID =0x7438f7e8 
    QUALNAME ="types.DialogFilter"

    def __init__ (self ,*,id :int ,title :str ,pinned_peers :List ["raw.base.InputPeer"],include_peers :List ["raw.base.InputPeer"],exclude_peers :List ["raw.base.InputPeer"],contacts :Optional [bool ]=None ,non_contacts :Optional [bool ]=None ,groups :Optional [bool ]=None ,broadcasts :Optional [bool ]=None ,bots :Optional [bool ]=None ,exclude_muted :Optional [bool ]=None ,exclude_read :Optional [bool ]=None ,exclude_archived :Optional [bool ]=None ,emoticon :Optional [str ]=None )->None :
        self .id =id 
        self .title =title 
        self .pinned_peers =pinned_peers 
        self .include_peers =include_peers 
        self .exclude_peers =exclude_peers 
        self .contacts =contacts 
        self .non_contacts =non_contacts 
        self .groups =groups 
        self .broadcasts =broadcasts 
        self .bots =bots 
        self .exclude_muted =exclude_muted 
        self .exclude_read =exclude_read 
        self .exclude_archived =exclude_archived 
        self .emoticon =emoticon 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DialogFilter":

        flags =Int .read (b )

        contacts =True if flags &(1 <<0 )else False 
        non_contacts =True if flags &(1 <<1 )else False 
        groups =True if flags &(1 <<2 )else False 
        broadcasts =True if flags &(1 <<3 )else False 
        bots =True if flags &(1 <<4 )else False 
        exclude_muted =True if flags &(1 <<11 )else False 
        exclude_read =True if flags &(1 <<12 )else False 
        exclude_archived =True if flags &(1 <<13 )else False 
        id =Int .read (b )

        title =String .read (b )

        emoticon =String .read (b )if flags &(1 <<25 )else None 
        pinned_peers =TLObject .read (b )

        include_peers =TLObject .read (b )

        exclude_peers =TLObject .read (b )

        return DialogFilter (id =id ,title =title ,pinned_peers =pinned_peers ,include_peers =include_peers ,exclude_peers =exclude_peers ,contacts =contacts ,non_contacts =non_contacts ,groups =groups ,broadcasts =broadcasts ,bots =bots ,exclude_muted =exclude_muted ,exclude_read =exclude_read ,exclude_archived =exclude_archived ,emoticon =emoticon )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .contacts else 0 
        flags |=(1 <<1 )if self .non_contacts else 0 
        flags |=(1 <<2 )if self .groups else 0 
        flags |=(1 <<3 )if self .broadcasts else 0 
        flags |=(1 <<4 )if self .bots else 0 
        flags |=(1 <<11 )if self .exclude_muted else 0 
        flags |=(1 <<12 )if self .exclude_read else 0 
        flags |=(1 <<13 )if self .exclude_archived else 0 
        flags |=(1 <<25 )if self .emoticon is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        b .write (String (self .title ))

        if self .emoticon is not None :
            b .write (String (self .emoticon ))

        b .write (Vector (self .pinned_peers ))

        b .write (Vector (self .include_peers ))

        b .write (Vector (self .exclude_peers ))

        return b .getvalue ()
