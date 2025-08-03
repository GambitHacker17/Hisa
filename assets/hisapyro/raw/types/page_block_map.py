
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockMap (TLObject ):
    """"""

    __slots__ :List [str ]=["geo","zoom","w","h","caption"]

    ID =0xa44f3ef6 
    QUALNAME ="types.PageBlockMap"

    def __init__ (self ,*,geo :"raw.base.GeoPoint",zoom :int ,w :int ,h :int ,caption :"raw.base.PageCaption")->None :
        self .geo =geo 
        self .zoom =zoom 
        self .w =w 
        self .h =h 
        self .caption =caption 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockMap":

        geo =TLObject .read (b )

        zoom =Int .read (b )

        w =Int .read (b )

        h =Int .read (b )

        caption =TLObject .read (b )

        return PageBlockMap (geo =geo ,zoom =zoom ,w =w ,h =h ,caption =caption )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .geo .write ())

        b .write (Int (self .zoom ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        b .write (self .caption .write ())

        return b .getvalue ()
