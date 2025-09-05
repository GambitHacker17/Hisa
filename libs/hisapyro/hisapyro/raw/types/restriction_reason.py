
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RestrictionReason (TLObject ):
    """"""

    __slots__ :List [str ]=["platform","reason","text"]

    ID =0xd072acb4 
    QUALNAME ="types.RestrictionReason"

    def __init__ (self ,*,platform :str ,reason :str ,text :str )->None :
        self .platform =platform 
        self .reason =reason 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RestrictionReason":

        platform =String .read (b )

        reason =String .read (b )

        text =String .read (b )

        return RestrictionReason (platform =platform ,reason =reason ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .platform ))

        b .write (String (self .reason ))

        b .write (String (self .text ))

        return b .getvalue ()
