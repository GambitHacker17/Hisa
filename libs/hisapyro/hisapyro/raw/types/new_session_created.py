
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class NewSessionCreated (TLObject ):
    """"""

    __slots__ :List [str ]=["first_msg_id","unique_id","server_salt"]

    ID =0x9ec20908 
    QUALNAME ="types.NewSessionCreated"

    def __init__ (self ,*,first_msg_id :int ,unique_id :int ,server_salt :int )->None :
        self .first_msg_id =first_msg_id 
        self .unique_id =unique_id 
        self .server_salt =server_salt 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"NewSessionCreated":

        first_msg_id =Long .read (b )

        unique_id =Long .read (b )

        server_salt =Long .read (b )

        return NewSessionCreated (first_msg_id =first_msg_id ,unique_id =unique_id ,server_salt =server_salt )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .first_msg_id ))

        b .write (Long (self .unique_id ))

        b .write (Long (self .server_salt ))

        return b .getvalue ()
