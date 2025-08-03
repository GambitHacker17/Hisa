
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class Poll (TLObject ):
    """"""

    __slots__ :List [str ]=["id","question","answers","closed","public_voters","multiple_choice","quiz","close_period","close_date"]

    ID =0x86e18161 
    QUALNAME ="types.Poll"

    def __init__ (self ,*,id :int ,question :str ,answers :List ["raw.base.PollAnswer"],closed :Optional [bool ]=None ,public_voters :Optional [bool ]=None ,multiple_choice :Optional [bool ]=None ,quiz :Optional [bool ]=None ,close_period :Optional [int ]=None ,close_date :Optional [int ]=None )->None :
        self .id =id 
        self .question =question 
        self .answers =answers 
        self .closed =closed 
        self .public_voters =public_voters 
        self .multiple_choice =multiple_choice 
        self .quiz =quiz 
        self .close_period =close_period 
        self .close_date =close_date 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"Poll":

        id =Long .read (b )

        flags =Int .read (b )

        closed =True if flags &(1 <<0 )else False 
        public_voters =True if flags &(1 <<1 )else False 
        multiple_choice =True if flags &(1 <<2 )else False 
        quiz =True if flags &(1 <<3 )else False 
        question =String .read (b )

        answers =TLObject .read (b )

        close_period =Int .read (b )if flags &(1 <<4 )else None 
        close_date =Int .read (b )if flags &(1 <<5 )else None 
        return Poll (id =id ,question =question ,answers =answers ,closed =closed ,public_voters =public_voters ,multiple_choice =multiple_choice ,quiz =quiz ,close_period =close_period ,close_date =close_date )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (Long (self .id ))
        flags =0 
        flags |=(1 <<0 )if self .closed else 0 
        flags |=(1 <<1 )if self .public_voters else 0 
        flags |=(1 <<2 )if self .multiple_choice else 0 
        flags |=(1 <<3 )if self .quiz else 0 
        flags |=(1 <<4 )if self .close_period is not None else 0 
        flags |=(1 <<5 )if self .close_date is not None else 0 
        b .write (Int (flags ))

        b .write (String (self .question ))

        b .write (Vector (self .answers ))

        if self .close_period is not None :
            b .write (Int (self .close_period ))

        if self .close_date is not None :
            b .write (Int (self .close_date ))

        return b .getvalue ()
