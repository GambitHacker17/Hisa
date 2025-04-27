import copy 
import functools 
import hashlib 
import io 
import itertools 
import os 
import pathlib 
import re 
import typing 
from io import BytesIO 
import asyncio 

from ..crypto import AES 

from ..import utils ,helpers ,hints 
from ..tl import types ,functions ,custom 

try :
    import PIL 
    import PIL .Image 
except ImportError :
    PIL =None 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

class _CacheType :
    """"""
    def __init__ (self ,cls ):
        self ._cls =cls 

    def __call__ (self ,*args ,**kwargs ):
        return self ._cls (*args ,file_reference =b'',**kwargs )

    def __eq__ (self ,other ):
        return self ._cls ==other 

def _resize_photo_if_needed (
file ,is_image ,width =2560 ,height =2560 ,background =(255 ,255 ,255 )):

    if (not is_image 
    or PIL is None 
    or (isinstance (file ,io .IOBase )and not file .seekable ())):
        return file 

    if isinstance (file ,bytes ):
        file =io .BytesIO (file )

    before =file .tell ()if isinstance (file ,io .IOBase )else None 

    try :

        image =PIL .Image .open (file )
        try :
            kwargs ={'exif':image .info ['exif']}
        except KeyError :
            kwargs ={}

        if image .width <=width and image .height <=height :
            return file 

        image .thumbnail ((width ,height ),PIL .Image .ANTIALIAS )

        alpha_index =image .mode .find ('A')
        if alpha_index ==-1 :

            result =image 
        else :

            result =PIL .Image .new ('RGB',image .size ,background )
            result .paste (image ,mask =image .split ()[alpha_index ])

        buffer =io .BytesIO ()
        result .save (buffer ,'JPEG',progressive =True ,**kwargs )
        buffer .seek (0 )
        return buffer 

    except IOError :
        return file 
    finally :
        if before is not None :
            file .seek (before ,io .SEEK_SET )

class UploadMethods :

    async def send_file (
    self :'TelegramClient',
    entity :'hints.EntityLike',
    file :'typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]',
    *,
    caption :typing .Union [str ,typing .Sequence [str ]]=None ,
    force_document :bool =False ,
    file_size :int =None ,
    clear_draft :bool =False ,
    progress_callback :'hints.ProgressCallback'=None ,
    reply_to :'typing.Union[hints.MessageIDLike, types.TypeInputReplyTo]'=None ,
    attributes :'typing.Sequence[types.TypeDocumentAttribute]'=None ,
    thumb :'hints.FileLike'=None ,
    allow_cache :bool =True ,
    parse_mode :str =(),
    formatting_entities :typing .Optional [typing .List [types .TypeMessageEntity ]]=None ,
    voice_note :bool =False ,
    video_note :bool =False ,
    buttons :typing .Optional ['hints.MarkupLike']=None ,
    silent :bool =None ,
    background :bool =None ,
    supports_streaming :bool =False ,
    schedule :'hints.DateLike'=None ,
    comment_to :'typing.Union[int, types.Message]'=None ,
    top_msg_id :int =None ,
    ttl :int =None ,
    nosound_video :bool =None ,
    **kwargs )->'types.Message':
        """"""

        if not file :
            raise TypeError ('Cannot use {!r} as file'.format (file ))

        if not caption :
            caption =''

        entity =await self .get_input_entity (entity )
        if comment_to is not None :
            entity ,reply_to =await self ._get_comment_data (entity ,comment_to )

        reply_to =utils .get_input_reply_to (entity ,reply_to ,top_msg_id )

        if utils .is_list_like (file ):
            if utils .is_list_like (caption ):
                captions =caption 
            else :
                captions =[caption ]

            result =[]
            while file :
                result +=await self ._send_album (
                entity ,file [:10 ],caption =captions [:10 ],
                progress_callback =progress_callback ,reply_to =reply_to ,
                parse_mode =parse_mode ,silent =silent ,schedule =schedule ,
                supports_streaming =supports_streaming ,clear_draft =clear_draft ,
                force_document =force_document ,background =background ,
                )
                file =file [10 :]
                captions =captions [10 :]

            for doc ,cap in zip (file ,captions ):
                result .append (await self .send_file (
                entity ,doc ,allow_cache =allow_cache ,
                caption =cap ,force_document =force_document ,
                progress_callback =progress_callback ,reply_to =reply_to ,
                top_msg_id =top_msg_id ,
                attributes =attributes ,thumb =thumb ,voice_note =voice_note ,
                video_note =video_note ,buttons =buttons ,silent =silent ,
                supports_streaming =supports_streaming ,schedule =schedule ,
                clear_draft =clear_draft ,background =background ,
                **kwargs 
                ))

            return result 

        if formatting_entities is not None :
            msg_entities =formatting_entities 
        else :
            caption ,msg_entities =await self ._parse_message_text (caption ,parse_mode )

        file_handle ,media ,image =await self ._file_to_media (
        file ,force_document =force_document ,
        file_size =file_size ,
        progress_callback =progress_callback ,
        attributes =attributes ,allow_cache =allow_cache ,thumb =thumb ,
        voice_note =voice_note ,video_note =video_note ,
        supports_streaming =supports_streaming ,ttl =ttl ,
        nosound_video =nosound_video 
        )

        if not media :
            raise TypeError ('Cannot use {!r} as file'.format (file ))

        markup =self .build_reply_markup (buttons )
        request =functions .messages .SendMediaRequest (
        entity ,media ,reply_to =reply_to ,message =caption ,
        entities =msg_entities ,reply_markup =markup ,silent =silent ,
        schedule_date =schedule ,clear_draft =clear_draft ,
        background =background 
        )
        return self ._get_response_message (request ,await self (request ),entity )

    async def _send_album (self :'TelegramClient',entity ,files ,caption ='',
    progress_callback =None ,reply_to =None ,
    parse_mode =(),silent =None ,schedule =None ,
    supports_streaming =None ,clear_draft =None ,
    force_document =False ,background =None ,ttl =None ,
    top_msg_id =None ):
        """"""

        entity =await self .get_input_entity (entity )
        if not utils .is_list_like (caption ):
            caption =(caption ,)

        captions =[]
        for c in reversed (caption ):
            captions .append (await self ._parse_message_text (c or '',parse_mode ))

        reply_to =utils .get_message_id (reply_to )

        used_callback =None if not progress_callback else (

        lambda s ,t :progress_callback (sent_count +1 if s ==t else sent_count +s /t ,len (files ))
        )

        media =[]
        for sent_count ,file in enumerate (files ):

            fh ,fm ,_ =await self ._file_to_media (
            file ,supports_streaming =supports_streaming ,
            force_document =force_document ,ttl =ttl ,
            progress_callback =used_callback ,nosound_video =True )
            if isinstance (fm ,(types .InputMediaUploadedPhoto ,types .InputMediaPhotoExternal )):
                r =await self (functions .messages .UploadMediaRequest (
                entity ,media =fm 
                ))

                fm =utils .get_input_media (r .photo )
            elif isinstance (fm ,types .InputMediaUploadedDocument ):
                r =await self (functions .messages .UploadMediaRequest (
                entity ,media =fm 
                ))

                fm =utils .get_input_media (
                r .document ,supports_streaming =supports_streaming )

            if captions :
                caption ,msg_entities =captions .pop ()
            else :
                caption ,msg_entities ='',None 
            media .append (types .InputSingleMedia (
            fm ,
            message =caption ,
            entities =msg_entities 

            ))

        request =functions .messages .SendMultiMediaRequest (
        entity ,reply_to_msg_id =reply_to ,multi_media =media ,
        silent =silent ,schedule_date =schedule ,clear_draft =clear_draft ,
        background =background )
        result =await self (request )

        random_ids =[m .random_id for m in media ]
        return self ._get_response_message (random_ids ,result ,entity )

    async def upload_file (
    self :'TelegramClient',
    file :'hints.FileLike',
    *,
    part_size_kb :float =None ,
    file_size :int =None ,
    file_name :str =None ,
    use_cache :type =None ,
    key :bytes =None ,
    iv :bytes =None ,
    progress_callback :'hints.ProgressCallback'=None )->'types.TypeInputFile':
        """"""
        if isinstance (file ,(types .InputFile ,types .InputFileBig )):
            return file 

        pos =0 
        async with helpers ._FileStream (file ,file_size =file_size )as stream :

            file_size =stream .file_size 

            if not part_size_kb :
                part_size_kb =utils .get_appropriated_part_size (file_size )

            if part_size_kb >512 :
                raise ValueError ('The part size must be less or equal to 512KB')

            part_size =int (part_size_kb *1024 )
            if part_size %1024 !=0 :
                raise ValueError (
                'The part size must be evenly divisible by 1024')

            file_id =helpers .generate_random_long ()
            if not file_name :
                file_name =stream .name or str (file_id )

            if not os .path .splitext (file_name )[-1 ]:
                file_name +=utils ._get_extension (stream )

            is_big =file_size >10 *1024 *1024 
            hash_md5 =hashlib .md5 ()

            part_count =(file_size +part_size -1 )//part_size 
            self ._log [__name__ ].info ('Uploading file of %d bytes in %d chunks of %d',
            file_size ,part_count ,part_size )

            pos =0 
            for part_index in range (part_count ):

                part =await helpers ._maybe_await (stream .read (part_size ))

                if not isinstance (part ,bytes ):
                    raise TypeError (
                    'file descriptor returned {}, not bytes (you must '
                    'open the file in bytes mode)'.format (type (part )))

                if len (part )!=part_size and part_index <part_count -1 :
                    raise ValueError (
                    'read less than {} before reaching the end; either '
                    '`file_size` or `read` are wrong'.format (part_size ))

                pos +=len (part )

                if key and iv :
                    part =AES .encrypt_ige (part ,key ,iv )

                if not is_big :

                    hash_md5 .update (part )

                if is_big :
                    request =functions .upload .SaveBigFilePartRequest (
                    file_id ,part_index ,part_count ,part )
                else :
                    request =functions .upload .SaveFilePartRequest (
                    file_id ,part_index ,part )

                result =await self (request )
                if result :
                    self ._log [__name__ ].debug ('Uploaded %d/%d',
                    part_index +1 ,part_count )
                    if progress_callback :
                        await helpers ._maybe_await (progress_callback (pos ,file_size ))
                else :
                    raise RuntimeError (
                    'Failed to upload file part {}.'.format (part_index ))

        if is_big :
            return types .InputFileBig (file_id ,part_count ,file_name )
        else :
            return custom .InputSizedFile (
            file_id ,part_count ,file_name ,md5 =hash_md5 ,size =file_size 
            )

    async def _file_to_media (
    self ,file ,force_document =False ,file_size =None ,
    progress_callback =None ,attributes =None ,thumb =None ,
    allow_cache =True ,voice_note =False ,video_note =False ,
    supports_streaming =False ,mime_type =None ,as_image =None ,
    ttl =None ,nosound_video =None ):
        if not file :
            return None ,None ,None 

        if isinstance (file ,pathlib .Path ):
            file =str (file .absolute ())

        is_image =utils .is_image (file )
        if as_image is None :
            as_image =is_image and not force_document 

        if not isinstance (file ,(str ,bytes ,types .InputFile ,types .InputFileBig ))and not hasattr (file ,'read'):

            try :
                return (None ,utils .get_input_media (
                file ,
                is_photo =as_image ,
                attributes =attributes ,
                force_document =force_document ,
                voice_note =voice_note ,
                video_note =video_note ,
                supports_streaming =supports_streaming ,
                ttl =ttl 
                ),as_image )
            except TypeError :

                return None ,None ,as_image 

        media =None 
        file_handle =None 

        if isinstance (file ,(types .InputFile ,types .InputFileBig )):
            file_handle =file 
        elif not isinstance (file ,str )or os .path .isfile (file ):
            file_handle =await self .upload_file (
            _resize_photo_if_needed (file ,as_image ),
            file_size =file_size ,
            progress_callback =progress_callback 
            )
        elif re .match ('https?://',file ):
            if as_image :
                media =types .InputMediaPhotoExternal (file ,ttl_seconds =ttl )
            else :
                media =types .InputMediaDocumentExternal (file ,ttl_seconds =ttl )
        else :
            bot_file =utils .resolve_bot_file_id (file )
            if bot_file :
                media =utils .get_input_media (bot_file ,ttl =ttl )

        if media :
            pass 
        elif not file_handle :
            raise ValueError (
            'Failed to convert {} to media. Not an existing file, '
            'an HTTP URL or a valid bot-API-like file ID'.format (file )
            )
        elif as_image :
            media =types .InputMediaUploadedPhoto (file_handle ,ttl_seconds =ttl )
        else :
            attributes ,mime_type =utils .get_attributes (
            file ,
            mime_type =mime_type ,
            attributes =attributes ,
            force_document =force_document and not is_image ,
            voice_note =voice_note ,
            video_note =video_note ,
            supports_streaming =supports_streaming ,
            thumb =thumb 
            )

            if not thumb :
                thumb =None 
            else :
                if isinstance (thumb ,pathlib .Path ):
                    thumb =str (thumb .absolute ())
                thumb =await self .upload_file (thumb ,file_size =file_size )

            nosound_video =nosound_video if mime_type .split ("/")[0 ]=='video'else None 

            media =types .InputMediaUploadedDocument (
            file =file_handle ,
            mime_type =mime_type ,
            attributes =attributes ,
            thumb =thumb ,
            force_file =force_document and not is_image ,
            ttl_seconds =ttl ,
            nosound_video =nosound_video 
            )
        return file_handle ,media ,as_image 

