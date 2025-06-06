
from datetime import datetime 
from typing import Union ,List 

import hisapyro 
from hisapyro import raw ,utils 
from hisapyro import types ,enums 

class SendPoll :
    async def send_poll (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    question :str ,
    options :List [str ],
    is_anonymous :bool =True ,
    type :"enums.PollType"=enums .PollType .REGULAR ,
    allows_multiple_answers :bool =None ,
    correct_option_id :int =None ,
    explanation :str =None ,
    explanation_parse_mode :"enums.ParseMode"=None ,
    explanation_entities :List ["types.MessageEntity"]=None ,
    open_period :int =None ,
    close_date :datetime =None ,
    is_closed :bool =None ,
    disable_notification :bool =None ,
    protect_content :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"types.Message":
        """"""

        solution ,solution_entities =(await utils .parse_text_entities (
        self ,explanation ,explanation_parse_mode ,explanation_entities 
        )).values ()

        r =await self .invoke (
        raw .functions .messages .SendMedia (
        peer =await self .resolve_peer (chat_id ),
        media =raw .types .InputMediaPoll (
        poll =raw .types .Poll (
        id =self .rnd_id (),
        question =question ,
        answers =[
        raw .types .PollAnswer (text =text ,option =bytes ([i ]))
        for i ,text in enumerate (options )
        ],
        closed =is_closed ,
        public_voters =not is_anonymous ,
        multiple_choice =allows_multiple_answers ,
        quiz =type ==enums .PollType .QUIZ or False ,
        close_period =open_period ,
        close_date =utils .datetime_to_timestamp (close_date )
        ),
        correct_answers =[bytes ([correct_option_id ])]if correct_option_id is not None else None ,
        solution =solution ,
        solution_entities =solution_entities or []
        ),
        message ="",
        silent =disable_notification ,
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
