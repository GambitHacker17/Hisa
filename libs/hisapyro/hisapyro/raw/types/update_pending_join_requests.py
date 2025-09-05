
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePendingJoinRequests (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","requests_pending","recent_requesters"]

    ID =0x7063c3db 
    QUALNAME ="types.UpdatePendingJoinRequests"

    def __init__ (self ,*,peer :"raw.base.Peer",requests_pending :int ,recent_requesters :List [int ])->None :
        self .peer =peer 
        self .requests_pending =requests_pending 
        self .recent_requesters =recent_requesters 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePendingJoinRequests":

        peer =TLObject .read (b )

        requests_pending =Int .read (b )

        recent_requesters =TLObject .read (b ,Long )

        return UpdatePendingJoinRequests (peer =peer ,requests_pending =requests_pending ,recent_requesters =recent_requesters )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .requests_pending ))

        b .write (Vector (self .recent_requesters ,Long ))

        return b .getvalue ()
