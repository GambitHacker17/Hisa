
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PageBlockDetails (TLObject ):
    """"""

    __slots__ :List [str ]=["blocks","title","open"]

    ID =0x76768bed 
    QUALNAME ="types.PageBlockDetails"

    def __init__ (self ,*,blocks :List ["raw.base.PageBlock"],title :"raw.base.RichText",open :Optional [bool ]=None )->None :
        self .blocks =blocks 
        self .title =title 
        self .open =open 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PageBlockDetails":

        flags =Int .read (b )

        open =True if flags &(1 <<0 )else False 
        blocks =TLObject .read (b )

        title =TLObject .read (b )

        return PageBlockDetails (blocks =blocks ,title =title ,open =open )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .open else 0 
        b .write (Int (flags ))

        b .write (Vector (self .blocks ))

        b .write (self .title .write ())

        return b .getvalue ()
