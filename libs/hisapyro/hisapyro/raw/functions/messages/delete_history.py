
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteHistory (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","max_id","just_clear","revoke","min_date","max_date"]

    ID =0xb08f922a 
    QUALNAME ="functions.messages.DeleteHistory"

    def __init__ (self ,*,peer :"raw.base.InputPeer",max_id :int ,just_clear :Optional [bool ]=None ,revoke :Optional [bool ]=None ,min_date :Optional [int ]=None ,max_date :Optional [int ]=None )->None :
        self .peer =peer 
        self .max_id =max_id 
        self .just_clear =just_clear 
        self .revoke =revoke 
        self .min_date =min_date 
        self .max_date =max_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteHistory":

        flags =Int .read (b )

        just_clear =True if flags &(1 <<0 )else False 
        revoke =True if flags &(1 <<1 )else False 
        peer =TLObject .read (b )

        max_id =Int .read (b )

        min_date =Int .read (b )if flags &(1 <<2 )else None 
        max_date =Int .read (b )if flags &(1 <<3 )else None 
        return DeleteHistory (peer =peer ,max_id =max_id ,just_clear =just_clear ,revoke =revoke ,min_date =min_date ,max_date =max_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .just_clear else 0 
        flags |=(1 <<1 )if self .revoke else 0 
        flags |=(1 <<2 )if self .min_date is not None else 0 
        flags |=(1 <<3 )if self .max_date is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .max_id ))

        if self .min_date is not None :
            b .write (Int (self .min_date ))

        if self .max_date is not None :
            b .write (Int (self .max_date ))

        return b .getvalue ()
