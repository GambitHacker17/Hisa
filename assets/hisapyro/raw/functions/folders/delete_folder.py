
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteFolder (TLObject ):
    """"""

    __slots__ :List [str ]=["folder_id"]

    ID =0x1c295881 
    QUALNAME ="functions.folders.DeleteFolder"

    def __init__ (self ,*,folder_id :int )->None :
        self .folder_id =folder_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteFolder":

        folder_id =Int .read (b )

        return DeleteFolder (folder_id =folder_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Int (self .folder_id ))

        return b .getvalue ()
