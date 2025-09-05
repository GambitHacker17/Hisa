
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AcceptUrlAuth (TLObject ):
    """"""

    __slots__ :List [str ]=["write_allowed","peer","msg_id","button_id","url"]

    ID =0xb12c7125 
    QUALNAME ="functions.messages.AcceptUrlAuth"

    def __init__ (self ,*,write_allowed :Optional [bool ]=None ,peer :"raw.base.InputPeer"=None ,msg_id :Optional [int ]=None ,button_id :Optional [int ]=None ,url :Optional [str ]=None )->None :
        self .write_allowed =write_allowed 
        self .peer =peer 
        self .msg_id =msg_id 
        self .button_id =button_id 
        self .url =url 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AcceptUrlAuth":

        flags =Int .read (b )

        write_allowed =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )if flags &(1 <<1 )else None 

        msg_id =Int .read (b )if flags &(1 <<1 )else None 
        button_id =Int .read (b )if flags &(1 <<1 )else None 
        url =String .read (b )if flags &(1 <<2 )else None 
        return AcceptUrlAuth (write_allowed =write_allowed ,peer =peer ,msg_id =msg_id ,button_id =button_id ,url =url )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .write_allowed else 0 
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
