
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UrlAuthResultRequest (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","domain","request_write_access"]

    ID =0x92d33a0e 
    QUALNAME ="types.UrlAuthResultRequest"

    def __init__ (self ,*,bot :"raw.base.User",domain :str ,request_write_access :Optional [bool ]=None )->None :
        self .bot =bot 
        self .domain =domain 
        self .request_write_access =request_write_access 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UrlAuthResultRequest":

        flags =Int .read (b )

        request_write_access =True if flags &(1 <<0 )else False 
        bot =TLObject .read (b )

        domain =String .read (b )

        return UrlAuthResultRequest (bot =bot ,domain =domain ,request_write_access =request_write_access )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .request_write_access else 0 
        b .write (Int (flags ))

        b .write (self .bot .write ())

        b .write (String (self .domain ))

        return b .getvalue ()
