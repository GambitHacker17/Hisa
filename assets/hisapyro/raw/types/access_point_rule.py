
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AccessPointRule (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_prefix_rules","dc_id","ips"]

    ID =0x4679b65f 
    QUALNAME ="types.AccessPointRule"

    def __init__ (self ,*,phone_prefix_rules :str ,dc_id :int ,ips :List ["raw.base.IpPort"])->None :
        self .phone_prefix_rules =phone_prefix_rules 
        self .dc_id =dc_id 
        self .ips =ips 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AccessPointRule":

        phone_prefix_rules =String .read (b )

        dc_id =Int .read (b )

        ips =TLObject .read (b )

        return AccessPointRule (phone_prefix_rules =phone_prefix_rules ,dc_id =dc_id ,ips =ips )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_prefix_rules ))

        b .write (Int (self .dc_id ))

        b .write (Vector (self .ips ))

        return b .getvalue ()
