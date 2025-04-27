
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChannelForbidden (TLObject ):
    """"""

    __slots__ :List [str ]=["id","access_hash","title","broadcast","megagroup","until_date"]

    ID =0x17d493d5 
    QUALNAME ="types.ChannelForbidden"

    def __init__ (self ,*,id :int ,access_hash :int ,title :str ,broadcast :Optional [bool ]=None ,megagroup :Optional [bool ]=None ,until_date :Optional [int ]=None )->None :
        self .id =id 
        self .access_hash =access_hash 
        self .title =title 
        self .broadcast =broadcast 
        self .megagroup =megagroup 
        self .until_date =until_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChannelForbidden":

        flags =Int .read (b )

        broadcast =True if flags &(1 <<5 )else False 
        megagroup =True if flags &(1 <<8 )else False 
        id =Long .read (b )

        access_hash =Long .read (b )

        title =String .read (b )

        until_date =Int .read (b )if flags &(1 <<16 )else None 
        return ChannelForbidden (id =id ,access_hash =access_hash ,title =title ,broadcast =broadcast ,megagroup =megagroup ,until_date =until_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .broadcast else 0 
        flags |=(1 <<8 )if self .megagroup else 0 
        flags |=(1 <<16 )if self .until_date is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .id ))

        b .write (Long (self .access_hash ))

        b .write (String (self .title ))

        if self .until_date is not None :
            b .write (Int (self .until_date ))

        return b .getvalue ()
