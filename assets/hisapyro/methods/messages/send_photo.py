
import os 
import re 
from datetime import datetime 
from typing import Union ,BinaryIO ,List ,Optional ,Callable 

import hisapyro 
from hisapyro import raw ,enums 
from hisapyro import types 
from hisapyro import utils 
from hisapyro .errors import FilePartMissing 
from hisapyro .file_id import FileType 

class SendPhoto :
    async def send_photo (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    photo :Union [str ,BinaryIO ],
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    ttl_seconds :int =None ,
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
            if isinstance (photo ,str ):
                if os .path .isfile (photo ):
                    file =await self .save_file (photo ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedPhoto (
                    file =file ,
                    ttl_seconds =ttl_seconds ,
                    spoiler =has_spoiler ,
                    )
                elif re .match ("^https?://",photo ):
                    media =raw .types .InputMediaPhotoExternal (
                    url =photo ,
                    ttl_seconds =ttl_seconds ,
                    spoiler =has_spoiler 
                    )
                else :
                    media =utils .get_input_media_from_file_id (photo ,FileType .PHOTO ,ttl_seconds =ttl_seconds )
            else :
                file =await self .save_file (photo ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedPhoto (
                file =file ,
                ttl_seconds =ttl_seconds ,
                spoiler =has_spoiler 
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
                    await self .save_file (photo ,file_id =file .id ,file_part =e .value )
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
        except hisapyro .StopTransmission :
            return None 
