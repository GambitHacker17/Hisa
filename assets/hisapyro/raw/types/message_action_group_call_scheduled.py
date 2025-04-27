
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionGroupCallScheduled (TLObject ):
    """"""

    __slots__ :List [str ]=["call","schedule_date"]

    ID =0xb3a07661 
    QUALNAME ="types.MessageActionGroupCallScheduled"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",schedule_date :int )->None :
        self .call =call 
        self .schedule_date =schedule_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionGroupCallScheduled":

        call =TLObject .read (b )

        schedule_date =Int .read (b )

        return MessageActionGroupCallScheduled (call =call ,schedule_date =schedule_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Int (self .schedule_date ))

        return b .getvalue ()
