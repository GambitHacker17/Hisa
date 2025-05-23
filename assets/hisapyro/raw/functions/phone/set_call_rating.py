
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetCallRating (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","rating","comment","user_initiative"]

    ID =0x59ead627 
    QUALNAME ="functions.phone.SetCallRating"

    def __init__ (self ,*,peer :"raw.base.InputPhoneCall",rating :int ,comment :str ,user_initiative :Optional [bool ]=None )->None :
        self .peer =peer 
        self .rating =rating 
        self .comment =comment 
        self .user_initiative =user_initiative 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetCallRating":

        flags =Int .read (b )

        user_initiative =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        rating =Int .read (b )

        comment =String .read (b )

        return SetCallRating (peer =peer ,rating =rating ,comment =comment ,user_initiative =user_initiative )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .user_initiative else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .rating ))

        b .write (String (self .comment ))

        return b .getvalue ()
