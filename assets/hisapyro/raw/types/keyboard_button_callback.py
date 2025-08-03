
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonCallback (TLObject ):
    """"""

    __slots__ :List [str ]=["text","data","requires_password"]

    ID =0x35bbdb6b 
    QUALNAME ="types.KeyboardButtonCallback"

    def __init__ (self ,*,text :str ,data :bytes ,requires_password :Optional [bool ]=None )->None :
        self .text =text 
        self .data =data 
        self .requires_password =requires_password 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonCallback":

        flags =Int .read (b )

        requires_password =True if flags &(1 <<0 )else False 
        text =String .read (b )

        data =Bytes .read (b )

        return KeyboardButtonCallback (text =text ,data =data ,requires_password =requires_password )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .requires_password else 0 
        b .write (Int (flags ))

        b .write (String (self .text ))

        b .write (Bytes (self .data ))

        return b .getvalue ()
