
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetCustomEmojiDocuments (TLObject ):
    """"""

    __slots__ :List [str ]=["document_id"]

    ID =0xd9ab0f54 
    QUALNAME ="functions.messages.GetCustomEmojiDocuments"

    def __init__ (self ,*,document_id :List [int ])->None :
        self .document_id =document_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetCustomEmojiDocuments":

        document_id =TLObject .read (b ,Long )

        return GetCustomEmojiDocuments (document_id =document_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .document_id ,Long ))

        return b .getvalue ()
