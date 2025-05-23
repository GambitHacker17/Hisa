
from datetime import datetime 
from typing import Union 

import hisapyro 
from hisapyro import raw ,utils 
from hisapyro import types 

class SendContact :
    async def send_contact (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    phone_number :str ,
    first_name :str ,
    last_name :str =None ,
    vcard :str =None ,
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
        r =await self .invoke (
        raw .functions .messages .SendMedia (
        peer =await self .resolve_peer (chat_id ),
        media =raw .types .InputMediaContact (
        phone_number =phone_number ,
        first_name =first_name ,
        last_name =last_name or "",
        vcard =vcard or ""
        ),
        message ="",
        silent =disable_notification or None ,
        reply_to_msg_id =reply_to_message_id ,
        random_id =self .rnd_id (),
        schedule_date =utils .datetime_to_timestamp (schedule_date ),
        noforwards =protect_content ,
        reply_markup =await reply_markup .write (self )if reply_markup else None 
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
