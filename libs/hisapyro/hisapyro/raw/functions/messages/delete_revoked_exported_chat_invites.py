
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DeleteRevokedExportedChatInvites (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","admin_id"]

    ID =0x56987bd5 
    QUALNAME ="functions.messages.DeleteRevokedExportedChatInvites"

    def __init__ (self ,*,peer :"raw.base.InputPeer",admin_id :"raw.base.InputUser")->None :
        self .peer =peer 
        self .admin_id =admin_id 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DeleteRevokedExportedChatInvites":

        peer =TLObject .read (b )

        admin_id =TLObject .read (b )

        return DeleteRevokedExportedChatInvites (peer =peer ,admin_id =admin_id )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (self .admin_id .write ())

        return b .getvalue ()
