
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotInlineQuery (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","user_id","query","offset","geo","peer_type"]

    ID =0x496f379c 
    QUALNAME ="types.UpdateBotInlineQuery"

    def __init__ (self ,*,query_id :int ,user_id :int ,query :str ,offset :str ,geo :"raw.base.GeoPoint"=None ,peer_type :"raw.base.InlineQueryPeerType"=None )->None :
        self .query_id =query_id 
        self .user_id =user_id 
        self .query =query 
        self .offset =offset 
        self .geo =geo 
        self .peer_type =peer_type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotInlineQuery":

        flags =Int .read (b )

        query_id =Long .read (b )

        user_id =Long .read (b )

        query =String .read (b )

        geo =TLObject .read (b )if flags &(1 <<0 )else None 

        peer_type =TLObject .read (b )if flags &(1 <<1 )else None 

        offset =String .read (b )

        return UpdateBotInlineQuery (query_id =query_id ,user_id =user_id ,query =query ,offset =offset ,geo =geo ,peer_type =peer_type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .geo is not None else 0 
        flags |=(1 <<1 )if self .peer_type is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .query_id ))

        b .write (Long (self .user_id ))

        b .write (String (self .query ))

        if self .geo is not None :
            b .write (self .geo .write ())

        if self .peer_type is not None :
            b .write (self .peer_type .write ())

        b .write (String (self .offset ))

        return b .getvalue ()
