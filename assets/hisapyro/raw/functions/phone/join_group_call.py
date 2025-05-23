
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class JoinGroupCall (TLObject ):
    """"""

    __slots__ :List [str ]=["call","join_as","params","muted","video_stopped","invite_hash"]

    ID =0xb132ff7b 
    QUALNAME ="functions.phone.JoinGroupCall"

    def __init__ (self ,*,call :"raw.base.InputGroupCall",join_as :"raw.base.InputPeer",params :"raw.base.DataJSON",muted :Optional [bool ]=None ,video_stopped :Optional [bool ]=None ,invite_hash :Optional [str ]=None )->None :
        self .call =call 
        self .join_as =join_as 
        self .params =params 
        self .muted =muted 
        self .video_stopped =video_stopped 
        self .invite_hash =invite_hash 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"JoinGroupCall":

        flags =Int .read (b )

        muted =True if flags &(1 <<0 )else False 
        video_stopped =True if flags &(1 <<2 )else False 
        call =TLObject .read (b )

        join_as =TLObject .read (b )

        invite_hash =String .read (b )if flags &(1 <<1 )else None 
        params =TLObject .read (b )

        return JoinGroupCall (call =call ,join_as =join_as ,params =params ,muted =muted ,video_stopped =video_stopped ,invite_hash =invite_hash )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .muted else 0 
        flags |=(1 <<2 )if self .video_stopped else 0 
        flags |=(1 <<1 )if self .invite_hash is not None else 0 
        b .write (Int (flags ))

        b .write (self .call .write ())

        b .write (self .join_as .write ())

        if self .invite_hash is not None :
            b .write (String (self .invite_hash ))

        b .write (self .params .write ())

        return b .getvalue ()
