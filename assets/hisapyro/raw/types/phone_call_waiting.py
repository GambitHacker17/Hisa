
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneCallWaiting (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","date","admin_id","participant_id","protocol","video","receive_date"]

    ID =0xc5226f17 
    QUALNAME ="types.PhoneCallWaiting"

    def __init__ (self ,*,id :int ,access_hash :int ,date :int ,admin_id :int ,participant_id :int ,protocol :"raw.base.PhoneCallProtocol",video :Optional [bool ]=None ,receive_date :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .date =date 
        self .admin_id =admin_id 
        self .participant_id =participant_id 
        self .protocol =protocol 
        self .video =video 
        self .receive_date =receive_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneCallWaiting":

        flags =Int .read (b )

        video =True if flags &(1 <<6 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        date =Int .read (b )

        admin_id =Long .read (b )

        participant_id =Long .read (b )

        protocol =TLObject .read (b )

        receive_date =Int .read (b )if flags &(1 <<0 )else None 
        return PhoneCallWaiting (id =id ,access_hash =access_hash ,date =date ,admin_id =admin_id ,participant_id =participant_id ,protocol =protocol ,video =video ,receive_date =receive_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<6 )if self .video else 0 
        flags |=(1 <<0 )if self .receive_date is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (Int (self .date ))

        b .write (Long (self .admin_id ))

        b .write (Long (self .participant_id ))

        b .write (self .protocol .write ())

        if self .receive_date is not None :
            b .write (Int (self .receive_date ))

        return b .getvalue ()
