
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetSearchResultsCalendar (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","filter","offset_id","offset_date"]

    ID =0x49f0bde9 
    QUALNAME ="functions.messages.GetSearchResultsCalendar"

    def __init__ (self ,*,peer :"raw.base.InputPeer",filter :"raw.base.MessagesFilter",offset_id :int ,offset_date :int )->None :
        self .peer =peer 
        self .filter =filter 
        self .offset_id =offset_id 
        self .offset_date =offset_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetSearchResultsCalendar":

        peer =TLObject .read (b )

        filter =TLObject .read (b )

        offset_id =Int .read (b )

        offset_date =Int .read (b )

        return GetSearchResultsCalendar (peer =peer ,filter =filter ,offset_id =offset_id ,offset_date =offset_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .filter .write ())

        b .write (Int (self .offset_id ))

        b .write (Int (self .offset_date ))

        return b .getvalue ()
