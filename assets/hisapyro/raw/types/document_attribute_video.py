
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DocumentAttributeVideo (TLObject ):
    """"""

    __slots__ :List [str ]=["duration","w","h","round_message","supports_streaming"]

    ID =0xef02ce6 
    QUALNAME ="types.DocumentAttributeVideo"

    def __init__ (self ,*,duration :int ,w :int ,h :int ,round_message :Optional [bool ]=None ,supports_streaming :Optional [bool ]=None )->None :
        self .duration =duration 
        self .w =w 
        self .h =h 
        self .round_message =round_message 
        self .supports_streaming =supports_streaming 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DocumentAttributeVideo":

        flags =Int .read (b )

        round_message =True if flags &(1 <<0 )else False 
        supports_streaming =True if flags &(1 <<1 )else False 
        duration =Int .read (b )

        w =Int .read (b )

        h =Int .read (b )

        return DocumentAttributeVideo (duration =duration ,w =w ,h =h ,round_message =round_message ,supports_streaming =supports_streaming )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .round_message else 0 
        flags |=(1 <<1 )if self .supports_streaming else 0 
        b .write (Int (flags ))

        b .write (Int (self .duration ))

        b .write (Int (self .w ))

        b .write (Int (self .h ))

        return b .getvalue ()
