
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PhoneConnection (TLObject ):
    """"""

    __slots__ :List [str ]=["id","ip","ipv6","port","peer_tag","tcp"]

    ID =0x9cc123c7 
    QUALNAME ="types.PhoneConnection"

    def __init__ (self ,*,id :int ,ip :str ,ipv6 :str ,port :int ,peer_tag :bytes ,tcp :Optional [bool ]=None )->None :
        self .id =id 
        self .ip =ip 
        self .ipv6 =ipv6 
        self .port =port 
        self .peer_tag =peer_tag 
        self .tcp =tcp 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PhoneConnection":

        flags =Int .read (b )

        tcp =True if flags &(1 <<0 )else False 
        id =Long .read (b )

        ip =String .read (b )

        ipv6 =String .read (b )

        port =Int .read (b )

        peer_tag =Bytes .read (b )

        return PhoneConnection (id =id ,ip =ip ,ipv6 =ipv6 ,port =port ,peer_tag =peer_tag ,tcp =tcp )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .tcp else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (String (self .ip ))

        b .write (String (self .ipv6 ))

        b .write (Int (self .port ))

        b .write (Bytes (self .peer_tag ))

        return b .getvalue ()
