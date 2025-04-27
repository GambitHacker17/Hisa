
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonSwitchInline (TLObject ):
    """"""

    __slots__ :List [str ]=["text","query","same_peer","peer_types"]

    ID =0x93b9fbb5 
    QUALNAME ="types.KeyboardButtonSwitchInline"

    def __init__ (self ,*,text :str ,query :str ,same_peer :Optional [bool ]=None ,peer_types :Optional [List ["raw.base.InlineQueryPeerType"]]=None )->None :
        self .text =text 
        self .query =query 
        self .same_peer =same_peer 
        self .peer_types =peer_types 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonSwitchInline":

        flags =Int .read (b )

        same_peer =True if flags &(1 <<0 )else False 
        text =String .read (b )

        query =String .read (b )

        peer_types =TLObject .read (b )if flags &(1 <<1 )else []

        return KeyboardButtonSwitchInline (text =text ,query =query ,same_peer =same_peer ,peer_types =peer_types )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .same_peer else 0 
        flags |=(1 <<1 )if self .peer_types else 0 
        b .write (Int (flags ))

        b .write (String (self .text ))

        b .write (String (self .query ))

        if self .peer_types is not None :
            b .write (Vector (self .peer_types ))

        return b .getvalue ()
