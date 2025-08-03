
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BotInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["user_id","description","description_photo","description_document","commands","menu_button"]

    ID =0x8f300b57 
    QUALNAME ="types.BotInfo"

    def __init__ (self ,*,user_id :Optional [int ]=None ,description :Optional [str ]=None ,description_photo :"raw.base.Photo"=None ,description_document :"raw.base.Document"=None ,commands :Optional [List ["raw.base.BotCommand"]]=None ,menu_button :"raw.base.BotMenuButton"=None )->None :
        self .user_id =user_id 
        self .description =description 
        self .description_photo =description_photo 
        self .description_document =description_document 
        self .commands =commands 
        self .menu_button =menu_button 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BotInfo":

        flags =Int .read (b )

        user_id =Long .read (b )if flags &(1 <<0 )else None 
        description =String .read (b )if flags &(1 <<1 )else None 
        description_photo =TLObject .read (b )if flags &(1 <<4 )else None 

        description_document =TLObject .read (b )if flags &(1 <<5 )else None 

        commands =TLObject .read (b )if flags &(1 <<2 )else []

        menu_button =TLObject .read (b )if flags &(1 <<3 )else None 

        return BotInfo (user_id =user_id ,description =description ,description_photo =description_photo ,description_document =description_document ,commands =commands ,menu_button =menu_button )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .user_id is not None else 0 
        flags |=(1 <<1 )if self .description is not None else 0 
        flags |=(1 <<4 )if self .description_photo is not None else 0 
        flags |=(1 <<5 )if self .description_document is not None else 0 
        flags |=(1 <<2 )if self .commands else 0 
        flags |=(1 <<3 )if self .menu_button is not None else 0 
        b .write (Int (flags ))

        if self .user_id is not None :
            b .write (Long (self .user_id ))

        if self .description is not None :
            b .write (String (self .description ))

        if self .description_photo is not None :
            b .write (self .description_photo .write ())

        if self .description_document is not None :
            b .write (self .description_document .write ())

        if self .commands is not None :
            b .write (Vector (self .commands ))

        if self .menu_button is not None :
            b .write (self .menu_button .write ())

        return b .getvalue ()
