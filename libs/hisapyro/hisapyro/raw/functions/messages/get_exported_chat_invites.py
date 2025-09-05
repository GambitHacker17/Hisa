
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GetExportedChatInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","admin_id","limit","revoked","offset_date","offset_link"]

    ID =0xa2b5a3f6 
    QUALNAME ="functions.messages.GetExportedChatInvites"

    def __init__ (self ,*,peer :"raw.base.InputPeer",admin_id :"raw.base.InputUser",limit :int ,revoked :Optional [bool ]=None ,offset_date :Optional [int ]=None ,offset_link :Optional [str ]=None )->None :
        self .peer =peer 
        self .admin_id =admin_id 
        self .limit =limit 
        self .revoked =revoked 
        self .offset_date =offset_date 
        self .offset_link =offset_link 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GetExportedChatInvites":

        flags =Int .read (b )

        revoked =True if flags &(1 <<3 )else False 
        peer =TLObject .read (b )

        admin_id =TLObject .read (b )

        offset_date =Int .read (b )if flags &(1 <<2 )else None 
        offset_link =String .read (b )if flags &(1 <<2 )else None 
        limit =Int .read (b )

        return GetExportedChatInvites (peer =peer ,admin_id =admin_id ,limit =limit ,revoked =revoked ,offset_date =offset_date ,offset_link =offset_link )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<3 )if self .revoked else 0 
        flags |=(1 <<2 )if self .offset_date is not None else 0 
        flags |=(1 <<2 )if self .offset_link is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (self .admin_id .write ())

        if self .offset_date is not None :
            b .write (Int (self .offset_date ))

        if self .offset_link is not None :
            b .write (String (self .offset_link ))

        b .write (Int (self .limit ))

        return b .getvalue ()
