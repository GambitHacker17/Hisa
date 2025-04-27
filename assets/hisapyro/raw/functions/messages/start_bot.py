
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class StartBot (TLObject ):
    """"""

    __slots__ :List [str ]=["bot","peer","random_id","start_param"]

    ID =0xe6df7378 
    QUALNAME ="functions.messages.StartBot"

    def __init__ (self ,*,bot :"raw.base.InputUser",peer :"raw.base.InputPeer",random_id :int ,start_param :str )->None :
        self .bot =bot 
        self .peer =peer 
        self .random_id =random_id 
        self .start_param =start_param 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"StartBot":

        bot =TLObject .read (b )

        peer =TLObject .read (b )

        random_id =Long .read (b )

        start_param =String .read (b )

        return StartBot (bot =bot ,peer =peer ,random_id =random_id ,start_param =start_param )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .bot .write ())

        b .write (self .peer .write ())

        b .write (Long (self .random_id ))

        b .write (String (self .start_param ))

        return b .getvalue ()
