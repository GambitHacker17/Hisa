
from typing import Union 

import hisapyro 
from hisapyro import raw 

class SetChatTitle :
    async def set_chat_title (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    title :str 
    )->bool :
        """"""
        peer =await self .resolve_peer (chat_id )

        if isinstance (peer ,raw .types .InputPeerChat ):
            await self .invoke (
            raw .functions .messages .EditChatTitle (
            chat_id =peer .chat_id ,
            title =title 
            )
            )
        elif isinstance (peer ,raw .types .InputPeerChannel ):
            await self .invoke (
            raw .functions .channels .EditTitle (
            channel =peer ,
            title =title 
            )
            )
        else :
            raise ValueError (f'The chat_id "{chat_id }" belongs to a user')

        return True 
