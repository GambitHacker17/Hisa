
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","message","random_id","no_webpage","silent","background","clear_draft","noforwards","update_stickersets_order","reply_to_msg_id","top_msg_id","reply_markup","entities","schedule_date","send_as"]

    ID =0x1cc20387 
    QUALNAME ="functions.messages.SendMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",message :str ,random_id :int ,no_webpage :Optional [bool ]=None ,silent :Optional [bool ]=None ,background :Optional [bool ]=None ,clear_draft :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,update_stickersets_order :Optional [bool ]=None ,reply_to_msg_id :Optional [int ]=None ,top_msg_id :Optional [int ]=None ,reply_markup :"raw.base.ReplyMarkup"=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,schedule_date :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .peer =peer 
        self .message =message 
        self .random_id =random_id 
        self .no_webpage =no_webpage 
        self .silent =silent 
        self .background =background 
        self .clear_draft =clear_draft 
        self .noforwards =noforwards 
        self .update_stickersets_order =update_stickersets_order 
        self .reply_to_msg_id =reply_to_msg_id 
        self .top_msg_id =top_msg_id 
        self .reply_markup =reply_markup 
        self .entities =entities 
        self .schedule_date =schedule_date 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendMessage":

        flags =Int .read (b )

        no_webpage =True if flags &(1 <<1 )else False 
        silent =True if flags &(1 <<5 )else False 
        background =True if flags &(1 <<6 )else False 
        clear_draft =True if flags &(1 <<7 )else False 
        noforwards =True if flags &(1 <<14 )else False 
        update_stickersets_order =True if flags &(1 <<15 )else False 
        peer =TLObject .read (b )

        reply_to_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<9 )else None 
        message =String .read (b )

        random_id =Long .read (b )

        reply_markup =TLObject .read (b )if flags &(1 <<2 )else None 

        entities =TLObject .read (b )if flags &(1 <<3 )else []

        schedule_date =Int .read (b )if flags &(1 <<10 )else None 
        send_as =TLObject .read (b )if flags &(1 <<13 )else None 

        return SendMessage (peer =peer ,message =message ,random_id =random_id ,no_webpage =no_webpage ,silent =silent ,background =background ,clear_draft =clear_draft ,noforwards =noforwards ,update_stickersets_order =update_stickersets_order ,reply_to_msg_id =reply_to_msg_id ,top_msg_id =top_msg_id ,reply_markup =reply_markup ,entities =entities ,schedule_date =schedule_date ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .no_webpage else 0 
        flags |=(1 <<5 )if self .silent else 0 
        flags |=(1 <<6 )if self .background else 0 
        flags |=(1 <<7 )if self .clear_draft else 0 
        flags |=(1 <<14 )if self .noforwards else 0 
        flags |=(1 <<15 )if self .update_stickersets_order else 0 
        flags |=(1 <<0 )if self .reply_to_msg_id is not None else 0 
        flags |=(1 <<9 )if self .top_msg_id is not None else 0 
        flags |=(1 <<2 )if self .reply_markup is not None else 0 
        flags |=(1 <<3 )if self .entities else 0 
        flags |=(1 <<10 )if self .schedule_date is not None else 0 
        flags |=(1 <<13 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .reply_to_msg_id is not None :
            b .write (Int (self .reply_to_msg_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (String (self .message ))

        b .write (Long (self .random_id ))

        if self .reply_markup is not None :
            b .write (self .reply_markup .write ())

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .schedule_date is not None :
            b .write (Int (self .schedule_date ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
