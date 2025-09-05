
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class VideoSize (TLObject ):
    """"""

    __slots__ :List [str ]=["type","w","h","size","video_start_ts"]

    ID =0xde33b094 
    QUALNAME ="types.VideoSize"

    def __init__ (self ,*,type :str ,w :int ,h :int ,size :int ,video_start_ts :Optional [float ]=None )->None :
        self .type =type 
        self .w =w 
        self .h =h 
        self .size =size 
        self .video_start_ts =video_start_ts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"VideoSize":

        flags =Int .read (b )

        type =String .read (b )

        w =Int .read (b )

        h =Int .read (b )

        size =Int .read (b )

        video_start_ts =Double .read (b )if flags &(1 <<0 )else None 
        return VideoSize (type =type ,w =w ,h =h ,size =size ,video_start_ts =video_start_ts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .video_start_ts is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .type ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        b .write (Int (self .size ))

        if self .video_start_ts is not None :
            b .write (Double (self .video_start_ts ))

        return b .getvalue ()
