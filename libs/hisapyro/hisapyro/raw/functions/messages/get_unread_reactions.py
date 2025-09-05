
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetUnreadReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","offset_id","add_offset","limit","max_id","min_id","top_msg_id"]

    ID =0x3223495b 
    QUALNAME ="functions.messages.GetUnreadReactions"

    def __init__ (self ,*,peer :"raw.base.InputPeer",offset_id :int ,add_offset :int ,limit :int ,max_id :int ,min_id :int ,top_msg_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .offset_id =offset_id 
        self .add_offset =add_offset 
        self .limit =limit 
        self .max_id =max_id 
        self .min_id =min_id 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetUnreadReactions":

        flags =Int .read (b )

        peer =TLObject .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        offset_id =Int .read (b )

        add_offset =Int .read (b )

        limit =Int .read (b )

        max_id =Int .read (b )

        min_id =Int .read (b )

        return GetUnreadReactions (peer =peer ,offset_id =offset_id ,add_offset =add_offset ,limit =limit ,max_id =max_id ,min_id =min_id ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (Int (self .offset_id ))

        b .write (Int (self .add_offset ))

        b .write (Int (self .limit ))

        b .write (Int (self .max_id ))

        b .write (Int (self .min_id ))

        return b .getvalue ()
