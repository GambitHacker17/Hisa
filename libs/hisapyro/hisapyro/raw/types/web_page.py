
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WebPage (TLObject ):
    """"""

    __slots__ :List [str ]=["id","url","display_url","hash","type","site_name","title","description","photo","embed_url","embed_type","embed_width","embed_height","duration","author","document","cached_page","attributes"]

    ID =0xe89c45b2 
    QUALNAME ="types.WebPage"

    def __init__ (self ,*,id :int ,url :str ,display_url :str ,hash :int ,type :Optional [str ]=None ,site_name :Optional [str ]=None ,title :Optional [str ]=None ,description :Optional [str ]=None ,photo :"raw.base.Photo"=None ,embed_url :Optional [str ]=None ,embed_type :Optional [str ]=None ,embed_width :Optional [int ]=None ,embed_height :Optional [int ]=None ,duration :Optional [int ]=None ,author :Optional [str ]=None ,document :"raw.base.Document"=None ,cached_page :"raw.base.Page"=None ,attributes :Optional [List ["raw.base.WebPageAttribute"]]=None )->None :
        self .id =id 
        self .url =url 
        self .display_url =display_url 
        self .hash =hash 
        self .type =type 
        self .site_name =site_name 
        self .title =title 
        self .description =description 
        self .photo =photo 
        self .embed_url =embed_url 
        self .embed_type =embed_type 
        self .embed_width =embed_width 
        self .embed_height =embed_height 
        self .duration =duration 
        self .author =author 
        self .document =document 
        self .cached_page =cached_page 
        self .attributes =attributes 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WebPage":

        flags =Int .read (b )

        id =Long .read (b )

        url =String .read (b )

        display_url =String .read (b )

        hash =Int .read (b )

        type =String .read (b )if flags &(1 <<0 )else None 
        site_name =String .read (b )if flags &(1 <<1 )else None 
        title =String .read (b )if flags &(1 <<2 )else None 
        description =String .read (b )if flags &(1 <<3 )else None 
        photo =TLObject .read (b )if flags &(1 <<4 )else None 

        embed_url =String .read (b )if flags &(1 <<5 )else None 
        embed_type =String .read (b )if flags &(1 <<5 )else None 
        embed_width =Int .read (b )if flags &(1 <<6 )else None 
        embed_height =Int .read (b )if flags &(1 <<6 )else None 
        duration =Int .read (b )if flags &(1 <<7 )else None 
        author =String .read (b )if flags &(1 <<8 )else None 
        document =TLObject .read (b )if flags &(1 <<9 )else None 

        cached_page =TLObject .read (b )if flags &(1 <<10 )else None 

        attributes =TLObject .read (b )if flags &(1 <<12 )else []

        return WebPage (id =id ,url =url ,display_url =display_url ,hash =hash ,type =type ,site_name =site_name ,title =title ,description =description ,photo =photo ,embed_url =embed_url ,embed_type =embed_type ,embed_width =embed_width ,embed_height =embed_height ,duration =duration ,author =author ,document =document ,cached_page =cached_page ,attributes =attributes )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .type is not None else 0 
        flags |=(1 <<1 )if self .site_name is not None else 0 
        flags |=(1 <<2 )if self .title is not None else 0 
        flags |=(1 <<3 )if self .description is not None else 0 
        flags |=(1 <<4 )if self .photo is not None else 0 
        flags |=(1 <<5 )if self .embed_url is not None else 0 
        flags |=(1 <<5 )if self .embed_type is not None else 0 
        flags |=(1 <<6 )if self .embed_width is not None else 0 
        flags |=(1 <<6 )if self .embed_height is not None else 0 
        flags |=(1 <<7 )if self .duration is not None else 0 
        flags |=(1 <<8 )if self .author is not None else 0 
        flags |=(1 <<9 )if self .document is not None else 0 
        flags |=(1 <<10 )if self .cached_page is not None else 0 
        flags |=(1 <<12 )if self .attributes else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (String (self .url ))

        b .write (String (self .display_url ))

        b .write (Int (self .hash ))

        if self .type is not None :
            b .write (String (self .type ))

        if self .site_name is not None :
            b .write (String (self .site_name ))

        if self .title is not None :
            b .write (String (self .title ))

        if self .description is not None :
            b .write (String (self .description ))

        if self .photo is not None :
            b .write (self .photo .write ())

        if self .embed_url is not None :
            b .write (String (self .embed_url ))

        if self .embed_type is not None :
            b .write (String (self .embed_type ))

        if self .embed_width is not None :
            b .write (Int (self .embed_width ))

        if self .embed_height is not None :
            b .write (Int (self .embed_height ))

        if self .duration is not None :
            b .write (Int (self .duration ))

        if self .author is not None :
            b .write (String (self .author ))

        if self .document is not None :
            b .write (self .document .write ())

        if self .cached_page is not None :
            b .write (self .cached_page .write ())

        if self .attributes is not None :
            b .write (Vector (self .attributes ))

        return b .getvalue ()
