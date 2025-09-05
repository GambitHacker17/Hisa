
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RecentMeUrlChat (TLObject ):
    """"""

    __slots__ :List [str ]=["url","chat_id"]

    ID =0xb2da71d2 
    QUALNAME ="types.RecentMeUrlChat"

    def __init__ (self ,*,url :str ,chat_id :int )->None :
        self .url =url 
        self .chat_id =chat_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RecentMeUrlChat":

        url =String .read (b )

        chat_id =Long .read (b )

        return RecentMeUrlChat (url =url ,chat_id =chat_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Long (self .chat_id ))

        return b .getvalue ()
