
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageExtendedMediaPreview (TLObject ):
    """"""

    __slots__ :List [str ]=["w","h","thumb","video_duration"]

    ID =0xad628cc8 
    QUALNAME ="types.MessageExtendedMediaPreview"

    def __init__ (self ,*,w :Optional [int ]=None ,h :Optional [int ]=None ,thumb :"raw.base.PhotoSize"=None ,video_duration :Optional [int ]=None )->None :
        self .w =w 
        self .h =h 
        self .thumb =thumb 
        self .video_duration =video_duration 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageExtendedMediaPreview":

        flags =Int .read (b )

        w =Int .read (b )if flags &(1 <<0 )else None 
        h =Int .read (b )if flags &(1 <<0 )else None 
        thumb =TLObject .read (b )if flags &(1 <<1 )else None 

        video_duration =Int .read (b )if flags &(1 <<2 )else None 
        return MessageExtendedMediaPreview (w =w ,h =h ,thumb =thumb ,video_duration =video_duration )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .w is not None else 0 
        flags |=(1 <<0 )if self .h is not None else 0 
        flags |=(1 <<1 )if self .thumb is not None else 0 
        flags |=(1 <<2 )if self .video_duration is not None else 0 
        b .write (Int (flags ))

        if self .w is not None :
            b .write (Int (self .w ))

        if self .h is not None :
            b .write (Int (self .h ))

        if self .thumb is not None :
            b .write (self .thumb .write ())

        if self .video_duration is not None :
            b .write (Int (self .video_duration ))

        return b .getvalue ()
