
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class RequestWebView (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","bot","platform","from_bot_menu","silent","url","start_param","theme_params","reply_to_msg_id","top_msg_id","send_as"]

    ID =0x178b480b 
    QUALNAME ="functions.messages.RequestWebView"

    def __init__ (self ,*,peer :"raw.base.InputPeer",bot :"raw.base.InputUser",platform :str ,from_bot_menu :Optional [bool ]=None ,silent :Optional [bool ]=None ,url :Optional [str ]=None ,start_param :Optional [str ]=None ,theme_params :"raw.base.DataJSON"=None ,reply_to_msg_id :Optional [int ]=None ,top_msg_id :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .peer =peer 
        self .bot =bot 
        self .platform =platform 
        self .from_bot_menu =from_bot_menu 
        self .silent =silent 
        self .url =url 
        self .start_param =start_param 
        self .theme_params =theme_params 
        self .reply_to_msg_id =reply_to_msg_id 
        self .top_msg_id =top_msg_id 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"RequestWebView":

        flags =Int .read (b )

        from_bot_menu =True if flags &(1 <<4 )else False 
        silent =True if flags &(1 <<5 )else False 
        peer =TLObject .read (b )

        bot =TLObject .read (b )

        url =String .read (b )if flags &(1 <<1 )else None 
        start_param =String .read (b )if flags &(1 <<3 )else None 
        theme_params =TLObject .read (b )if flags &(1 <<2 )else None 

        platform =String .read (b )

        reply_to_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<9 )else None 
        send_as =TLObject .read (b )if flags &(1 <<13 )else None 

        return RequestWebView (peer =peer ,bot =bot ,platform =platform ,from_bot_menu =from_bot_menu ,silent =silent ,url =url ,start_param =start_param ,theme_params =theme_params ,reply_to_msg_id =reply_to_msg_id ,top_msg_id =top_msg_id ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<4 )if self .from_bot_menu else 0 
        flags |=(1 <<5 )if self .silent else 0 
        flags |=(1 <<1 )if self .url is not None else 0 
        flags |=(1 <<3 )if self .start_param is not None else 0 
        flags |=(1 <<2 )if self .theme_params is not None else 0 
        flags |=(1 <<0 )if self .reply_to_msg_id is not None else 0 
        flags |=(1 <<9 )if self .top_msg_id is not None else 0 
        flags |=(1 <<13 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (self .bot .write ())

        if self .url is not None :
            b .write (String (self .url ))

        if self .start_param is not None :
            b .write (String (self .start_param ))

        if self .theme_params is not None :
            b .write (self .theme_params .write ())

        b .write (String (self .platform ))

        if self .reply_to_msg_id is not None :
            b .write (Int (self .reply_to_msg_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
