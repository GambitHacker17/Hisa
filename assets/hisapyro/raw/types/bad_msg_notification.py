
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BadMsgNotification (TLObject ):
    """"""

    __slots__ :List [str ]=["bad_msg_id","bad_msg_seqno","error_code"]

    ID =0xa7eff811 
    QUALNAME ="types.BadMsgNotification"

    def __init__ (self ,*,bad_msg_id :int ,bad_msg_seqno :int ,error_code :int )->None :
        self .bad_msg_id =bad_msg_id 
        self .bad_msg_seqno =bad_msg_seqno 
        self .error_code =error_code 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BadMsgNotification":

        bad_msg_id =Long .read (b )

        bad_msg_seqno =Int .read (b )

        error_code =Int .read (b )

        return BadMsgNotification (bad_msg_id =bad_msg_id ,bad_msg_seqno =bad_msg_seqno ,error_code =error_code )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .bad_msg_id ))

        b .write (Int (self .bad_msg_seqno ))

        b .write (Int (self .error_code ))

        return b .getvalue ()
