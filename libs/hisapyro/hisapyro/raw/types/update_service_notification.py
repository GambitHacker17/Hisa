
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateServiceNotification (TLObject ):
    """"""

    __slots__ :List [str ]=["type","message","media","entities","popup","inbox_date"]

    ID =0xebe46819 
    QUALNAME ="types.UpdateServiceNotification"

    def __init__ (self ,*,type :str ,message :str ,media :"raw.base.MessageMedia",entities :List ["raw.base.MessageEntity"],popup :Optional [bool ]=None ,inbox_date :Optional [int ]=None )->None :
        self .type =type 
        self .message =message 
        self .media =media 
        self .entities =entities 
        self .popup =popup 
        self .inbox_date =inbox_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateServiceNotification":

        flags =Int .read (b )

        popup =True if flags &(1 <<0 )else False 
        inbox_date =Int .read (b )if flags &(1 <<1 )else None 
        type =String .read (b )

        message =String .read (b )

        media =TLObject .read (b )

        entities =TLObject .read (b )

        return UpdateServiceNotification (type =type ,message =message ,media =media ,entities =entities ,popup =popup ,inbox_date =inbox_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .popup else 0 
        flags |=(1 <<1 )if self .inbox_date is not None else 0 
        b .write (Int (flags ))

        if self .inbox_date is not None :
            b .write (Int (self .inbox_date ))

        b .write (String (self .type ))

        b .write (String (self .message ))

        b .write (self .media .write ())

        b .write (Vector (self .entities ))

        return b .getvalue ()
