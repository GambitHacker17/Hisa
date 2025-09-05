
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDialogUnreadMark (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","unread"]

    ID =0xe16459c3 
    QUALNAME ="types.UpdateDialogUnreadMark"

    def __init__ (self ,*,peer :"raw.base.DialogPeer",unread :Optional [bool ]=None )->None :
        self .peer =peer 
        self .unread =unread 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDialogUnreadMark":

        flags =Int .read (b )

        unread =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        return UpdateDialogUnreadMark (peer =peer ,unread =unread )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .unread else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        return b .getvalue ()
