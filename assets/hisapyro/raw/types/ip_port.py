
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class IpPort (TLObject ):
    """"""

    __slots__ :List [str ]=["ipv4","port"]

    ID =0xd433ad73 
    QUALNAME ="types.IpPort"

    def __init__ (self ,*,ipv4 :int ,port :int )->None :
        self .ipv4 =ipv4 
        self .port =port 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"IpPort":

        ipv4 =Int .read (b )

        port =Int .read (b )

        return IpPort (ipv4 =ipv4 ,port =port )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .ipv4 ))

        b .write (Int (self .port ))

        return b .getvalue ()
