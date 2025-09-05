
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetChannels (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0xa7f6bbb 
    QUALNAME ="functions.channels.GetChannels"

    def __init__ (self ,*,id :List ["raw.base.InputChannel"])->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetChannels":

        id =TLObject .read (b )

        return GetChannels (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .id ))

        return b .getvalue ()
