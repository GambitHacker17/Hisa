
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

class SendVideo :
    async def send_video (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    video :Union [str ,BinaryIO ],
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    ttl_seconds :int =None ,
    duration :int =0 ,
    width :int =0 ,
    height :int =0 ,
    thumb :Union [str ,BinaryIO ]=None ,
    file_name :str =None ,
    supports_streaming :bool =True ,
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
            if isinstance (video ,str ):
                if os .path .isfile (video ):
                    thumb =await self .save_file (thumb )
                    file =await self .save_file (video ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedDocument (
                    mime_type =self .guess_mime_type (video )or "video/mp4",
                    file =file ,
                    ttl_seconds =ttl_seconds ,
                    spoiler =has_spoiler ,
                    thumb =thumb ,
                    attributes =[
                    raw .types .DocumentAttributeVideo (
                    supports_streaming =supports_streaming or None ,
                    duration =duration ,
                    w =width ,
                    h =height 
                    ),
                    raw .types .DocumentAttributeFilename (file_name =file_name or os .path .basename (video ))
                    ]
                    )
                elif re .match ("^https?://",video ):
                    media =raw .types .InputMediaDocumentExternal (
                    url =video ,
                    ttl_seconds =ttl_seconds ,
                    spoiler =has_spoiler 
                    )
                else :
                    media =utils .get_input_media_from_file_id (video ,FileType .VIDEO ,ttl_seconds =ttl_seconds )
            else :
                thumb =await self .save_file (thumb )
                file =await self .save_file (video ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedDocument (
                mime_type =self .guess_mime_type (file_name or video .name )or "video/mp4",
                file =file ,
                ttl_seconds =ttl_seconds ,
                spoiler =has_spoiler ,
                thumb =thumb ,
                attributes =[
                raw .types .DocumentAttributeVideo (
                supports_streaming =supports_streaming or None ,
                duration =duration ,
                w =width ,
                h =height 
                ),
                raw .types .DocumentAttributeFilename (file_name =file_name or video .name )
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
                    await self .save_file (video ,file_id =file .id ,file_part =e .value )
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
