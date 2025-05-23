
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipantAdmin (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","promoted_by","date","admin_rights","can_edit","is_self","inviter_id","rank"]

    ID =0x34c3bb53 
    QUALNAME ="types.ChannelParticipantAdmin"

    def __init__ (self ,*,user_id :int ,promoted_by :int ,date :int ,admin_rights :"raw.base.ChatAdminRights",can_edit :Optional [bool ]=None ,is_self :Optional [bool ]=None ,inviter_id :Optional [int ]=None ,rank :Optional [str ]=None )->None :
        self .user_id =user_id 
        self .promoted_by =promoted_by 
        self .date =date 
        self .admin_rights =admin_rights 
        self .can_edit =can_edit 
        self .is_self =is_self 
        self .inviter_id =inviter_id 
        self .rank =rank 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipantAdmin":

        flags =Int .read (b )

        can_edit =True if flags &(1 <<0 )else False 
        is_self =True if flags &(1 <<1 )else False 
        user_id =Long .read (b )

        inviter_id =Long .read (b )if flags &(1 <<1 )else None 
        promoted_by =Long .read (b )

        date =Int .read (b )

        admin_rights =TLObject .read (b )

        rank =String .read (b )if flags &(1 <<2 )else None 
        return ChannelParticipantAdmin (user_id =user_id ,promoted_by =promoted_by ,date =date ,admin_rights =admin_rights ,can_edit =can_edit ,is_self =is_self ,inviter_id =inviter_id ,rank =rank )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .can_edit else 0 
        flags |=(1 <<1 )if self .is_self else 0 
        flags |=(1 <<1 )if self .inviter_id is not None else 0 
        flags |=(1 <<2 )if self .rank is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .user_id ))

        if self .inviter_id is not None :
            b .write (Long (self .inviter_id ))

        b .write (Long (self .promoted_by ))

        b .write (Int (self .date ))

        b .write (self .admin_rights .write ())

        if self .rank is not None :
            b .write (String (self .rank ))

        return b .getvalue ()
