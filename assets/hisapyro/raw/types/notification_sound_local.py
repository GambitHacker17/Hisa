
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class NotificationSoundLocal (TLObject ):
    """"""

    __slots__ :List [str ]=["title","data"]

    ID =0x830b9ae4 
    QUALNAME ="types.NotificationSoundLocal"

    def __init__ (self ,*,title :str ,data :str )->None :
        self .title =title 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"NotificationSoundLocal":

        title =String .read (b )

        data =String .read (b )

        return NotificationSoundLocal (title =title ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .title ))

        b .write (String (self .data ))

        return b .getvalue ()
