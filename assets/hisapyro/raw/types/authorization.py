
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Authorization (TLObject ):
    """"""

    __slots__ :List [str ]=["hash","device_model","platform","system_version","api_id","app_name","app_version","date_created","date_active","ip","country","region","current","official_app","password_pending","encrypted_requests_disabled","call_requests_disabled"]

    ID =0xad01d61d 
    QUALNAME ="types.Authorization"

    def __init__ (self ,*,hash :int ,device_model :str ,platform :str ,system_version :str ,api_id :int ,app_name :str ,app_version :str ,date_created :int ,date_active :int ,ip :str ,country :str ,region :str ,current :Optional [bool ]=None ,official_app :Optional [bool ]=None ,password_pending :Optional [bool ]=None ,encrypted_requests_disabled :Optional [bool ]=None ,call_requests_disabled :Optional [bool ]=None )->None :
        self .hash =hash 
        self .device_model =device_model 
        self .platform =platform 
        self .system_version =system_version 
        self .api_id =api_id 
        self .app_name =app_name 
        self .app_version =app_version 
        self .date_created =date_created 
        self .date_active =date_active 
        self .ip =ip 
        self .country =country 
        self .region =region 
        self .current =current 
        self .official_app =official_app 
        self .password_pending =password_pending 
        self .encrypted_requests_disabled =encrypted_requests_disabled 
        self .call_requests_disabled =call_requests_disabled 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Authorization":

        flags =Int .read (b )

        current =True if flags &(1 <<0 )else False 
        official_app =True if flags &(1 <<1 )else False 
        password_pending =True if flags &(1 <<2 )else False 
        encrypted_requests_disabled =True if flags &(1 <<3 )else False 
        call_requests_disabled =True if flags &(1 <<4 )else False 
        hash =Long .read (b )

        device_model =String .read (b )

        platform =String .read (b )

        system_version =String .read (b )

        api_id =Int .read (b )

        app_name =String .read (b )

        app_version =String .read (b )

        date_created =Int .read (b )

        date_active =Int .read (b )

        ip =String .read (b )

        country =String .read (b )

        region =String .read (b )

        return Authorization (hash =hash ,device_model =device_model ,platform =platform ,system_version =system_version ,api_id =api_id ,app_name =app_name ,app_version =app_version ,date_created =date_created ,date_active =date_active ,ip =ip ,country =country ,region =region ,current =current ,official_app =official_app ,password_pending =password_pending ,encrypted_requests_disabled =encrypted_requests_disabled ,call_requests_disabled =call_requests_disabled )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .current else 0 
        flags |=(1 <<1 )if self .official_app else 0 
        flags |=(1 <<2 )if self .password_pending else 0 
        flags |=(1 <<3 )if self .encrypted_requests_disabled else 0 
        flags |=(1 <<4 )if self .call_requests_disabled else 0 
        b .write (Int (flags ))

        b .write (Long (self .hash ))

        b .write (String (self .device_model ))

        b .write (String (self .platform ))

        b .write (String (self .system_version ))

        b .write (Int (self .api_id ))

        b .write (String (self .app_name ))

        b .write (String (self .app_version ))

        b .write (Int (self .date_created ))

        b .write (Int (self .date_active ))

        b .write (String (self .ip ))

        b .write (String (self .country ))

        b .write (String (self .region ))

        return b .getvalue ()
