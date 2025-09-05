
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InitHistoryImport (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","file","media_count"]

    ID =0x34090c3b 
    QUALNAME ="functions.messages.InitHistoryImport"

    def __init__ (self ,*,peer :"raw.base.InputPeer",file :"raw.base.InputFile",media_count :int )->None :
        self .peer =peer 
        self .file =file 
        self .media_count =media_count 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InitHistoryImport":

        peer =TLObject .read (b )

        file =TLObject .read (b )

        media_count =Int .read (b )

        return InitHistoryImport (peer =peer ,file =file ,media_count =media_count )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .file .write ())

        b .write (Int (self .media_count ))

        return b .getvalue ()
