
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Config (TLObject ):
    """"""

    __slots__ :List [str ]=["date","expires","test_mode","this_dc","dc_options","dc_txt_domain_name","chat_size_max","megagroup_size_max","forwarded_count_max","online_update_period_ms","offline_blur_timeout_ms","offline_idle_timeout_ms","online_cloud_timeout_ms","notify_cloud_delay_ms","notify_default_delay_ms","push_chat_period_ms","push_chat_limit","edit_time_limit","revoke_time_limit","revoke_pm_time_limit","rating_e_decay","stickers_recent_limit","channels_read_media_period","call_receive_timeout_ms","call_ring_timeout_ms","call_connect_timeout_ms","call_packet_timeout_ms","me_url_prefix","caption_length_max","message_length_max","webfile_dc_id","default_p2p_contacts","preload_featured_stickers","revoke_pm_inbox","blocked_mode","force_try_ipv6","tmp_sessions","autoupdate_url_prefix","gif_search_username","venue_search_username","img_search_username","static_maps_provider","suggested_lang_code","lang_pack_version","base_lang_pack_version","reactions_default","autologin_token"]

    ID =0xcc1a241e 
    QUALNAME ="types.Config"

    def __init__ (self ,*,date :int ,expires :int ,test_mode :bool ,this_dc :int ,dc_options :List ["raw.base.DcOption"],dc_txt_domain_name :str ,chat_size_max :int ,megagroup_size_max :int ,forwarded_count_max :int ,online_update_period_ms :int ,offline_blur_timeout_ms :int ,offline_idle_timeout_ms :int ,online_cloud_timeout_ms :int ,notify_cloud_delay_ms :int ,notify_default_delay_ms :int ,push_chat_period_ms :int ,push_chat_limit :int ,edit_time_limit :int ,revoke_time_limit :int ,revoke_pm_time_limit :int ,rating_e_decay :int ,stickers_recent_limit :int ,channels_read_media_period :int ,call_receive_timeout_ms :int ,call_ring_timeout_ms :int ,call_connect_timeout_ms :int ,call_packet_timeout_ms :int ,me_url_prefix :str ,caption_length_max :int ,message_length_max :int ,webfile_dc_id :int ,default_p2p_contacts :Optional [bool ]=None ,preload_featured_stickers :Optional [bool ]=None ,revoke_pm_inbox :Optional [bool ]=None ,blocked_mode :Optional [bool ]=None ,force_try_ipv6 :Optional [bool ]=None ,tmp_sessions :Optional [int ]=None ,autoupdate_url_prefix :Optional [str ]=None ,gif_search_username :Optional [str ]=None ,venue_search_username :Optional [str ]=None ,img_search_username :Optional [str ]=None ,static_maps_provider :Optional [str ]=None ,suggested_lang_code :Optional [str ]=None ,lang_pack_version :Optional [int ]=None ,base_lang_pack_version :Optional [int ]=None ,reactions_default :"raw.base.Reaction"=None ,autologin_token :Optional [str ]=None )->None :
        self .date =date 
        self .expires =expires 
        self .test_mode =test_mode 
        self .this_dc =this_dc 
        self .dc_options =dc_options 
        self .dc_txt_domain_name =dc_txt_domain_name 
        self .chat_size_max =chat_size_max 
        self .megagroup_size_max =megagroup_size_max 
        self .forwarded_count_max =forwarded_count_max 
        self .online_update_period_ms =online_update_period_ms 
        self .offline_blur_timeout_ms =offline_blur_timeout_ms 
        self .offline_idle_timeout_ms =offline_idle_timeout_ms 
        self .online_cloud_timeout_ms =online_cloud_timeout_ms 
        self .notify_cloud_delay_ms =notify_cloud_delay_ms 
        self .notify_default_delay_ms =notify_default_delay_ms 
        self .push_chat_period_ms =push_chat_period_ms 
        self .push_chat_limit =push_chat_limit 
        self .edit_time_limit =edit_time_limit 
        self .revoke_time_limit =revoke_time_limit 
        self .revoke_pm_time_limit =revoke_pm_time_limit 
        self .rating_e_decay =rating_e_decay 
        self .stickers_recent_limit =stickers_recent_limit 
        self .channels_read_media_period =channels_read_media_period 
        self .call_receive_timeout_ms =call_receive_timeout_ms 
        self .call_ring_timeout_ms =call_ring_timeout_ms 
        self .call_connect_timeout_ms =call_connect_timeout_ms 
        self .call_packet_timeout_ms =call_packet_timeout_ms 
        self .me_url_prefix =me_url_prefix 
        self .caption_length_max =caption_length_max 
        self .message_length_max =message_length_max 
        self .webfile_dc_id =webfile_dc_id 
        self .default_p2p_contacts =default_p2p_contacts 
        self .preload_featured_stickers =preload_featured_stickers 
        self .revoke_pm_inbox =revoke_pm_inbox 
        self .blocked_mode =blocked_mode 
        self .force_try_ipv6 =force_try_ipv6 
        self .tmp_sessions =tmp_sessions 
        self .autoupdate_url_prefix =autoupdate_url_prefix 
        self .gif_search_username =gif_search_username 
        self .venue_search_username =venue_search_username 
        self .img_search_username =img_search_username 
        self .static_maps_provider =static_maps_provider 
        self .suggested_lang_code =suggested_lang_code 
        self .lang_pack_version =lang_pack_version 
        self .base_lang_pack_version =base_lang_pack_version 
        self .reactions_default =reactions_default 
        self .autologin_token =autologin_token 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Config":

        flags =Int .read (b )

        default_p2p_contacts =True if flags &(1 <<3 )else False 
        preload_featured_stickers =True if flags &(1 <<4 )else False 
        revoke_pm_inbox =True if flags &(1 <<6 )else False 
        blocked_mode =True if flags &(1 <<8 )else False 
        force_try_ipv6 =True if flags &(1 <<14 )else False 
        date =Int .read (b )

        expires =Int .read (b )

        test_mode =Bool .read (b )

        this_dc =Int .read (b )

        dc_options =TLObject .read (b )

        dc_txt_domain_name =String .read (b )

        chat_size_max =Int .read (b )

        megagroup_size_max =Int .read (b )

        forwarded_count_max =Int .read (b )

        online_update_period_ms =Int .read (b )

        offline_blur_timeout_ms =Int .read (b )

        offline_idle_timeout_ms =Int .read (b )

        online_cloud_timeout_ms =Int .read (b )

        notify_cloud_delay_ms =Int .read (b )

        notify_default_delay_ms =Int .read (b )

        push_chat_period_ms =Int .read (b )

        push_chat_limit =Int .read (b )

        edit_time_limit =Int .read (b )

        revoke_time_limit =Int .read (b )

        revoke_pm_time_limit =Int .read (b )

        rating_e_decay =Int .read (b )

        stickers_recent_limit =Int .read (b )

        channels_read_media_period =Int .read (b )

        tmp_sessions =Int .read (b )if flags &(1 <<0 )else None 
        call_receive_timeout_ms =Int .read (b )

        call_ring_timeout_ms =Int .read (b )

        call_connect_timeout_ms =Int .read (b )

        call_packet_timeout_ms =Int .read (b )

        me_url_prefix =String .read (b )

        autoupdate_url_prefix =String .read (b )if flags &(1 <<7 )else None 
        gif_search_username =String .read (b )if flags &(1 <<9 )else None 
        venue_search_username =String .read (b )if flags &(1 <<10 )else None 
        img_search_username =String .read (b )if flags &(1 <<11 )else None 
        static_maps_provider =String .read (b )if flags &(1 <<12 )else None 
        caption_length_max =Int .read (b )

        message_length_max =Int .read (b )

        webfile_dc_id =Int .read (b )

        suggested_lang_code =String .read (b )if flags &(1 <<2 )else None 
        lang_pack_version =Int .read (b )if flags &(1 <<2 )else None 
        base_lang_pack_version =Int .read (b )if flags &(1 <<2 )else None 
        reactions_default =TLObject .read (b )if flags &(1 <<15 )else None 

        autologin_token =String .read (b )if flags &(1 <<16 )else None 
        return Config (date =date ,expires =expires ,test_mode =test_mode ,this_dc =this_dc ,dc_options =dc_options ,dc_txt_domain_name =dc_txt_domain_name ,chat_size_max =chat_size_max ,megagroup_size_max =megagroup_size_max ,forwarded_count_max =forwarded_count_max ,online_update_period_ms =online_update_period_ms ,offline_blur_timeout_ms =offline_blur_timeout_ms ,offline_idle_timeout_ms =offline_idle_timeout_ms ,online_cloud_timeout_ms =online_cloud_timeout_ms ,notify_cloud_delay_ms =notify_cloud_delay_ms ,notify_default_delay_ms =notify_default_delay_ms ,push_chat_period_ms =push_chat_period_ms ,push_chat_limit =push_chat_limit ,edit_time_limit =edit_time_limit ,revoke_time_limit =revoke_time_limit ,revoke_pm_time_limit =revoke_pm_time_limit ,rating_e_decay =rating_e_decay ,stickers_recent_limit =stickers_recent_limit ,channels_read_media_period =channels_read_media_period ,call_receive_timeout_ms =call_receive_timeout_ms ,call_ring_timeout_ms =call_ring_timeout_ms ,call_connect_timeout_ms =call_connect_timeout_ms ,call_packet_timeout_ms =call_packet_timeout_ms ,me_url_prefix =me_url_prefix ,caption_length_max =caption_length_max ,message_length_max =message_length_max ,webfile_dc_id =webfile_dc_id ,default_p2p_contacts =default_p2p_contacts ,preload_featured_stickers =preload_featured_stickers ,revoke_pm_inbox =revoke_pm_inbox ,blocked_mode =blocked_mode ,force_try_ipv6 =force_try_ipv6 ,tmp_sessions =tmp_sessions ,autoupdate_url_prefix =autoupdate_url_prefix ,gif_search_username =gif_search_username ,venue_search_username =venue_search_username ,img_search_username =img_search_username ,static_maps_provider =static_maps_provider ,suggested_lang_code =suggested_lang_code ,lang_pack_version =lang_pack_version ,base_lang_pack_version =base_lang_pack_version ,reactions_default =reactions_default ,autologin_token =autologin_token )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .default_p2p_contacts else 0 
        flags |=(1 <<4 )if self .preload_featured_stickers else 0 
        flags |=(1 <<6 )if self .revoke_pm_inbox else 0 
        flags |=(1 <<8 )if self .blocked_mode else 0 
        flags |=(1 <<14 )if self .force_try_ipv6 else 0 
        flags |=(1 <<0 )if self .tmp_sessions is not None else 0 
        flags |=(1 <<7 )if self .autoupdate_url_prefix is not None else 0 
        flags |=(1 <<9 )if self .gif_search_username is not None else 0 
        flags |=(1 <<10 )if self .venue_search_username is not None else 0 
        flags |=(1 <<11 )if self .img_search_username is not None else 0 
        flags |=(1 <<12 )if self .static_maps_provider is not None else 0 
        flags |=(1 <<2 )if self .suggested_lang_code is not None else 0 
        flags |=(1 <<2 )if self .lang_pack_version is not None else 0 
        flags |=(1 <<2 )if self .base_lang_pack_version is not None else 0 
        flags |=(1 <<15 )if self .reactions_default is not None else 0 
        flags |=(1 <<16 )if self .autologin_token is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .date ))

        b .write (Int (self .expires ))

        b .write (Bool (self .test_mode ))

        b .write (Int (self .this_dc ))

        b .write (Vector (self .dc_options ))

        b .write (String (self .dc_txt_domain_name ))

        b .write (Int (self .chat_size_max ))

        b .write (Int (self .megagroup_size_max ))

        b .write (Int (self .forwarded_count_max ))

        b .write (Int (self .online_update_period_ms ))

        b .write (Int (self .offline_blur_timeout_ms ))

        b .write (Int (self .offline_idle_timeout_ms ))

        b .write (Int (self .online_cloud_timeout_ms ))

        b .write (Int (self .notify_cloud_delay_ms ))

        b .write (Int (self .notify_default_delay_ms ))

        b .write (Int (self .push_chat_period_ms ))

        b .write (Int (self .push_chat_limit ))

        b .write (Int (self .edit_time_limit ))

        b .write (Int (self .revoke_time_limit ))

        b .write (Int (self .revoke_pm_time_limit ))

        b .write (Int (self .rating_e_decay ))

        b .write (Int (self .stickers_recent_limit ))

        b .write (Int (self .channels_read_media_period ))

        if self .tmp_sessions is not None :
            b .write (Int (self .tmp_sessions ))

        b .write (Int (self .call_receive_timeout_ms ))

        b .write (Int (self .call_ring_timeout_ms ))

        b .write (Int (self .call_connect_timeout_ms ))

        b .write (Int (self .call_packet_timeout_ms ))

        b .write (String (self .me_url_prefix ))

        if self .autoupdate_url_prefix is not None :
            b .write (String (self .autoupdate_url_prefix ))

        if self .gif_search_username is not None :
            b .write (String (self .gif_search_username ))

        if self .venue_search_username is not None :
            b .write (String (self .venue_search_username ))

        if self .img_search_username is not None :
            b .write (String (self .img_search_username ))

        if self .static_maps_provider is not None :
            b .write (String (self .static_maps_provider ))

        b .write (Int (self .caption_length_max ))

        b .write (Int (self .message_length_max ))

        b .write (Int (self .webfile_dc_id ))

        if self .suggested_lang_code is not None :
            b .write (String (self .suggested_lang_code ))

        if self .lang_pack_version is not None :
            b .write (Int (self .lang_pack_version ))

        if self .base_lang_pack_version is not None :
            b .write (Int (self .base_lang_pack_version ))

        if self .reactions_default is not None :
            b .write (self .reactions_default .write ())

        if self .autologin_token is not None :
            b .write (String (self .autologin_token ))

        return b .getvalue ()
