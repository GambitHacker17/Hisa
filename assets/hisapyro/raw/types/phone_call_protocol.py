
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneCallProtocol (TLObject ):
    """"""

    __slots__ :List [str ]=["min_layer","max_layer","library_versions","udp_p2p","udp_reflector"]

    ID =0xfc878fc8 
    QUALNAME ="types.PhoneCallProtocol"

    def __init__ (self ,*,min_layer :int ,max_layer :int ,library_versions :List [str ],udp_p2p :Optional [bool ]=None ,udp_reflector :Optional [bool ]=None )->None :
        self .min_layer =min_layer 
        self .max_layer =max_layer 
        self .library_versions =library_versions 
        self .udp_p2p =udp_p2p 
        self .udp_reflector =udp_reflector 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneCallProtocol":

        flags =Int .read (b )

        udp_p2p =True if flags &(1 <<0 )else False 
        udp_reflector =True if flags &(1 <<1 )else False 
        min_layer =Int .read (b )

        max_layer =Int .read (b )

        library_versions =TLObject .read (b ,String )

        return PhoneCallProtocol (min_layer =min_layer ,max_layer =max_layer ,library_versions =library_versions ,udp_p2p =udp_p2p ,udp_reflector =udp_reflector )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .udp_p2p else 0 
        flags |=(1 <<1 )if self .udp_reflector else 0 
        b .write (Int (flags ))

        b .write (Int (self .min_layer ))

        b .write (Int (self .max_layer ))

        b .write (Vector (self .library_versions ,String ))

        return b .getvalue ()
