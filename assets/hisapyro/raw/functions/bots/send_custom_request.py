
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendCustomRequest (TLObject ):
    """"""

    __slots__ :List [str ]=["custom_method","params"]

    ID =0xaa2769ed 
    QUALNAME ="functions.bots.SendCustomRequest"

    def __init__ (self ,*,custom_method :str ,params :"raw.base.DataJSON")->None :
        self .custom_method =custom_method 
        self .params =params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendCustomRequest":

        custom_method =String .read (b )

        params =TLObject .read (b )

        return SendCustomRequest (custom_method =custom_method ,params =params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .custom_method ))

        b .write (self .params .write ())

        return b .getvalue ()
