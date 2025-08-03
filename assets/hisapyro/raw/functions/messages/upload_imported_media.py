
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UploadImportedMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","import_id","file_name","media"]

    ID =0x2a862092 
    QUALNAME ="functions.messages.UploadImportedMedia"

    def __init__ (self ,*,peer :"raw.base.InputPeer",import_id :int ,file_name :str ,media :"raw.base.InputMedia")->None :
        self .peer =peer 
        self .import_id =import_id 
        self .file_name =file_name 
        self .media =media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UploadImportedMedia":

        peer =TLObject .read (b )

        import_id =Long .read (b )

        file_name =String .read (b )

        media =TLObject .read (b )

        return UploadImportedMedia (peer =peer ,import_id =import_id ,file_name =file_name ,media =media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Long (self .import_id ))

        b .write (String (self .file_name ))

        b .write (self .media .write ())

        return b .getvalue ()
