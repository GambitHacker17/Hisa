
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReactionCustomEmoji (TLObject ):
    """"""

    __slots__ :List [str ]=["document_id"]

    ID =0x8935fc73 
    QUALNAME ="types.ReactionCustomEmoji"

    def __init__ (self ,*,document_id :int )->None :
        self .document_id =document_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReactionCustomEmoji":

        document_id =Long .read (b )

        return ReactionCustomEmoji (document_id =document_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .document_id ))

        return b .getvalue ()
