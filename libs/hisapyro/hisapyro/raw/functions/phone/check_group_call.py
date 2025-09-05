
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class CheckGroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call","sources"]

    ID =0xb59cf977 
    QUALNAME ="functions.phone.CheckGroupCall"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",sources :List [int ])->None :
        self .call =call 
        self .sources =sources 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"CheckGroupCall":

        call =TLObject .read (b )

        sources =TLObject .read (b ,Int )

        return CheckGroupCall (call =call ,sources =sources )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Vector (self .sources ,Int ))

        return b .getvalue ()
