
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatBannedRights (TLObject ):
    """"""

    __slots__ :List [str ]=["until_date","view_messages","send_messages","send_media","send_stickers","send_gifs","send_games","send_inline","embed_links","send_polls","change_info","invite_users","pin_messages","manage_topics","send_photos","send_videos","send_roundvideos","send_audios","send_voices","send_docs","send_plain"]

    ID =0x9f120418 
    QUALNAME ="types.ChatBannedRights"

    def __init__ (self ,*,until_date :int ,view_messages :Optional [bool ]=None ,send_messages :Optional [bool ]=None ,send_media :Optional [bool ]=None ,send_stickers :Optional [bool ]=None ,send_gifs :Optional [bool ]=None ,send_games :Optional [bool ]=None ,send_inline :Optional [bool ]=None ,embed_links :Optional [bool ]=None ,send_polls :Optional [bool ]=None ,change_info :Optional [bool ]=None ,invite_users :Optional [bool ]=None ,pin_messages :Optional [bool ]=None ,manage_topics :Optional [bool ]=None ,send_photos :Optional [bool ]=None ,send_videos :Optional [bool ]=None ,send_roundvideos :Optional [bool ]=None ,send_audios :Optional [bool ]=None ,send_voices :Optional [bool ]=None ,send_docs :Optional [bool ]=None ,send_plain :Optional [bool ]=None )->None :
        self .until_date =until_date 
        self .view_messages =view_messages 
        self .send_messages =send_messages 
        self .send_media =send_media 
        self .send_stickers =send_stickers 
        self .send_gifs =send_gifs 
        self .send_games =send_games 
        self .send_inline =send_inline 
        self .embed_links =embed_links 
        self .send_polls =send_polls 
        self .change_info =change_info 
        self .invite_users =invite_users 
        self .pin_messages =pin_messages 
        self .manage_topics =manage_topics 
        self .send_photos =send_photos 
        self .send_videos =send_videos 
        self .send_roundvideos =send_roundvideos 
        self .send_audios =send_audios 
        self .send_voices =send_voices 
        self .send_docs =send_docs 
        self .send_plain =send_plain 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatBannedRights":

        flags =Int .read (b )

        view_messages =True if flags &(1 <<0 )else False 
        send_messages =True if flags &(1 <<1 )else False 
        send_media =True if flags &(1 <<2 )else False 
        send_stickers =True if flags &(1 <<3 )else False 
        send_gifs =True if flags &(1 <<4 )else False 
        send_games =True if flags &(1 <<5 )else False 
        send_inline =True if flags &(1 <<6 )else False 
        embed_links =True if flags &(1 <<7 )else False 
        send_polls =True if flags &(1 <<8 )else False 
        change_info =True if flags &(1 <<10 )else False 
        invite_users =True if flags &(1 <<15 )else False 
        pin_messages =True if flags &(1 <<17 )else False 
        manage_topics =True if flags &(1 <<18 )else False 
        send_photos =True if flags &(1 <<19 )else False 
        send_videos =True if flags &(1 <<20 )else False 
        send_roundvideos =True if flags &(1 <<21 )else False 
        send_audios =True if flags &(1 <<22 )else False 
        send_voices =True if flags &(1 <<23 )else False 
        send_docs =True if flags &(1 <<24 )else False 
        send_plain =True if flags &(1 <<25 )else False 
        until_date =Int .read (b )

        return ChatBannedRights (until_date =until_date ,view_messages =view_messages ,send_messages =send_messages ,send_media =send_media ,send_stickers =send_stickers ,send_gifs =send_gifs ,send_games =send_games ,send_inline =send_inline ,embed_links =embed_links ,send_polls =send_polls ,change_info =change_info ,invite_users =invite_users ,pin_messages =pin_messages ,manage_topics =manage_topics ,send_photos =send_photos ,send_videos =send_videos ,send_roundvideos =send_roundvideos ,send_audios =send_audios ,send_voices =send_voices ,send_docs =send_docs ,send_plain =send_plain )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .view_messages else 0 
        flags |=(1 <<1 )if self .send_messages else 0 
        flags |=(1 <<2 )if self .send_media else 0 
        flags |=(1 <<3 )if self .send_stickers else 0 
        flags |=(1 <<4 )if self .send_gifs else 0 
        flags |=(1 <<5 )if self .send_games else 0 
        flags |=(1 <<6 )if self .send_inline else 0 
        flags |=(1 <<7 )if self .embed_links else 0 
        flags |=(1 <<8 )if self .send_polls else 0 
        flags |=(1 <<10 )if self .change_info else 0 
        flags |=(1 <<15 )if self .invite_users else 0 
        flags |=(1 <<17 )if self .pin_messages else 0 
        flags |=(1 <<18 )if self .manage_topics else 0 
        flags |=(1 <<19 )if self .send_photos else 0 
        flags |=(1 <<20 )if self .send_videos else 0 
        flags |=(1 <<21 )if self .send_roundvideos else 0 
        flags |=(1 <<22 )if self .send_audios else 0 
        flags |=(1 <<23 )if self .send_voices else 0 
        flags |=(1 <<24 )if self .send_docs else 0 
        flags |=(1 <<25 )if self .send_plain else 0 
        b .write (Int (flags ))

        b .write (Int (self .until_date ))

        return b .getvalue ()
