
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputStickerSetItem (TLObject ):
    """"""

    __slots__ :List [str ]=["document","emoji","mask_coords","keywords"]

    ID =0x32da9e9c 
    QUALNAME ="types.InputStickerSetItem"

    def __init__ (self ,*,document :"raw.base.InputDocument",emoji :str ,mask_coords :"raw.base.MaskCoords"=None ,keywords :Optional [str ]=None )->None :
        self .document =document 
        self .emoji =emoji 
        self .mask_coords =mask_coords 
        self .keywords =keywords 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputStickerSetItem":

        flags =Int .read (b )

        document =TLObject .read (b )

        emoji =String .read (b )

        mask_coords =TLObject .read (b )if flags &(1 <<0 )else None 

        keywords =String .read (b )if flags &(1 <<1 )else None 
        return InputStickerSetItem (document =document ,emoji =emoji ,mask_coords =mask_coords ,keywords =keywords )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .mask_coords is not None else 0 
        flags |=(1 <<1 )if self .keywords is not None else 0 
        b .write (Int (flags ))

        b .write (self .document .write ())

        b .write (String (self .emoji ))

        if self .mask_coords is not None :
            b .write (self .mask_coords .write ())

        if self .keywords is not None :
            b .write (String (self .keywords ))

        return b .getvalue ()
