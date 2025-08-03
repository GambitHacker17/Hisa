
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TermsOfService (TLObject ):
    """"""

    __slots__ :List [str ]=["id","text","entities","popup","min_age_confirm"]

    ID =0x780a0310 
    QUALNAME ="types.help.TermsOfService"

    def __init__ (self ,*,id :"raw.base.DataJSON",text :str ,entities :List ["raw.base.MessageEntity"],popup :Optional [bool ]=None ,min_age_confirm :Optional [int ]=None )->None :
        self .id =id 
        self .text =text 
        self .entities =entities 
        self .popup =popup 
        self .min_age_confirm =min_age_confirm 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TermsOfService":

        flags =Int .read (b )

        popup =True if flags &(1 <<0 )else False 
        id =TLObject .read (b )

        text =String .read (b )

        entities =TLObject .read (b )

        min_age_confirm =Int .read (b )if flags &(1 <<1 )else None 
        return TermsOfService (id =id ,text =text ,entities =entities ,popup =popup ,min_age_confirm =min_age_confirm )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .popup else 0 
        flags |=(1 <<1 )if self .min_age_confirm is not None else 0 
        b .write (Int (flags ))

        b .write (self .id .write ())

        b .write (String (self .text ))

        b .write (Vector (self .entities ))

        if self .min_age_confirm is not None :
            b .write (Int (self .min_age_confirm ))

        return b .getvalue ()
