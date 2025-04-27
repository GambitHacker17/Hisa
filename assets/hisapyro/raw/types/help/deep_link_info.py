
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeepLinkInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["message","update_app","entities"]

    ID =0x6a4ee832 
    QUALNAME ="types.help.DeepLinkInfo"

    def __init__ (self ,*,message :str ,update_app :Optional [bool ]=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .message =message 
        self .update_app =update_app 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeepLinkInfo":

        flags =Int .read (b )

        update_app =True if flags &(1 <<0 )else False 
        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<1 )else []

        return DeepLinkInfo (message =message ,update_app =update_app ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .update_app else 0 
        flags |=(1 <<1 )if self .entities else 0 
        b .write (Int (flags ))

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        return b .getvalue ()
