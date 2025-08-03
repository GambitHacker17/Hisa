
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDialogFilterOrder (TLObject ):
    """"""

    __slots__ :List [str ]=["order"]

    ID =0xa5d72105 
    QUALNAME ="types.UpdateDialogFilterOrder"

    def __init__ (self ,*,order :List [int ])->None :
        self .order =order 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDialogFilterOrder":

        order =TLObject .read (b ,Int )

        return UpdateDialogFilterOrder (order =order )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .order ,Int ))

        return b .getvalue ()
