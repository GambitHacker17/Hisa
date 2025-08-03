
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class EditExportedChatInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","link","revoked","expire_date","usage_limit","request_needed","title"]

    ID =0xbdca2f75 
    QUALNAME ="functions.messages.EditExportedChatInvite"

    def __init__ (self ,*,peer :"raw.base.InputPeer",link :str ,revoked :Optional [bool ]=None ,expire_date :Optional [int ]=None ,usage_limit :Optional [int ]=None ,request_needed :Optional [bool ]=None ,title :Optional [str ]=None )->None :
        self .peer =peer 
        self .link =link 
        self .revoked =revoked 
        self .expire_date =expire_date 
        self .usage_limit =usage_limit 
        self .request_needed =request_needed 
        self .title =title 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"EditExportedChatInvite":

        flags =Int .read (b )

        revoked =True if flags &(1 <<2 )else False 
        peer =TLObject .read (b )

        link =String .read (b )

        expire_date =Int .read (b )if flags &(1 <<0 )else None 
        usage_limit =Int .read (b )if flags &(1 <<1 )else None 
        request_needed =Bool .read (b )if flags &(1 <<3 )else None 
        title =String .read (b )if flags &(1 <<4 )else None 
        return EditExportedChatInvite (peer =peer ,link =link ,revoked =revoked ,expire_date =expire_date ,usage_limit =usage_limit ,request_needed =request_needed ,title =title )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<2 )if self .revoked else 0 
        flags |=(1 <<0 )if self .expire_date is not None else 0 
        flags |=(1 <<1 )if self .usage_limit is not None else 0 
        flags |=(1 <<3 )if self .request_needed is not None else 0 
        flags |=(1 <<4 )if self .title is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (String (self .link ))

        if self .expire_date is not None :
            b .write (Int (self .expire_date ))

        if self .usage_limit is not None :
            b .write (Int (self .usage_limit ))

        if self .request_needed is not None :
            b .write (Bool (self .request_needed ))

        if self .title is not None :
            b .write (String (self .title ))

        return b .getvalue ()
