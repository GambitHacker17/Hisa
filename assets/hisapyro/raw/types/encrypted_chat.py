
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EncryptedChat (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","date","admin_id","participant_id","g_a_or_b","key_fingerprint"]

    ID =0x61f0d4c7 
    QUALNAME ="types.EncryptedChat"

    def __init__ (self ,*,id :int ,access_hash :int ,date :int ,admin_id :int ,participant_id :int ,g_a_or_b :bytes ,key_fingerprint :int )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .date =date 
        self .admin_id =admin_id 
        self .participant_id =participant_id 
        self .g_a_or_b =g_a_or_b 
        self .key_fingerprint =key_fingerprint 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EncryptedChat":

        id =Int .read (b )

        access_hash =Long .read (b )

        date =Int .read (b )

        admin_id =Long .read (b )

        participant_id =Long .read (b )

        g_a_or_b =Bytes .read (b )

        key_fingerprint =Long .read (b )

        return EncryptedChat (id =id ,access_hash =access_hash ,date =date ,admin_id =admin_id ,participant_id =participant_id ,g_a_or_b =g_a_or_b ,key_fingerprint =key_fingerprint )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .date ))

        b .write (Long (self .admin_id ))

        b .write (Long (self .participant_id ))

        b .write (Bytes (self .g_a_or_b ))

        b .write (Long (self .key_fingerprint ))

        return b .getvalue ()
