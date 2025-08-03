
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageRange (TLObject ):
    """"""

    __slots__ :List [str ]=["min_id","max_id"]

    ID =0xae30253 
    QUALNAME ="types.MessageRange"

    def __init__ (self ,*,min_id :int ,max_id :int )->None :
        self .min_id =min_id 
        self .max_id =max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageRange":

        min_id =Int .read (b )

        max_id =Int .read (b )

        return MessageRange (min_id =min_id ,max_id =max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .min_id ))

        b .write (Int (self .max_id ))

        return b .getvalue ()
