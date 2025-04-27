
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class KeyboardButtonUrlAuth (TLObject ):
    """"""

    __slots__ :List [str ]=["text","url","button_id","fwd_text"]

    ID =0x10b78d29 
    QUALNAME ="types.KeyboardButtonUrlAuth"

    def __init__ (self ,*,text :str ,url :str ,button_id :int ,fwd_text :Optional [str ]=None )->None :
        self .text =text 
        self .url =url 
        self .button_id =button_id 
        self .fwd_text =fwd_text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"KeyboardButtonUrlAuth":

        flags =Int .read (b )

        text =String .read (b )

        fwd_text =String .read (b )if flags &(1 <<0 )else None 
        url =String .read (b )

        button_id =Int .read (b )

        return KeyboardButtonUrlAuth (text =text ,url =url ,button_id =button_id ,fwd_text =fwd_text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .fwd_text is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .text ))

        if self .fwd_text is not None :
            b .write (String (self .fwd_text ))

        b .write (String (self .url ))

        b .write (Int (self .button_id ))

        return b .getvalue ()
