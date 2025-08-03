
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputChatlistDialogFilter (TLObject ):
    """"""

    __slots__ :List [str ]=["filter_id"]

    ID =0xf3e0da33 
    QUALNAME ="types.InputChatlistDialogFilter"

    def __init__ (self ,*,filter_id :int )->None :
        self .filter_id =filter_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputChatlistDialogFilter":

        filter_id =Int .read (b )

        return InputChatlistDialogFilter (filter_id =filter_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .filter_id ))

        return b .getvalue ()
