
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UploadRingtone (TLObject ):
    """"""

    __slots__ :List [str ]=["file","file_name","mime_type"]

    ID =0x831a83a2 
    QUALNAME ="functions.account.UploadRingtone"

    def __init__ (self ,*,file :"raw.base.InputFile",file_name :str ,mime_type :str )->None :
        self .file =file 
        self .file_name =file_name 
        self .mime_type =mime_type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UploadRingtone":

        file =TLObject .read (b )

        file_name =String .read (b )

        mime_type =String .read (b )

        return UploadRingtone (file =file ,file_name =file_name ,mime_type =mime_type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .file .write ())

        b .write (String (self .file_name ))

        b .write (String (self .mime_type ))

        return b .getvalue ()
