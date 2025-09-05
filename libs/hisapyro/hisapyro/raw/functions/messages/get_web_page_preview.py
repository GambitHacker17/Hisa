
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetWebPagePreview (TLObject ):
    """"""

    __slots__ :List [str ]=["message","entities"]

    ID =0x8b68b0cc 
    QUALNAME ="functions.messages.GetWebPagePreview"

    def __init__ (self ,*,message :str ,entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .message =message 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetWebPagePreview":

        flags =Int .read (b )

        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<3 )else []

        return GetWebPagePreview (message =message ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .entities else 0 
        b .write (Int (flags ))

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        return b .getvalue ()
