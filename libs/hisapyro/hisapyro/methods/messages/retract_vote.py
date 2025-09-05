
from typing import Union 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class RetractVote :
    async def retract_vote (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    message_id :int 
    )->"types.Poll":
        """"""
        r =await self .invoke (
        raw .functions .messages .SendVote (
        peer =await self .resolve_peer (chat_id ),
        msg_id =message_id ,
        options =[]
        )
        )

        return types .Poll ._parse (self ,r .updates [0 ])
