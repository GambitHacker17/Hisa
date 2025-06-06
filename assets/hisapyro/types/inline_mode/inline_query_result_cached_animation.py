
from typing import Optional ,List 

import hisapyro 
from hisapyro import raw ,types ,utils ,enums 
from .inline_query_result import InlineQueryResult 
from ...file_id import FileId 

class InlineQueryResultCachedAnimation (InlineQueryResult ):
    """"""

    def __init__ (
    self ,
    animation_file_id :str ,
    id :str =None ,
    title :str =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    reply_markup :"types.InlineKeyboardMarkup"=None ,
    input_message_content :"types.InputMessageContent"=None 
    ):
        super ().__init__ ("gif",id ,input_message_content ,reply_markup )

        self .animation_file_id =animation_file_id 
        self .title =title 
        self .caption =caption 
        self .parse_mode =parse_mode 
        self .caption_entities =caption_entities 
        self .reply_markup =reply_markup 
        self .input_message_content =input_message_content 

    async def write (self ,client :"hisapyro.Client"):
        message ,entities =(await utils .parse_text_entities (
        client ,self .caption ,self .parse_mode ,self .caption_entities 
        )).values ()

        file_id =FileId .decode (self .animation_file_id )

        return raw .types .InputBotInlineResultDocument (
        id =self .id ,
        type =self .type ,
        title =self .title ,
        document =raw .types .InputDocument (
        id =file_id .media_id ,
        access_hash =file_id .access_hash ,
        file_reference =file_id .file_reference ,
        ),
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
