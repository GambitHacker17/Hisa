
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SendEncryptedFile (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","random_id","data","file","silent"]

    ID =0x5559481d 
    QUALNAME ="functions.messages.SendEncryptedFile"

    def __init__ (self ,*,peer :"raw.base.InputEncryptedChat",random_id :int ,data :bytes ,file :"raw.base.InputEncryptedFile",silent :Optional [bool ]=None )->None :
        self .peer =peer 
        self .random_id =random_id 
        self .data =data 
        self .file =file 
        self .silent =silent 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SendEncryptedFile":

        flags =Int .read (b )

        silent =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        random_id =Long .read (b )

        data =Bytes .read (b )

        file =TLObject .read (b )

        return SendEncryptedFile (peer =peer ,random_id =random_id ,data =data ,file =file ,silent =silent )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .silent else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Long (self .random_id ))

        b .write (Bytes (self .data ))

        b .write (self .file .write ())

        return b .getvalue ()
