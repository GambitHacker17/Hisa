
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMessagesFilterPhoneCalls (TLObject ):
    """"""

    __slots__ :List [str ]=["missed"]

    ID =0x80c99768 
    QUALNAME ="types.InputMessagesFilterPhoneCalls"

    def __init__ (self ,*,missed :Optional [bool ]=None )->None :
        self .missed =missed 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMessagesFilterPhoneCalls":

        flags =Int .read (b )

        missed =True if flags &(1 <<0 )else False 
        return InputMessagesFilterPhoneCalls (missed =missed )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .missed else 0 
        b .write (Int (flags ))

        return b .getvalue ()
