
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TranscribedAudio (TLObject ):
    """"""

    __slots__ :List [str ]=["transcription_id","text","pending"]

    ID =0x93752c52 
    QUALNAME ="types.messages.TranscribedAudio"

    def __init__ (self ,*,transcription_id :int ,text :str ,pending :Optional [bool ]=None )->None :
        self .transcription_id =transcription_id 
        self .text =text 
        self .pending =pending 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TranscribedAudio":

        flags =Int .read (b )

        pending =True if flags &(1 <<0 )else False 
        transcription_id =Long .read (b )

        text =String .read (b )

        return TranscribedAudio (transcription_id =transcription_id ,text =text ,pending =pending )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pending else 0 
        b .write (Int (flags ))

        b .write (Long (self .transcription_id ))

        b .write (String (self .text ))

        return b .getvalue ()
