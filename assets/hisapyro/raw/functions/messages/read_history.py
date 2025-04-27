
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ReadHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","max_id"]

    ID =0xe306d3a 
    QUALNAME ="functions.messages.ReadHistory"

    def __init__ (self ,*,peer :"raw.base.InputPeer",max_id :int )->None :
        self .peer =peer 
        self .max_id =max_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ReadHistory":

        peer =TLObject .read (b )

        max_id =Int .read (b )

        return ReadHistory (peer =peer ,max_id =max_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .max_id ))

        return b .getvalue ()
