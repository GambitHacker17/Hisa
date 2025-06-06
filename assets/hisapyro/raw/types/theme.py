
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Theme (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","slug","title","creator","default","for_chat","document","settings","emoticon","installs_count"]

    ID =0xa00e67d6 
    QUALNAME ="types.Theme"

    def __init__ (self ,*,id :int ,access_hash :int ,slug :str ,title :str ,creator :Optional [bool ]=None ,default :Optional [bool ]=None ,for_chat :Optional [bool ]=None ,document :"raw.base.Document"=None ,settings :Optional [List ["raw.base.ThemeSettings"]]=None ,emoticon :Optional [str ]=None ,installs_count :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .slug =slug 
        self .title =title 
        self .creator =creator 
        self .default =default 
        self .for_chat =for_chat 
        self .document =document 
        self .settings =settings 
        self .emoticon =emoticon 
        self .installs_count =installs_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Theme":

        flags =Int .read (b )

        creator =True if flags &(1 <<0 )else False 
        default =True if flags &(1 <<1 )else False 
        for_chat =True if flags &(1 <<5 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        slug =String .read (b )

        title =String .read (b )

        document =TLObject .read (b )if flags &(1 <<2 )else None 

        settings =TLObject .read (b )if flags &(1 <<3 )else []

        emoticon =String .read (b )if flags &(1 <<6 )else None 
        installs_count =Int .read (b )if flags &(1 <<4 )else None 
        return Theme (id =id ,access_hash =access_hash ,slug =slug ,title =title ,creator =creator ,default =default ,for_chat =for_chat ,document =document ,settings =settings ,emoticon =emoticon ,installs_count =installs_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .creator else 0 
        flags |=(1 <<1 )if self .default else 0 
        flags |=(1 <<5 )if self .for_chat else 0 
        flags |=(1 <<2 )if self .document is not None else 0 
        flags |=(1 <<3 )if self .settings else 0 
        flags |=(1 <<6 )if self .emoticon is not None else 0 
        flags |=(1 <<4 )if self .installs_count is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (String (self .slug ))

        b .write (String (self .title ))

        if self .document is not None :
            b .write (self .document .write ())

        if self .settings is not None :
            b .write (Vector (self .settings ))

        if self .emoticon is not None :
            b .write (String (self .emoticon ))

        if self .installs_count is not None :
            b .write (Int (self .installs_count ))

        return b .getvalue ()
