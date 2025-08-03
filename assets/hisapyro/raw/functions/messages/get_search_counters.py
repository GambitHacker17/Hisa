
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetSearchCounters (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","filters","top_msg_id"]

    ID =0xae7cc1 
    QUALNAME ="functions.messages.GetSearchCounters"

    def __init__ (self ,*,peer :"raw.base.InputPeer",filters :List ["raw.base.MessagesFilter"],top_msg_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .filters =filters 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetSearchCounters":

        flags =Int .read (b )

        peer =TLObject .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        filters =TLObject .read (b )

        return GetSearchCounters (peer =peer ,filters =filters ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (Vector (self .filters ))

        return b .getvalue ()
