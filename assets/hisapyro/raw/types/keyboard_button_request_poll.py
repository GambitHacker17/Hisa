
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonRequestPoll (TLObject ):
    """"""

    __slots__ :List [str ]=["text","quiz"]

    ID =0xbbc7515d 
    QUALNAME ="types.KeyboardButtonRequestPoll"

    def __init__ (self ,*,text :str ,quiz :Optional [bool ]=None )->None :
        self .text =text 
        self .quiz =quiz 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonRequestPoll":

        flags =Int .read (b )

        quiz =Bool .read (b )if flags &(1 <<0 )else None 
        text =String .read (b )

        return KeyboardButtonRequestPoll (text =text ,quiz =quiz )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .quiz is not None else 0 
        b .write (Int (flags ))

        if self .quiz is not None :
            b .write (Bool (self .quiz ))

        b .write (String (self .text ))

        return b .getvalue ()
