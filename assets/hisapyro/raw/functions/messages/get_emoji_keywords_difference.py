
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetEmojiKeywordsDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code","from_version"]

    ID =0x1508b6af 
    QUALNAME ="functions.messages.GetEmojiKeywordsDifference"

    def __init__ (self ,*,lang_code :str ,from_version :int )->None :
        self .lang_code =lang_code 
        self .from_version =from_version 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetEmojiKeywordsDifference":

        lang_code =String .read (b )

        from_version =Int .read (b )

        return GetEmojiKeywordsDifference (lang_code =lang_code ,from_version =from_version )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        b .write (Int (self .from_version ))

        return b .getvalue ()
