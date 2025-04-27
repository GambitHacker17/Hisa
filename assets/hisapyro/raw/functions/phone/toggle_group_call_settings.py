
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ToggleGroupCallSettings (TLObject ):
    """"""

    __slots__ :List [str ]=["call","reset_invite_hash","join_muted"]

    ID =0x74bbb43d 
    QUALNAME ="functions.phone.ToggleGroupCallSettings"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",reset_invite_hash :Optional [bool ]=None ,join_muted :Optional [bool ]=None )->None :
        self .call =call 
        self .reset_invite_hash =reset_invite_hash 
        self .join_muted =join_muted 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ToggleGroupCallSettings":

        flags =Int .read (b )

        reset_invite_hash =True if flags &(1 <<1 )else False 
        call =TLObject .read (b )

        join_muted =Bool .read (b )if flags &(1 <<0 )else None 
        return ToggleGroupCallSettings (call =call ,reset_invite_hash =reset_invite_hash ,join_muted =join_muted )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .reset_invite_hash else 0 
        flags |=(1 <<0 )if self .join_muted is not None else 0 
        b .write (Int (flags ))

        b .write (self .call .write ())

        if self .join_muted is not None :
            b .write (Bool (self .join_muted ))

        return b .getvalue ()
