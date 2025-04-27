
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BotInlineMessageText (TLObject ):
    """"""

    __slots__ :List [str ]=["message","no_webpage","entities","reply_markup"]

    ID =0x8c7f65e2 
    QUALNAME ="types.BotInlineMessageText"

    def __init__ (self ,*,message :str ,no_webpage :Optional [bool ]=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,reply_markup :"raw.base.ReplyMarkup"=None )->None :
        self .message =message 
        self .no_webpage =no_webpage 
        self .entities =entities 
        self .reply_markup =reply_markup 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BotInlineMessageText":

        flags =Int .read (b )

        no_webpage =True if flags &(1 <<0 )else False 
        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<1 )else []

        reply_markup =TLObject .read (b )if flags &(1 <<2 )else None 

        return BotInlineMessageText (message =message ,no_webpage =no_webpage ,entities =entities ,reply_markup =reply_markup )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .no_webpage else 0 
        flags |=(1 <<1 )if self .entities else 0 
        flags |=(1 <<2 )if self .reply_markup is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        return b .getvalue ()
