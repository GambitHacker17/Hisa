
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BotApp (TLObject ):
    """"""

    __slots__ :List [str ]=["app","inactive","request_write_access"]

    ID =0xeb50adf5 
    QUALNAME ="types.messages.BotApp"

    def __init__ (self ,*,app :"raw.base.BotApp",inactive :Optional [bool ]=None ,request_write_access :Optional [bool ]=None )->None :
        self .app =app 
        self .inactive =inactive 
        self .request_write_access =request_write_access 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BotApp":

        flags =Int .read (b )

        inactive =True if flags &(1 <<0 )else False 
        request_write_access =True if flags &(1 <<1 )else False 
        app =TLObject .read (b )

        return BotApp (app =app ,inactive =inactive ,request_write_access =request_write_access )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .inactive else 0 
        flags |=(1 <<1 )if self .request_write_access else 0 
        b .write (Int (flags ))

        b .write (self .app .write ())

        return b .getvalue ()
