
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Search (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","q","filter","min_date","max_date","offset_id","add_offset","limit","max_id","min_id","hash","from_id","top_msg_id"]

    ID =0xa0fda762 
    QUALNAME ="functions.messages.Search"

    def __init__ (self ,*,peer :"raw.base.InputPeer",q :str ,filter :"raw.base.MessagesFilter",min_date :int ,max_date :int ,offset_id :int ,add_offset :int ,limit :int ,max_id :int ,min_id :int ,hash :int ,from_id :"raw.base.InputPeer"=None ,top_msg_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .q =q 
        self .filter =filter 
        self .min_date =min_date 
        self .max_date =max_date 
        self .offset_id =offset_id 
        self .add_offset =add_offset 
        self .limit =limit 
        self .max_id =max_id 
        self .min_id =min_id 
        self .hash =hash 
        self .from_id =from_id 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Search":

        flags =Int .read (b )

        peer =TLObject .read (b )

        q =String .read (b )

        from_id =TLObject .read (b )if flags &(1 <<0 )else None 

        top_msg_id =Int .read (b )if flags &(1 <<1 )else None 
        filter =TLObject .read (b )

        min_date =Int .read (b )

        max_date =Int .read (b )

        offset_id =Int .read (b )

        add_offset =Int .read (b )

        limit =Int .read (b )

        max_id =Int .read (b )

        min_id =Int .read (b )

        hash =Long .read (b )

        return Search (peer =peer ,q =q ,filter =filter ,min_date =min_date ,max_date =max_date ,offset_id =offset_id ,add_offset =add_offset ,limit =limit ,max_id =max_id ,min_id =min_id ,hash =hash ,from_id =from_id ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .from_id is not None else 0 
        flags |=(1 <<1 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (String (self .q ))

        if self .from_id is not None :
            b .write (self .from_id .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (self .filter .write ())

        b .write (Int (self .min_date ))

        b .write (Int (self .max_date ))

        b .write (Int (self .offset_id ))

        b .write (Int (self .add_offset ))

        b .write (Int (self .limit ))

        b .write (Int (self .max_id ))

        b .write (Int (self .min_id ))

        b .write (Long (self .hash ))

        return b .getvalue ()
