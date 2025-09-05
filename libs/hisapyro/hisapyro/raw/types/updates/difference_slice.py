
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class DifferenceSlice (TLObject ):
    """"""

    __slots__ :List [str ]=["new_messages","new_encrypted_messages","other_updates","chats","users","intermediate_state"]

    ID =0xa8fb1981 
    QUALNAME ="types.updates.DifferenceSlice"

    def __init__ (self ,*,new_messages :List ["raw.base.Message"],new_encrypted_messages :List ["raw.base.EncryptedMessage"],other_updates :List ["raw.base.Update"],chats :List ["raw.base.Chat"],users :List ["raw.base.User"],intermediate_state :"raw.base.updates.State")->None :
        self .new_messages =new_messages 
        self .new_encrypted_messages =new_encrypted_messages 
        self .other_updates =other_updates 
        self .chats =chats 
        self .users =users 
        self .intermediate_state =intermediate_state 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"DifferenceSlice":

        new_messages =TLObject .read (b )

        new_encrypted_messages =TLObject .read (b )

        other_updates =TLObject .read (b )

        chats =TLObject .read (b )

        users =TLObject .read (b )

        intermediate_state =TLObject .read (b )

        return DifferenceSlice (new_messages =new_messages ,new_encrypted_messages =new_encrypted_messages ,other_updates =other_updates ,chats =chats ,users =users ,intermediate_state =intermediate_state )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Vector (self .new_messages ))

        b .write (Vector (self .new_encrypted_messages ))

        b .write (Vector (self .other_updates ))

        b .write (Vector (self .chats ))

        b .write (Vector (self .users ))

        b .write (self .intermediate_state .write ())

        return b .getvalue ()
