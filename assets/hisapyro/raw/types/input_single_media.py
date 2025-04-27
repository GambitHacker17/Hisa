
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputSingleMedia (TLObject ):
    """"""

    __slots__ :List [str ]=["media","random_id","message","entities"]

    ID =0x1cc6e91f 
    QUALNAME ="types.InputSingleMedia"

    def __init__ (self ,*,media :"raw.base.InputMedia",random_id :int ,message :str ,entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .media =media 
        self .random_id =random_id 
        self .message =message 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputSingleMedia":

        flags =Int .read (b )

        media =TLObject .read (b )

        random_id =Long .read (b )

        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<0 )else []

        return InputSingleMedia (media =media ,random_id =random_id ,message =message ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .entities else 0 
        b .write (Int (flags ))

        b .write (self .media .write ())

        b .write (Long (self .random_id ))

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        return b .getvalue ()
