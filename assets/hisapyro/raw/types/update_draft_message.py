
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateDraftMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","draft","top_msg_id"]

    ID =0x1b49ec6d 
    QUALNAME ="types.UpdateDraftMessage"

    def __init__ (self ,*,peer :"raw.base.Peer",draft :"raw.base.DraftMessage",top_msg_id :Optional [int ]=None )->None :
        self .peer =peer 
        self .draft =draft 
        self .top_msg_id =top_msg_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateDraftMessage":

        flags =Int .read (b )

        peer =TLObject .read (b )

        top_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        draft =TLObject .read (b )

        return UpdateDraftMessage (peer =peer ,draft =draft ,top_msg_id =top_msg_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .top_msg_id is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (self .draft .write ())

        return b .getvalue ()
