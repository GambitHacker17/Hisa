
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentMeUrlUser (TLObject ):
    """"""

    __slots__ :List [str ]=["url","user_id"]

    ID =0xb92c09e2 
    QUALNAME ="types.RecentMeUrlUser"

    def __init__ (self ,*,url :str ,user_id :int )->None :
        self .url =url 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentMeUrlUser":

        url =String .read (b )

        user_id =Long .read (b )

        return RecentMeUrlUser (url =url ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Long (self .user_id ))

        return b .getvalue ()
