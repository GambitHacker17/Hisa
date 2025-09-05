""""""
import base64 
import binascii 
import imghdr 
import inspect 
import io 
import itertools 
import logging 
import math 
import mimetypes 
import os 
import pathlib 
import re 
import struct 
from collections import namedtuple 
from mimetypes import guess_extension 
from types import GeneratorType 
import typing 

from .extensions import markdown ,html 
from .helpers import add_surrogate ,del_surrogate ,strip_text 
from .tl import types 

try :
    import hachoir 
    import hachoir .metadata 
    import hachoir .parser 
except ImportError :
    hachoir =None 

mimetypes .add_type ('image/png','.png')
mimetypes .add_type ('image/jpeg','.jpeg')
mimetypes .add_type ('image/webp','.webp')
mimetypes .add_type ('image/gif','.gif')
mimetypes .add_type ('image/bmp','.bmp')
mimetypes .add_type ('image/x-tga','.tga')
mimetypes .add_type ('image/tiff','.tiff')
mimetypes .add_type ('image/vnd.adobe.photoshop','.psd')

mimetypes .add_type ('video/mp4','.mp4')
mimetypes .add_type ('video/quicktime','.mov')
mimetypes .add_type ('video/avi','.avi')

mimetypes .add_type ('audio/mpeg','.mp3')
mimetypes .add_type ('audio/m4a','.m4a')
mimetypes .add_type ('audio/aac','.aac')
mimetypes .add_type ('audio/ogg','.ogg')
mimetypes .add_type ('audio/flac','.flac')

mimetypes .add_type ('application/x-tgsticker','.tgs')

USERNAME_RE =re .compile (
r'@|(?:https?://)?(?:www\.)?(?:telegram\.(?:me|dog)|t\.me)/(@|\+|joinchat/)?'
)
TG_JOIN_RE =re .compile (
r'tg://(join)\?invite='
)

VALID_USERNAME_RE =re .compile (
r'^[a-z](?:(?!__)\w){1,30}[a-z\d]$',
re .IGNORECASE 
)

_FileInfo =namedtuple ('FileInfo','dc_id location size')

_log =logging .getLogger (__name__ )

def chunks (iterable ,size =100 ):
    """"""
    it =iter (iterable )
    size -=1 
    for head in it :
        yield itertools .chain ([head ],itertools .islice (it ,size ))

def get_display_name (entity ):
    """"""
    if isinstance (entity ,types .User ):
        if entity .last_name and entity .first_name :
            return '{} {}'.format (entity .first_name ,entity .last_name )
        elif entity .first_name :
            return entity .first_name 
        elif entity .last_name :
            return entity .last_name 
        else :
            return ''

    elif isinstance (entity ,(types .Chat ,types .ChatForbidden ,types .Channel )):
        return entity .title 

    return ''

def get_extension (media ):
    """"""

    try :
        get_input_photo (media )
        return '.jpg'
    except TypeError :

        if isinstance (media ,(types .UserProfilePhoto ,types .ChatPhoto )):
            return '.jpg'

    if isinstance (media ,types .MessageMediaDocument ):
        media =media .document 
    if isinstance (media ,(
    types .Document ,types .WebDocument ,types .WebDocumentNoProxy )):
        if media .mime_type =='application/octet-stream':

            return ''
        else :
            return guess_extension (media .mime_type )or ''

    return ''

def _raise_cast_fail (entity ,target ):
    raise TypeError ('Cannot cast {} to any kind of {}.'.format (
    type (entity ).__name__ ,target ))

def get_input_peer (entity ,allow_self =True ,check_hash =True ):
    """"""

    try :
        if entity .SUBCLASS_OF_ID ==0xc91c90b6 :
            return entity 
    except AttributeError :

        if allow_self and hasattr (entity ,'input_entity'):
            return entity .input_entity 
        elif hasattr (entity ,'entity'):
            return get_input_peer (entity .entity )
        else :
            _raise_cast_fail (entity ,'InputPeer')

    if isinstance (entity ,types .User ):
        if entity .is_self and allow_self :
            return types .InputPeerSelf ()
        elif (entity .access_hash is not None and not entity .min )or not check_hash :
            return types .InputPeerUser (entity .id ,entity .access_hash )
        else :
            raise TypeError ('User without access_hash or min info cannot be input')

    if isinstance (entity ,(types .Chat ,types .ChatEmpty ,types .ChatForbidden )):
        return types .InputPeerChat (entity .id )

    if isinstance (entity ,types .Channel ):
        if (entity .access_hash is not None and not entity .min )or not check_hash :
            return types .InputPeerChannel (entity .id ,entity .access_hash )
        else :
            raise TypeError ('Channel without access_hash or min info cannot be input')
    if isinstance (entity ,types .ChannelForbidden ):

        return types .InputPeerChannel (entity .id ,entity .access_hash )

    if isinstance (entity ,types .InputUser ):
        return types .InputPeerUser (entity .user_id ,entity .access_hash )

    if isinstance (entity ,types .InputChannel ):
        return types .InputPeerChannel (entity .channel_id ,entity .access_hash )

    if isinstance (entity ,types .InputUserSelf ):
        return types .InputPeerSelf ()

    if isinstance (entity ,types .InputUserFromMessage ):
        return types .InputPeerUserFromMessage (entity .peer ,entity .msg_id ,entity .user_id )

    if isinstance (entity ,types .InputChannelFromMessage ):
        return types .InputPeerChannelFromMessage (entity .peer ,entity .msg_id ,entity .channel_id )

    if isinstance (entity ,types .UserEmpty ):
        return types .InputPeerEmpty ()

    if isinstance (entity ,types .UserFull ):
        return get_input_peer (entity .user )

    if isinstance (entity ,types .ChatFull ):
        return types .InputPeerChat (entity .id )

    if isinstance (entity ,types .PeerChat ):
        return types .InputPeerChat (entity .chat_id )

    _raise_cast_fail (entity ,'InputPeer')

def get_input_channel (entity ):
    """"""
    try :
        if entity .SUBCLASS_OF_ID ==0x40f202fd :
            return entity 
    except AttributeError :
        _raise_cast_fail (entity ,'InputChannel')

    if isinstance (entity ,(types .Channel ,types .ChannelForbidden )):
        return types .InputChannel (entity .id ,entity .access_hash or 0 )

    if isinstance (entity ,types .InputPeerChannel ):
        return types .InputChannel (entity .channel_id ,entity .access_hash )

    if isinstance (entity ,types .InputPeerChannelFromMessage ):
        return types .InputChannelFromMessage (entity .peer ,entity .msg_id ,entity .channel_id )

    _raise_cast_fail (entity ,'InputChannel')

def get_input_user (entity ):
    """"""
    try :
        if entity .SUBCLASS_OF_ID ==0xe669bf46 :
            return entity 
    except AttributeError :
        _raise_cast_fail (entity ,'InputUser')

    if isinstance (entity ,types .User ):
        if entity .is_self :
            return types .InputUserSelf ()
        else :
            return types .InputUser (entity .id ,entity .access_hash or 0 )

    if isinstance (entity ,types .InputPeerSelf ):
        return types .InputUserSelf ()

    if isinstance (entity ,(types .UserEmpty ,types .InputPeerEmpty )):
        return types .InputUserEmpty ()

    if isinstance (entity ,types .UserFull ):
        return get_input_user (entity .user )

    if isinstance (entity ,types .InputPeerUser ):
        return types .InputUser (entity .user_id ,entity .access_hash )

    if isinstance (entity ,types .InputPeerUserFromMessage ):
        return types .InputUserFromMessage (entity .peer ,entity .msg_id ,entity .user_id )

    _raise_cast_fail (entity ,'InputUser')

def get_input_dialog (dialog ):
    """"""
    try :
        if dialog .SUBCLASS_OF_ID ==0xa21c9795 :
            return dialog 
        if dialog .SUBCLASS_OF_ID ==0xc91c90b6 :
            return types .InputDialogPeer (dialog )
    except AttributeError :
        _raise_cast_fail (dialog ,'InputDialogPeer')

    try :
        return types .InputDialogPeer (get_input_peer (dialog ))
    except TypeError :
        pass 

    _raise_cast_fail (dialog ,'InputDialogPeer')

def get_input_document (document ):
    """"""
    try :
        if document .SUBCLASS_OF_ID ==0xf33fdb68 :
            return document 
    except AttributeError :
        _raise_cast_fail (document ,'InputDocument')

    if isinstance (document ,types .Document ):
        return types .InputDocument (
        id =document .id ,access_hash =document .access_hash ,
        file_reference =document .file_reference )

    if isinstance (document ,types .DocumentEmpty ):
        return types .InputDocumentEmpty ()

    if isinstance (document ,types .MessageMediaDocument ):
        return get_input_document (document .document )

    if isinstance (document ,types .Message ):
        return get_input_document (document .media )

    _raise_cast_fail (document ,'InputDocument')

def get_input_photo (photo ):
    """"""
    try :
        if photo .SUBCLASS_OF_ID ==0x846363e0 :
            return photo 
    except AttributeError :
        _raise_cast_fail (photo ,'InputPhoto')

    if isinstance (photo ,types .Message ):
        photo =photo .media 

    if isinstance (photo ,(types .photos .Photo ,types .MessageMediaPhoto )):
        photo =photo .photo 

    if isinstance (photo ,types .Photo ):
        return types .InputPhoto (id =photo .id ,access_hash =photo .access_hash ,
        file_reference =photo .file_reference )

    if isinstance (photo ,types .PhotoEmpty ):
        return types .InputPhotoEmpty ()

    if isinstance (photo ,types .messages .ChatFull ):
        photo =photo .full_chat 

    if isinstance (photo ,types .ChannelFull ):
        return get_input_photo (photo .chat_photo )
    elif isinstance (photo ,types .UserFull ):
        return get_input_photo (photo .profile_photo )
    elif isinstance (photo ,(types .Channel ,types .Chat ,types .User )):
        return get_input_photo (photo .photo )

    if isinstance (photo ,(types .UserEmpty ,types .ChatEmpty ,
    types .ChatForbidden ,types .ChannelForbidden )):
        return types .InputPhotoEmpty ()

    _raise_cast_fail (photo ,'InputPhoto')

def get_input_chat_photo (photo ):
    """"""
    try :
        if photo .SUBCLASS_OF_ID ==0xd4eb2d74 :
            return photo 
        elif photo .SUBCLASS_OF_ID ==0xe7655f1f :
            return types .InputChatUploadedPhoto (photo )
    except AttributeError :
        _raise_cast_fail (photo ,'InputChatPhoto')

    photo =get_input_photo (photo )
    if isinstance (photo ,types .InputPhoto ):
        return types .InputChatPhoto (photo )
    elif isinstance (photo ,types .InputPhotoEmpty ):
        return types .InputChatPhotoEmpty ()

    _raise_cast_fail (photo ,'InputChatPhoto')

def get_input_geo (geo ):
    """"""
    try :
        if geo .SUBCLASS_OF_ID ==0x430d225 :
            return geo 
    except AttributeError :
        _raise_cast_fail (geo ,'InputGeoPoint')

    if isinstance (geo ,types .GeoPoint ):
        return types .InputGeoPoint (lat =geo .lat ,long =geo .long )

    if isinstance (geo ,types .GeoPointEmpty ):
        return types .InputGeoPointEmpty ()

    if isinstance (geo ,types .MessageMediaGeo ):
        return get_input_geo (geo .geo )

    if isinstance (geo ,types .Message ):
        return get_input_geo (geo .media )

    _raise_cast_fail (geo ,'InputGeoPoint')

def get_input_media (
media ,*,
is_photo =False ,attributes =None ,force_document =False ,
voice_note =False ,video_note =False ,supports_streaming =False ,
ttl =None 
):
    """"""
    try :
        if media .SUBCLASS_OF_ID ==0xfaf846f4 :
            return media 
        elif media .SUBCLASS_OF_ID ==0x846363e0 :
            return types .InputMediaPhoto (media ,ttl_seconds =ttl )
        elif media .SUBCLASS_OF_ID ==0xf33fdb68 :
            return types .InputMediaDocument (media ,ttl_seconds =ttl )
    except AttributeError :
        _raise_cast_fail (media ,'InputMedia')

    if isinstance (media ,types .MessageMediaPhoto ):
        return types .InputMediaPhoto (
        id =get_input_photo (media .photo ),
        ttl_seconds =ttl or media .ttl_seconds 
        )

    if isinstance (media ,(types .Photo ,types .photos .Photo ,types .PhotoEmpty )):
        return types .InputMediaPhoto (
        id =get_input_photo (media ),
        ttl_seconds =ttl 
        )

    if isinstance (media ,types .MessageMediaDocument ):
        return types .InputMediaDocument (
        id =get_input_document (media .document ),
        ttl_seconds =ttl or media .ttl_seconds 
        )

    if isinstance (media ,(types .Document ,types .DocumentEmpty )):
        return types .InputMediaDocument (
        id =get_input_document (media ),
        ttl_seconds =ttl 
        )

    if isinstance (media ,(types .InputFile ,types .InputFileBig )):
        if is_photo :
            return types .InputMediaUploadedPhoto (file =media ,ttl_seconds =ttl )
        else :
            attrs ,mime =get_attributes (
            media ,
            attributes =attributes ,
            force_document =force_document ,
            voice_note =voice_note ,
            video_note =video_note ,
            supports_streaming =supports_streaming 
            )
            return types .InputMediaUploadedDocument (
            file =media ,mime_type =mime ,attributes =attrs ,force_file =force_document ,
            ttl_seconds =ttl )

    if isinstance (media ,types .MessageMediaGame ):
        return types .InputMediaGame (id =types .InputGameID (
        id =media .game .id ,
        access_hash =media .game .access_hash 
        ))

    if isinstance (media ,types .MessageMediaContact ):
        return types .InputMediaContact (
        phone_number =media .phone_number ,
        first_name =media .first_name ,
        last_name =media .last_name ,
        vcard =''
        )

    if isinstance (media ,types .MessageMediaGeo ):
        return types .InputMediaGeoPoint (geo_point =get_input_geo (media .geo ))

    if isinstance (media ,types .MessageMediaVenue ):
        return types .InputMediaVenue (
        geo_point =get_input_geo (media .geo ),
        title =media .title ,
        address =media .address ,
        provider =media .provider ,
        venue_id =media .venue_id ,
        venue_type =''
        )

    if isinstance (media ,types .MessageMediaDice ):
        return types .InputMediaDice (media .emoticon )

    if isinstance (media ,(
    types .MessageMediaEmpty ,types .MessageMediaUnsupported ,
    types .ChatPhotoEmpty ,types .UserProfilePhotoEmpty ,
    types .ChatPhoto ,types .UserProfilePhoto )):
        return types .InputMediaEmpty ()

    if isinstance (media ,types .Message ):
        return get_input_media (media .media ,is_photo =is_photo ,ttl =ttl )

    if isinstance (media ,types .MessageMediaPoll ):
        if media .poll .quiz :
            if not media .results .results :

                raise TypeError ('Cannot cast unanswered quiz to any kind of InputMedia.')

            correct_answers =[r .option for r in media .results .results if r .correct ]
        else :
            correct_answers =None 

        return types .InputMediaPoll (
        poll =media .poll ,
        correct_answers =correct_answers ,
        solution =media .results .solution ,
        solution_entities =media .results .solution_entities ,
        )

    if isinstance (media ,types .Poll ):
        return types .InputMediaPoll (media )

    _raise_cast_fail (media ,'InputMedia')

def get_input_message (message ):
    """"""
    try :
        if isinstance (message ,int ):
            return types .InputMessageID (message )
        elif message .SUBCLASS_OF_ID ==0x54b6bcc5 :
            return message 
        elif message .SUBCLASS_OF_ID ==0x790009e3 :
            return types .InputMessageID (message .id )
    except AttributeError :
        pass 

    _raise_cast_fail (message ,'InputMedia')

def get_input_group_call (call ):
    """"""
    try :
        if call .SUBCLASS_OF_ID ==0x58611ab1 :
            return call 
        elif call .SUBCLASS_OF_ID ==0x20b4f320 :
            return types .InputGroupCall (id =call .id ,access_hash =call .access_hash )
    except AttributeError :
        _raise_cast_fail (call ,'InputGroupCall')

def _get_entity_pair (entity_id ,entities ,cache ,
get_input_peer =get_input_peer ):
    """"""
    entity =entities .get (entity_id )
    try :
        input_entity =cache [entity_id ]
    except KeyError :

        try :
            input_entity =get_input_peer (entity )
        except TypeError :
            input_entity =None 

    return entity ,input_entity 

def get_message_id (message ):
    """"""
    if message is None :
        return None 

    if isinstance (message ,int ):
        return message 

    try :
        if message .SUBCLASS_OF_ID ==0x790009e3 :

            return message .id 
    except AttributeError :
        pass 

    raise TypeError ('Invalid message type: {}'.format (type (message )))

def _get_metadata (file ):
    if not hachoir :
        return 

    stream =None 
    close_stream =True 
    seekable =True 

    try :

        if isinstance (file ,str ):
            stream =open (file ,'rb')
        elif isinstance (file ,bytes ):
            stream =io .BytesIO (file )
        else :
            stream =file 
            close_stream =False 
            if getattr (file ,'seekable',None ):
                seekable =file .seekable ()
            else :
                seekable =False 

        if not seekable :
            return None 

        pos =stream .tell ()
        filename =getattr (file ,'name','')

        parser =hachoir .parser .guess .guessParser (hachoir .stream .InputIOStream (
        stream ,
        source ='file:'+filename ,
        tags =[],
        filename =filename 
        ))

        return hachoir .metadata .extractMetadata (parser )

    except Exception as e :
        _log .warning ('Failed to analyze %s: %s %s',file ,e .__class__ ,e )

    finally :
        if stream and close_stream :
            stream .close ()
        elif stream and seekable :
            stream .seek (pos )

def get_attributes (file ,*,attributes =None ,mime_type =None ,
force_document =False ,voice_note =False ,video_note =False ,
supports_streaming =False ,thumb =None ):
    """"""

    name =file if isinstance (file ,str )else getattr (file ,'name','unnamed')
    if mime_type is None :
        mime_type =mimetypes .guess_type (name )[0 ]

    attr_dict ={types .DocumentAttributeFilename :
    types .DocumentAttributeFilename (os .path .basename (name ))}

    if is_audio (file ):
        m =_get_metadata (file )
        if m :
            if m .has ('author'):
                performer =m .get ('author')
            elif m .has ('artist'):
                performer =m .get ('artist')
            else :
                performer =None 

            attr_dict [types .DocumentAttributeAudio ]=types .DocumentAttributeAudio (
            voice =voice_note ,
            title =m .get ('title')if m .has ('title')else None ,
            performer =performer ,
            duration =int (m .get ('duration').seconds 
            if m .has ('duration')else 0 )
            )

    if not force_document and is_video (file ):
        m =_get_metadata (file )
        if m :
            doc =types .DocumentAttributeVideo (
            round_message =video_note ,
            w =m .get ('width')if m .has ('width')else 1 ,
            h =m .get ('height')if m .has ('height')else 1 ,
            duration =int (m .get ('duration').seconds 
            if m .has ('duration')else 1 ),
            supports_streaming =supports_streaming 
            )
        elif thumb :
            t_m =_get_metadata (thumb )
            width =1 
            height =1 
            if t_m and t_m .has ("width"):
                width =t_m .get ("width")
            if t_m and t_m .has ("height"):
                height =t_m .get ("height")

            doc =types .DocumentAttributeVideo (
            0 ,width ,height ,round_message =video_note ,
            supports_streaming =supports_streaming )
        else :
            doc =types .DocumentAttributeVideo (
            0 ,1 ,1 ,round_message =video_note ,
            supports_streaming =supports_streaming )

        attr_dict [types .DocumentAttributeVideo ]=doc 

    if voice_note :
        if types .DocumentAttributeAudio in attr_dict :
            attr_dict [types .DocumentAttributeAudio ].voice =True 
        else :
            attr_dict [types .DocumentAttributeAudio ]=types .DocumentAttributeAudio (0 ,voice =True )

    if attributes :
        for a in attributes :
            attr_dict [type (a )]=a 

    if not mime_type :
        mime_type ='application/octet-stream'

    return list (attr_dict .values ()),mime_type 

def sanitize_parse_mode (mode ):
    """"""
    if not mode :
        return None 

    if callable (mode ):
        class CustomMode :
            @staticmethod 
            def unparse (text ,entities ):
                raise NotImplementedError 

        CustomMode .parse =mode 
        return CustomMode 
    elif (all (hasattr (mode ,x )for x in ('parse','unparse'))
    and all (callable (x )for x in (mode .parse ,mode .unparse ))):
        return mode 
    elif isinstance (mode ,str ):
        try :
            return {
            'md':markdown ,
            'markdown':markdown ,
            'htm':html ,
            'html':html 
            }[mode .lower ()]
        except KeyError :
            raise ValueError ('Unknown parse mode {}'.format (mode ))
    else :
        raise TypeError ('Invalid parse mode type {}'.format (mode ))

def get_input_location (location ):
    """"""
    info =_get_file_info (location )
    return info .dc_id ,info .location 

def _get_file_info (location ):
    try :
        if location .SUBCLASS_OF_ID ==0x1523d462 :
            return _FileInfo (None ,location ,None )
    except AttributeError :
        _raise_cast_fail (location ,'InputFileLocation')

    if isinstance (location ,types .Message ):
        location =location .media 

    if isinstance (location ,types .MessageMediaDocument ):
        location =location .document 
    elif isinstance (location ,types .MessageMediaPhoto ):
        location =location .photo 

    if isinstance (location ,types .Document ):
        return _FileInfo (location .dc_id ,types .InputDocumentFileLocation (
        id =location .id ,
        access_hash =location .access_hash ,
        file_reference =location .file_reference ,
        thumb_size =''
        ),location .size )
    elif isinstance (location ,types .Photo ):
        return _FileInfo (location .dc_id ,types .InputPhotoFileLocation (
        id =location .id ,
        access_hash =location .access_hash ,
        file_reference =location .file_reference ,
        thumb_size =location .sizes [-1 ].type 
        ),_photo_size_byte_count (location .sizes [-1 ]))

    _raise_cast_fail (location ,'InputFileLocation')

def _get_extension (file ):
    """"""
    if isinstance (file ,str ):
        return os .path .splitext (file )[-1 ]
    elif isinstance (file ,pathlib .Path ):
        return file .suffix 
    elif isinstance (file ,bytes ):
        kind =imghdr .what (io .BytesIO (file ))
        return ('.'+kind )if kind else ''
    elif isinstance (file ,io .IOBase )and not isinstance (file ,io .TextIOBase )and file .seekable ():
        kind =imghdr .what (file )
        return ('.'+kind )if kind is not None else ''
    elif getattr (file ,'name',None ):

        return _get_extension (file .name )
    else :

        return get_extension (file )

def is_image (file ):
    """"""
    match =re .match (r'\.(png|jpe?g)',_get_extension (file ),re .IGNORECASE )
    if match :
        return True 
    else :
        return isinstance (resolve_bot_file_id (file ),types .Photo )

def is_gif (file ):
    """"""
    return re .match (r'\.gif',_get_extension (file ),re .IGNORECASE )

def is_audio (file ):
    """"""
    ext =_get_extension (file )
    if not ext :
        metadata =_get_metadata (file )
        if metadata and metadata .has ('mime_type'):
            return metadata .get ('mime_type').startswith ('audio/')
        else :
            return False 
    else :
        file ='a'+ext 
        return (mimetypes .guess_type (file )[0 ]or '').startswith ('audio/')

def is_video (file ):
    """"""
    ext =_get_extension (file )
    if not ext :
        metadata =_get_metadata (file )
        if metadata and metadata .has ('mime_type'):
            return metadata .get ('mime_type').startswith ('video/')
        else :
            return False 
    else :
        file ='a'+ext 
        return (mimetypes .guess_type (file )[0 ]or '').startswith ('video/')

def is_list_like (obj ):
    """"""
    return isinstance (obj ,(list ,tuple ,set ,dict ,GeneratorType ))

def parse_phone (phone ):
    """"""
    if isinstance (phone ,int ):
        return str (phone )
    else :
        phone =re .sub (r'[+()\s-]','',str (phone ))
        if phone .isdigit ():
            return phone 

def parse_username (username ):
    """"""
    username =username .strip ()
    m =USERNAME_RE .match (username )or TG_JOIN_RE .match (username )
    if m :
        username =username [m .end ():]
        is_invite =bool (m .group (1 ))
        if is_invite :
            return username ,True 
        else :
            username =username .rstrip ('/')

    if VALID_USERNAME_RE .match (username ):
        return username .lower (),False 
    else :
        return None ,False 

def get_inner_text (text ,entities ):
    """"""
    text =add_surrogate (text )
    result =[]
    for e in entities :
        start =e .offset 
        end =e .offset +e .length 
        result .append (del_surrogate (text [start :end ]))

    return result 

def get_peer (peer ):
    try :
        if isinstance (peer ,int ):
            pid ,cls =resolve_id (peer )
            return cls (pid )
        elif peer .SUBCLASS_OF_ID ==0x2d45687 :
            return peer 
        elif isinstance (peer ,(
        types .contacts .ResolvedPeer ,types .InputNotifyPeer ,
        types .TopPeer ,types .Dialog ,types .DialogPeer )):
            return peer .peer 
        elif isinstance (peer ,types .ChannelFull ):
            return types .PeerChannel (peer .id )
        elif isinstance (peer ,types .UserEmpty ):
            return types .PeerUser (peer .id )
        elif isinstance (peer ,types .ChatEmpty ):
            return types .PeerChat (peer .id )

        if peer .SUBCLASS_OF_ID in (0x7d7c6f86 ,0xd9c7fc18 ):

            return types .PeerUser (peer .user_id )

        peer =get_input_peer (peer ,allow_self =False ,check_hash =False )
        if isinstance (peer ,(types .InputPeerUser ,types .InputPeerUserFromMessage )):
            return types .PeerUser (peer .user_id )
        elif isinstance (peer ,types .InputPeerChat ):
            return types .PeerChat (peer .chat_id )
        elif isinstance (peer ,(types .InputPeerChannel ,types .InputPeerChannelFromMessage )):
            return types .PeerChannel (peer .channel_id )
    except (AttributeError ,TypeError ):
        pass 
    _raise_cast_fail (peer ,'Peer')

def get_peer_id (peer ,add_mark =True ):
    """"""

    if isinstance (peer ,int ):
        return peer if add_mark else resolve_id (peer )[0 ]

    if isinstance (peer ,types .InputPeerSelf ):
        _raise_cast_fail (peer ,'int (you might want to use client.get_peer_id)')

    try :
        peer =get_peer (peer )
    except TypeError :
        _raise_cast_fail (peer ,'int')

    if isinstance (peer ,types .PeerUser ):
        return peer .user_id 
    elif isinstance (peer ,types .PeerChat ):

        if not (0 <peer .chat_id <=9999999999 ):
            peer .chat_id =resolve_id (peer .chat_id )[0 ]

        return -peer .chat_id if add_mark else peer .chat_id 
    else :

        if not (0 <peer .channel_id <=9999999999 ):
            peer .channel_id =resolve_id (peer .channel_id )[0 ]

        if not add_mark :
            return peer .channel_id 

        return -(1000000000000 +peer .channel_id )

def resolve_id (marked_id ):
    """"""
    if marked_id >=0 :
        return marked_id ,types .PeerUser 

    marked_id =-marked_id 
    if marked_id >1000000000000 :
        marked_id -=1000000000000 
        return marked_id ,types .PeerChannel 
    else :
        return marked_id ,types .PeerChat 

def _rle_decode (data ):
    """"""
    if not data :
        return data 

    new =b''
    last =b''
    for cur in data :
        if last ==b'\0':
            new +=last *cur 
            last =b''
        else :
            new +=last 
            last =bytes ([cur ])

    return new +last 

def _rle_encode (string ):
    new =b''
    count =0 
    for cur in string :
        if not cur :
            count +=1 
        else :
            if count :
                new +=b'\0'+bytes ([count ])
                count =0 

            new +=bytes ([cur ])
    return new 

def _decode_telegram_base64 (string ):
    """"""
    try :
        return base64 .urlsafe_b64decode (string +'='*(len (string )%4 ))
    except (binascii .Error ,ValueError ,TypeError ):
        return None 

def _encode_telegram_base64 (string ):
    """"""
    try :
        return base64 .urlsafe_b64encode (string ).rstrip (b'=').decode ('ascii')
    except (binascii .Error ,ValueError ,TypeError ):
        return None 

def resolve_bot_file_id (file_id ):
    """"""
    data =_rle_decode (_decode_telegram_base64 (file_id ))
    if not data :
        return None 

    data ,version =data [:-1 ],data [-1 ]
    if version not in (2 ,4 ):
        return None 

    if (version ==2 and len (data )==24 )or (version ==4 and len (data )==25 ):
        if version ==2 :
            file_type ,dc_id ,media_id ,access_hash =struct .unpack ('<iiqq',data )

        else :

            file_type ,dc_id ,media_id ,access_hash ,_ =struct .unpack ('<iiqqb',data )

        if not (1 <=dc_id <=5 ):

            return None 

        attributes =[]
        if file_type ==3 or file_type ==9 :
            attributes .append (types .DocumentAttributeAudio (
            duration =0 ,
            voice =file_type ==3 
            ))
        elif file_type ==4 or file_type ==13 :
            attributes .append (types .DocumentAttributeVideo (
            duration =0 ,
            w =0 ,
            h =0 ,
            round_message =file_type ==13 
            ))

        elif file_type ==8 :
            attributes .append (types .DocumentAttributeSticker (
            alt ='',
            stickerset =types .InputStickerSetEmpty ()
            ))
        elif file_type ==10 :
            attributes .append (types .DocumentAttributeAnimated ())

        return types .Document (
        id =media_id ,
        access_hash =access_hash ,
        date =None ,
        mime_type ='',
        size =0 ,
        thumbs =None ,
        dc_id =dc_id ,
        attributes =attributes ,
        file_reference =b''
        )
    elif (version ==2 and len (data )==44 )or (version ==4 and len (data )in (49 ,77 )):
        if version ==2 :
            (file_type ,dc_id ,media_id ,access_hash ,
            volume_id ,secret ,local_id )=struct .unpack ('<iiqqqqi',data )

        elif len (data )==49 :

            (file_type ,dc_id ,media_id ,access_hash ,
            volume_id ,secret ,local_id ,_ )=struct .unpack ('<iiqqqqi5s',data )
        elif len (data )==77 :

            (file_type ,dc_id ,_ ,media_id ,access_hash ,volume_id ,_ ,local_id ,_ )=struct .unpack ('<ii28sqqq12sib',data )
        else :
            return None 

        if not (1 <=dc_id <=5 ):
            return None 

        photo_size ='s'if media_id or access_hash else 'x'
        return types .Photo (
        id =media_id ,
        access_hash =access_hash ,
        file_reference =b'',
        date =None ,
        sizes =[types .PhotoSize (
        type =photo_size ,
        w =0 ,
        h =0 ,
        size =0 
        )],
        dc_id =dc_id ,
        has_stickers =None 
        )

def pack_bot_file_id (file ):
    """"""
    if isinstance (file ,types .MessageMediaDocument ):
        file =file .document 
    elif isinstance (file ,types .MessageMediaPhoto ):
        file =file .photo 

    if isinstance (file ,types .Document ):
        file_type =5 
        for attribute in file .attributes :
            if isinstance (attribute ,types .DocumentAttributeAudio ):
                file_type =3 if attribute .voice else 9 
            elif isinstance (attribute ,types .DocumentAttributeVideo ):
                file_type =13 if attribute .round_message else 4 
            elif isinstance (attribute ,types .DocumentAttributeSticker ):
                file_type =8 
            elif isinstance (attribute ,types .DocumentAttributeAnimated ):
                file_type =10 
            else :
                continue 
            break 

        return _encode_telegram_base64 (_rle_encode (struct .pack (
        '<iiqqb',file_type ,file .dc_id ,file .id ,file .access_hash ,2 )))

    elif isinstance (file ,types .Photo ):
        size =next ((x for x in reversed (file .sizes )if isinstance (
        x ,(types .PhotoSize ,types .PhotoCachedSize ))),None )

        if not size :
            return None 

        size =size .location 
        return _encode_telegram_base64 (_rle_encode (struct .pack (
        '<iiqqqqib',2 ,file .dc_id ,file .id ,file .access_hash ,
        size .volume_id ,0 ,size .local_id ,2 
        )))
    else :
        return None 

def resolve_invite_link (link ):
    """"""
    link_hash ,is_link =parse_username (link )
    if not is_link :

        link_hash =link 

    if re .match (r'[a-fA-F\d]+',link_hash )and len (link_hash )in (24 ,32 ):
        payload =bytes .fromhex (link_hash )
    else :
        payload =_decode_telegram_base64 (link_hash )

    try :
        if len (payload )==12 :
            return (0 ,*struct .unpack ('>LQ',payload ))
        elif len (payload )==16 :
            return struct .unpack ('>LLQ',payload )
        else :
            pass 
    except (struct .error ,TypeError ):
        pass 
    return None ,None ,None 

def resolve_inline_message_id (inline_msg_id ):
    """"""
    try :
        dc_id ,message_id ,pid ,access_hash =struct .unpack ('<iiiq',_decode_telegram_base64 (inline_msg_id ))
        peer =types .PeerChannel (-pid )if pid <0 else types .PeerUser (pid )
        return message_id ,peer ,dc_id ,access_hash 
    except (struct .error ,TypeError ):
        return None ,None ,None ,None 

def get_appropriated_part_size (file_size ):
    """"""
    if file_size <=104857600 :
        return 128 
    if file_size <=786432000 :
        return 256 
    return 512 

def encode_waveform (waveform ):
    """"""
    bits_count =len (waveform )*5 
    bytes_count =(bits_count +7 )//8 
    result =bytearray (bytes_count +1 )

    for i in range (len (waveform )):
        byte_index ,bit_shift =divmod (i *5 ,8 )
        value =(waveform [i ]&0b00011111 )<<bit_shift 

        or_what =struct .unpack ('<H',(result [byte_index :byte_index +2 ]))[0 ]
        or_what |=value 
        result [byte_index :byte_index +2 ]=struct .pack ('<H',or_what )

    return bytes (result [:bytes_count ])

def decode_waveform (waveform ):
    """"""
    bit_count =len (waveform )*8 
    value_count =bit_count //5 
    if value_count ==0 :
        return b''

    result =bytearray (value_count )
    for i in range (value_count -1 ):
        byte_index ,bit_shift =divmod (i *5 ,8 )
        value =struct .unpack ('<H',waveform [byte_index :byte_index +2 ])[0 ]
        result [i ]=(value >>bit_shift )&0b00011111 

    byte_index ,bit_shift =divmod (value_count -1 ,8 )
    if byte_index ==len (waveform )-1 :
        value =waveform [byte_index ]
    else :
        value =struct .unpack ('<H',waveform [byte_index :byte_index +2 ])[0 ]

    result [value_count -1 ]=(value >>bit_shift )&0b00011111 
    return bytes (result )

def split_text (text ,entities ,*,limit =4096 ,max_entities =100 ,split_at =(r'\n',r'\s','.')):
    """"""

    def update (ent ,**updates ):
        kwargs =ent .to_dict ()
        del kwargs ['_']
        kwargs .update (updates )
        return ent .__class__ (**kwargs )

    text =add_surrogate (text )
    split_at =tuple (map (re .compile ,split_at ))

    while True :
        if len (entities )>max_entities :
            last_ent =entities [max_entities -1 ]
            cur_limit =min (limit ,last_ent .offset +last_ent .length )
        else :
            cur_limit =limit 

        if len (text )<=cur_limit :
            break 

        for split in split_at :
            for i in reversed (range (cur_limit )):
                m =split .match (text ,pos =i )
                if m :
                    cur_text ,new_text =text [:m .end ()],text [m .end ():]
                    cur_ent ,new_ent =[],[]
                    for ent in entities :
                        if ent .offset <m .end ():
                            if ent .offset +ent .length >m .end ():
                                cur_ent .append (update (ent ,length =m .end ()-ent .offset ))
                                new_ent .append (update (ent ,offset =0 ,length =ent .offset +ent .length -m .end ()))
                            else :
                                cur_ent .append (ent )
                        else :
                            new_ent .append (update (ent ,offset =ent .offset -m .end ()))

                    yield del_surrogate (cur_text ),cur_ent 
                    text ,entities =new_text ,new_ent 
                    break 
            else :
                continue 
            break 
        else :

            break 

    yield del_surrogate (text ),entities 

class AsyncClassWrapper :
    def __init__ (self ,wrapped ):
        self .wrapped =wrapped 

    def __getattr__ (self ,item ):
        w =getattr (self .wrapped ,item )
        async def wrapper (*args ,**kwargs ):
            val =w (*args ,**kwargs )
            return await val if inspect .isawaitable (val )else val 

        if callable (w ):
            return wrapper 
        else :
            return w 

def stripped_photo_to_jpg (stripped ):
    """"""

    if len (stripped )<3 or stripped [0 ]!=1 :
        return stripped 

    header =bytearray (b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00(\x1c\x1e#\x1e\x19(#!#-+(0<dA<77<{X]Id\x91\x80\x99\x96\x8f\x80\x8c\x8a\xa0\xb4\xe6\xc3\xa0\xaa\xda\xad\x8a\x8c\xc8\xff\xcb\xda\xee\xf5\xff\xff\xff\x9b\xc1\xff\xff\xff\xfa\xff\xe6\xfd\xff\xf8\xff\xdb\x00C\x01+--<5<vAAv\xf8\xa5\x8c\xa5\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xff\xc0\x00\x11\x08\x00\x00\x00\x00\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02w\x00\x01\x02\x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\xf0\x15br\xd1\n\x16$4\xe1%\xf1\x17\x18\x19\x1a&\'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00')
    footer =b"\xff\xd9"
    header [164 ]=stripped [1 ]
    header [166 ]=stripped [2 ]
    return bytes (header )+stripped [3 :]+footer 

def _photo_size_byte_count (size ):
    if isinstance (size ,types .PhotoSize ):
        return size .size 
    elif isinstance (size ,types .PhotoStrippedSize ):
        if len (size .bytes )<3 or size .bytes [0 ]!=1 :
            return len (size .bytes )

        return len (size .bytes )+622 
    elif isinstance (size ,types .PhotoCachedSize ):
        return len (size .bytes )
    elif isinstance (size ,types .PhotoSizeEmpty ):
        return 0 
    elif isinstance (size ,types .PhotoSizeProgressive ):
        return max (size .sizes )
    else :
        return None 

def convert_reaction (
reaction :"typing.Optional[hints.Reaction]"=None ,
)->"typing.Optional[typing.Union[typing.List[types.ReactionEmoji], typing.List[types.ReactionCustomEmoji]]]":
    """"""
    if not reaction :
        return None 

    if isinstance (reaction ,str ):
        reaction =types .ReactionEmoji (reaction )

    if isinstance (reaction ,int ):
        reaction =types .ReactionCustomEmoji (reaction )

    if isinstance (reaction ,(types .ReactionEmoji ,types .ReactionCustomEmoji )):
        reaction =[reaction ]

    for r in reaction :
        if isinstance (r ,str ):
            reaction [reaction .index (r )]=types .ReactionEmoji (r )

        if isinstance (r ,int ):
            reaction [reaction .index (r )]=types .ReactionCustomEmoji (r )

    return reaction 

def get_input_reply_to (
entity :typing .Optional [typing .Union [int ,types .InputUser ,types .InputChannel ]]=None ,
reply_to :typing .Optional [typing .Union [int ,types .Message ,types .StoryItem ]]=None ,
top_msg_id :typing .Optional [int ]=None ,
stories :bool =False ,
):
    """"""
    if isinstance (reply_to ,types .StoryItem ):
        return types .InputReplyToStory (entity ,reply_to .id )

    if isinstance (reply_to ,types .Message ):
        return types .InputReplyToMessage (
        reply_to .id ,
        top_msg_id or getattr (reply_to .reply_to ,"reply_to_msg_id",None ),
        )

    if isinstance (reply_to ,int ):
        return (
        types .InputReplyToStory (entity ,reply_to )
        if stories 
        else types .InputReplyToMessage (reply_to ,top_msg_id )
        )

    return reply_to or None 

def get_input_story_id (
story :'hints.StoryItemLike',
)->int :
    """"""
    return story if isinstance (story ,int )else story .id 
