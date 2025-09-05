
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveDefaultGroupCallJoinAs (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","join_as"]

    ID =0x575e1f8c 
    QUALNAME ="functions.phone.SaveDefaultGroupCallJoinAs"

    def __init__ (self ,*,peer :"raw.base.InputPeer",join_as :"raw.base.InputPeer")->None :
        self .peer =peer 
        self .join_as =join_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveDefaultGroupCallJoinAs":

        peer =TLObject .read (b )

        join_as =TLObject .read (b )

        return SaveDefaultGroupCallJoinAs (peer =peer ,join_as =join_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .join_as .write ())

        return b .getvalue ()
