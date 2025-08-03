
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class LeaveGroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call","source"]

    ID =0x500377f9 
    QUALNAME ="functions.phone.LeaveGroupCall"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",source :int )->None :
        self .call =call 
        self .source =source 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"LeaveGroupCall":

        call =TLObject .read (b )

        source =Int .read (b )

        return LeaveGroupCall (call =call ,source =source )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Int (self .source ))

        return b .getvalue ()
