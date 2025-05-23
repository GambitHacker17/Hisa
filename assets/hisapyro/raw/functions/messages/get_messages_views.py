
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetMessagesViews (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","increment"]

    ID =0x5784d3e1 
    QUALNAME ="functions.messages.GetMessagesViews"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :List [int ],increment :bool )->None :
        self .peer =peer 
        self .id =id 
        self .increment =increment 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetMessagesViews":

        peer =TLObject .read (b )

        id =TLObject .read (b ,Int )

        increment =Bool .read (b )

        return GetMessagesViews (peer =peer ,id =id ,increment =increment )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Vector (self .id ,Int ))

        b .write (Bool (self .increment ))

        return b .getvalue ()
