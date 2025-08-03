
from datetime import datetime 
from typing import Union ,List ,Optional 

import hisapyro 
from hisapyro import raw ,utils ,enums 
from hisapyro import types 

class SendMessage :
    async def send_message (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    text :str ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    entities :List ["types.MessageEntity"]=None ,
    disable_web_page_preview :bool =None ,
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

        message ,entities =(await utils .parse_text_entities (self ,text ,parse_mode ,entities )).values ()

        r =await self .invoke (
        raw .functions .messages .SendMessage (
        peer =await self .resolve_peer (chat_id ),
        no_webpage =disable_web_page_preview or None ,
        silent =disable_notification or None ,
        reply_to_msg_id =reply_to_message_id ,
        random_id =self .rnd_id (),
        schedule_date =utils .datetime_to_timestamp (schedule_date ),
        reply_markup =await reply_markup .write (self )if reply_markup else None ,
        message =message ,
        entities =entities ,
        noforwards =protect_content 
        )
        )

        if isinstance (r ,raw .types .UpdateShortSentMessage ):
            peer =await self .resolve_peer (chat_id )

            peer_id =(
            peer .user_id 
            if isinstance (peer ,raw .types .InputPeerUser )
            else -peer .chat_id 
            )

            return types .Message (
            id =r .id ,
            chat =types .Chat (
            id =peer_id ,
            type =enums .ChatType .PRIVATE ,
            client =self 
            ),
            text =message ,
            date =utils .timestamp_to_datetime (r .date ),
            outgoing =r .out ,
            reply_markup =reply_markup ,
            entities =[
            types .MessageEntity ._parse (None ,entity ,{})
            for entity in entities 
            ]if entities else None ,
            client =self 
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
