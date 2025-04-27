
from datetime import datetime 
from typing import Union ,List ,Optional 

import hisapyro 
from hisapyro import raw ,enums 
from hisapyro import types 
from hisapyro import utils 

class SendCachedMedia :
    async def send_cached_media (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    file_id :str ,
    caption :str ="",
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
    )->Optional ["types.Message"]:
        """"""

        r =await self .invoke (
        raw .functions .messages .SendMedia (
        peer =await self .resolve_peer (chat_id ),
        media =utils .get_input_media_from_file_id (file_id ),
        silent =disable_notification or None ,
        reply_to_msg_id =reply_to_message_id ,
        random_id =self .rnd_id (),
        schedule_date =utils .datetime_to_timestamp (schedule_date ),
        noforwards =protect_content ,
        reply_markup =await reply_markup .write (self )if reply_markup else None ,
        **await utils .parse_text_entities (self ,caption ,parse_mode ,caption_entities )
        )
        )

        for i in r .updates :
            if isinstance (i ,(raw .types .UpdateNewMessage ,
            raw .types .UpdateNewChannelMessage ,
            raw .types .UpdateNewScheduledMessage )):
                return await types .Message ._parse (
                self ,i .message ,
                {i .id :i for i in r .users },
                {i .id :i for i in r .chats },
                is_scheduled =isinstance (i ,raw .types .UpdateNewScheduledMessage )
                )
