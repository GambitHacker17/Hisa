
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextWithEntities (TLObject ):
    """"""

    __slots__ :List [str ]=["text","entities"]

    ID =0x751f3146 
    QUALNAME ="types.TextWithEntities"

    def __init__ (self ,*,text :str ,entities :List ["raw.base.MessageEntity"])->None :
        self .text =text 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextWithEntities":

        text =String .read (b )

        entities =TLObject .read (b )

        return TextWithEntities (text =text ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .text ))

        b .write (Vector (self .entities ))

        return b .getvalue ()
