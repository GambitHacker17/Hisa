
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaInvoice (TLObject ):
    """"""

    __slots__ :List [str ]=["title","description","invoice","payload","provider","provider_data","photo","start_param","extended_media"]

    ID =0x8eb5a6d5 
    QUALNAME ="types.InputMediaInvoice"

    def __init__ (self ,*,title :str ,description :str ,invoice :"raw.base.Invoice",payload :bytes ,provider :str ,provider_data :"raw.base.DataJSON",photo :"raw.base.InputWebDocument"=None ,start_param :Optional [str ]=None ,extended_media :"raw.base.InputMedia"=None )->None :
        self .title =title 
        self .description =description 
        self .invoice =invoice 
        self .payload =payload 
        self .provider =provider 
        self .provider_data =provider_data 
        self .photo =photo 
        self .start_param =start_param 
        self .extended_media =extended_media 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaInvoice":

        flags =Int .read (b )

        title =String .read (b )

        description =String .read (b )

        photo =TLObject .read (b )if flags &(1 <<0 )else None 

        invoice =TLObject .read (b )

        payload =Bytes .read (b )

        provider =String .read (b )

        provider_data =TLObject .read (b )

        start_param =String .read (b )if flags &(1 <<1 )else None 
        extended_media =TLObject .read (b )if flags &(1 <<2 )else None 

        return InputMediaInvoice (title =title ,description =description ,invoice =invoice ,payload =payload ,provider =provider ,provider_data =provider_data ,photo =photo ,start_param =start_param ,extended_media =extended_media )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .photo is not None else 0 
        flags |=(1 <<1 )if self .start_param is not None else 0 
        flags |=(1 <<2 )if self .extended_media is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .title ))

        b .write (String (self .description ))

        if self .photo is not None :
            b .write (self .photo .write ())

        b .write (self .invoice .write ())

        b .write (Bytes (self .payload ))

        b .write (String (self .provider ))

        b .write (self .provider_data .write ())

        if self .start_param is not None :
            b .write (String (self .start_param ))

        if self .extended_media is not None :
            b .write (self .extended_media .write ())

        return b .getvalue ()
