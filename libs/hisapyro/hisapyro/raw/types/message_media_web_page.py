
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageMediaWebPage (TLObject ):
    """"""

    __slots__ :List [str ]=["webpage"]

    ID =0xa32dd600 
    QUALNAME ="types.MessageMediaWebPage"

    def __init__ (self ,*,webpage :"raw.base.WebPage")->None :
        self .webpage =webpage 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageMediaWebPage":

        webpage =TLObject .read (b )

        return MessageMediaWebPage (webpage =webpage )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .webpage .write ())

        return b .getvalue ()
