
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DraftMessageEmpty (TLObject ):
    """"""

    __slots__ :List [str ]=["date"]

    ID =0x1b0c841a 
    QUALNAME ="types.DraftMessageEmpty"

    def __init__ (self ,*,date :Optional [int ]=None )->None :
        self .date =date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DraftMessageEmpty":

        flags =Int .read (b )

        date =Int .read (b )if flags &(1 <<0 )else None 
        return DraftMessageEmpty (date =date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .date is not None else 0 
        b .write (Int (flags ))

        if self .date is not None :
            b .write (Int (self .date ))

        return b .getvalue ()
