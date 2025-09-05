
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GroupCallParticipantVideoSourceGroup (TLObject ):
    """"""

    __slots__ :List [str ]=["semantics","sources"]

    ID =0xdcb118b7 
    QUALNAME ="types.GroupCallParticipantVideoSourceGroup"

    def __init__ (self ,*,semantics :str ,sources :List [int ])->None :
        self .semantics =semantics 
        self .sources =sources 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GroupCallParticipantVideoSourceGroup":

        semantics =String .read (b )

        sources =TLObject .read (b ,Int )

        return GroupCallParticipantVideoSourceGroup (semantics =semantics ,sources =sources )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (String (self .semantics ))

        b .write (Vector (self .sources ,Int ))

        return b .getvalue ()
