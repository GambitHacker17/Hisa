
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Username (TLObject ):
    """"""

    __slots__ :List [str ]=["username","editable","active"]

    ID =0xb4073647 
    QUALNAME ="types.Username"

    def __init__ (self ,*,username :str ,editable :Optional [bool ]=None ,active :Optional [bool ]=None )->None :
        self .username =username 
        self .editable =editable 
        self .active =active 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Username":

        flags =Int .read (b )

        editable =True if flags &(1 <<0 )else False 
        active =True if flags &(1 <<1 )else False 
        username =String .read (b )

        return Username (username =username ,editable =editable ,active =active )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .editable else 0 
        flags |=(1 <<1 )if self .active else 0 
        b .write (Int (flags ))

        b .write (String (self .username ))

        return b .getvalue ()
