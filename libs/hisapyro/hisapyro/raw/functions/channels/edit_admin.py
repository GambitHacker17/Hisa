
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditAdmin (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","user_id","admin_rights","rank"]

    ID =0xd33c8902 
    QUALNAME ="functions.channels.EditAdmin"

    def __init__ (self ,*,channel :"raw.base.InputChannel",user_id :"raw.base.InputUser",admin_rights :"raw.base.ChatAdminRights",rank :str )->None :
        self .channel =channel 
        self .user_id =user_id 
        self .admin_rights =admin_rights 
        self .rank =rank 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditAdmin":

        channel =TLObject .read (b )

        user_id =TLObject .read (b )

        admin_rights =TLObject .read (b )

        rank =String .read (b )

        return EditAdmin (channel =channel ,user_id =user_id ,admin_rights =admin_rights ,rank =rank )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .user_id .write ())

        b .write (self .admin_rights .write ())

        b .write (String (self .rank ))

        return b .getvalue ()
