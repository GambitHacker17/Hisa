
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MarkDialogUnread (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","unread"]

    ID =0xc286d98f 
    QUALNAME ="functions.messages.MarkDialogUnread"

    def __init__ (self ,*,peer :"raw.base.InputDialogPeer",unread :Optional [bool ]=None )->None :
        self .peer =peer 
        self .unread =unread 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MarkDialogUnread":

        flags =Int .read (b )

        unread =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        return MarkDialogUnread (peer =peer ,unread =unread )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .unread else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        return b .getvalue ()
