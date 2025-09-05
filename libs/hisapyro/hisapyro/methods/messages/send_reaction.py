
from typing import Union 

import hisapyro 
from hisapyro import raw 

class SendReaction :
    async def send_reaction (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    message_id :int ,
    emoji :str ="",
    big :bool =False 
    )->bool :
        """"""
        await self .invoke (
        raw .functions .messages .SendReaction (
        peer =await self .resolve_peer (chat_id ),
        msg_id =message_id ,
        reaction =[raw .types .ReactionEmoji (emoticon =emoji )]if emoji else None ,
        big =big 
        )
        )

        return True 
