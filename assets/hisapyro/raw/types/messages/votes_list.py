
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class VotesList (TLObject ):
    """"""

    __slots__ :List [str ]=["count","votes","users","next_offset"]

    ID =0x823f649 
    QUALNAME ="types.messages.VotesList"

    def __init__ (self ,*,count :int ,votes :List ["raw.base.MessageUserVote"],users :List ["raw.base.User"],next_offset :Optional [str ]=None )->None :
        self .count =count 
        self .votes =votes 
        self .users =users 
        self .next_offset =next_offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"VotesList":

        flags =Int .read (b )

        count =Int .read (b )

        votes =TLObject .read (b )

        users =TLObject .read (b )

        next_offset =String .read (b )if flags &(1 <<0 )else None 
        return VotesList (count =count ,votes =votes ,users =users ,next_offset =next_offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .next_offset is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .count ))

        b .write (Vector (self .votes ))

        b .write (Vector (self .users ))

        if self .next_offset is not None :
            b .write (String (self .next_offset ))

        return b .getvalue ()
