
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveRecentSticker (TLObject ):
    """"""

    __slots__ :List [str ]=["id","unsave","attached"]

    ID =0x392718f8 
    QUALNAME ="functions.messages.SaveRecentSticker"

    def __init__ (self ,*,id :"raw.base.InputDocument",unsave :bool ,attached :Optional [bool ]=None )->None :
        self .id =id 
        self .unsave =unsave 
        self .attached =attached 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveRecentSticker":

        flags =Int .read (b )

        attached =True if flags &(1 <<0 )else False 
        id =TLObject .read (b )

        unsave =Bool .read (b )

        return SaveRecentSticker (id =id ,unsave =unsave ,attached =attached )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .attached else 0 
        b .write (Int (flags ))

        b .write (self .id .write ())

        b .write (Bool (self .unsave ))

        return b .getvalue ()
