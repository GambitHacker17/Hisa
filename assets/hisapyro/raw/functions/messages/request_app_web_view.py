
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestAppWebView (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","app","platform","write_allowed","start_param","theme_params"]

    ID =0x8c5a3b3c 
    QUALNAME ="functions.messages.RequestAppWebView"

    def __init__ (self ,*,peer :"raw.base.InputPeer",app :"raw.base.InputBotApp",platform :str ,write_allowed :Optional [bool ]=None ,start_param :Optional [str ]=None ,theme_params :"raw.base.DataJSON"=None )->None :
        self .peer =peer 
        self .app =app 
        self .platform =platform 
        self .write_allowed =write_allowed 
        self .start_param =start_param 
        self .theme_params =theme_params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestAppWebView":

        flags =Int .read (b )

        write_allowed =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        app =TLObject .read (b )

        start_param =String .read (b )if flags &(1 <<1 )else None 
        theme_params =TLObject .read (b )if flags &(1 <<2 )else None 

        platform =String .read (b )

        return RequestAppWebView (peer =peer ,app =app ,platform =platform ,write_allowed =write_allowed ,start_param =start_param ,theme_params =theme_params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .write_allowed else 0 
        flags |=(1 <<1 )if self .start_param is not None else 0 
        flags |=(1 <<2 )if self .theme_params is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (self .app .write ())

        if self .start_param is not None :
            b .write (String (self .start_param ))

        if self .theme_params is not None :
            b .write (self .theme_params .write ())

        b .write (String (self .platform ))

        return b .getvalue ()
