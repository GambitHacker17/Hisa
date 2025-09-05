
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AcceptAuthorization (TLObject ):
    """"""

    __slots__ :List [str ]=["bot_id","scope","public_key","value_hashes","credentials"]

    ID =0xf3ed4c73 
    QUALNAME ="functions.account.AcceptAuthorization"

    def __init__ (self ,*,bot_id :int ,scope :str ,public_key :str ,value_hashes :List ["raw.base.SecureValueHash"],credentials :"raw.base.SecureCredentialsEncrypted")->None :
        self .bot_id =bot_id 
        self .scope =scope 
        self .public_key =public_key 
        self .value_hashes =value_hashes 
        self .credentials =credentials 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AcceptAuthorization":

        bot_id =Long .read (b )

        scope =String .read (b )

        public_key =String .read (b )

        value_hashes =TLObject .read (b )

        credentials =TLObject .read (b )

        return AcceptAuthorization (bot_id =bot_id ,scope =scope ,public_key =public_key ,value_hashes =value_hashes ,credentials =credentials )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .bot_id ))

        b .write (String (self .scope ))

        b .write (String (self .public_key ))

        b .write (Vector (self .value_hashes ))

        b .write (self .credentials .write ())

        return b .getvalue ()
