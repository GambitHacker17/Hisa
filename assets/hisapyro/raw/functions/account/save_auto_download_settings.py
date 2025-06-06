
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveAutoDownloadSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["settings","low","high"]

    ID =0x76f36233 
    QUALNAME ="functions.account.SaveAutoDownloadSettings"

    def __init__ (self ,*,settings :"raw.base.AutoDownloadSettings",low :Optional [bool ]=None ,high :Optional [bool ]=None )->None :
        self .settings =settings 
        self .low =low 
        self .high =high 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveAutoDownloadSettings":

        flags =Int .read (b )

        low =True if flags &(1 <<0 )else False 
        high =True if flags &(1 <<1 )else False 
        settings =TLObject .read (b )

        return SaveAutoDownloadSettings (settings =settings ,low =low ,high =high )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .low else 0 
        flags |=(1 <<1 )if self .high else 0 
        b .write (Int (flags ))

        b .write (self .settings .write ())

        return b .getvalue ()
