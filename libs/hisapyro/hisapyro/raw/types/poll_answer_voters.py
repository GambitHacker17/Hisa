
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PollAnswerVoters (TLObject ):
    """"""

    __slots__ :List [str ]=["option","voters","chosen","correct"]

    ID =0x3b6ddad2 
    QUALNAME ="types.PollAnswerVoters"

    def __init__ (self ,*,option :bytes ,voters :int ,chosen :Optional [bool ]=None ,correct :Optional [bool ]=None )->None :
        self .option =option 
        self .voters =voters 
        self .chosen =chosen 
        self .correct =correct 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PollAnswerVoters":

        flags =Int .read (b )

        chosen =True if flags &(1 <<0 )else False 
        correct =True if flags &(1 <<1 )else False 
        option =Bytes .read (b )

        voters =Int .read (b )

        return PollAnswerVoters (option =option ,voters =voters ,chosen =chosen ,correct =correct )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .chosen else 0 
        flags |=(1 <<1 )if self .correct else 0 
        b .write (Int (flags ))

        b .write (Bytes (self .option ))

        b .write (Int (self .voters ))

        return b .getvalue ()
