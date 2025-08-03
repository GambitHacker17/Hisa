
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetGameHighScores (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","user_id"]

    ID =0xe822649d 
    QUALNAME ="functions.messages.GetGameHighScores"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,user_id :"raw.base.InputUser")->None :
        self .peer =peer 
        self .id =id 
        self .user_id =user_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetGameHighScores":

        peer =TLObject .read (b )

        id =Int .read (b )

        user_id =TLObject .read (b )

        return GetGameHighScores (peer =peer ,id =id ,user_id =user_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        b .write (self .user_id .write ())

        return b .getvalue ()
