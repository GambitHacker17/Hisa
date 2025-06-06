
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Chat (TLObject ):
    """"""

    __slots__ :List [str ]=["id","title","photo","participants_count","date","version","creator","left","deactivated","call_active","call_not_empty","noforwards","migrated_to","admin_rights","default_banned_rights"]

    ID =0x41cbf256 
    QUALNAME ="types.Chat"

    def __init__ (self ,*,id :int ,title :str ,photo :"raw.base.ChatPhoto",participants_count :int ,date :int ,version :int ,creator :Optional [bool ]=None ,left :Optional [bool ]=None ,deactivated :Optional [bool ]=None ,call_active :Optional [bool ]=None ,call_not_empty :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,migrated_to :"raw.base.InputChannel"=None ,admin_rights :"raw.base.ChatAdminRights"=None ,default_banned_rights :"raw.base.ChatBannedRights"=None )->None :
        self .id =id 
        self .title =title 
        self .photo =photo 
        self .participants_count =participants_count 
        self .date =date 
        self .version =version 
        self .creator =creator 
        self .left =left 
        self .deactivated =deactivated 
        self .call_active =call_active 
        self .call_not_empty =call_not_empty 
        self .noforwards =noforwards 
        self .migrated_to =migrated_to 
        self .admin_rights =admin_rights 
        self .default_banned_rights =default_banned_rights 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Chat":

        flags =Int .read (b )

        creator =True if flags &(1 <<0 )else False 
        left =True if flags &(1 <<2 )else False 
        deactivated =True if flags &(1 <<5 )else False 
        call_active =True if flags &(1 <<23 )else False 
        call_not_empty =True if flags &(1 <<24 )else False 
        noforwards =True if flags &(1 <<25 )else False 
        id =Long .read (b )

        title =String .read (b )

        photo =TLObject .read (b )

        participants_count =Int .read (b )

        date =Int .read (b )

        version =Int .read (b )

        migrated_to =TLObject .read (b )if flags &(1 <<6 )else None 

        admin_rights =TLObject .read (b )if flags &(1 <<14 )else None 

        default_banned_rights =TLObject .read (b )if flags &(1 <<18 )else None 

        return Chat (id =id ,title =title ,photo =photo ,participants_count =participants_count ,date =date ,version =version ,creator =creator ,left =left ,deactivated =deactivated ,call_active =call_active ,call_not_empty =call_not_empty ,noforwards =noforwards ,migrated_to =migrated_to ,admin_rights =admin_rights ,default_banned_rights =default_banned_rights )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .creator else 0 
        flags |=(1 <<2 )if self .left else 0 
        flags |=(1 <<5 )if self .deactivated else 0 
        flags |=(1 <<23 )if self .call_active else 0 
        flags |=(1 <<24 )if self .call_not_empty else 0 
        flags |=(1 <<25 )if self .noforwards else 0 
        flags |=(1 <<6 )if self .migrated_to is not None else 0 
        flags |=(1 <<14 )if self .admin_rights is not None else 0 
        flags |=(1 <<18 )if self .default_banned_rights is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (String (self .title ))

        b .write (self .photo .write ())

        b .write (Int (self .participants_count ))

        b .write (Int (self .date ))

        b .write (Int (self .version ))

        if self .migrated_to is not None :
            b .write (self .migrated_to .write ())

        if self .admin_rights is not None :
            b .write (self .admin_rights .write ())

        if self .default_banned_rights is not None :
            b .write (self .default_banned_rights .write ())

        return b .getvalue ()
