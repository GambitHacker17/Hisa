
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HistoryImportParsed (TLObject ):
    """"""

    __slots__ :List [str ]=["pm","group","title"]

    ID =0x5e0fb7b9 
    QUALNAME ="types.messages.HistoryImportParsed"

    def __init__ (self ,*,pm :Optional [bool ]=None ,group :Optional [bool ]=None ,title :Optional [str ]=None )->None :
        self .pm =pm 
        self .group =group 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HistoryImportParsed":

        flags =Int .read (b )

        pm =True if flags &(1 <<0 )else False 
        group =True if flags &(1 <<1 )else False 
        title =String .read (b )if flags &(1 <<2 )else None 
        return HistoryImportParsed (pm =pm ,group =group ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pm else 0 
        flags |=(1 <<1 )if self .group else 0 
        flags |=(1 <<2 )if self .title is not None else 0 
        b .write (Int (flags ))

        if self .title is not None :
            b .write (String (self .title ))

        return b .getvalue ()
