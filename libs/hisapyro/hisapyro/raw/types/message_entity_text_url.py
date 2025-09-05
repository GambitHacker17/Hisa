
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageEntityTextUrl (TLObject ):
    """"""

    __slots__ :List [str ]=["offset","length","url"]

    ID =0x76a6d327 
    QUALNAME ="types.MessageEntityTextUrl"

    def __init__ (self ,*,offset :int ,length :int ,url :str )->None :
        self .offset =offset 
        self .length =length 
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageEntityTextUrl":

        offset =Int .read (b )

        length =Int .read (b )

        url =String .read (b )

        return MessageEntityTextUrl (offset =offset ,length =length ,url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .offset ))

        b .write (Int (self .length ))

        b .write (String (self .url ))

        return b .getvalue ()
