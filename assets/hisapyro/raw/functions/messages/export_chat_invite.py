
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportChatInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","legacy_revoke_permanent","request_needed","expire_date","usage_limit","title"]

    ID =0xa02ce5d5 
    QUALNAME ="functions.messages.ExportChatInvite"

    def __init__ (self ,*,peer :"raw.base.InputPeer",legacy_revoke_permanent :Optional [bool ]=None ,request_needed :Optional [bool ]=None ,expire_date :Optional [int ]=None ,usage_limit :Optional [int ]=None ,title :Optional [str ]=None )->None :
        self .peer =peer 
        self .legacy_revoke_permanent =legacy_revoke_permanent 
        self .request_needed =request_needed 
        self .expire_date =expire_date 
        self .usage_limit =usage_limit 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportChatInvite":

        flags =Int .read (b )

        legacy_revoke_permanent =True if flags &(1 <<2 )else False 
        request_needed =True if flags &(1 <<3 )else False 
        peer =TLObject .read (b )

        expire_date =Int .read (b )if flags &(1 <<0 )else None 
        usage_limit =Int .read (b )if flags &(1 <<1 )else None 
        title =String .read (b )if flags &(1 <<4 )else None 
        return ExportChatInvite (peer =peer ,legacy_revoke_permanent =legacy_revoke_permanent ,request_needed =request_needed ,expire_date =expire_date ,usage_limit =usage_limit ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .legacy_revoke_permanent else 0 
        flags |=(1 <<3 )if self .request_needed else 0 
        flags |=(1 <<0 )if self .expire_date is not None else 0 
        flags |=(1 <<1 )if self .usage_limit is not None else 0 
        flags |=(1 <<4 )if self .title is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .expire_date is not None :
            b .write (Int (self .expire_date ))

        if self .usage_limit is not None :
            b .write (Int (self .usage_limit ))

        if self .title is not None :
            b .write (String (self .title ))

        return b .getvalue ()
