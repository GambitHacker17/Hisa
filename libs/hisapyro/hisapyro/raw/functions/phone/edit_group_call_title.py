
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditGroupCallTitle (TLObject ):
    """"""

    __slots__ :List [str ]=["call","title"]

    ID =0x1ca6ac0a 
    QUALNAME ="functions.phone.EditGroupCallTitle"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",title :str )->None :
        self .call =call 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditGroupCallTitle":

        call =TLObject .read (b )

        title =String .read (b )

        return EditGroupCallTitle (call =call ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (String (self .title ))

        return b .getvalue ()
