
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Channel (TLObject ):
    """"""

    __slots__ :List [str ]=["id","title","photo","date","creator","left","broadcast","verified","megagroup","restricted","signatures","min","scam","has_link","has_geo","slowmode_enabled","call_active","call_not_empty","fake","gigagroup","noforwards","join_to_send","join_request","forum","access_hash","username","restriction_reason","admin_rights","banned_rights","default_banned_rights","participants_count","usernames"]

    ID =0x83259464 
    QUALNAME ="types.Channel"

    def __init__ (self ,*,id :int ,title :str ,photo :"raw.base.ChatPhoto",date :int ,creator :Optional [bool ]=None ,left :Optional [bool ]=None ,broadcast :Optional [bool ]=None ,verified :Optional [bool ]=None ,megagroup :Optional [bool ]=None ,restricted :Optional [bool ]=None ,signatures :Optional [bool ]=None ,min :Optional [bool ]=None ,scam :Optional [bool ]=None ,has_link :Optional [bool ]=None ,has_geo :Optional [bool ]=None ,slowmode_enabled :Optional [bool ]=None ,call_active :Optional [bool ]=None ,call_not_empty :Optional [bool ]=None ,fake :Optional [bool ]=None ,gigagroup :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,join_to_send :Optional [bool ]=None ,join_request :Optional [bool ]=None ,forum :Optional [bool ]=None ,access_hash :Optional [int ]=None ,username :Optional [str ]=None ,restriction_reason :Optional [List ["raw.base.RestrictionReason"]]=None ,admin_rights :"raw.base.ChatAdminRights"=None ,banned_rights :"raw.base.ChatBannedRights"=None ,default_banned_rights :"raw.base.ChatBannedRights"=None ,participants_count :Optional [int ]=None ,usernames :Optional [List ["raw.base.Username"]]=None )->None :
        self .id =id 
        self .title =title 
        self .photo =photo 
        self .date =date 
        self .creator =creator 
        self .left =left 
        self .broadcast =broadcast 
        self .verified =verified 
        self .megagroup =megagroup 
        self .restricted =restricted 
        self .signatures =signatures 
        self .min =min 
        self .scam =scam 
        self .has_link =has_link 
        self .has_geo =has_geo 
        self .slowmode_enabled =slowmode_enabled 
        self .call_active =call_active 
        self .call_not_empty =call_not_empty 
        self .fake =fake 
        self .gigagroup =gigagroup 
        self .noforwards =noforwards 
        self .join_to_send =join_to_send 
        self .join_request =join_request 
        self .forum =forum 
        self .access_hash =access_hash 
        self .username =username 
        self .restriction_reason =restriction_reason 
        self .admin_rights =admin_rights 
        self .banned_rights =banned_rights 
        self .default_banned_rights =default_banned_rights 
        self .participants_count =participants_count 
        self .usernames =usernames 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Channel":

        flags =Int .read (b )

        creator =True if flags &(1 <<0 )else False 
        left =True if flags &(1 <<2 )else False 
        broadcast =True if flags &(1 <<5 )else False 
        verified =True if flags &(1 <<7 )else False 
        megagroup =True if flags &(1 <<8 )else False 
        restricted =True if flags &(1 <<9 )else False 
        signatures =True if flags &(1 <<11 )else False 
        min =True if flags &(1 <<12 )else False 
        scam =True if flags &(1 <<19 )else False 
        has_link =True if flags &(1 <<20 )else False 
        has_geo =True if flags &(1 <<21 )else False 
        slowmode_enabled =True if flags &(1 <<22 )else False 
        call_active =True if flags &(1 <<23 )else False 
        call_not_empty =True if flags &(1 <<24 )else False 
        fake =True if flags &(1 <<25 )else False 
        gigagroup =True if flags &(1 <<26 )else False 
        noforwards =True if flags &(1 <<27 )else False 
        join_to_send =True if flags &(1 <<28 )else False 
        join_request =True if flags &(1 <<29 )else False 
        forum =True if flags &(1 <<30 )else False 
        flags2 =Int .read (b )

        id =Long .read (b )

        access_hash =Long .read (b )if flags &(1 <<13 )else None 
        title =String .read (b )

        username =String .read (b )if flags &(1 <<6 )else None 
        photo =TLObject .read (b )

        date =Int .read (b )

        restriction_reason =TLObject .read (b )if flags &(1 <<9 )else []

        admin_rights =TLObject .read (b )if flags &(1 <<14 )else None 

        banned_rights =TLObject .read (b )if flags &(1 <<15 )else None 

        default_banned_rights =TLObject .read (b )if flags &(1 <<18 )else None 

        participants_count =Int .read (b )if flags &(1 <<17 )else None 
        usernames =TLObject .read (b )if flags2 &(1 <<0 )else []

        return Channel (id =id ,title =title ,photo =photo ,date =date ,creator =creator ,left =left ,broadcast =broadcast ,verified =verified ,megagroup =megagroup ,restricted =restricted ,signatures =signatures ,min =min ,scam =scam ,has_link =has_link ,has_geo =has_geo ,slowmode_enabled =slowmode_enabled ,call_active =call_active ,call_not_empty =call_not_empty ,fake =fake ,gigagroup =gigagroup ,noforwards =noforwards ,join_to_send =join_to_send ,join_request =join_request ,forum =forum ,access_hash =access_hash ,username =username ,restriction_reason =restriction_reason ,admin_rights =admin_rights ,banned_rights =banned_rights ,default_banned_rights =default_banned_rights ,participants_count =participants_count ,usernames =usernames )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .creator else 0 
        flags |=(1 <<2 )if self .left else 0 
        flags |=(1 <<5 )if self .broadcast else 0 
        flags |=(1 <<7 )if self .verified else 0 
        flags |=(1 <<8 )if self .megagroup else 0 
        flags |=(1 <<9 )if self .restricted else 0 
        flags |=(1 <<11 )if self .signatures else 0 
        flags |=(1 <<12 )if self .min else 0 
        flags |=(1 <<19 )if self .scam else 0 
        flags |=(1 <<20 )if self .has_link else 0 
        flags |=(1 <<21 )if self .has_geo else 0 
        flags |=(1 <<22 )if self .slowmode_enabled else 0 
        flags |=(1 <<23 )if self .call_active else 0 
        flags |=(1 <<24 )if self .call_not_empty else 0 
        flags |=(1 <<25 )if self .fake else 0 
        flags |=(1 <<26 )if self .gigagroup else 0 
        flags |=(1 <<27 )if self .noforwards else 0 
        flags |=(1 <<28 )if self .join_to_send else 0 
        flags |=(1 <<29 )if self .join_request else 0 
        flags |=(1 <<30 )if self .forum else 0 
        flags |=(1 <<13 )if self .access_hash is not None else 0 
        flags |=(1 <<6 )if self .username is not None else 0 
        flags |=(1 <<9 )if self .restriction_reason else 0 
        flags |=(1 <<14 )if self .admin_rights is not None else 0 
        flags |=(1 <<15 )if self .banned_rights is not None else 0 
        flags |=(1 <<18 )if self .default_banned_rights is not None else 0 
        flags |=(1 <<17 )if self .participants_count is not None else 0 
        b .write (Int (flags ))
        flags2 =0 
        flags2 |=(1 <<0 )if self .usernames else 0 
        b .write (Int (flags2 ))

        b .write (Long (self .id ))

        if self .access_hash is not None :
            b .write (Long (self .access_hash ))

        b .write (String (self .title ))

        if self .username is not None :
            b .write (String (self .username ))

        b .write (self .photo .write ())

        b .write (Int (self .date ))

        if self .restriction_reason is not None :
            b .write (Vector (self .restriction_reason ))

        if self .admin_rights is not None :
            b .write (self .admin_rights .write ())

        if self .banned_rights is not None :
            b .write (self .banned_rights .write ())

        if self .default_banned_rights is not None :
            b .write (self .default_banned_rights .write ())

        if self .participants_count is not None :
            b .write (Int (self .participants_count ))

        if self .usernames is not None :
            b .write (Vector (self .usernames ))

        return b .getvalue ()
