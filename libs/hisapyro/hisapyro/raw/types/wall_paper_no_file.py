
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WallPaperNoFile (TLObject ):
    """"""

    __slots__ :List [str ]=["id","default","dark","settings"]

    ID =0xe0804116 
    QUALNAME ="types.WallPaperNoFile"

    def __init__ (self ,*,id :int ,default :Optional [bool ]=None ,dark :Optional [bool ]=None ,settings :"raw.base.WallPaperSettings"=None )->None :
        self .id =id 
        self .default =default 
        self .dark =dark 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WallPaperNoFile":

        id =Long .read (b )

        flags =Int .read (b )

        default =True if flags &(1 <<1 )else False 
        dark =True if flags &(1 <<4 )else False 
        settings =TLObject .read (b )if flags &(1 <<2 )else None 

        return WallPaperNoFile (id =id ,default =default ,dark =dark ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))
        flags =0 
        flags |=(1 <<1 )if self .default else 0 
        flags |=(1 <<4 )if self .dark else 0 
        flags |=(1 <<2 )if self .settings is not None else 0 
        b .write (Int (flags ))

        if self .settings is not None :
            b .write (self .settings .write ())

        return b .getvalue ()
