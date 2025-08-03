
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotWebhookJSON (TLObject ):
    """"""

    __slots__ :List [str ]=["data"]

    ID =0x8317c0c3 
    QUALNAME ="types.UpdateBotWebhookJSON"

    def __init__ (self ,*,data :"raw.base.DataJSON")->None :
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotWebhookJSON":

        data =TLObject .read (b )

        return UpdateBotWebhookJSON (data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .data .write ())

        return b .getvalue ()
