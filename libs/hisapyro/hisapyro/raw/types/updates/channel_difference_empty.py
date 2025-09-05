
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelDifferenceEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","final","timeout"]

    ID =0x3e11affb 
    QUALNAME ="types.updates.ChannelDifferenceEmpty"

    def __init__ (self ,*,pts :int ,final :Optional [bool ]=None ,timeout :Optional [int ]=None )->None :
        self .pts =pts 
        self .final =final 
        self .timeout =timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelDifferenceEmpty":

        flags =Int .read (b )

        final =True if flags &(1 <<0 )else False 
        pts =Int .read (b )

        timeout =Int .read (b )if flags &(1 <<1 )else None 
        return ChannelDifferenceEmpty (pts =pts ,final =final ,timeout =timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .final else 0 
        flags |=(1 <<1 )if self .timeout is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .pts ))

        if self .timeout is not None :
            b .write (Int (self .timeout ))

        return b .getvalue ()
