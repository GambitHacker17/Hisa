
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AddContact (TLObject ):
    """"""

    __slots__ :List [str ]=["id","first_name","last_name","phone","add_phone_privacy_exception"]

    ID =0xe8f463d0 
    QUALNAME ="functions.contacts.AddContact"

    def __init__ (self ,*,id :"raw.base.InputUser",first_name :str ,last_name :str ,phone :str ,add_phone_privacy_exception :Optional [bool ]=None )->None :
        self .id =id 
        self .first_name =first_name 
        self .last_name =last_name 
        self .phone =phone 
        self .add_phone_privacy_exception =add_phone_privacy_exception 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AddContact":

        flags =Int .read (b )

        add_phone_privacy_exception =True if flags &(1 <<0 )else False 
        id =TLObject .read (b )

        first_name =String .read (b )

        last_name =String .read (b )

        phone =String .read (b )

        return AddContact (id =id ,first_name =first_name ,last_name =last_name ,phone =phone ,add_phone_privacy_exception =add_phone_privacy_exception )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .add_phone_privacy_exception else 0 
        b .write (Int (flags ))

        b .write (self .id .write ())

        b .write (String (self .first_name ))

        b .write (String (self .last_name ))

        b .write (String (self .phone ))

        return b .getvalue ()
