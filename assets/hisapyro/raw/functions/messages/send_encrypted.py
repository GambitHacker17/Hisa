
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendEncrypted (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","random_id","data","silent"]

    ID =0x44fa7a15 
    QUALNAME ="functions.messages.SendEncrypted"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat",random_id :int ,data :bytes ,silent :Optional [bool ]=None )->None :
        self .peer =peer 
        self .random_id =random_id 
        self .data =data 
        self .silent =silent 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendEncrypted":

        flags =Int .read (b )

        silent =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        random_id =Long .read (b )

        data =Bytes .read (b )

        return SendEncrypted (peer =peer ,random_id =random_id ,data =data ,silent =silent )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .silent else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Long (self .random_id ))

        b .write (Bytes (self .data ))

        return b .getvalue ()
