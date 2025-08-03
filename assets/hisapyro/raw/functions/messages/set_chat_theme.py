
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetChatTheme (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","emoticon"]

    ID =0xe63be13f 
    QUALNAME ="functions.messages.SetChatTheme"

    def __init__ (self ,*,peer :"raw.base.InputPeer",emoticon :str )->None :
        self .peer =peer 
        self .emoticon =emoticon 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetChatTheme":

        peer =TLObject .read (b )

        emoticon =String .read (b )

        return SetChatTheme (peer =peer ,emoticon =emoticon )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (String (self .emoticon ))

        return b .getvalue ()
