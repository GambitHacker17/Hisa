
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveDefaultSendAs (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","send_as"]

    ID =0xccfddf96 
    QUALNAME ="functions.messages.SaveDefaultSendAs"

    def __init__ (self ,*,peer :"raw.base.InputPeer",send_as :"raw.base.InputPeer")->None :
        self .peer =peer 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveDefaultSendAs":

        peer =TLObject .read (b )

        send_as =TLObject .read (b )

        return SaveDefaultSendAs (peer =peer ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .send_as .write ())

        return b .getvalue ()
