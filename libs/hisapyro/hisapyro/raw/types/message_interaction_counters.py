
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageInteractionCounters (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_id","views","forwards"]

    ID =0xad4fc9bd 
    QUALNAME ="types.MessageInteractionCounters"

    def __init__ (self ,*,msg_id :int ,views :int ,forwards :int )->None :
        self .msg_id =msg_id 
        self .views =views 
        self .forwards =forwards 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageInteractionCounters":

        msg_id =Int .read (b )

        views =Int .read (b )

        forwards =Int .read (b )

        return MessageInteractionCounters (msg_id =msg_id ,views =views ,forwards =forwards )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .msg_id ))

        b .write (Int (self .views ))

        b .write (Int (self .forwards ))

        return b .getvalue ()
