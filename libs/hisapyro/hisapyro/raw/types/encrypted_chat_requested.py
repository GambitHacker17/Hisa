
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EncryptedChatRequested (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","date","admin_id","participant_id","g_a","folder_id"]

    ID =0x48f1d94c 
    QUALNAME ="types.EncryptedChatRequested"

    def __init__ (self ,*,id :int ,access_hash :int ,date :int ,admin_id :int ,participant_id :int ,g_a :bytes ,folder_id :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .date =date 
        self .admin_id =admin_id 
        self .participant_id =participant_id 
        self .g_a =g_a 
        self .folder_id =folder_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EncryptedChatRequested":

        flags =Int .read (b )

        folder_id =Int .read (b )if flags &(1 <<0 )else None 
        id =Int .read (b )

        access_hash =Long .read (b )

        date =Int .read (b )

        admin_id =Long .read (b )

        participant_id =Long .read (b )

        g_a =Bytes .read (b )

        return EncryptedChatRequested (id =id ,access_hash =access_hash ,date =date ,admin_id =admin_id ,participant_id =participant_id ,g_a =g_a ,folder_id =folder_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .folder_id is not None else 0 
        b .write (Int (flags ))

        if self .folder_id is not None :
            b .write (Int (self .folder_id ))

        b .write (Int (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .date ))

        b .write (Long (self .admin_id ))

        b .write (Long (self .participant_id ))

        b .write (Bytes (self .g_a ))

        return b .getvalue ()
