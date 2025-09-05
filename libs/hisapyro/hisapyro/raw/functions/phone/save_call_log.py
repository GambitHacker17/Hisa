
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveCallLog (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","file"]

    ID =0x41248786 
    QUALNAME ="functions.phone.SaveCallLog"

    def __init__ (self ,*,peer :"raw.base.InputPhoneCall",file :"raw.base.InputFile")->None :
        self .peer =peer 
        self .file =file 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveCallLog":

        peer =TLObject .read (b )

        file =TLObject .read (b )

        return SaveCallLog (peer =peer ,file =file )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .file .write ())

        return b .getvalue ()
