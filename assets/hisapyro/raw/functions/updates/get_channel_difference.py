
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetChannelDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","filter","pts","limit","force"]

    ID =0x3173d78 
    QUALNAME ="functions.updates.GetChannelDifference"

    def __init__ (self ,*,channel :"raw.base.InputChannel",filter :"raw.base.ChannelMessagesFilter",pts :int ,limit :int ,force :Optional [bool ]=None )->None :
        self .channel =channel 
        self .filter =filter 
        self .pts =pts 
        self .limit =limit 
        self .force =force 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetChannelDifference":

        flags =Int .read (b )

        force =True if flags &(1 <<0 )else False 
        channel =TLObject .read (b )

        filter =TLObject .read (b )

        pts =Int .read (b )

        limit =Int .read (b )

        return GetChannelDifference (channel =channel ,filter =filter ,pts =pts ,limit =limit ,force =force )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .force else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        b .write (self .filter .write ())

        b .write (Int (self .pts ))

        b .write (Int (self .limit ))

        return b .getvalue ()
