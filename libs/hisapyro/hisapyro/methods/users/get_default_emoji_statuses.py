
from typing import List 

import hisapyro 
from hisapyro import raw 
from hisapyro import types 

class GetDefaultEmojiStatuses :
    async def get_default_emoji_statuses (
    self :"hisapyro.Client",
    )->List ["types.EmojiStatus"]:
        """"""
        r =await self .invoke (
        raw .functions .account .GetDefaultEmojiStatuses (hash =0 )
        )

        return types .List ([types .EmojiStatus ._parse (self ,i )for i in r .statuses ])
