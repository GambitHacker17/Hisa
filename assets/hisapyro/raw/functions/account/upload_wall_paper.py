
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UploadWallPaper (TLObject ):
    """"""

    __slots__ :List [str ]=["file","mime_type","settings","for_chat"]

    ID =0xe39a8f03 
    QUALNAME ="functions.account.UploadWallPaper"

    def __init__ (self ,*,file :"raw.base.InputFile",mime_type :str ,settings :"raw.base.WallPaperSettings",for_chat :Optional [bool ]=None )->None :
        self .file =file 
        self .mime_type =mime_type 
        self .settings =settings 
        self .for_chat =for_chat 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UploadWallPaper":

        flags =Int .read (b )

        for_chat =True if flags &(1 <<0 )else False 
        file =TLObject .read (b )

        mime_type =String .read (b )

        settings =TLObject .read (b )

        return UploadWallPaper (file =file ,mime_type =mime_type ,settings =settings ,for_chat =for_chat )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .for_chat else 0 
        b .write (Int (flags ))

        b .write (self .file .write ())

        b .write (String (self .mime_type ))

        b .write (self .settings .write ())

        return b .getvalue ()
