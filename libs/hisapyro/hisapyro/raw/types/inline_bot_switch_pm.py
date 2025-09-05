
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InlineBotSwitchPM (TLObject ):
    """"""

    __slots__ :List [str ]=["text","start_param"]

    ID =0x3c20629f 
    QUALNAME ="types.InlineBotSwitchPM"

    def __init__ (self ,*,text :str ,start_param :str )->None :
        self .text =text 
        self .start_param =start_param 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InlineBotSwitchPM":

        text =String .read (b )

        start_param =String .read (b )

        return InlineBotSwitchPM (text =text ,start_param =start_param )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (String (self .start_param ))

        return b .getvalue ()
