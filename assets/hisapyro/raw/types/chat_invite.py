
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ChatInvite (TLObject ):
    """"""

    __slots__ :List [str ]=["title","photo","participants_count","channel","broadcast","public","megagroup","request_needed","about","participants"]

    ID =0x300c44c1 
    QUALNAME ="types.ChatInvite"

    def __init__ (self ,*,title :str ,photo :"raw.base.Photo",participants_count :int ,channel :Optional [bool ]=None ,broadcast :Optional [bool ]=None ,public :Optional [bool ]=None ,megagroup :Optional [bool ]=None ,request_needed :Optional [bool ]=None ,about :Optional [str ]=None ,participants :Optional [List ["raw.base.User"]]=None )->None :
        self .title =title 
        self .photo =photo 
        self .participants_count =participants_count 
        self .channel =channel 
        self .broadcast =broadcast 
        self .public =public 
        self .megagroup =megagroup 
        self .request_needed =request_needed 
        self .about =about 
        self .participants =participants 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ChatInvite":

        flags =Int .read (b )

        channel =True if flags &(1 <<0 )else False 
        broadcast =True if flags &(1 <<1 )else False 
        public =True if flags &(1 <<2 )else False 
        megagroup =True if flags &(1 <<3 )else False 
        request_needed =True if flags &(1 <<6 )else False 
        title =String .read (b )

        about =String .read (b )if flags &(1 <<5 )else None 
        photo =TLObject .read (b )

        participants_count =Int .read (b )

        participants =TLObject .read (b )if flags &(1 <<4 )else []

        return ChatInvite (title =title ,photo =photo ,participants_count =participants_count ,channel =channel ,broadcast =broadcast ,public =public ,megagroup =megagroup ,request_needed =request_needed ,about =about ,participants =participants )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .channel else 0 
        flags |=(1 <<1 )if self .broadcast else 0 
        flags |=(1 <<2 )if self .public else 0 
        flags |=(1 <<3 )if self .megagroup else 0 
        flags |=(1 <<6 )if self .request_needed else 0 
        flags |=(1 <<5 )if self .about is not None else 0 
        flags |=(1 <<4 )if self .participants else 0 
        b .write (Int (flags ))

        b .write (String (self .title ))

        if self .about is not None :
            b .write (String (self .about ))

        b .write (self .photo .write ())

        b .write (Int (self .participants_count ))

        if self .participants is not None :
            b .write (Vector (self .participants ))

        return b .getvalue ()
