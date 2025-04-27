
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","no_webpage","message","media","reply_markup","entities","schedule_date"]

    ID =0x48f71778 
    QUALNAME ="functions.messages.EditMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,no_webpage :Optional [bool ]=None ,message :Optional [str ]=None ,media :"raw.base.InputMedia"=None ,reply_markup :"raw.base.ReplyMarkup"=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,schedule_date :Optional [int ]=None )->None :
        self .peer =peer 
        self .id =id 
        self .no_webpage =no_webpage 
        self .message =message 
        self .media =media 
        self .reply_markup =reply_markup 
        self .entities =entities 
        self .schedule_date =schedule_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditMessage":

        flags =Int .read (b )

        no_webpage =True if flags &(1 <<1 )else False 
        peer =TLObject .read (b )

        id =Int .read (b )

        message =String .read (b )if flags &(1 <<11 )else None 
        media =TLObject .read (b )if flags &(1 <<14 )else None 

        reply_markup =TLObject .read (b )if flags &(1 <<2 )else None 

        entities =TLObject .read (b )if flags &(1 <<3 )else []

        schedule_date =Int .read (b )if flags &(1 <<15 )else None 
        return EditMessage (peer =peer ,id =id ,no_webpage =no_webpage ,message =message ,media =media ,reply_markup =reply_markup ,entities =entities ,schedule_date =schedule_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .no_webpage else 0 
        flags |=(1 <<11 )if self .message is not None else 0 
        flags |=(1 <<14 )if self .media is not None else 0 
        flags |=(1 <<2 )if self .reply_markup is not None else 0 
        flags |=(1 <<3 )if self .entities else 0 
        flags |=(1 <<15 )if self .schedule_date is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        if self .message is not None :
            b .write (String (self .message ))

        if self .media is not None :
            b .write (self .media .write ())

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .schedule_date is not None :
            b .write (Int (self .schedule_date ))

        return b .getvalue ()
