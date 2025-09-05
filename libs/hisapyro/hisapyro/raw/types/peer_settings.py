
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PeerSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["report_spam","add_contact","block_contact","share_contact","need_contacts_exception","report_geo","autoarchived","invite_members","request_chat_broadcast","geo_distance","request_chat_title","request_chat_date"]

    ID =0xa518110d 
    QUALNAME ="types.PeerSettings"

    def __init__ (self ,*,report_spam :Optional [bool ]=None ,add_contact :Optional [bool ]=None ,block_contact :Optional [bool ]=None ,share_contact :Optional [bool ]=None ,need_contacts_exception :Optional [bool ]=None ,report_geo :Optional [bool ]=None ,autoarchived :Optional [bool ]=None ,invite_members :Optional [bool ]=None ,request_chat_broadcast :Optional [bool ]=None ,geo_distance :Optional [int ]=None ,request_chat_title :Optional [str ]=None ,request_chat_date :Optional [int ]=None )->None :
        self .report_spam =report_spam 
        self .add_contact =add_contact 
        self .block_contact =block_contact 
        self .share_contact =share_contact 
        self .need_contacts_exception =need_contacts_exception 
        self .report_geo =report_geo 
        self .autoarchived =autoarchived 
        self .invite_members =invite_members 
        self .request_chat_broadcast =request_chat_broadcast 
        self .geo_distance =geo_distance 
        self .request_chat_title =request_chat_title 
        self .request_chat_date =request_chat_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PeerSettings":

        flags =Int .read (b )

        report_spam =True if flags &(1 <<0 )else False 
        add_contact =True if flags &(1 <<1 )else False 
        block_contact =True if flags &(1 <<2 )else False 
        share_contact =True if flags &(1 <<3 )else False 
        need_contacts_exception =True if flags &(1 <<4 )else False 
        report_geo =True if flags &(1 <<5 )else False 
        autoarchived =True if flags &(1 <<7 )else False 
        invite_members =True if flags &(1 <<8 )else False 
        request_chat_broadcast =True if flags &(1 <<10 )else False 
        geo_distance =Int .read (b )if flags &(1 <<6 )else None 
        request_chat_title =String .read (b )if flags &(1 <<9 )else None 
        request_chat_date =Int .read (b )if flags &(1 <<9 )else None 
        return PeerSettings (report_spam =report_spam ,add_contact =add_contact ,block_contact =block_contact ,share_contact =share_contact ,need_contacts_exception =need_contacts_exception ,report_geo =report_geo ,autoarchived =autoarchived ,invite_members =invite_members ,request_chat_broadcast =request_chat_broadcast ,geo_distance =geo_distance ,request_chat_title =request_chat_title ,request_chat_date =request_chat_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .report_spam else 0 
        flags |=(1 <<1 )if self .add_contact else 0 
        flags |=(1 <<2 )if self .block_contact else 0 
        flags |=(1 <<3 )if self .share_contact else 0 
        flags |=(1 <<4 )if self .need_contacts_exception else 0 
        flags |=(1 <<5 )if self .report_geo else 0 
        flags |=(1 <<7 )if self .autoarchived else 0 
        flags |=(1 <<8 )if self .invite_members else 0 
        flags |=(1 <<10 )if self .request_chat_broadcast else 0 
        flags |=(1 <<6 )if self .geo_distance is not None else 0 
        flags |=(1 <<9 )if self .request_chat_title is not None else 0 
        flags |=(1 <<9 )if self .request_chat_date is not None else 0 
        b .write (Int (flags ))

        if self .geo_distance is not None :
            b .write (Int (self .geo_distance ))

        if self .request_chat_title is not None :
            b .write (String (self .request_chat_title ))

        if self .request_chat_date is not None :
            b .write (Int (self .request_chat_date ))

        return b .getvalue ()
