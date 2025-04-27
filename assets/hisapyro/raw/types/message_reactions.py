
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MessageReactions (TLObject ):
    """"""

    __slots__ :List [str ]=["results","min","can_see_list","recent_reactions"]

    ID =0x4f2b9479 
    QUALNAME ="types.MessageReactions"

    def __init__ (self ,*,results :List ["raw.base.ReactionCount"],min :Optional [bool ]=None ,can_see_list :Optional [bool ]=None ,recent_reactions :Optional [List ["raw.base.MessagePeerReaction"]]=None )->None :
        self .results =results 
        self .min =min 
        self .can_see_list =can_see_list 
        self .recent_reactions =recent_reactions 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MessageReactions":

        flags =Int .read (b )

        min =True if flags &(1 <<0 )else False 
        can_see_list =True if flags &(1 <<2 )else False 
        results =TLObject .read (b )

        recent_reactions =TLObject .read (b )if flags &(1 <<1 )else []

        return MessageReactions (results =results ,min =min ,can_see_list =can_see_list ,recent_reactions =recent_reactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .min else 0 
        flags |=(1 <<2 )if self .can_see_list else 0 
        flags |=(1 <<1 )if self .recent_reactions else 0 
        b .write (Int (flags ))

        b .write (Vector (self .results ))

        if self .recent_reactions is not None :
            b .write (Vector (self .recent_reactions ))

        return b .getvalue ()
