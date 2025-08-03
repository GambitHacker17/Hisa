
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JoinGroupCallPresentation (TLObject ):
    """"""

    __slots__ :List [str ]=["call","params"]

    ID =0xcbea6bc4 
    QUALNAME ="functions.phone.JoinGroupCallPresentation"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",params :"raw.base.DataJSON")->None :
        self .call =call 
        self .params =params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JoinGroupCallPresentation":

        call =TLObject .read (b )

        params =TLObject .read (b )

        return JoinGroupCallPresentation (call =call ,params =params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (self .params .write ())

        return b .getvalue ()
