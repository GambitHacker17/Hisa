
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SavedInfo (TLObject ):
    """"""

    __slots__ :List [str ]=["has_saved_credentials","saved_info"]

    ID =0xfb8fe43c 
    QUALNAME ="types.payments.SavedInfo"

    def __init__ (self ,*,has_saved_credentials :Optional [bool ]=None ,saved_info :"raw.base.PaymentRequestedInfo"=None )->None :
        self .has_saved_credentials =has_saved_credentials 
        self .saved_info =saved_info 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SavedInfo":

        flags =Int .read (b )

        has_saved_credentials =True if flags &(1 <<1 )else False 
        saved_info =TLObject .read (b )if flags &(1 <<0 )else None 

        return SavedInfo (has_saved_credentials =has_saved_credentials ,saved_info =saved_info )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .has_saved_credentials else 0 
        flags |=(1 <<0 )if self .saved_info is not None else 0 
        b .write (Int (flags ))

        if self .saved_info is not None :
            b .write (self .saved_info .write ())

        return b .getvalue ()
