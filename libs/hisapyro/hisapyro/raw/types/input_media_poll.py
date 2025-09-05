
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputMediaPoll (TLObject ):
    """"""

    __slots__ :List [str ]=["poll","correct_answers","solution","solution_entities"]

    ID =0xf94e5f1 
    QUALNAME ="types.InputMediaPoll"

    def __init__ (self ,*,poll :"raw.base.Poll",correct_answers :Optional [List [bytes ]]=None ,solution :Optional [str ]=None ,solution_entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .poll =poll 
        self .correct_answers =correct_answers 
        self .solution =solution 
        self .solution_entities =solution_entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputMediaPoll":

        flags =Int .read (b )

        poll =TLObject .read (b )

        correct_answers =TLObject .read (b ,Bytes )if flags &(1 <<0 )else []

        solution =String .read (b )if flags &(1 <<1 )else None 
        solution_entities =TLObject .read (b )if flags &(1 <<1 )else []

        return InputMediaPoll (poll =poll ,correct_answers =correct_answers ,solution =solution ,solution_entities =solution_entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .correct_answers else 0 
        flags |=(1 <<1 )if self .solution is not None else 0 
        flags |=(1 <<1 )if self .solution_entities else 0 
        b .write (Int (flags ))

        b .write (self .poll .write ())

        if self .correct_answers is not None :
            b .write (Vector (self .correct_answers ,Bytes ))

        if self .solution is not None :
            b .write (String (self .solution ))

        if self .solution_entities is not None :
            b .write (Vector (self .solution_entities ))

        return b .getvalue ()
