
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelDifference (TLObject ):
    """"""

    __slots__ :List [str ]=["pts","new_messages","other_updates","chats","users","final","timeout"]

    ID =0x2064674e 
    QUALNAME ="types.updates.ChannelDifference"

    def __init__ (self ,*,pts :int ,new_messages :List ["raw.base.Message"],other_updates :List ["raw.base.Update"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],final :Optional [bool ]=None ,timeout :Optional [int ]=None )->None :
        self .pts =pts 
        self .new_messages =new_messages 
        self .other_updates =other_updates 
        self .chats =chats 
        self .users =users 
        self .final =final 
        self .timeout =timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelDifference":

        flags =Int .read (b )

        final =True if flags &(1 <<0 )else False 
        pts =Int .read (b )

        timeout =Int .read (b )if flags &(1 <<1 )else None 
        new_messages =TLObject .read (b )

        other_updates =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChannelDifference (pts =pts ,new_messages =new_messages ,other_updates =other_updates ,chats =chats ,users =users ,final =final ,timeout =timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .final else 0 
        flags |=(1 <<1 )if self .timeout is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .pts ))

        if self .timeout is not None :
            b .write (Int (self .timeout ))

        b .write (Vector (self .new_messages ))

        b .write (Vector (self .other_updates ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
