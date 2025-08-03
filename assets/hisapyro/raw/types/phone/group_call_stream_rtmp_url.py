
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCallStreamRtmpUrl (TLObject ):
    """"""

    __slots__ :List [str ]=["url","key"]

    ID =0x2dbf3432 
    QUALNAME ="types.phone.GroupCallStreamRtmpUrl"

    def __init__ (self ,*,url :str ,key :str )->None :
        self .url =url 
        self .key =key 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCallStreamRtmpUrl":

        url =String .read (b )

        key =String .read (b )

        return GroupCallStreamRtmpUrl (url =url ,key =key )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (String (self .key ))

        return b .getvalue ()
