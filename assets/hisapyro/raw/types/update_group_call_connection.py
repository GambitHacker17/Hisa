
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateGroupCallConnection (TLObject ):
    """"""

    __slots__ :List [str ]=["params","presentation"]

    ID =0xb783982 
    QUALNAME ="types.UpdateGroupCallConnection"

    def __init__ (self ,*,params :"raw.base.DataJSON",presentation :Optional [bool ]=None )->None :
        self .params =params 
        self .presentation =presentation 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateGroupCallConnection":

        flags =Int .read (b )

        presentation =True if flags &(1 <<0 )else False 
        params =TLObject .read (b )

        return UpdateGroupCallConnection (params =params ,presentation =presentation )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .presentation else 0 
        b .write (Int (flags ))

        b .write (self .params .write ())

        return b .getvalue ()
