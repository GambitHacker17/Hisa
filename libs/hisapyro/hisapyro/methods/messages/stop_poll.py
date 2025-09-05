
from typing import Union 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class StopPoll :
    async def stop_poll (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    message_id :int ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"types.Poll":
        """"""
        poll =(await self .get_messages (chat_id ,message_id )).poll 

        r =await self .invoke (
        raw .functions .messages .EditMessage (
        peer =await self .resolve_peer (chat_id ),
        id =message_id ,
        media =raw .types .InputMediaPoll (
        poll =raw .types .Poll (
        id =int (poll .id ),
        closed =True ,
        question ="",
        answers =[]
        )
        ),
        reply_markup =await reply_markup .write (self )if reply_markup else None 
        )
        )

        return types .Poll ._parse (self ,r .updates [0 ])
