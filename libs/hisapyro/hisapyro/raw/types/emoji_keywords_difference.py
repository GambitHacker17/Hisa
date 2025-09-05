
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EmojiKeywordsDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["lang_code","from_version","version","keywords"]

    ID =0x5cc761bd 
    QUALNAME ="types.EmojiKeywordsDifference"

    def __init__ (self ,*,lang_code :str ,from_version :int ,version :int ,keywords :List ["raw.base.EmojiKeyword"])->None :
        self .lang_code =lang_code 
        self .from_version =from_version 
        self .version =version 
        self .keywords =keywords 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EmojiKeywordsDifference":

        lang_code =String .read (b )

        from_version =Int .read (b )

        version =Int .read (b )

        keywords =TLObject .read (b )

        return EmojiKeywordsDifference (lang_code =lang_code ,from_version =from_version ,version =version ,keywords =keywords )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .lang_code ))

        b .write (Int (self .from_version ))

        b .write (Int (self .version ))

        b .write (Vector (self .keywords ))

        return b .getvalue ()
