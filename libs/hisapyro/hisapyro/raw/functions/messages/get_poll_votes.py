
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetPollVotes (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","limit","option","offset"]

    ID =0xb86e380e 
    QUALNAME ="functions.messages.GetPollVotes"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,limit :int ,option :Optional [bytes ]=None ,offset :Optional [str ]=None )->None :
        self .peer =peer 
        self .id =id 
        self .limit =limit 
        self .option =option 
        self .offset =offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetPollVotes":

        flags =Int .read (b )

        peer =TLObject .read (b )

        id =Int .read (b )

        option =Bytes .read (b )if flags &(1 <<0 )else None 
        offset =String .read (b )if flags &(1 <<1 )else None 
        limit =Int .read (b )

        return GetPollVotes (peer =peer ,id =id ,limit =limit ,option =option ,offset =offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .option is not None else 0 
        flags |=(1 <<1 )if self .offset is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        if self .option is not None :
            b .write (Bytes (self .option ))

        if self .offset is not None :
            b .write (String (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
