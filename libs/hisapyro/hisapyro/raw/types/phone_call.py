
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneCall (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","date","admin_id","participant_id","g_a_or_b","key_fingerprint","protocol","connections","start_date","p2p_allowed","video"]

    ID =0x967f7c67 
    QUALNAME ="types.PhoneCall"

    def __init__ (self ,*,id :int ,access_hash :int ,date :int ,admin_id :int ,participant_id :int ,g_a_or_b :bytes ,key_fingerprint :int ,protocol :"raw.base.PhoneCallProtocol",connections :List ["raw.base.PhoneConnection"],start_date :int ,p2p_allowed :Optional [bool ]=None ,video :Optional [bool ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .date =date 
        self .admin_id =admin_id 
        self .participant_id =participant_id 
        self .g_a_or_b =g_a_or_b 
        self .key_fingerprint =key_fingerprint 
        self .protocol =protocol 
        self .connections =connections 
        self .start_date =start_date 
        self .p2p_allowed =p2p_allowed 
        self .video =video 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneCall":

        flags =Int .read (b )

        p2p_allowed =True if flags &(1 <<5 )else False 
        video =True if flags &(1 <<6 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        date =Int .read (b )

        admin_id =Long .read (b )

        participant_id =Long .read (b )

        g_a_or_b =Bytes .read (b )

        key_fingerprint =Long .read (b )

        protocol =TLObject .read (b )

        connections =TLObject .read (b )

        start_date =Int .read (b )

        return PhoneCall (id =id ,access_hash =access_hash ,date =date ,admin_id =admin_id ,participant_id =participant_id ,g_a_or_b =g_a_or_b ,key_fingerprint =key_fingerprint ,protocol =protocol ,connections =connections ,start_date =start_date ,p2p_allowed =p2p_allowed ,video =video )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .p2p_allowed else 0 
        flags |=(1 <<6 )if self .video else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .date ))

        b .write (Long (self .admin_id ))

        b .write (Long (self .participant_id ))

        b .write (Bytes (self .g_a_or_b ))

        b .write (Long (self .key_fingerprint ))

        b .write (self .protocol .write ())

        b .write (Vector (self .connections ))

        b .write (Int (self .start_date ))

        return b .getvalue ()
