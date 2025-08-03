
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestUrlAuth (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","msg_id","button_id","url"]

    ID =0x198fb446 
    QUALNAME ="functions.messages.RequestUrlAuth"

    def __init__ (self ,*,peer :"raw.base.InputPeer"=None ,msg_id :Optional [int ]=None ,button_id :Optional [int ]=None ,url :Optional [str ]=None )->None :
        self .peer =peer 
        self .msg_id =msg_id 
        self .button_id =button_id 
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestUrlAuth":

        flags =Int .read (b )

        peer =TLObject .read (b )if flags &(1 <<1 )else None 

        msg_id =Int .read (b )if flags &(1 <<1 )else None 
        button_id =Int .read (b )if flags &(1 <<1 )else None 
        url =String .read (b )if flags &(1 <<2 )else None 
        return RequestUrlAuth (peer =peer ,msg_id =msg_id ,button_id =button_id ,url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .peer is not None else 0 
        flags |=(1 <<1 )if self .msg_id is not None else 0 
        flags |=(1 <<1 )if self .button_id is not None else 0 
        flags |=(1 <<2 )if self .url is not None else 0 
        b .write (Int (flags ))

        if self .peer is not None :
            b .write (self .peer .write ())

        if self .msg_id is not None :
            b .write (Int (self .msg_id ))

        if self .button_id is not None :
            b .write (Int (self .button_id ))

        if self .url is not None :
            b .write (String (self .url ))

        return b .getvalue ()
