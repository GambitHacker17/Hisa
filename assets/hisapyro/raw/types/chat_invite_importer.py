
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatInviteImporter (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","date","requested","via_chatlist","about","approved_by"]

    ID =0x8c5adfd9 
    QUALNAME ="types.ChatInviteImporter"

    def __init__ (self ,*,user_id :int ,date :int ,requested :Optional [bool ]=None ,via_chatlist :Optional [bool ]=None ,about :Optional [str ]=None ,approved_by :Optional [int ]=None )->None :
        self .user_id =user_id 
        self .date =date 
        self .requested =requested 
        self .via_chatlist =via_chatlist 
        self .about =about 
        self .approved_by =approved_by 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatInviteImporter":

        flags =Int .read (b )

        requested =True if flags &(1 <<0 )else False 
        via_chatlist =True if flags &(1 <<3 )else False 
        user_id =Long .read (b )

        date =Int .read (b )

        about =String .read (b )if flags &(1 <<2 )else None 
        approved_by =Long .read (b )if flags &(1 <<1 )else None 
        return ChatInviteImporter (user_id =user_id ,date =date ,requested =requested ,via_chatlist =via_chatlist ,about =about ,approved_by =approved_by )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .requested else 0 
        flags |=(1 <<3 )if self .via_chatlist else 0 
        flags |=(1 <<2 )if self .about is not None else 0 
        flags |=(1 <<1 )if self .approved_by is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .user_id ))

        b .write (Int (self .date ))

        if self .about is not None :
            b .write (String (self .about ))

        if self .approved_by is not None :
            b .write (Long (self .approved_by ))

        return b .getvalue ()
