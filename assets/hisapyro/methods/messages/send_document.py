
import os 
import re 
from datetime import datetime 
from typing import Union ,BinaryIO ,List ,Optional ,Callable 

import hisapyro 
from hisapyro import StopTransmission ,enums 
from hisapyro import raw 
from hisapyro import types 
from hisapyro import utils 
from hisapyro .errors import FilePartMissing 
from hisapyro .file_id import FileType 

class SendDocument :
    async def send_document (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    document :Union [str ,BinaryIO ],
    thumb :Union [str ,BinaryIO ]=None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    file_name :str =None ,
    force_document :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    protect_content :bool =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->Optional ["types.Message"]:
        """"""
        file =None 

        try :
            if isinstance (document ,str ):
                if os .path .isfile (document ):
                    thumb =await self .save_file (thumb )
                    file =await self .save_file (document ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedDocument (
                    mime_type =self .guess_mime_type (document )or "application/zip",
                    file =file ,
                    force_file =force_document or None ,
                    thumb =thumb ,
                    attributes =[
                    raw .types .DocumentAttributeFilename (file_name =file_name or os .path .basename (document ))
                    ]
                    )
                elif re .match ("^https?://",document ):
                    media =raw .types .InputMediaDocumentExternal (
                    url =document 
                    )
                else :
                    media =utils .get_input_media_from_file_id (document ,FileType .DOCUMENT )
            else :
                thumb =await self .save_file (thumb )
                file =await self .save_file (document ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedDocument (
                mime_type =self .guess_mime_type (file_name or document .name )or "application/zip",
                file =file ,
                thumb =thumb ,
                attributes =[
                raw .types .DocumentAttributeFilename (file_name =file_name or document .name )
                ]
                )

            while True :
                try :
                    r =await self .invoke (
                    raw .functions .messages .SendMedia (
                    peer =await self .resolve_peer (chat_id ),
                    media =media ,
                    silent =disable_notification or None ,
                    reply_to_msg_id =reply_to_message_id ,
                    random_id =self .rnd_id (),
                    schedule_date =utils .datetime_to_timestamp (schedule_date ),
                    noforwards =protect_content ,
                    reply_markup =await reply_markup .write (self )if reply_markup else None ,
                    **await utils .parse_text_entities (self ,caption ,parse_mode ,caption_entities )
                    )
                    )
                except FilePartMissing as e :
                    await self .save_file (document ,file_id =file .id ,file_part =e .value )
                else :
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
        except StopTransmission :
            return None 
