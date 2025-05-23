
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

class SendAudio :
    async def send_audio (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    audio :Union [str ,BinaryIO ],
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    duration :int =0 ,
    performer :str =None ,
    title :str =None ,
    thumb :Union [str ,BinaryIO ]=None ,
    file_name :str =None ,
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
            if isinstance (audio ,str ):
                if os .path .isfile (audio ):
                    thumb =await self .save_file (thumb )
                    file =await self .save_file (audio ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedDocument (
                    mime_type =self .guess_mime_type (audio )or "audio/mpeg",
                    file =file ,
                    thumb =thumb ,
                    attributes =[
                    raw .types .DocumentAttributeAudio (
                    duration =duration ,
                    performer =performer ,
                    title =title 
                    ),
                    raw .types .DocumentAttributeFilename (file_name =file_name or os .path .basename (audio ))
                    ]
                    )
                elif re .match ("^https?://",audio ):
                    media =raw .types .InputMediaDocumentExternal (
                    url =audio 
                    )
                else :
                    media =utils .get_input_media_from_file_id (audio ,FileType .AUDIO )
            else :
                thumb =await self .save_file (thumb )
                file =await self .save_file (audio ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedDocument (
                mime_type =self .guess_mime_type (file_name or audio .name )or "audio/mpeg",
                file =file ,
                thumb =thumb ,
                attributes =[
                raw .types .DocumentAttributeAudio (
                duration =duration ,
                performer =performer ,
                title =title 
                ),
                raw .types .DocumentAttributeFilename (file_name =file_name or audio .name )
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
                    await self .save_file (audio ,file_id =file .id ,file_part =e .value )
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
