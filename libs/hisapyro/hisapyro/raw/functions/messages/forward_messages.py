
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ForwardMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["from_peer","id","random_id","to_peer","silent","background","with_my_score","drop_author","drop_media_captions","noforwards","top_msg_id","schedule_date","send_as"]

    ID =0xc661bbc4 
    QUALNAME ="functions.messages.ForwardMessages"

    def __init__ (self ,*,from_peer :"raw.base.InputPeer",id :List [int ],random_id :List [int ],to_peer :"raw.base.InputPeer",silent :Optional [bool ]=None ,background :Optional [bool ]=None ,with_my_score :Optional [bool ]=None ,drop_author :Optional [bool ]=None ,drop_media_captions :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,top_msg_id :Optional [int ]=None ,schedule_date :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .from_peer =from_peer 
        self .id =id 
        self .random_id =random_id 
        self .to_peer =to_peer 
        self .silent =silent 
        self .background =background 
        self .with_my_score =with_my_score 
        self .drop_author =drop_author 
        self .drop_media_captions =drop_media_captions 
        self .noforwards =noforwards 
        self .top_msg_id =top_msg_id 
        self .schedule_date =schedule_date 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ForwardMessages":

        flags =Int .read (b )

        silent =True if flags &(1 <<5 )else False 
        background =True if flags &(1 <<6 )else False 
        with_my_score =True if flags &(1 <<8 )else False 
        drop_author =True if flags &(1 <<11 )else False 
        drop_media_captions =True if flags &(1 <<12 )else False 
        noforwards =True if flags &(1 <<14 )else False 
        from_peer =TLObject .read (b )

        id =TLObject .read (b ,Int )

        random_id =TLObject .read (b ,Long )

        to_peer =TLObject .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<9 )else None 
        schedule_date =Int .read (b )if flags &(1 <<10 )else None 
        send_as =TLObject .read (b )if flags &(1 <<13 )else None 

        return ForwardMessages (from_peer =from_peer ,id =id ,random_id =random_id ,to_peer =to_peer ,silent =silent ,background =background ,with_my_score =with_my_score ,drop_author =drop_author ,drop_media_captions =drop_media_captions ,noforwards =noforwards ,top_msg_id =top_msg_id ,schedule_date =schedule_date ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .silent else 0 
        flags |=(1 <<6 )if self .background else 0 
        flags |=(1 <<8 )if self .with_my_score else 0 
        flags |=(1 <<11 )if self .drop_author else 0 
        flags |=(1 <<12 )if self .drop_media_captions else 0 
        flags |=(1 <<14 )if self .noforwards else 0 
        flags |=(1 <<9 )if self .top_msg_id is not None else 0 
        flags |=(1 <<10 )if self .schedule_date is not None else 0 
        flags |=(1 <<13 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .from_peer .write ())

        b .write (Vector (self .id ,Int ))

        b .write (Vector (self .random_id ,Long ))

        b .write (self .to_peer .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        if self .schedule_date is not None :
            b .write (Int (self .schedule_date ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
