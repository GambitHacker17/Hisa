
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["id"]

    ID =0x63c66506 
    QUALNAME ="functions.messages.GetMessages"

    def __init__ (self ,*,id :List ["raw.base.InputMessage"])->None :
        self .id =id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMessages":

        id =TLObject .read (b )

        return GetMessages (id =id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .id ))

        return b .getvalue ()
