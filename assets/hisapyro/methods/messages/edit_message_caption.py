
from typing import Union ,List ,Optional 

import hisapyro 
from hisapyro import types ,enums 

class EditMessageCaption :
    async def edit_message_caption (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    message_id :int ,
    caption :str ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"types.Message":
        """"""
        return await self .edit_message_text (
        chat_id =chat_id ,
        message_id =message_id ,
        text =caption ,
        parse_mode =parse_mode ,
        entities =caption_entities ,
        reply_markup =reply_markup 
        )
