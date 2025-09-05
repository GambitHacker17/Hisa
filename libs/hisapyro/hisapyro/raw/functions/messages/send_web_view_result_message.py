
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendWebViewResultMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["bot_query_id","result"]

    ID =0xa4314f5 
    QUALNAME ="functions.messages.SendWebViewResultMessage"

    def __init__ (self ,*,bot_query_id :str ,result :"raw.base.InputBotInlineResult")->None :
        self .bot_query_id =bot_query_id 
        self .result =result 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendWebViewResultMessage":

        bot_query_id =String .read (b )

        result =TLObject .read (b )

        return SendWebViewResultMessage (bot_query_id =bot_query_id ,result =result )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .bot_query_id ))

        b .write (self .result .write ())

        return b .getvalue ()
