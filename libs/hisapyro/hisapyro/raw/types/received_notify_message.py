
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReceivedNotifyMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["id","flags"]

    ID =0xa384b779 
    QUALNAME ="types.ReceivedNotifyMessage"

    def __init__ (self ,*,id :int ,flags :int )->None :
        self .id =id 
        self .flags =flags 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReceivedNotifyMessage":

        id =Int .read (b )

        flags =Int .read (b )

        return ReceivedNotifyMessage (id =id ,flags =flags )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .id ))

        b .write (Int (self .flags ))

        return b .getvalue ()
