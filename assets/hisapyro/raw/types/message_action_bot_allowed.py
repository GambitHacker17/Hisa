
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageActionBotAllowed (TLObject ):
    """"""

    __slots__ :List [str ]=["attach_menu","domain","app"]

    ID =0xc516d679 
    QUALNAME ="types.MessageActionBotAllowed"

    def __init__ (self ,*,attach_menu :Optional [bool ]=None ,domain :Optional [str ]=None ,app :"raw.base.BotApp"=None )->None :
        self .attach_menu =attach_menu 
        self .domain =domain 
        self .app =app 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageActionBotAllowed":

        flags =Int .read (b )

        attach_menu =True if flags &(1 <<1 )else False 
        domain =String .read (b )if flags &(1 <<0 )else None 
        app =TLObject .read (b )if flags &(1 <<2 )else None 

        return MessageActionBotAllowed (attach_menu =attach_menu ,domain =domain ,app =app )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .attach_menu else 0 
        flags |=(1 <<0 )if self .domain is not None else 0 
        flags |=(1 <<2 )if self .app is not None else 0 
        b .write (Int (flags ))

        if self .domain is not None :
            b .write (String (self .domain ))

        if self .app is not None :
            b .write (self .app .write ())

        return b .getvalue ()
