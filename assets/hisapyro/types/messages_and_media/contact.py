
import hisapyro 
from hisapyro import raw 
from ..object import Object 

class Contact (Object ):
    """"""

    def __init__ (
    self ,
    *,
    client :"hisapyro.Client"=None ,
    phone_number :str ,
    first_name :str ,
    last_name :str =None ,
    user_id :int =None ,
    vcard :str =None 
    ):
        super ().__init__ (client )

        self .phone_number =phone_number 
        self .first_name =first_name 
        self .last_name =last_name 
        self .user_id =user_id 
        self .vcard =vcard 

    @staticmethod 
    def _parse (client :"hisapyro.Client",contact :"raw.types.MessageMediaContact")->"Contact":
        return Contact (
        phone_number =contact .phone_number ,
        first_name =contact .first_name ,
        last_name =contact .last_name or None ,
        vcard =contact .vcard or None ,
        user_id =contact .user_id or None ,
        client =client 
        )
