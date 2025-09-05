
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckedHistoryImportPeer (TLObject ):
    """"""

    __slots__ :List [str ]=["confirm_text"]

    ID =0xa24de717 
    QUALNAME ="types.messages.CheckedHistoryImportPeer"

    def __init__ (self ,*,confirm_text :str )->None :
        self .confirm_text =confirm_text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckedHistoryImportPeer":

        confirm_text =String .read (b )

        return CheckedHistoryImportPeer (confirm_text =confirm_text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .confirm_text ))

        return b .getvalue ()
