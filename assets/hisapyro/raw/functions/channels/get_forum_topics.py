
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetForumTopics (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","offset_date","offset_id","offset_topic","limit","q"]

    ID =0xde560d1 
    QUALNAME ="functions.channels.GetForumTopics"

    def __init__ (self ,*,channel :"raw.base.InputChannel",offset_date :int ,offset_id :int ,offset_topic :int ,limit :int ,q :Optional [str ]=None )->None :
        self .channel =channel 
        self .offset_date =offset_date 
        self .offset_id =offset_id 
        self .offset_topic =offset_topic 
        self .limit =limit 
        self .q =q 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetForumTopics":

        flags =Int .read (b )

        channel =TLObject .read (b )

        q =String .read (b )if flags &(1 <<0 )else None 
        offset_date =Int .read (b )

        offset_id =Int .read (b )

        offset_topic =Int .read (b )

        limit =Int .read (b )

        return GetForumTopics (channel =channel ,offset_date =offset_date ,offset_id =offset_id ,offset_topic =offset_topic ,limit =limit ,q =q )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .q is not None else 0 
        b .write (Int (flags ))

        b .write (self .channel .write ())

        if self .q is not None :
            b .write (String (self .q ))

        b .write (Int (self .offset_date ))

        b .write (Int (self .offset_id ))

        b .write (Int (self .offset_topic ))

        b .write (Int (self .limit ))

        return b .getvalue ()
