
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionSetMessagesTTL (TLObject ):
    """"""

    __slots__ :List [str ]=["period","auto_setting_from"]

    ID =0x3c134d7b 
    QUALNAME ="types.MessageActionSetMessagesTTL"

    def __init__ (self ,*,period :int ,auto_setting_from :Optional [int ]=None )->None :
        self .period =period 
        self .auto_setting_from =auto_setting_from 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionSetMessagesTTL":

        flags =Int .read (b )

        period =Int .read (b )

        auto_setting_from =Long .read (b )if flags &(1 <<0 )else None 
        return MessageActionSetMessagesTTL (period =period ,auto_setting_from =auto_setting_from )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .auto_setting_from is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .period ))

        if self .auto_setting_from is not None :
            b .write (Long (self .auto_setting_from ))

        return b .getvalue ()
