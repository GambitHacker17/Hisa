
from typing import Optional 

import hisapyro 
from hisapyro import raw ,types 

class SetEmojiStatus :
    async def set_emoji_status (
    self :"hisapyro.Client",
    emoji_status :Optional ["types.EmojiStatus"]=None 
    )->bool :
        """"""
        await self .invoke (
        raw .functions .account .UpdateEmojiStatus (
        emoji_status =(
        emoji_status .write ()
        if emoji_status 
        else raw .types .EmojiStatusEmpty ()
        )
        )
        )

        return True 
