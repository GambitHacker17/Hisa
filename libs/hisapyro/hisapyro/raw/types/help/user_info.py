
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UserInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["message","entities","author","date"]

    ID =0x1eb3758 
    QUALNAME ="types.help.UserInfo"

    def __init__ (self ,*,message :str ,entities :List ["raw.base.MessageEntity"],author :str ,date :int )->None :
        self .message =message 
        self .entities =entities 
        self .author =author 
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UserInfo":

        message =String .read (b )

        entities =TLObject .read (b )

        author =String .read (b )

        date =Int .read (b )

        return UserInfo (message =message ,entities =entities ,author =author ,date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .message ))

        b .write (Vector (self .entities ))

        b .write (String (self .author ))

        b .write (Int (self .date ))

        return b .getvalue ()
