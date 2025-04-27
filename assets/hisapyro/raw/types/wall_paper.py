
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","slug","document","creator","default","pattern","dark","settings"]

    ID =0xa437c3ed 
    QUALNAME ="types.WallPaper"

    def __init__ (self ,*,id :int ,access_hash :int ,slug :str ,document :"raw.base.Document",creator :Optional [bool ]=None ,default :Optional [bool ]=None ,pattern :Optional [bool ]=None ,dark :Optional [bool ]=None ,settings :"raw.base.WallPaperSettings"=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .slug =slug 
        self .document =document 
        self .creator =creator 
        self .default =default 
        self .pattern =pattern 
        self .dark =dark 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WallPaper":

        id =Long .read (b )

        flags =Int .read (b )

        creator =True if flags &(1 <<0 )else False 
        default =True if flags &(1 <<1 )else False 
        pattern =True if flags &(1 <<3 )else False 
        dark =True if flags &(1 <<4 )else False 
        access_hash =Long .read (b )

        slug =String .read (b )

        document =TLObject .read (b )

        settings =TLObject .read (b )if flags &(1 <<2 )else None 

        return WallPaper (id =id ,access_hash =access_hash ,slug =slug ,document =document ,creator =creator ,default =default ,pattern =pattern ,dark =dark ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))
        flags =0 
        flags |=(1 <<0 )if self .creator else 0 
        flags |=(1 <<1 )if self .default else 0 
        flags |=(1 <<3 )if self .pattern else 0 
        flags |=(1 <<4 )if self .dark else 0 
        flags |=(1 <<2 )if self .settings is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .access_hash ))

        b .write (String (self .slug ))

        b .write (self .document .write ())

        if self .settings is not None :
            b .write (self .settings .write ())

        return b .getvalue ()
