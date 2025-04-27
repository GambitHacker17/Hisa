
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetWebFile (TLObject ):
    """"""

    __slots__ :List [str ]=["location","offset","limit"]

    ID =0x24e6818d 
    QUALNAME ="functions.upload.GetWebFile"

    def __init__ (self ,*,location :"raw.base.InputWebFileLocation",offset :int ,limit :int )->None :
        self .location =location 
        self .offset =offset 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetWebFile":

        location =TLObject .read (b )

        offset =Int .read (b )

        limit =Int .read (b )

        return GetWebFile (location =location ,offset =offset ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .location .write ())

        b .write (Int (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
