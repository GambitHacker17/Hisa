
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestSimpleWebView (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","url","platform","from_switch_webview","theme_params"]

    ID =0x299bec8e 
    QUALNAME ="functions.messages.RequestSimpleWebView"

    def __init__ (self ,*,bot :"raw.base.InputUser",url :str ,platform :str ,from_switch_webview :Optional [bool ]=None ,theme_params :"raw.base.DataJSON"=None )->None :
        self .bot =bot 
        self .url =url 
        self .platform =platform 
        self .from_switch_webview =from_switch_webview 
        self .theme_params =theme_params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestSimpleWebView":

        flags =Int .read (b )

        from_switch_webview =True if flags &(1 <<1 )else False 
        bot =TLObject .read (b )

        url =String .read (b )

        theme_params =TLObject .read (b )if flags &(1 <<0 )else None 

        platform =String .read (b )

        return RequestSimpleWebView (bot =bot ,url =url ,platform =platform ,from_switch_webview =from_switch_webview ,theme_params =theme_params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .from_switch_webview else 0 
        flags |=(1 <<0 )if self .theme_params is not None else 0 
        b .write (Int (flags ))

        b .write (self .bot .write ())

        b .write (String (self .url ))

        if self .theme_params is not None :
            b .write (self .theme_params .write ())

        b .write (String (self .platform ))

        return b .getvalue ()
