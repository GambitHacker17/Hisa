
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelDifferenceTooLong (TLObject ):
    """"""

    __slots__ :List [str ]=["dialog","messages","chats","users","final","timeout"]

    ID =0xa4bcc6fe 
    QUALNAME ="types.updates.ChannelDifferenceTooLong"

    def __init__ (self ,*,dialog :"raw.base.Dialog",messages :List ["raw.base.Message"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],final :Optional [bool ]=None ,timeout :Optional [int ]=None )->None :
        self .dialog =dialog 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .final =final 
        self .timeout =timeout 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelDifferenceTooLong":

        flags =Int .read (b )

        final =True if flags &(1 <<0 )else False 
        timeout =Int .read (b )if flags &(1 <<1 )else None 
        dialog =TLObject .read (b )

        messages =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        return ChannelDifferenceTooLong (dialog =dialog ,messages =messages ,chats =chats ,users =users ,final =final ,timeout =timeout )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .final else 0 
        flags |=(1 <<1 )if self .timeout is not None else 0 
        b .write (Int (flags ))

        if self .timeout is not None :
            b .write (Int (self .timeout ))

        b .write (self .dialog .write ())

        b .write (Vector (self .messages ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        return b .getvalue ()
