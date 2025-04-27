
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetChatAvailableReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","available_reactions"]

    ID =0xfeb16771 
    QUALNAME ="functions.messages.SetChatAvailableReactions"

    def __init__ (self ,*,peer :"raw.base.InputPeer",available_reactions :"raw.base.ChatReactions")->None :
        self .peer =peer 
        self .available_reactions =available_reactions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetChatAvailableReactions":

        peer =TLObject .read (b )

        available_reactions =TLObject .read (b )

        return SetChatAvailableReactions (peer =peer ,available_reactions =available_reactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .available_reactions .write ())

        return b .getvalue ()
