
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PremiumGiftOption (TLObject ):
    """"""

    __slots__ :List [str ]=["months","currency","amount","bot_url","store_product"]

    ID =0x74c34319 
    QUALNAME ="types.PremiumGiftOption"

    def __init__ (self ,*,months :int ,currency :str ,amount :int ,bot_url :str ,store_product :Optional [str ]=None )->None :
        self .months =months 
        self .currency =currency 
        self .amount =amount 
        self .bot_url =bot_url 
        self .store_product =store_product 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PremiumGiftOption":

        flags =Int .read (b )

        months =Int .read (b )

        currency =String .read (b )

        amount =Long .read (b )

        bot_url =String .read (b )

        store_product =String .read (b )if flags &(1 <<0 )else None 
        return PremiumGiftOption (months =months ,currency =currency ,amount =amount ,bot_url =bot_url ,store_product =store_product )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .store_product is not None else 0 
        b .write (Int (flags ))

        b .write (Int (self .months ))

        b .write (String (self .currency ))

        b .write (Long (self .amount ))

        b .write (String (self .bot_url ))

        if self .store_product is not None :
            b .write (String (self .store_product ))

        return b .getvalue ()
