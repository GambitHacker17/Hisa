
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Support (TLObject ):
    """"""

    __slots__ :List [str ]=["phone_number","user"]

    ID =0x17c6b5f6 
    QUALNAME ="types.help.Support"

    def __init__ (self ,*,phone_number :str ,user :"raw.base.User")->None :
        self .phone_number =phone_number 
        self .user =user 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Support":

        phone_number =String .read (b )

        user =TLObject .read (b )

        return Support (phone_number =phone_number ,user =user )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .phone_number ))

        b .write (self .user .write ())

        return b .getvalue ()
