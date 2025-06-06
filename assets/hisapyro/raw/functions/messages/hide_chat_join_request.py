
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class HideChatJoinRequest (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","user_id","approved"]

    ID =0x7fe7e815 
    QUALNAME ="functions.messages.HideChatJoinRequest"

    def __init__ (self ,*,peer :"raw.base.InputPeer",user_id :"raw.base.InputUser",approved :Optional [bool ]=None )->None :
        self .peer =peer 
        self .user_id =user_id 
        self .approved =approved 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"HideChatJoinRequest":

        flags =Int .read (b )

        approved =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        user_id =TLObject .read (b )

        return HideChatJoinRequest (peer =peer ,user_id =user_id ,approved =approved )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .approved else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (self .user_id .write ())

        return b .getvalue ()
