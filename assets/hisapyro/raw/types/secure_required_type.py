
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SecureRequiredType (TLObject ):
    """"""

    __slots__ :List [str ]=["type","native_names","selfie_required","translation_required"]

    ID =0x829d99da 
    QUALNAME ="types.SecureRequiredType"

    def __init__ (self ,*,type :"raw.base.SecureValueType",native_names :Optional [bool ]=None ,selfie_required :Optional [bool ]=None ,translation_required :Optional [bool ]=None )->None :
        self .type =type 
        self .native_names =native_names 
        self .selfie_required =selfie_required 
        self .translation_required =translation_required 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SecureRequiredType":

        flags =Int .read (b )

        native_names =True if flags &(1 <<0 )else False 
        selfie_required =True if flags &(1 <<1 )else False 
        translation_required =True if flags &(1 <<2 )else False 
        type =TLObject .read (b )

        return SecureRequiredType (type =type ,native_names =native_names ,selfie_required =selfie_required ,translation_required =translation_required )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .native_names else 0 
        flags |=(1 <<1 )if self .selfie_required else 0 
        flags |=(1 <<2 )if self .translation_required else 0 
        b .write (Int (flags ))

        b .write (self .type .write ())

        return b .getvalue ()
