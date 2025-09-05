
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetBroadcastStats (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","dark"]

    ID =0xab42441a 
    QUALNAME ="functions.stats.GetBroadcastStats"

    def __init__ (self ,*,channel :"raw.base.InputChannel",dark :Optional [bool ]=None )->None :
        self .channel =channel 
        self .dark =dark 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetBroadcastStats":

        flags =Int .read (b )

        dark =True if flags &(1 <<0 )else False 
        channel =TLObject .read (b )

        return GetBroadcastStats (channel =channel ,dark =dark )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .dark else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        return b .getvalue ()
