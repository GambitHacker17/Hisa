
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelParticipantCreator (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","admin_rights","rank"]

    ID =0x2fe601d3 
    QUALNAME ="types.ChannelParticipantCreator"

    def __init__ (self ,*,user_id :int ,admin_rights :"raw.base.ChatAdminRights",rank :Optional [str ]=None )->None :
        self .user_id =user_id 
        self .admin_rights =admin_rights 
        self .rank =rank 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelParticipantCreator":

        flags =Int .read (b )

        user_id =Long .read (b )

        admin_rights =TLObject .read (b )

        rank =String .read (b )if flags &(1 <<0 )else None 
        return ChannelParticipantCreator (user_id =user_id ,admin_rights =admin_rights ,rank =rank )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .rank is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .user_id ))

        b .write (self .admin_rights .write ())

        if self .rank is not None :
            b .write (String (self .rank ))

        return b .getvalue ()
