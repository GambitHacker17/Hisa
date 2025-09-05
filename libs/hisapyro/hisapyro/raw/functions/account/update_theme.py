
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateTheme (TLObject ):
    """"""

    __slots__ :List [str ]=["format","theme","slug","title","document","settings"]

    ID =0x2bf40ccc 
    QUALNAME ="functions.account.UpdateTheme"

    def __init__ (self ,*,format :str ,theme :"raw.base.InputTheme",slug :Optional [str ]=None ,title :Optional [str ]=None ,document :"raw.base.InputDocument"=None ,settings :Optional [List ["raw.base.InputThemeSettings"]]=None )->None :
        self .format =format 
        self .theme =theme 
        self .slug =slug 
        self .title =title 
        self .document =document 
        self .settings =settings 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateTheme":

        flags =Int .read (b )

        format =String .read (b )

        theme =TLObject .read (b )

        slug =String .read (b )if flags &(1 <<0 )else None 
        title =String .read (b )if flags &(1 <<1 )else None 
        document =TLObject .read (b )if flags &(1 <<2 )else None 

        settings =TLObject .read (b )if flags &(1 <<3 )else []

        return UpdateTheme (format =format ,theme =theme ,slug =slug ,title =title ,document =document ,settings =settings )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .slug is not None else 0 
        flags |=(1 <<1 )if self .title is not None else 0 
        flags |=(1 <<2 )if self .document is not None else 0 
        flags |=(1 <<3 )if self .settings else 0 
        b .write (Int (flags ))

        b .write (String (self .format ))

        b .write (self .theme .write ())

        if self .slug is not None :
            b .write (String (self .slug ))

        if self .title is not None :
            b .write (String (self .title ))

        if self .document is not None :
            b .write (self .document .write ())

        if self .settings is not None :
            b .write (Vector (self .settings ))

        return b .getvalue ()
