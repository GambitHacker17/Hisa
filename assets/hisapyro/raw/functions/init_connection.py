
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InitConnection (TLObject ):
    """"""

    __slots__ :List [str ]=["api_id","device_model","system_version","app_version","system_lang_code","lang_pack","lang_code","query","proxy","params"]

    ID =0xc1cd5ea9 
    QUALNAME ="functions.InitConnection"

    def __init__ (self ,*,api_id :int ,device_model :str ,system_version :str ,app_version :str ,system_lang_code :str ,lang_pack :str ,lang_code :str ,query :TLObject ,proxy :"raw.base.InputClientProxy"=None ,params :"raw.base.JSONValue"=None )->None :
        self .api_id =api_id 
        self .device_model =device_model 
        self .system_version =system_version 
        self .app_version =app_version 
        self .system_lang_code =system_lang_code 
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .query =query 
        self .proxy =proxy 
        self .params =params 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InitConnection":

        flags =Int .read (b )

        api_id =Int .read (b )

        device_model =String .read (b )

        system_version =String .read (b )

        app_version =String .read (b )

        system_lang_code =String .read (b )

        lang_pack =String .read (b )

        lang_code =String .read (b )

        proxy =TLObject .read (b )if flags &(1 <<0 )else None 

        params =TLObject .read (b )if flags &(1 <<1 )else None 

        query =TLObject .read (b )

        return InitConnection (api_id =api_id ,device_model =device_model ,system_version =system_version ,app_version =app_version ,system_lang_code =system_lang_code ,lang_pack =lang_pack ,lang_code =lang_code ,query =query ,proxy =proxy ,params =params )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .proxy is not None else 0 
        flags |=(1 <<1 )if self .params is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .api_id ))

        b .write (String (self .device_model ))

        b .write (String (self .system_version ))

        b .write (String (self .app_version ))

        b .write (String (self .system_lang_code ))

        b .write (String (self .lang_pack ))

        b .write (String (self .lang_code ))

        if self .proxy is not None :
            b .write (self .proxy .write ())

        if self .params is not None :
            b .write (self .params .write ())

        b .write (self .query .write ())

        return b .getvalue ()
