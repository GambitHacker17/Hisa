
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PromoData (TLObject ):
    """"""

    __slots__ :List [str ]=["expires","peer","chats","users","proxy","psa_type","psa_message"]

    ID =0x8c39793f 
    QUALNAME ="types.help.PromoData"

    def __init__ (self ,*,expires :int ,peer :"raw.base.Peer",chats :List ["raw.base.Chat"],users :List ["raw.base.User"],proxy :Optional [bool ]=None ,psa_type :Optional [str ]=None ,psa_message :Optional [str ]=None )->None :
        self .expires =expires 
        self .peer =peer 
        self .chats =chats 
        self .users =users 
        self .proxy =proxy 
        self .psa_type =psa_type 
        self .psa_message =psa_message 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PromoData":

        flags =Int .read (b )

        proxy =True if flags &(1 <<0 )else False 
        expires =Int .read (b )

        peer =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        psa_type =String .read (b )if flags &(1 <<1 )else None 
        psa_message =String .read (b )if flags &(1 <<2 )else None 
        return PromoData (expires =expires ,peer =peer ,chats =chats ,users =users ,proxy =proxy ,psa_type =psa_type ,psa_message =psa_message )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .proxy else 0 
        flags |=(1 <<1 )if self .psa_type is not None else 0 
        flags |=(1 <<2 )if self .psa_message is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .expires ))

        b .write (self .peer .write ())

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        if self .psa_type is not None :
            b .write (String (self .psa_type ))

        if self .psa_message is not None :
            b .write (String (self .psa_message ))

        return b .getvalue ()
