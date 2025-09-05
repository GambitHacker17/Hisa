
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatAdminWithInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["admin_id","invites_count","revoked_invites_count"]

    ID =0xf2ecef23 
    QUALNAME ="types.ChatAdminWithInvites"

    def __init__ (self ,*,admin_id :int ,invites_count :int ,revoked_invites_count :int )->None :
        self .admin_id =admin_id 
        self .invites_count =invites_count 
        self .revoked_invites_count =revoked_invites_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatAdminWithInvites":

        admin_id =Long .read (b )

        invites_count =Int .read (b )

        revoked_invites_count =Int .read (b )

        return ChatAdminWithInvites (admin_id =admin_id ,invites_count =invites_count ,revoked_invites_count =revoked_invites_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .admin_id ))

        b .write (Int (self .invites_count ))

        b .write (Int (self .revoked_invites_count ))

        return b .getvalue ()
