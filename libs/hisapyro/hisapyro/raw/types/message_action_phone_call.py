
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionPhoneCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call_id","video","reason","duration"]

    ID =0x80e11a7f 
    QUALNAME ="types.MessageActionPhoneCall"

    def __init__ (self ,*,call_id :int ,video :Optional [bool ]=None ,reason :"raw.base.PhoneCallDiscardReason"=None ,duration :Optional [int ]=None )->None :
        self .call_id =call_id 
        self .video =video 
        self .reason =reason 
        self .duration =duration 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionPhoneCall":

        flags =Int .read (b )

        video =True if flags &(1 <<2 )else False 
        call_id =Long .read (b )

        reason =TLObject .read (b )if flags &(1 <<0 )else None 

        duration =Int .read (b )if flags &(1 <<1 )else None 
        return MessageActionPhoneCall (call_id =call_id ,video =video ,reason =reason ,duration =duration )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .video else 0 
        flags |=(1 <<0 )if self .reason is not None else 0 
        flags |=(1 <<1 )if self .duration is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .call_id ))

        if self .reason is not None :
            b .write (self .reason .write ())

        if self .duration is not None :
            b .write (Int (self .duration ))

        return b .getvalue ()
