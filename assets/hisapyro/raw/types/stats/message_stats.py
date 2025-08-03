
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageStats (TLObject ):
    """"""

    __slots__ :List [str ]=["views_graph"]

    ID =0x8999f295 
    QUALNAME ="types.stats.MessageStats"

    def __init__ (self ,*,views_graph :"raw.base.StatsGraph")->None :
        self .views_graph =views_graph 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageStats":

        views_graph =TLObject .read (b )

        return MessageStats (views_graph =views_graph )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .views_graph .write ())

        return b .getvalue ()
