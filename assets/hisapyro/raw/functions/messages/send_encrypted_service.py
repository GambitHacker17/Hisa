
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendEncryptedService (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","random_id","data"]

    ID =0x32d439a4 
    QUALNAME ="functions.messages.SendEncryptedService"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat",random_id :int ,data :bytes )->None :
        self .peer =peer 
        self .random_id =random_id 
        self .data =data 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendEncryptedService":

        peer =TLObject .read (b )

        random_id =Long .read (b )

        data =Bytes .read (b )

        return SendEncryptedService (peer =peer ,random_id =random_id ,data =data )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .peer .write ())

        b .write (Long (self .random_id ))

        b .write (Bytes (self .data ))

        return b .getvalue ()
