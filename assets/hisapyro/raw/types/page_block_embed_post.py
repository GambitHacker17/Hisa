
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockEmbedPost (TLObject ):
    """"""

    __slots__ :List [str ]=["url","webpage_id","author_photo_id","author","date","blocks","caption"]

    ID =0xf259a80b 
    QUALNAME ="types.PageBlockEmbedPost"

    def __init__ (self ,*,url :str ,webpage_id :int ,author_photo_id :int ,author :str ,date :int ,blocks :List ["raw.base.PageBlock"],caption :"raw.base.PageCaption")->None :
        self .url =url 
        self .webpage_id =webpage_id 
        self .author_photo_id =author_photo_id 
        self .author =author 
        self .date =date 
        self .blocks =blocks 
        self .caption =caption 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockEmbedPost":

        url =String .read (b )

        webpage_id =Long .read (b )

        author_photo_id =Long .read (b )

        author =String .read (b )

        date =Int .read (b )

        blocks =TLObject .read (b )

        caption =TLObject .read (b )

        return PageBlockEmbedPost (url =url ,webpage_id =webpage_id ,author_photo_id =author_photo_id ,author =author ,date =date ,blocks =blocks ,caption =caption )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .url ))

        b .write (Long (self .webpage_id ))

        b .write (Long (self .author_photo_id ))

        b .write (String (self .author ))

        b .write (Int (self .date ))

        b .write (Vector (self .blocks ))

        b .write (self .caption .write ())

        return b .getvalue ()
