
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetBotInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code","bot"]

    ID =0xdcd914fd 
    QUALNAME ="functions.bots.GetBotInfo"

    def __init__ (self ,*,lang_code :str ,bot :"raw.base.InputUser"=None )->None :
        self .lang_code =lang_code 
        self .bot =bot 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetBotInfo":

        flags =Int .read (b )

        bot =TLObject .read (b )if flags &(1 <<0 )else None 

        lang_code =String .read (b )

        return GetBotInfo (lang_code =lang_code ,bot =bot )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .bot is not None else 0 
        b .write (Int (flags ))

        if self .bot is not None :
            b .write (self .bot .write ())

        b .write (String (self .lang_code ))

        return b .getvalue ()
