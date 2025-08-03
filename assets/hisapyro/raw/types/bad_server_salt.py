
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BadServerSalt (TLObject ):
    """"""

    __slots__ :List [str ]=["bad_msg_id","bad_msg_seqno","error_code","new_server_salt"]

    ID =0xedab447b 
    QUALNAME ="types.BadServerSalt"

    def __init__ (self ,*,bad_msg_id :int ,bad_msg_seqno :int ,error_code :int ,new_server_salt :int )->None :
        self .bad_msg_id =bad_msg_id 
        self .bad_msg_seqno =bad_msg_seqno 
        self .error_code =error_code 
        self .new_server_salt =new_server_salt 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BadServerSalt":

        bad_msg_id =Long .read (b )

        bad_msg_seqno =Int .read (b )

        error_code =Int .read (b )

        new_server_salt =Long .read (b )

        return BadServerSalt (bad_msg_id =bad_msg_id ,bad_msg_seqno =bad_msg_seqno ,error_code =error_code ,new_server_salt =new_server_salt )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .bad_msg_id ))

        b .write (Int (self .bad_msg_seqno ))

        b .write (Int (self .error_code ))

        b .write (Long (self .new_server_salt ))

        return b .getvalue ()
