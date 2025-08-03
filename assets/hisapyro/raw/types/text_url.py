
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TextUrl (TLObject ):
    """"""

    __slots__ :List [str ]=["text","url","webpage_id"]

    ID =0x3c2884c1 
    QUALNAME ="types.TextUrl"

    def __init__ (self ,*,text :"raw.base.RichText",url :str ,webpage_id :int )->None :
        self .text =text 
        self .url =url 
        self .webpage_id =webpage_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TextUrl":

        text =TLObject .read (b )

        url =String .read (b )

        webpage_id =Long .read (b )

        return TextUrl (text =text ,url =url ,webpage_id =webpage_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .text .write ())

        b .write (String (self .url ))

        b .write (Long (self .webpage_id ))

        return b .getvalue ()
