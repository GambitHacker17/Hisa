
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotPrecheckoutQuery (TLObject ):
    """"""

    __slots__ :List [str ]=["query_id","user_id","payload","currency","total_amount","info","shipping_option_id"]

    ID =0x8caa9a96 
    QUALNAME ="types.UpdateBotPrecheckoutQuery"

    def __init__ (self ,*,query_id :int ,user_id :int ,payload :bytes ,currency :str ,total_amount :int ,info :"raw.base.PaymentRequestedInfo"=None ,shipping_option_id :Optional [str ]=None )->None :
        self .query_id =query_id 
        self .user_id =user_id 
        self .payload =payload 
        self .currency =currency 
        self .total_amount =total_amount 
        self .info =info 
        self .shipping_option_id =shipping_option_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotPrecheckoutQuery":

        flags =Int .read (b )

        query_id =Long .read (b )

        user_id =Long .read (b )

        payload =Bytes .read (b )

        info =TLObject .read (b )if flags &(1 <<0 )else None 

        shipping_option_id =String .read (b )if flags &(1 <<1 )else None 
        currency =String .read (b )

        total_amount =Long .read (b )

        return UpdateBotPrecheckoutQuery (query_id =query_id ,user_id =user_id ,payload =payload ,currency =currency ,total_amount =total_amount ,info =info ,shipping_option_id =shipping_option_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .info is not None else 0 
        flags |=(1 <<1 )if self .shipping_option_id is not None else 0 
        b .write (Int (flags ))

        b .write (Long (self .query_id ))

        b .write (Long (self .user_id ))

        b .write (Bytes (self .payload ))

        if self .info is not None :
            b .write (self .info .write ())

        if self .shipping_option_id is not None :
            b .write (String (self .shipping_option_id ))

        b .write (String (self .currency ))

        b .write (Long (self .total_amount ))

        return b .getvalue ()
