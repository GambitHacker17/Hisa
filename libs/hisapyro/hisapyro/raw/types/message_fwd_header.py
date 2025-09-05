
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageFwdHeader (TLObject ):
    """"""

    __slots__ :List [str ]=["date","imported","from_id","from_name","channel_post","post_author","saved_from_peer","saved_from_msg_id","psa_type"]

    ID =0x5f777dce 
    QUALNAME ="types.MessageFwdHeader"

    def __init__ (self ,*,date :int ,imported :Optional [bool ]=None ,from_id :"raw.base.Peer"=None ,from_name :Optional [str ]=None ,channel_post :Optional [int ]=None ,post_author :Optional [str ]=None ,saved_from_peer :"raw.base.Peer"=None ,saved_from_msg_id :Optional [int ]=None ,psa_type :Optional [str ]=None )->None :
        self .date =date 
        self .imported =imported 
        self .from_id =from_id 
        self .from_name =from_name 
        self .channel_post =channel_post 
        self .post_author =post_author 
        self .saved_from_peer =saved_from_peer 
        self .saved_from_msg_id =saved_from_msg_id 
        self .psa_type =psa_type 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageFwdHeader":

        flags =Int .read (b )

        imported =True if flags &(1 <<7 )else False 
        from_id =TLObject .read (b )if flags &(1 <<0 )else None 

        from_name =String .read (b )if flags &(1 <<5 )else None 
        date =Int .read (b )

        channel_post =Int .read (b )if flags &(1 <<2 )else None 
        post_author =String .read (b )if flags &(1 <<3 )else None 
        saved_from_peer =TLObject .read (b )if flags &(1 <<4 )else None 

        saved_from_msg_id =Int .read (b )if flags &(1 <<4 )else None 
        psa_type =String .read (b )if flags &(1 <<6 )else None 
        return MessageFwdHeader (date =date ,imported =imported ,from_id =from_id ,from_name =from_name ,channel_post =channel_post ,post_author =post_author ,saved_from_peer =saved_from_peer ,saved_from_msg_id =saved_from_msg_id ,psa_type =psa_type )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<7 )if self .imported else 0 
        flags |=(1 <<0 )if self .from_id is not None else 0 
        flags |=(1 <<5 )if self .from_name is not None else 0 
        flags |=(1 <<2 )if self .channel_post is not None else 0 
        flags |=(1 <<3 )if self .post_author is not None else 0 
        flags |=(1 <<4 )if self .saved_from_peer is not None else 0 
        flags |=(1 <<4 )if self .saved_from_msg_id is not None else 0 
        flags |=(1 <<6 )if self .psa_type is not None else 0 
        b .write (Int (flags ))

        if self .from_id is not None :
            b .write (self .from_id .write ())

        if self .from_name is not None :
            b .write (String (self .from_name ))

        b .write (Int (self .date ))

        if self .channel_post is not None :
            b .write (Int (self .channel_post ))

        if self .post_author is not None :
            b .write (String (self .post_author ))

        if self .saved_from_peer is not None :
            b .write (self .saved_from_peer .write ())

        if self .saved_from_msg_id is not None :
            b .write (Int (self .saved_from_msg_id ))

        if self .psa_type is not None :
            b .write (String (self .psa_type ))

        return b .getvalue ()
