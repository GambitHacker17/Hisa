
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteMessages (TLObject ):
    """"""

    __slots__ :List [str ]=["id","revoke"]

    ID =0xe58e95d2 
    QUALNAME ="functions.messages.DeleteMessages"

    def __init__ (self ,*,id :List [int ],revoke :Optional [bool ]=None )->None :
        self .id =id 
        self .revoke =revoke 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteMessages":

        flags =Int .read (b )

        revoke =True if flags &(1 <<0 )else False 
        id =TLObject .read (b ,Int )

        return DeleteMessages (id =id ,revoke =revoke )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .revoke else 0 
        b .write (Int (flags ))

        b .write (Vector (self .id ,Int ))

        return b .getvalue ()
