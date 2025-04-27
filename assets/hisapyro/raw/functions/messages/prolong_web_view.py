
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class ProlongWebView (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","bot","query_id","silent","reply_to_msg_id","top_msg_id","send_as"]

    ID =0x7ff34309 
    QUALNAME ="functions.messages.ProlongWebView"

    def __init__ (self ,*,peer :"raw.base.InputPeer",bot :"raw.base.InputUser",query_id :int ,silent :Optional [bool ]=None ,reply_to_msg_id :Optional [int ]=None ,top_msg_id :Optional [int ]=None ,send_as :"raw.base.InputPeer"=None )->None :
        self .peer =peer 
        self .bot =bot 
        self .query_id =query_id 
        self .silent =silent 
        self .reply_to_msg_id =reply_to_msg_id 
        self .top_msg_id =top_msg_id 
        self .send_as =send_as 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"ProlongWebView":

        flags =Int .read (b )

        silent =True if flags &(1 <<5 )else False 
        peer =TLObject .read (b )

        bot =TLObject .read (b )

        query_id =Long .read (b )

        reply_to_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<9 )else None 
        send_as =TLObject .read (b )if flags &(1 <<13 )else None 

        return ProlongWebView (peer =peer ,bot =bot ,query_id =query_id ,silent =silent ,reply_to_msg_id =reply_to_msg_id ,top_msg_id =top_msg_id ,send_as =send_as )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .silent else 0 
        flags |=(1 <<0 )if self .reply_to_msg_id is not None else 0 
        flags |=(1 <<9 )if self .top_msg_id is not None else 0 
        flags |=(1 <<13 )if self .send_as is not None else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (self .bot .write ())

        b .write (Long (self .query_id ))

        if self .reply_to_msg_id is not None :
            b .write (Int (self .reply_to_msg_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        if self .send_as is not None :
            b .write (self .send_as .write ())

        return b .getvalue ()
