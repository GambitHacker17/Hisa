
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SearchGlobal (TLObject ):
    """"""

    __slots__ :List [str ]=["q","filter","min_date","max_date","offset_rate","offset_peer","offset_id","limit","folder_id"]

    ID =0x4bc6589a 
    QUALNAME ="functions.messages.SearchGlobal"

    def __init__ (self ,*,q :str ,filter :"raw.base.MessagesFilter",min_date :int ,max_date :int ,offset_rate :int ,offset_peer :"raw.base.InputPeer",offset_id :int ,limit :int ,folder_id :Optional [int ]=None )->None :
        self .q =q 
        self .filter =filter 
        self .min_date =min_date 
        self .max_date =max_date 
        self .offset_rate =offset_rate 
        self .offset_peer =offset_peer 
        self .offset_id =offset_id 
        self .limit =limit 
        self .folder_id =folder_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SearchGlobal":

        flags =Int .read (b )

        folder_id =Int .read (b )if flags &(1 <<0 )else None 
        q =String .read (b )

        filter =TLObject .read (b )

        min_date =Int .read (b )

        max_date =Int .read (b )

        offset_rate =Int .read (b )

        offset_peer =TLObject .read (b )

        offset_id =Int .read (b )

        limit =Int .read (b )

        return SearchGlobal (q =q ,filter =filter ,min_date =min_date ,max_date =max_date ,offset_rate =offset_rate ,offset_peer =offset_peer ,offset_id =offset_id ,limit =limit ,folder_id =folder_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .folder_id is not None else 0 
        b .write (Int (flags ))

        if self .folder_id is not None :
            b .write (Int (self .folder_id ))

        b .write (String (self .q ))

        b .write (self .filter .write ())

        b .write (Int (self .min_date ))

        b .write (Int (self .max_date ))

        b .write (Int (self .offset_rate ))

        b .write (self .offset_peer .write ())

        b .write (Int (self .offset_id ))

        b .write (Int (self .limit ))

        return b .getvalue ()
