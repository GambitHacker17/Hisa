
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class PollResults (TLObject ):
    """"""

    __slots__ :List [str ]=["min","results","total_voters","recent_voters","solution","solution_entities"]

    ID =0xdcb82ea3 
    QUALNAME ="types.PollResults"

    def __init__ (self ,*,min :Optional [bool ]=None ,results :Optional [List ["raw.base.PollAnswerVoters"]]=None ,total_voters :Optional [int ]=None ,recent_voters :Optional [List [int ]]=None ,solution :Optional [str ]=None ,solution_entities :Optional [List ["raw.base.MessageEntity"]]=None )->None :
        self .min =min 
        self .results =results 
        self .total_voters =total_voters 
        self .recent_voters =recent_voters 
        self .solution =solution 
        self .solution_entities =solution_entities 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"PollResults":

        flags =Int .read (b )

        min =True if flags &(1 <<0 )else False 
        results =TLObject .read (b )if flags &(1 <<1 )else []

        total_voters =Int .read (b )if flags &(1 <<2 )else None 
        recent_voters =TLObject .read (b ,Long )if flags &(1 <<3 )else []

        solution =String .read (b )if flags &(1 <<4 )else None 
        solution_entities =TLObject .read (b )if flags &(1 <<4 )else []

        return PollResults (min =min ,results =results ,total_voters =total_voters ,recent_voters =recent_voters ,solution =solution ,solution_entities =solution_entities )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .min else 0 
        flags |=(1 <<1 )if self .results else 0 
        flags |=(1 <<2 )if self .total_voters is not None else 0 
        flags |=(1 <<3 )if self .recent_voters else 0 
        flags |=(1 <<4 )if self .solution is not None else 0 
        flags |=(1 <<4 )if self .solution_entities else 0 
        b .write (Int (flags ))

        if self .results is not None :
            b .write (Vector (self .results ))

        if self .total_voters is not None :
            b .write (Int (self .total_voters ))

        if self .recent_voters is not None :
            b .write (Vector (self .recent_voters ,Long ))

        if self .solution is not None :
            b .write (String (self .solution ))

        if self .solution_entities is not None :
            b .write (Vector (self .solution_entities ))

        return b .getvalue ()
