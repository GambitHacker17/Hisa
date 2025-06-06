
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SetGameScore (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","user_id","score","edit_message","force"]

    ID =0x8ef8ecc0 
    QUALNAME ="functions.messages.SetGameScore"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,user_id :"raw.base.InputUser",score :int ,edit_message :Optional [bool ]=None ,force :Optional [bool ]=None )->None :
        self .peer =peer 
        self .id =id 
        self .user_id =user_id 
        self .score =score 
        self .edit_message =edit_message 
        self .force =force 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SetGameScore":

        flags =Int .read (b )

        edit_message =True if flags &(1 <<0 )else False 
        force =True if flags &(1 <<1 )else False 
        peer =TLObject .read (b )

        id =Int .read (b )

        user_id =TLObject .read (b )

        score =Int .read (b )

        return SetGameScore (peer =peer ,id =id ,user_id =user_id ,score =score ,edit_message =edit_message ,force =force )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .edit_message else 0 
        flags |=(1 <<1 )if self .force else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        b .write (self .user_id .write ())

        b .write (Int (self .score ))

        return b .getvalue ()
