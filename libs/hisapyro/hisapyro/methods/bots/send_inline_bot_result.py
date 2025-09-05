
from typing import Union 

import hisapyro 
from hisapyro import raw 

class SendInlineBotResult :
    async def send_inline_bot_result (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    query_id :int ,
    result_id :str ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None 
    )->"raw.base.Updates":
        """"""
        return await self .invoke (
        raw .functions .messages .SendInlineBotResult (
        peer =await self .resolve_peer (chat_id ),
        query_id =query_id ,
        id =result_id ,
        random_id =self .rnd_id (),
        silent =disable_notification or None ,
        reply_to_msg_id =reply_to_message_id 
        )
        )
