
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetGroupParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["call","ids","sources","offset","limit"]

    ID =0xc558d8ab 
    QUALNAME ="functions.phone.GetGroupParticipants"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",ids :List ["raw.base.InputPeer"],sources :List [int ],offset :str ,limit :int )->None :
        self .call =call 
        self .ids =ids 
        self .sources =sources 
        self .offset =offset 
        self .limit =limit 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetGroupParticipants":

        call =TLObject .read (b )

        ids =TLObject .read (b )

        sources =TLObject .read (b ,Int )

        offset =String .read (b )

        limit =Int .read (b )

        return GetGroupParticipants (call =call ,ids =ids ,sources =sources ,offset =offset ,limit =limit )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .call .write ())

        b .write (Vector (self .ids ))

        b .write (Vector (self .sources ,Int ))

        b .write (String (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
