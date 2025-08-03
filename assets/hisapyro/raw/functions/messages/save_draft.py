
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SaveDraft (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","message","no_webpage","reply_to_msg_id","top_msg_id","entities"]

    ID =0xb4331e3f 
    QUALNAME ="functions.messages.SaveDraft"

    def __init__ (self ,*,peer :"raw.base.InputPeer",message :str ,no_webpage :Optional [bool ]=None ,reply_to_msg_id :Optional [int ]=None ,top_msg_id :Optional [int ]=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .peer =peer 
        self .message =message 
        self .no_webpage =no_webpage 
        self .reply_to_msg_id =reply_to_msg_id 
        self .top_msg_id =top_msg_id 
        self .entities =entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SaveDraft":

        flags =Int .read (b )

        no_webpage =True if flags &(1 <<1 )else False 
        reply_to_msg_id =Int .read (b )if flags &(1 <<0 )else None 
        top_msg_id =Int .read (b )if flags &(1 <<2 )else None 
        peer =TLObject .read (b )

        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<3 )else []

        return SaveDraft (peer =peer ,message =message ,no_webpage =no_webpage ,reply_to_msg_id =reply_to_msg_id ,top_msg_id =top_msg_id ,entities =entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<1 )if self .no_webpage else 0 
        flags |=(1 <<0 )if self .reply_to_msg_id is not None else 0 
        flags |=(1 <<2 )if self .top_msg_id is not None else 0 
        flags |=(1 <<3 )if self .entities else 0 
        b .write (Int (flags ))

        if self .reply_to_msg_id is not None :
            b .write (Int (self .reply_to_msg_id ))

        if self .top_msg_id is not None :
            b .write (Int (self .top_msg_id ))

        b .write (self .peer .write ())

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        return b .getvalue ()
