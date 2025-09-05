
import os 
import re 
from datetime import datetime 
from typing import Union ,BinaryIO ,Optional ,Callable 

import hisapyro 
from hisapyro import StopTransmission 
from hisapyro import raw 
from hisapyro import types 
from hisapyro import utils 
from hisapyro .errors import FilePartMissing 
from hisapyro .file_id import FileType 

class SendSticker :
    async def send_sticker (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    sticker :Union [str ,BinaryIO ],
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
            if isinstance (sticker ,str ):
                if os .path .isfile (sticker ):
                    file =await self .save_file (sticker ,progress =progress ,progress_args =progress_args )
                    media =raw .types .InputMediaUploadedDocument (
                    mime_type =self .guess_mime_type (sticker )or "image/webp",
                    file =file ,
                    attributes =[
                    raw .types .DocumentAttributeFilename (file_name =os .path .basename (sticker ))
                    ]
                    )
                elif re .match ("^https?://",sticker ):
                    media =raw .types .InputMediaDocumentExternal (
                    url =sticker 
                    )
                else :
                    media =utils .get_input_media_from_file_id (sticker ,FileType .STICKER )
            else :
                file =await self .save_file (sticker ,progress =progress ,progress_args =progress_args )
                media =raw .types .InputMediaUploadedDocument (
                mime_type =self .guess_mime_type (sticker .name )or "image/webp",
                file =file ,
                attributes =[
                raw .types .DocumentAttributeFilename (file_name =sticker .name )
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
                    message =""
                    )
                    )
                except FilePartMissing as e :
                    await self .save_file (sticker ,file_id =file .id ,file_part =e .value )
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
