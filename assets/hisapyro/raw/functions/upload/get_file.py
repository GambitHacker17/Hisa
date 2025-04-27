
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetFile (TLObject ):
    """"""

    __slots__ :List [str ]=["location","offset","limit","precise","cdn_supported"]

    ID =0xbe5335be 
    QUALNAME ="functions.upload.GetFile"

    def __init__ (self ,*,location :"raw.base.InputFileLocation",offset :int ,limit :int ,precise :Optional [bool ]=None ,cdn_supported :Optional [bool ]=None )->None :
        self .location =location 
        self .offset =offset 
        self .limit =limit 
        self .precise =precise 
        self .cdn_supported =cdn_supported 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetFile":

        flags =Int .read (b )

        precise =True if flags &(1 <<0 )else False 
        cdn_supported =True if flags &(1 <<1 )else False 
        location =TLObject .read (b )

        offset =Long .read (b )

        limit =Int .read (b )

        return GetFile (location =location ,offset =offset ,limit =limit ,precise =precise ,cdn_supported =cdn_supported )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .precise else 0 
        flags |=(1 <<1 )if self .cdn_supported else 0 
        b .write (Int (flags ))

        b .write (self .location .write ())

        b .write (Long (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
