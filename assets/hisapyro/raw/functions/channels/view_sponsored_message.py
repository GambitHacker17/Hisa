
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ViewSponsoredMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","random_id"]

    ID =0xbeaedb94 
    QUALNAME ="functions.channels.ViewSponsoredMessage"

    def __init__ (self ,*,channel :"raw.base.InputChannel",random_id :bytes )->None :
        self .channel =channel 
        self .random_id =random_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ViewSponsoredMessage":

        channel =TLObject .read (b )

        random_id =Bytes .read (b )

        return ViewSponsoredMessage (channel =channel ,random_id =random_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (Bytes (self .random_id ))

        return b .getvalue ()
