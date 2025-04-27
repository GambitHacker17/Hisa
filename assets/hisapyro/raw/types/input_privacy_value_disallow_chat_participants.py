
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPrivacyValueDisallowChatParticipants (TLObject ):
    """"""

    __slots__ :List [str ]=["chats"]

    ID =0xe94f0f86 
    QUALNAME ="types.InputPrivacyValueDisallowChatParticipants"

    def __init__ (self ,*,chats :List [int ])->None :
        self .chats =chats 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPrivacyValueDisallowChatParticipants":

        chats =TLObject .read (b ,Long )

        return InputPrivacyValueDisallowChatParticipants (chats =chats )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .chats ,Long ))

        return b .getvalue ()
