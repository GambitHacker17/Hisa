
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ExportMessageLink (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","id","grouped","thread"]

    ID =0xe63fadeb 
    QUALNAME ="functions.channels.ExportMessageLink"

    def __init__ (self ,*,channel :"raw.base.InputChannel",id :int ,grouped :Optional [bool ]=None ,thread :Optional [bool ]=None )->None :
        self .channel =channel 
        self .id =id 
        self .grouped =grouped 
        self .thread =thread 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ExportMessageLink":

        flags =Int .read (b )

        grouped =True if flags &(1 <<0 )else False 
        thread =True if flags &(1 <<1 )else False 
        channel =TLObject .read (b )

        id =Int .read (b )

        return ExportMessageLink (channel =channel ,id =id ,grouped =grouped ,thread =thread )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .grouped else 0 
        flags |=(1 <<1 )if self .thread else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        b .write (Int (self .id ))

        return b .getvalue ()
