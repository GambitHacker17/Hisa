
from typing import List ,Optional 

import hisapyro 
from hisapyro import raw ,types ,utils ,enums 
from .inline_query_result import InlineQueryResult 

class InlineQueryResultAudio (InlineQueryResult ):
    """"""

    def __init__ (
    self ,
    audio_url :str ,
    title :str ,
    id :str =None ,
    performer :str ="",
    audio_duration :int =0 ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    reply_markup :"types.InlineKeyboardMarkup"=None ,
    input_message_content :"types.InputMessageContent"=None 
    ):
        super ().__init__ ("audio",id ,input_message_content ,reply_markup )

        self .audio_url =audio_url 
        self .title =title 
        self .performer =performer 
        self .audio_duration =audio_duration 
        self .caption =caption 
        self .parse_mode =parse_mode 
        self .caption_entities =caption_entities 

    async def write (self ,client :"hisapyro.Client"):
        audio =raw .types .InputWebDocument (
        url =self .audio_url ,
        size =0 ,
        mime_type ="audio/mpeg",
        attributes =[raw .types .DocumentAttributeAudio (
        duration =self .audio_duration ,
        title =self .title ,
        performer =self .performer 
        )]
        )

        message ,entities =(await utils .parse_text_entities (
        client ,self .caption ,self .parse_mode ,self .caption_entities 
        )).values ()

        return raw .types .InputBotInlineResult (
        id =self .id ,
        type =self .type ,
        title =self .title ,
        content =audio ,
        send_message =(
        await self .input_message_content .write (client ,self .reply_markup )
        if self .input_message_content 
        else raw .types .InputBotInlineMessageMediaAuto (
        reply_markup =await self .reply_markup .write (client )if self .reply_markup else None ,
        message =message ,
        entities =entities 
        )
        )
        )
