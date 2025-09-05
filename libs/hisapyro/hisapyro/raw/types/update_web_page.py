
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateWebPage (TLObject ):
    """"""

    __slots__ :List [str ]=["webpage","pts","pts_count"]

    ID =0x7f891213 
    QUALNAME ="types.UpdateWebPage"

    def __init__ (self ,*,webpage :"raw.base.WebPage",pts :int ,pts_count :int )->None :
        self .webpage =webpage 
        self .pts =pts 
        self .pts_count =pts_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateWebPage":

        webpage =TLObject .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        return UpdateWebPage (webpage =webpage ,pts =pts ,pts_count =pts_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .webpage .write ())

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        return b .getvalue ()
