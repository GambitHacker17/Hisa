
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetSearchResultsPositions (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","filter","offset_id","limit"]

    ID =0x6e9583a3 
    QUALNAME ="functions.messages.GetSearchResultsPositions"

    def __init__ (self ,*,peer :"raw.base.InputPeer",filter :"raw.base.MessagesFilter",offset_id :int ,limit :int )->None :
        self .peer =peer 
        self .filter =filter 
        self .offset_id =offset_id 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetSearchResultsPositions":

        peer =TLObject .read (b )

        filter =TLObject .read (b )

        offset_id =Int .read (b )

        limit =Int .read (b )

        return GetSearchResultsPositions (peer =peer ,filter =filter ,offset_id =offset_id ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .filter .write ())

        b .write (Int (self .offset_id ))

        b .write (Int (self .limit ))

        return b .getvalue ()
