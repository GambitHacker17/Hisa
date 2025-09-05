
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextImage (TLObject ):
    """"""

    __slots__ :List [str ]=["document_id","w","h"]

    ID =0x81ccf4f 
    QUALNAME ="types.TextImage"

    def __init__ (self ,*,document_id :int ,w :int ,h :int )->None :
        self .document_id =document_id 
        self .w =w 
        self .h =h 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextImage":

        document_id =Long .read (b )

        w =Int .read (b )

        h =Int .read (b )

        return TextImage (document_id =document_id ,w =w ,h =h )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .document_id ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        return b .getvalue ()
