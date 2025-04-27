
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBotIcon (TLObject ):
    """"""

    __slots__ :List [str ]=["name","icon","colors"]

    ID =0xb2a7386b 
    QUALNAME ="types.AttachMenuBotIcon"

    def __init__ (self ,*,name :str ,icon :"raw.base.Document",colors :Optional [List ["raw.base.AttachMenuBotIconColor"]]=None )->None :
        self .name =name 
        self .icon =icon 
        self .colors =colors 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBotIcon":

        flags =Int .read (b )

        name =String .read (b )

        icon =TLObject .read (b )

        colors =TLObject .read (b )if flags &(1 <<0 )else []

        return AttachMenuBotIcon (name =name ,icon =icon ,colors =colors )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .colors else 0 
        b .write (Int (flags ))

        b .write (String (self .name ))

        b .write (self .icon .write ())

        if self .colors is not None :
            b .write (Vector (self .colors ))

        return b .getvalue ()
