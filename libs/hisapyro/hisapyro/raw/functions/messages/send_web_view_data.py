
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendWebViewData (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","random_id","button_text","data"]

    ID =0xdc0242c8 
    QUALNAME ="functions.messages.SendWebViewData"

    def __init__ (self ,*,bot :"raw.base.InputUser",random_id :int ,button_text :str ,data :str )->None :
        self .bot =bot 
        self .random_id =random_id 
        self .button_text =button_text 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendWebViewData":

        bot =TLObject .read (b )

        random_id =Long .read (b )

        button_text =String .read (b )

        data =String .read (b )

        return SendWebViewData (bot =bot ,random_id =random_id ,button_text =button_text ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .bot .write ())

        b .write (Long (self .random_id ))

        b .write (String (self .button_text ))

        b .write (String (self .data ))

        return b .getvalue ()
