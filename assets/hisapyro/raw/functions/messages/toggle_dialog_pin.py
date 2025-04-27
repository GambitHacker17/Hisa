
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleDialogPin (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","pinned"]

    ID =0xa731e257 
    QUALNAME ="functions.messages.ToggleDialogPin"

    def __init__ (self ,*,peer :"raw.base.InputDialogPeer",pinned :Optional [bool ]=None )->None :
        self .peer =peer 
        self .pinned =pinned 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleDialogPin":

        flags =Int .read (b )

        pinned =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        return ToggleDialogPin (peer =peer ,pinned =pinned )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .pinned else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        return b .getvalue ()
