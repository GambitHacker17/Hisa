
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchCounter (TLObject ):
    """"""

    __slots__ :List [str ]=["filter","count","inexact"]

    ID =0xe844ebff 
    QUALNAME ="types.messages.SearchCounter"

    def __init__ (self ,*,filter :"raw.base.MessagesFilter",count :int ,inexact :Optional [bool ]=None )->None :
        self .filter =filter 
        self .count =count 
        self .inexact =inexact 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchCounter":

        flags =Int .read (b )

        inexact =True if flags &(1 <<1 )else False 
        filter =TLObject .read (b )

        count =Int .read (b )

        return SearchCounter (filter =filter ,count =count ,inexact =inexact )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .inexact else 0 
        b .write (Int (flags ))

        b .write (self .filter .write ())

        b .write (Int (self .count ))

        return b .getvalue ()
