
import logging 
from datetime import datetime 
from typing import Union ,List ,Optional 

import hisapyro 
from hisapyro import types ,enums 

log =logging .getLogger (__name__ )

class CopyMessage :
    async def copy_message (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    from_chat_id :Union [int ,str ],
    message_id :int ,
    caption :str =None ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    protect_content :bool =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"types.Message":
        """"""
        message :types .Message =await self .get_messages (from_chat_id ,message_id )

        return await message .copy (
        chat_id =chat_id ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        schedule_date =schedule_date ,
        protect_content =protect_content ,
        reply_markup =reply_markup 
        )
