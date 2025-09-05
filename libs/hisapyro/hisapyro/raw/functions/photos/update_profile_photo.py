
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateProfilePhoto (TLObject ):
    """"""

    __slots__ :List [str ]=["id","fallback","bot"]

    ID =0x9e82039 
    QUALNAME ="functions.photos.UpdateProfilePhoto"

    def __init__ (self ,*,id :"raw.base.InputPhoto",fallback :Optional [bool ]=None ,bot :"raw.base.InputUser"=None )->None :
        self .id =id 
        self .fallback =fallback 
        self .bot =bot 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateProfilePhoto":

        flags =Int .read (b )

        fallback =True if flags &(1 <<0 )else False 
        bot =TLObject .read (b )if flags &(1 <<1 )else None 

        id =TLObject .read (b )

        return UpdateProfilePhoto (id =id ,fallback =fallback ,bot =bot )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .fallback else 0 
        flags |=(1 <<1 )if self .bot is not None else 0 
        b .write (Int (flags ))

        if self .bot is not None :
            b .write (self .bot .write ())

        b .write (self .id .write ())

        return b .getvalue ()
