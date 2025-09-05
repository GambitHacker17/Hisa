
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMessageReactionsList (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","limit","reaction","offset"]

    ID =0x461b3f48 
    QUALNAME ="functions.messages.GetMessageReactionsList"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,limit :int ,reaction :"raw.base.Reaction"=None ,offset :Optional [str ]=None )->None :
        self .peer =peer 
        self .id =id 
        self .limit =limit 
        self .reaction =reaction 
        self .offset =offset 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMessageReactionsList":

        flags =Int .read (b )

        peer =TLObject .read (b )

        id =Int .read (b )

        reaction =TLObject .read (b )if flags &(1 <<0 )else None 

        offset =String .read (b )if flags &(1 <<1 )else None 
        limit =Int .read (b )

        return GetMessageReactionsList (peer =peer ,id =id ,limit =limit ,reaction =reaction ,offset =offset )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .reaction is not None else 0 
        flags |=(1 <<1 )if self .offset is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        if self .reaction is not None :
            b .write (self .reaction .write ())

        if self .offset is not None :
            b .write (String (self .offset ))

        b .write (Int (self .limit ))

        return b .getvalue ()
