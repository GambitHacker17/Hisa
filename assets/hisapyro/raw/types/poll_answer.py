
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PollAnswer (TLObject ):
    """"""

    __slots__ :List [str ]=["text","option"]

    ID =0x6ca9c2e9 
    QUALNAME ="types.PollAnswer"

    def __init__ (self ,*,text :str ,option :bytes )->None :
        self .text =text 
        self .option =option 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PollAnswer":

        text =String .read (b )

        option =Bytes .read (b )

        return PollAnswer (text =text ,option =option )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (Bytes (self .option ))

        return b .getvalue ()
