
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebViewMessageSent (TLObject ):
    """"""

    __slots__ :List [str ]=["msg_id"]

    ID =0xc94511c 
    QUALNAME ="types.WebViewMessageSent"

    def __init__ (self ,*,msg_id :"raw.base.InputBotInlineMessageID"=None )->None :
        self .msg_id =msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebViewMessageSent":

        flags =Int .read (b )

        msg_id =TLObject .read (b )if flags &(1 <<0 )else None 

        return WebViewMessageSent (msg_id =msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .msg_id is not None else 0 
        b .write (Int (flags ))

        if self .msg_id is not None :
            b .write (self .msg_id .write ())

        return b .getvalue ()
