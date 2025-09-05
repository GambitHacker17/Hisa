
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class WallPaperSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["blur","motion","background_color","second_background_color","third_background_color","fourth_background_color","intensity","rotation"]

    ID =0x1dc1bca4 
    QUALNAME ="types.WallPaperSettings"

    def __init__ (self ,*,blur :Optional [bool ]=None ,motion :Optional [bool ]=None ,background_color :Optional [int ]=None ,second_background_color :Optional [int ]=None ,third_background_color :Optional [int ]=None ,fourth_background_color :Optional [int ]=None ,intensity :Optional [int ]=None ,rotation :Optional [int ]=None )->None :
        self .blur =blur 
        self .motion =motion 
        self .background_color =background_color 
        self .second_background_color =second_background_color 
        self .third_background_color =third_background_color 
        self .fourth_background_color =fourth_background_color 
        self .intensity =intensity 
        self .rotation =rotation 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"WallPaperSettings":

        flags =Int .read (b )

        blur =True if flags &(1 <<1 )else False 
        motion =True if flags &(1 <<2 )else False 
        background_color =Int .read (b )if flags &(1 <<0 )else None 
        second_background_color =Int .read (b )if flags &(1 <<4 )else None 
        third_background_color =Int .read (b )if flags &(1 <<5 )else None 
        fourth_background_color =Int .read (b )if flags &(1 <<6 )else None 
        intensity =Int .read (b )if flags &(1 <<3 )else None 
        rotation =Int .read (b )if flags &(1 <<4 )else None 
        return WallPaperSettings (blur =blur ,motion =motion ,background_color =background_color ,second_background_color =second_background_color ,third_background_color =third_background_color ,fourth_background_color =fourth_background_color ,intensity =intensity ,rotation =rotation )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .blur else 0 
        flags |=(1 <<2 )if self .motion else 0 
        flags |=(1 <<0 )if self .background_color is not None else 0 
        flags |=(1 <<4 )if self .second_background_color is not None else 0 
        flags |=(1 <<5 )if self .third_background_color is not None else 0 
        flags |=(1 <<6 )if self .fourth_background_color is not None else 0 
        flags |=(1 <<3 )if self .intensity is not None else 0 
        flags |=(1 <<4 )if self .rotation is not None else 0 
        b .write (Int (flags ))

        if self .background_color is not None :
            b .write (Int (self .background_color ))

        if self .second_background_color is not None :
            b .write (Int (self .second_background_color ))

        if self .third_background_color is not None :
            b .write (Int (self .third_background_color ))

        if self .fourth_background_color is not None :
            b .write (Int (self .fourth_background_color ))

        if self .intensity is not None :
            b .write (Int (self .intensity ))

        if self .rotation is not None :
            b .write (Int (self .rotation ))

        return b .getvalue ()
