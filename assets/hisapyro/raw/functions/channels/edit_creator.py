
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditCreator (TLObject ):
    """"""

    __slots__ :List [str ]=["channel","user_id","password"]

    ID =0x8f38cd1f 
    QUALNAME ="functions.channels.EditCreator"

    def __init__ (self ,*,channel :"raw.base.InputChannel",user_id :"raw.base.InputUser",password :"raw.base.InputCheckPasswordSRP")->None :
        self .channel =channel 
        self .user_id =user_id 
        self .password =password 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditCreator":

        channel =TLObject .read (b )

        user_id =TLObject .read (b )

        password =TLObject .read (b )

        return EditCreator (channel =channel ,user_id =user_id ,password =password )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .channel .write ())

        b .write (self .user_id .write ())

        b .write (self .password .write ())

        return b .getvalue ()
