
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendMultiMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","multi_media","silent","background","clear_draft","noforwards","update_stickersets_order","reply_to_msg_id","top_msg_id","schedule_date","send_as"]

    ID =0xb6f11a1c 
    QUALNAME ="functions.messages.SendMultiMedia"

    def __init__ (self ,*,peer :"raw.base.InputPeer",multi_media :List ["raw.base.InputSingleMedia"],silent :Optional [bool ]=None ,background :Optional [bool ]=None ,clear_draft :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,update_stickersets_order :Optional [bool ]=None ,reply_to_msg_id :Optional [int ]=None ,top_msg_id :Optional [int ]=None ,schedule_date :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .peer =peer 
        self .multi_media =multi_media 
        self .silent =silent 
        self .background =background 
        self .clear_draft =clear_draft 
        self .noforwards =noforwards 
        self .update_stickersets_order =update_stickersets_order 
        self .reply_to_msg_id =reply_to_msg_id 
        self .top_msg_id =top_msg_id 
        self .schedule_date =schedule_date 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendMultiMedia":

        flags =Int .read (b )

        silent =True if flags &(1 <<5 )else False 
        background =True if flags &(1 <<6 )else False 
        clear_draft =True if flags &(1 <<7 )else False 
        noforwards =True if flags &(1 <<14 )else False 
        update_stickersets_order =True if flags &(1 <<15 )else False 
        peer =TLObject .read (b )

        reply_to_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<9 )else None 
        multi_media =TLObject .read (b )

        schedule_date =Int .read (b )if flags &(1 <<10 )else None 
        send_as =TLObject .read (b )if flags &(1 <<13 )else None 

        return SendMultiMedia (peer =peer ,multi_media =multi_media ,silent =silent ,background =background ,clear_draft =clear_draft ,noforwards =noforwards ,update_stickersets_order =update_stickersets_order ,reply_to_msg_id =reply_to_msg_id ,top_msg_id =top_msg_id ,schedule_date =schedule_date ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .silent else 0 
        flags |=(1 <<6 )if self .background else 0 
        flags |=(1 <<7 )if self .clear_draft else 0 
        flags |=(1 <<14 )if self .noforwards else 0 
        flags |=(1 <<15 )if self .update_stickersets_order else 0 
        flags |=(1 <<0 )if self .reply_to_msg_id is not None else 0 
        flags |=(1 <<9 )if self .top_msg_id is not None else 0 
        flags |=(1 <<10 )if self .schedule_date is not None else 0 
        flags |=(1 <<13 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .reply_to_msg_id is not None :
            b .write (Int (self .reply_to_msg_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (Vector (self .multi_media ))

        if self .schedule_date is not None :
            b .write (Int (self .schedule_date ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
