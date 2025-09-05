
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveCallDebug (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","debug"]

    ID =0x277add7e 
    QUALNAME ="functions.phone.SaveCallDebug"

    def __init__ (self ,*,peer :"raw.base.InputPhoneCall",debug :"raw.base.DataJSON")->None :
        self .peer =peer 
        self .debug =debug 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveCallDebug":

        peer =TLObject .read (b )

        debug =TLObject .read (b )

        return SaveCallDebug (peer =peer ,debug =debug )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .debug .write ())

        return b .getvalue ()
