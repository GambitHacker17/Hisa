
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateGroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["chat_id","call"]

    ID =0x14b24500 
    QUALNAME ="types.UpdateGroupCall"

    def __init__ (self ,*,chat_id :int ,call :"raw.base.GroupCall")->None :
        self .chat_id =chat_id 
        self .call =call 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateGroupCall":

        chat_id =Long .read (b )

        call =TLObject .read (b )

        return UpdateGroupCall (chat_id =chat_id ,call =call )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .chat_id ))

        b .write (self .call .write ())

        return b .getvalue ()
