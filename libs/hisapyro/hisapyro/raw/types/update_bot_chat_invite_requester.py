
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdateBotChatInviteRequester (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","date","user_id","about","invite","qts"]

    ID =0x11dfa986 
    QUALNAME ="types.UpdateBotChatInviteRequester"

    def __init__ (self ,*,peer :"raw.base.Peer",date :int ,user_id :int ,about :str ,invite :"raw.base.ExportedChatInvite",qts :int )->None :
        self .peer =peer 
        self .date =date 
        self .user_id =user_id 
        self .about =about 
        self .invite =invite 
        self .qts =qts 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdateBotChatInviteRequester":

        peer =TLObject .read (b )

        date =Int .read (b )

        user_id =Long .read (b )

        about =String .read (b )

        invite =TLObject .read (b )

        qts =Int .read (b )

        return UpdateBotChatInviteRequester (peer =peer ,date =date ,user_id =user_id ,about =about ,invite =invite ,qts =qts )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Int (self .date ))

        b .write (Long (self .user_id ))

        b .write (String (self .about ))

        b .write (self .invite .write ())

        b .write (Int (self .qts ))

        return b .getvalue ()
