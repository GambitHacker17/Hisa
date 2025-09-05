
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AutoDownloadSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["photo_size_max","video_size_max","file_size_max","video_upload_maxbitrate","disabled","video_preload_large","audio_preload_next","phonecalls_less_data"]

    ID =0x8efab953 
    QUALNAME ="types.AutoDownloadSettings"

    def __init__ (self ,*,photo_size_max :int ,video_size_max :int ,file_size_max :int ,video_upload_maxbitrate :int ,disabled :Optional [bool ]=None ,video_preload_large :Optional [bool ]=None ,audio_preload_next :Optional [bool ]=None ,phonecalls_less_data :Optional [bool ]=None )->None :
        self .photo_size_max =photo_size_max 
        self .video_size_max =video_size_max 
        self .file_size_max =file_size_max 
        self .video_upload_maxbitrate =video_upload_maxbitrate 
        self .disabled =disabled 
        self .video_preload_large =video_preload_large 
        self .audio_preload_next =audio_preload_next 
        self .phonecalls_less_data =phonecalls_less_data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AutoDownloadSettings":

        flags =Int .read (b )

        disabled =True if flags &(1 <<0 )else False 
        video_preload_large =True if flags &(1 <<1 )else False 
        audio_preload_next =True if flags &(1 <<2 )else False 
        phonecalls_less_data =True if flags &(1 <<3 )else False 
        photo_size_max =Int .read (b )

        video_size_max =Long .read (b )

        file_size_max =Long .read (b )

        video_upload_maxbitrate =Int .read (b )

        return AutoDownloadSettings (photo_size_max =photo_size_max ,video_size_max =video_size_max ,file_size_max =file_size_max ,video_upload_maxbitrate =video_upload_maxbitrate ,disabled =disabled ,video_preload_large =video_preload_large ,audio_preload_next =audio_preload_next ,phonecalls_less_data =phonecalls_less_data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .disabled else 0 
        flags |=(1 <<1 )if self .video_preload_large else 0 
        flags |=(1 <<2 )if self .audio_preload_next else 0 
        flags |=(1 <<3 )if self .phonecalls_less_data else 0 
        b .write (Int (flags ))

        b .write (Int (self .photo_size_max ))

        b .write (Long (self .video_size_max ))

        b .write (Long (self .file_size_max ))

        b .write (Int (self .video_upload_maxbitrate ))

        return b .getvalue ()
