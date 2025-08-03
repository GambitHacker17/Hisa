
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class NotificationSoundRingtone (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0xff6c8049 
    QUALNAME ="types.NotificationSoundRingtone"

    def __init__ (self ,*,id :int )->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"NotificationSoundRingtone":

        id =Long .read (b )

        return NotificationSoundRingtone (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))

        return b .getvalue ()
