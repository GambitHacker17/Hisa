
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

class SendAnimation :
    async def send_animation (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    animation :Union [str ,BinaryIO ],
    caption :str ="",
    unsave :bool =False ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    duration :int =0 ,
    width :int =0 ,
    height :int =0 ,
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
            if isinstance (animation ,str ):
                if os .path .isfile (animation ):
                    thumb =await self .save_file (thumb )
                    file =await self .save_file (animation ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedDocument (
                    mime_type =self .guess_mime_type (animation )or "video/mp4",
                    file =file ,
                    thumb =thumb ,
                    spoiler =has_spoiler ,
                    attributes =[
                    raw .types .DocumentAttributeVideo (
                    supports_streaming =True ,
                    duration =duration ,
                    w =width ,
                    h =height 
                    ),
                    raw .types .DocumentAttributeFilename (file_name =file_name or os .path .basename (animation )),
                    raw .types .DocumentAttributeAnimated ()
                    ]
                    )
                elif re .match ("^https?://",animation ):
                    media =raw .types .InputMediaDocumentExternal (
                    url =animation ,
                    spoiler =has_spoiler 
                    )
                else :
                    media =utils .get_input_media_from_file_id (animation ,FileType .ANIMATION )
            else :
                thumb =await self .save_file (thumb )
                file =await self .save_file (animation ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedDocument (
                mime_type =self .guess_mime_type (file_name or animation .name )or "video/mp4",
                file =file ,
                thumb =thumb ,
                spoiler =has_spoiler ,
                attributes =[
                raw .types .DocumentAttributeVideo (
                supports_streaming =True ,
                duration =duration ,
                w =width ,
                h =height 
                ),
                raw .types .DocumentAttributeFilename (file_name =file_name or animation .name ),
                raw .types .DocumentAttributeAnimated ()
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
                    await self .save_file (animation ,file_id =file .id ,file_part =e .value )
                else :
                    for i in r .updates :
                        if isinstance (i ,(raw .types .UpdateNewMessage ,
                        raw .types .UpdateNewChannelMessage ,
                        raw .types .UpdateNewScheduledMessage )):
                            message =await types .Message ._parse (
                            self ,i .message ,
                            {i .id :i for i in r .users },
                            {i .id :i for i in r .chats },
                            is_scheduled =isinstance (i ,raw .types .UpdateNewScheduledMessage )
                            )

                            if unsave :
                                document =message .animation or message .document 
                                document_id =utils .get_input_media_from_file_id (
                                document .file_id ,FileType .ANIMATION 
                                ).id 

                                await self .invoke (
                                raw .functions .messages .SaveGif (
                                id =document_id ,
                                unsave =True 
                                )
                                )

                            return message 

        except StopTransmission :
            return None 
