
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockVideo (TLObject ):
    """"""

    __slots__ :List [str ]=["video_id","caption","autoplay","loop"]

    ID =0x7c8fe7b6 
    QUALNAME ="types.PageBlockVideo"

    def __init__ (self ,*,video_id :int ,caption :"raw.base.PageCaption",autoplay :Optional [bool ]=None ,loop :Optional [bool ]=None )->None :
        self .video_id =video_id 
        self .caption =caption 
        self .autoplay =autoplay 
        self .loop =loop 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockVideo":

        flags =Int .read (b )

        autoplay =True if flags &(1 <<0 )else False 
        loop =True if flags &(1 <<1 )else False 
        video_id =Long .read (b )

        caption =TLObject .read (b )

        return PageBlockVideo (video_id =video_id ,caption =caption ,autoplay =autoplay ,loop =loop )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .autoplay else 0 
        flags |=(1 <<1 )if self .loop else 0 
        b .write (Int (flags ))

        b .write (Long (self .video_id ))

        b .write (self .caption .write ())

        return b .getvalue ()
