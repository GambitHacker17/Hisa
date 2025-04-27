
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MaskCoords (TLObject ):
    """"""

    __slots__ :List [str ]=["n","x","y","zoom"]

    ID =0xaed6dbb2 
    QUALNAME ="types.MaskCoords"

    def __init__ (self ,*,n :int ,x :float ,y :float ,zoom :float )->None :
        self .n =n 
        self .x =x 
        self .y =y 
        self .zoom =zoom 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MaskCoords":

        n =Int .read (b )

        x =Double .read (b )

        y =Double .read (b )

        zoom =Double .read (b )

        return MaskCoords (n =n ,x =x ,y =y ,zoom =zoom )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .n ))

        b .write (Double (self .x ))

        b .write (Double (self .y ))

        b .write (Double (self .zoom ))

        return b .getvalue ()
