
from typing import Union ,List ,Optional 

import hisapyro 
from hisapyro import raw ,enums 
from hisapyro import types 
from hisapyro import utils 

class EditMessageText :
    async def edit_message_text (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    message_id :int ,
    text :str ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    entities :List ["types.MessageEntity"]=None ,
    disable_web_page_preview :bool =None ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"types.Message":
        """"""

        r =await self .invoke (
        raw .functions .messages .EditMessage (
        peer =await self .resolve_peer (chat_id ),
        id =message_id ,
        no_webpage =disable_web_page_preview or None ,
        reply_markup =await reply_markup .write (self )if reply_markup else None ,
        **await utils .parse_text_entities (self ,text ,parse_mode ,entities )
        )
        )

        for i in r .updates :
            if isinstance (i ,(raw .types .UpdateEditMessage ,raw .types .UpdateEditChannelMessage )):
                return await types .Message ._parse (
                self ,i .message ,
                {i .id :i for i in r .users },
                {i .id :i for i in r .chats }
                )
