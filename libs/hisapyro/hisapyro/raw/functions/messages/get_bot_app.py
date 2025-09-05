
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetBotApp (TLObject ):
    """"""

    __slots__ :List [str ]=["app","hash"]

    ID =0x34fdc5c3 
    QUALNAME ="functions.messages.GetBotApp"

    def __init__ (self ,*,app :"raw.base.InputBotApp",hash :int )->None :
        self .app =app 
        self .hash =hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetBotApp":

        app =TLObject .read (b )

        hash =Long .read (b )

        return GetBotApp (app =app ,hash =hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .app .write ())

        b .write (Long (self .hash ))

        return b .getvalue ()
