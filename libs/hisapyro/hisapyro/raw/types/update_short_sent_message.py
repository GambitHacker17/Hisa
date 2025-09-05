
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateShortSentMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["id","pts","pts_count","date","out","media","entities","ttl_period"]

    ID =0x9015e101 
    QUALNAME ="types.UpdateShortSentMessage"

    def __init__ (self ,*,id :int ,pts :int ,pts_count :int ,date :int ,out :Optional [bool ]=None ,media :"raw.base.MessageMedia"=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,ttl_period :Optional [int ]=None )->None :
        self .id =id 
        self .pts =pts 
        self .pts_count =pts_count 
        self .date =date 
        self .out =out 
        self .media =media 
        self .entities =entities 
        self .ttl_period =ttl_period 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateShortSentMessage":

        flags =Int .read (b )

        out =True if flags &(1 <<1 )else False 
        id =Int .read (b )

        pts =Int .read (b )

        pts_count =Int .read (b )

        date =Int .read (b )

        media =TLObject .read (b )if flags &(1 <<9 )else None 

        entities =TLObject .read (b )if flags &(1 <<7 )else []

        ttl_period =Int .read (b )if flags &(1 <<25 )else None 
        return UpdateShortSentMessage (id =id ,pts =pts ,pts_count =pts_count ,date =date ,out =out ,media =media ,entities =entities ,ttl_period =ttl_period )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .out else 0 
        flags |=(1 <<9 )if self .media is not None else 0 
        flags |=(1 <<7 )if self .entities else 0 
        flags |=(1 <<25 )if self .ttl_period is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .id ))

        b .write (Int (self .pts ))

        b .write (Int (self .pts_count ))

        b .write (Int (self .date ))

        if self .media is not None :
            b .write (self .media .write ())

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .ttl_period is not None :
            b .write (Int (self .ttl_period ))

        return b .getvalue ()
