
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetGroupCallStreamRtmpUrl (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","revoke"]

    ID =0xdeb3abbf 
    QUALNAME ="functions.phone.GetGroupCallStreamRtmpUrl"

    def __init__ (self ,*,peer :"raw.base.InputPeer",revoke :bool )->None :
        self .peer =peer 
        self .revoke =revoke 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetGroupCallStreamRtmpUrl":

        peer =TLObject .read (b )

        revoke =Bool .read (b )

        return GetGroupCallStreamRtmpUrl (peer =peer ,revoke =revoke )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Bool (self .revoke ))

        return b .getvalue ()
