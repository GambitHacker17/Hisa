
import logging 
from datetime import datetime 
from functools import partial 
from typing import List ,Match ,Union ,BinaryIO ,Optional ,Callable 

import hisapyro 
from hisapyro import raw ,enums 
from hisapyro import types 
from hisapyro import utils 
from hisapyro .errors import MessageIdsEmpty ,PeerIdInvalid 
from hisapyro .parser import utils as parser_utils ,Parser 
from ..object import Object 
from ..update import Update 

log =logging .getLogger (__name__ )

class Str (str ):
    def __init__ (self ,*args ):
        super ().__init__ ()

        self .entities =None 

    def init (self ,entities ):
        self .entities =entities 

        return self 

    @property 
    def markdown (self ):
        return Parser .unparse (self ,self .entities ,False )

    @property 
    def html (self ):
        return Parser .unparse (self ,self .entities ,True )

    def __getitem__ (self ,item ):
        return parser_utils .remove_surrogates (parser_utils .add_surrogates (self )[item ])

class Message (Object ,Update ):
    """"""

    def __init__ (
    self ,
    *,
    client :"hisapyro.Client"=None ,
    id :int ,
    from_user :"types.User"=None ,
    sender_chat :"types.Chat"=None ,
    date :datetime =None ,
    chat :"types.Chat"=None ,
    forward_from :"types.User"=None ,
    forward_sender_name :str =None ,
    forward_from_chat :"types.Chat"=None ,
    forward_from_message_id :int =None ,
    forward_signature :str =None ,
    forward_date :datetime =None ,
    reply_to_message_id :int =None ,
    reply_to_top_message_id :int =None ,
    reply_to_message :"Message"=None ,
    mentioned :bool =None ,
    empty :bool =None ,
    service :"enums.MessageServiceType"=None ,
    scheduled :bool =None ,
    from_scheduled :bool =None ,
    media :"enums.MessageMediaType"=None ,
    edit_date :datetime =None ,
    media_group_id :str =None ,
    author_signature :str =None ,
    has_protected_content :bool =None ,
    has_media_spoiler :bool =None ,
    text :Str =None ,
    entities :List ["types.MessageEntity"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    audio :"types.Audio"=None ,
    document :"types.Document"=None ,
    photo :"types.Photo"=None ,
    sticker :"types.Sticker"=None ,
    animation :"types.Animation"=None ,
    game :"types.Game"=None ,
    video :"types.Video"=None ,
    voice :"types.Voice"=None ,
    video_note :"types.VideoNote"=None ,
    caption :Str =None ,
    contact :"types.Contact"=None ,
    location :"types.Location"=None ,
    venue :"types.Venue"=None ,
    web_page :"types.WebPage"=None ,
    poll :"types.Poll"=None ,
    dice :"types.Dice"=None ,
    new_chat_members :List ["types.User"]=None ,
    left_chat_member :"types.User"=None ,
    new_chat_title :str =None ,
    new_chat_photo :"types.Photo"=None ,
    delete_chat_photo :bool =None ,
    group_chat_created :bool =None ,
    supergroup_chat_created :bool =None ,
    channel_chat_created :bool =None ,
    migrate_to_chat_id :int =None ,
    migrate_from_chat_id :int =None ,
    pinned_message :"Message"=None ,
    game_high_score :int =None ,
    views :int =None ,
    forwards :int =None ,
    via_bot :"types.User"=None ,
    outgoing :bool =None ,
    matches :List [Match ]=None ,
    command :List [str ]=None ,
    video_chat_scheduled :"types.VideoChatScheduled"=None ,
    video_chat_started :"types.VideoChatStarted"=None ,
    video_chat_ended :"types.VideoChatEnded"=None ,
    video_chat_members_invited :"types.VideoChatMembersInvited"=None ,
    web_app_data :"types.WebAppData"=None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    reactions :List ["types.Reaction"]=None 
    ):
        super ().__init__ (client )

        self .id =id 
        self .from_user =from_user 
        self .sender_chat =sender_chat 
        self .date =date 
        self .chat =chat 
        self .forward_from =forward_from 
        self .forward_sender_name =forward_sender_name 
        self .forward_from_chat =forward_from_chat 
        self .forward_from_message_id =forward_from_message_id 
        self .forward_signature =forward_signature 
        self .forward_date =forward_date 
        self .reply_to_message_id =reply_to_message_id 
        self .reply_to_top_message_id =reply_to_top_message_id 
        self .reply_to_message =reply_to_message 
        self .mentioned =mentioned 
        self .empty =empty 
        self .service =service 
        self .scheduled =scheduled 
        self .from_scheduled =from_scheduled 
        self .media =media 
        self .edit_date =edit_date 
        self .media_group_id =media_group_id 
        self .author_signature =author_signature 
        self .has_protected_content =has_protected_content 
        self .has_media_spoiler =has_media_spoiler 
        self .text =text 
        self .entities =entities 
        self .caption_entities =caption_entities 
        self .audio =audio 
        self .document =document 
        self .photo =photo 
        self .sticker =sticker 
        self .animation =animation 
        self .game =game 
        self .video =video 
        self .voice =voice 
        self .video_note =video_note 
        self .caption =caption 
        self .contact =contact 
        self .location =location 
        self .venue =venue 
        self .web_page =web_page 
        self .poll =poll 
        self .dice =dice 
        self .new_chat_members =new_chat_members 
        self .left_chat_member =left_chat_member 
        self .new_chat_title =new_chat_title 
        self .new_chat_photo =new_chat_photo 
        self .delete_chat_photo =delete_chat_photo 
        self .group_chat_created =group_chat_created 
        self .supergroup_chat_created =supergroup_chat_created 
        self .channel_chat_created =channel_chat_created 
        self .migrate_to_chat_id =migrate_to_chat_id 
        self .migrate_from_chat_id =migrate_from_chat_id 
        self .pinned_message =pinned_message 
        self .game_high_score =game_high_score 
        self .views =views 
        self .forwards =forwards 
        self .via_bot =via_bot 
        self .outgoing =outgoing 
        self .matches =matches 
        self .command =command 
        self .reply_markup =reply_markup 
        self .video_chat_scheduled =video_chat_scheduled 
        self .video_chat_started =video_chat_started 
        self .video_chat_ended =video_chat_ended 
        self .video_chat_members_invited =video_chat_members_invited 
        self .web_app_data =web_app_data 
        self .reactions =reactions 

    @staticmethod 
    async def _parse (
    client :"hisapyro.Client",
    message :raw .base .Message ,
    users :dict ,
    chats :dict ,
    is_scheduled :bool =False ,
    replies :int =1 
    ):
        if isinstance (message ,raw .types .MessageEmpty ):
            return Message (id =message .id ,empty =True ,client =client )

        from_id =utils .get_raw_peer_id (message .from_id )
        peer_id =utils .get_raw_peer_id (message .peer_id )
        user_id =from_id or peer_id 

        if isinstance (message .from_id ,raw .types .PeerUser )and isinstance (message .peer_id ,raw .types .PeerUser ):
            if from_id not in users or peer_id not in users :
                try :
                    r =await client .invoke (
                    raw .functions .users .GetUsers (
                    id =[
                    await client .resolve_peer (from_id ),
                    await client .resolve_peer (peer_id )
                    ]
                    )
                    )
                except PeerIdInvalid :
                    pass 
                else :
                    users .update ({i .id :i for i in r })

        if isinstance (message ,raw .types .MessageService ):
            action =message .action 

            new_chat_members =None 
            left_chat_member =None 
            new_chat_title =None 
            delete_chat_photo =None 
            migrate_to_chat_id =None 
            migrate_from_chat_id =None 
            group_chat_created =None 
            channel_chat_created =None 
            new_chat_photo =None 
            video_chat_scheduled =None 
            video_chat_started =None 
            video_chat_ended =None 
            video_chat_members_invited =None 
            web_app_data =None 

            service_type =None 

            if isinstance (action ,raw .types .MessageActionChatAddUser ):
                new_chat_members =[types .User ._parse (client ,users [i ])for i in action .users ]
                service_type =enums .MessageServiceType .NEW_CHAT_MEMBERS 
            elif isinstance (action ,raw .types .MessageActionChatJoinedByLink ):
                new_chat_members =[types .User ._parse (client ,users [utils .get_raw_peer_id (message .from_id )])]
                service_type =enums .MessageServiceType .NEW_CHAT_MEMBERS 
            elif isinstance (action ,raw .types .MessageActionChatDeleteUser ):
                left_chat_member =types .User ._parse (client ,users [action .user_id ])
                service_type =enums .MessageServiceType .LEFT_CHAT_MEMBERS 
            elif isinstance (action ,raw .types .MessageActionChatEditTitle ):
                new_chat_title =action .title 
                service_type =enums .MessageServiceType .NEW_CHAT_TITLE 
            elif isinstance (action ,raw .types .MessageActionChatDeletePhoto ):
                delete_chat_photo =True 
                service_type =enums .MessageServiceType .DELETE_CHAT_PHOTO 
            elif isinstance (action ,raw .types .MessageActionChatMigrateTo ):
                migrate_to_chat_id =action .channel_id 
                service_type =enums .MessageServiceType .MIGRATE_TO_CHAT_ID 
            elif isinstance (action ,raw .types .MessageActionChannelMigrateFrom ):
                migrate_from_chat_id =action .chat_id 
                service_type =enums .MessageServiceType .MIGRATE_FROM_CHAT_ID 
            elif isinstance (action ,raw .types .MessageActionChatCreate ):
                group_chat_created =True 
                service_type =enums .MessageServiceType .GROUP_CHAT_CREATED 
            elif isinstance (action ,raw .types .MessageActionChannelCreate ):
                channel_chat_created =True 
                service_type =enums .MessageServiceType .CHANNEL_CHAT_CREATED 
            elif isinstance (action ,raw .types .MessageActionChatEditPhoto ):
                new_chat_photo =types .Photo ._parse (client ,action .photo )
                service_type =enums .MessageServiceType .NEW_CHAT_PHOTO 
            elif isinstance (action ,raw .types .MessageActionGroupCallScheduled ):
                video_chat_scheduled =types .VideoChatScheduled ._parse (action )
                service_type =enums .MessageServiceType .VIDEO_CHAT_SCHEDULED 
            elif isinstance (action ,raw .types .MessageActionGroupCall ):
                if action .duration :
                    video_chat_ended =types .VideoChatEnded ._parse (action )
                    service_type =enums .MessageServiceType .VIDEO_CHAT_ENDED 
                else :
                    video_chat_started =types .VideoChatStarted ()
                    service_type =enums .MessageServiceType .VIDEO_CHAT_STARTED 
            elif isinstance (action ,raw .types .MessageActionInviteToGroupCall ):
                video_chat_members_invited =types .VideoChatMembersInvited ._parse (client ,action ,users )
                service_type =enums .MessageServiceType .VIDEO_CHAT_MEMBERS_INVITED 
            elif isinstance (action ,raw .types .MessageActionWebViewDataSentMe ):
                web_app_data =types .WebAppData ._parse (action )
                service_type =enums .MessageServiceType .WEB_APP_DATA 

            from_user =types .User ._parse (client ,users .get (user_id ,None ))
            sender_chat =types .Chat ._parse (client ,message ,users ,chats ,is_chat =False )if not from_user else None 

            parsed_message =Message (
            id =message .id ,
            date =utils .timestamp_to_datetime (message .date ),
            chat =types .Chat ._parse (client ,message ,users ,chats ,is_chat =True ),
            from_user =from_user ,
            sender_chat =sender_chat ,
            service =service_type ,
            new_chat_members =new_chat_members ,
            left_chat_member =left_chat_member ,
            new_chat_title =new_chat_title ,
            new_chat_photo =new_chat_photo ,
            delete_chat_photo =delete_chat_photo ,
            migrate_to_chat_id =utils .get_channel_id (migrate_to_chat_id )if migrate_to_chat_id else None ,
            migrate_from_chat_id =-migrate_from_chat_id if migrate_from_chat_id else None ,
            group_chat_created =group_chat_created ,
            channel_chat_created =channel_chat_created ,
            video_chat_scheduled =video_chat_scheduled ,
            video_chat_started =video_chat_started ,
            video_chat_ended =video_chat_ended ,
            video_chat_members_invited =video_chat_members_invited ,
            web_app_data =web_app_data ,
            client =client 

            )

            if isinstance (action ,raw .types .MessageActionPinMessage ):
                try :
                    parsed_message .pinned_message =await client .get_messages (
                    parsed_message .chat .id ,
                    reply_to_message_ids =message .id ,
                    replies =0 
                    )

                    parsed_message .service =enums .MessageServiceType .PINNED_MESSAGE 
                except MessageIdsEmpty :
                    pass 

            if isinstance (action ,raw .types .MessageActionGameScore ):
                parsed_message .game_high_score =types .GameHighScore ._parse_action (client ,message ,users )

                if message .reply_to and replies :
                    try :
                        parsed_message .reply_to_message =await client .get_messages (
                        parsed_message .chat .id ,
                        reply_to_message_ids =message .id ,
                        replies =0 
                        )

                        parsed_message .service =enums .MessageServiceType .GAME_HIGH_SCORE 
                    except MessageIdsEmpty :
                        pass 

            client .message_cache [(parsed_message .chat .id ,parsed_message .id )]=parsed_message 

            return parsed_message 

        if isinstance (message ,raw .types .Message ):
            entities =[types .MessageEntity ._parse (client ,entity ,users )for entity in message .entities ]
            entities =types .List (filter (lambda x :x is not None ,entities ))

            forward_from =None 
            forward_sender_name =None 
            forward_from_chat =None 
            forward_from_message_id =None 
            forward_signature =None 
            forward_date =None 

            forward_header =message .fwd_from 

            if forward_header :
                forward_date =utils .timestamp_to_datetime (forward_header .date )

                if forward_header .from_id :
                    raw_peer_id =utils .get_raw_peer_id (forward_header .from_id )
                    peer_id =utils .get_peer_id (forward_header .from_id )

                    if peer_id >0 :
                        forward_from =types .User ._parse (client ,users [raw_peer_id ])
                    else :
                        forward_from_chat =types .Chat ._parse_channel_chat (client ,chats [raw_peer_id ])
                        forward_from_message_id =forward_header .channel_post 
                        forward_signature =forward_header .post_author 
                elif forward_header .from_name :
                    forward_sender_name =forward_header .from_name 

            photo =None 
            location =None 
            contact =None 
            venue =None 
            game =None 
            audio =None 
            voice =None 
            animation =None 
            video =None 
            video_note =None 
            sticker =None 
            document =None 
            web_page =None 
            poll =None 
            dice =None 

            media =message .media 
            media_type =None 
            has_media_spoiler =None 

            if media :
                if isinstance (media ,raw .types .MessageMediaPhoto ):
                    photo =types .Photo ._parse (client ,media .photo ,media .ttl_seconds )
                    media_type =enums .MessageMediaType .PHOTO 
                    has_media_spoiler =media .spoiler 
                elif isinstance (media ,raw .types .MessageMediaGeo ):
                    location =types .Location ._parse (client ,media .geo )
                    media_type =enums .MessageMediaType .LOCATION 
                elif isinstance (media ,raw .types .MessageMediaContact ):
                    contact =types .Contact ._parse (client ,media )
                    media_type =enums .MessageMediaType .CONTACT 
                elif isinstance (media ,raw .types .MessageMediaVenue ):
                    venue =types .Venue ._parse (client ,media )
                    media_type =enums .MessageMediaType .VENUE 
                elif isinstance (media ,raw .types .MessageMediaGame ):
                    game =types .Game ._parse (client ,message )
                    media_type =enums .MessageMediaType .GAME 
                elif isinstance (media ,raw .types .MessageMediaDocument ):
                    doc =media .document 

                    if isinstance (doc ,raw .types .Document ):
                        attributes ={type (i ):i for i in doc .attributes }

                        file_name =getattr (
                        attributes .get (
                        raw .types .DocumentAttributeFilename ,None 
                        ),"file_name",None 
                        )

                        if raw .types .DocumentAttributeAnimated in attributes :
                            video_attributes =attributes .get (raw .types .DocumentAttributeVideo ,None )
                            animation =types .Animation ._parse (client ,doc ,video_attributes ,file_name )
                            media_type =enums .MessageMediaType .ANIMATION 
                            has_media_spoiler =media .spoiler 
                        elif raw .types .DocumentAttributeSticker in attributes :
                            sticker =await types .Sticker ._parse (client ,doc ,attributes )
                            media_type =enums .MessageMediaType .STICKER 
                        elif raw .types .DocumentAttributeVideo in attributes :
                            video_attributes =attributes [raw .types .DocumentAttributeVideo ]

                            if video_attributes .round_message :
                                video_note =types .VideoNote ._parse (client ,doc ,video_attributes )
                                media_type =enums .MessageMediaType .VIDEO_NOTE 
                            else :
                                video =types .Video ._parse (client ,doc ,video_attributes ,file_name ,media .ttl_seconds )
                                media_type =enums .MessageMediaType .VIDEO 
                                has_media_spoiler =media .spoiler 
                        elif raw .types .DocumentAttributeAudio in attributes :
                            audio_attributes =attributes [raw .types .DocumentAttributeAudio ]

                            if audio_attributes .voice :
                                voice =types .Voice ._parse (client ,doc ,audio_attributes )
                                media_type =enums .MessageMediaType .VOICE 
                            else :
                                audio =types .Audio ._parse (client ,doc ,audio_attributes ,file_name )
                                media_type =enums .MessageMediaType .AUDIO 
                        else :
                            document =types .Document ._parse (client ,doc ,file_name )
                            media_type =enums .MessageMediaType .DOCUMENT 
                elif isinstance (media ,raw .types .MessageMediaWebPage ):
                    if isinstance (media .webpage ,raw .types .WebPage ):
                        web_page =types .WebPage ._parse (client ,media .webpage )
                        media_type =enums .MessageMediaType .WEB_PAGE 
                    else :
                        media =None 
                elif isinstance (media ,raw .types .MessageMediaPoll ):
                    poll =types .Poll ._parse (client ,media )
                    media_type =enums .MessageMediaType .POLL 
                elif isinstance (media ,raw .types .MessageMediaDice ):
                    dice =types .Dice ._parse (client ,media )
                    media_type =enums .MessageMediaType .DICE 
                else :
                    media =None 

            reply_markup =message .reply_markup 

            if reply_markup :
                if isinstance (reply_markup ,raw .types .ReplyKeyboardForceReply ):
                    reply_markup =types .ForceReply .read (reply_markup )
                elif isinstance (reply_markup ,raw .types .ReplyKeyboardMarkup ):
                    reply_markup =types .ReplyKeyboardMarkup .read (reply_markup )
                elif isinstance (reply_markup ,raw .types .ReplyInlineMarkup ):
                    reply_markup =types .InlineKeyboardMarkup .read (reply_markup )
                elif isinstance (reply_markup ,raw .types .ReplyKeyboardHide ):
                    reply_markup =types .ReplyKeyboardRemove .read (reply_markup )
                else :
                    reply_markup =None 

            from_user =types .User ._parse (client ,users .get (user_id ,None ))
            sender_chat =types .Chat ._parse (client ,message ,users ,chats ,is_chat =False )if not from_user else None 

            reactions =types .MessageReactions ._parse (client ,message .reactions )

            parsed_message =Message (
            id =message .id ,
            date =utils .timestamp_to_datetime (message .date ),
            chat =types .Chat ._parse (client ,message ,users ,chats ,is_chat =True ),
            from_user =from_user ,
            sender_chat =sender_chat ,
            text =(
            Str (message .message ).init (entities )or None 
            if media is None or web_page is not None 
            else None 
            ),
            caption =(
            Str (message .message ).init (entities )or None 
            if media is not None and web_page is None 
            else None 
            ),
            entities =(
            entities or None 
            if media is None or web_page is not None 
            else None 
            ),
            caption_entities =(
            entities or None 
            if media is not None and web_page is None 
            else None 
            ),
            author_signature =message .post_author ,
            has_protected_content =message .noforwards ,
            has_media_spoiler =has_media_spoiler ,
            forward_from =forward_from ,
            forward_sender_name =forward_sender_name ,
            forward_from_chat =forward_from_chat ,
            forward_from_message_id =forward_from_message_id ,
            forward_signature =forward_signature ,
            forward_date =forward_date ,
            mentioned =message .mentioned ,
            scheduled =is_scheduled ,
            from_scheduled =message .from_scheduled ,
            media =media_type ,
            edit_date =utils .timestamp_to_datetime (message .edit_date ),
            media_group_id =message .grouped_id ,
            photo =photo ,
            location =location ,
            contact =contact ,
            venue =venue ,
            audio =audio ,
            voice =voice ,
            animation =animation ,
            game =game ,
            video =video ,
            video_note =video_note ,
            sticker =sticker ,
            document =document ,
            web_page =web_page ,
            poll =poll ,
            dice =dice ,
            views =message .views ,
            forwards =message .forwards ,
            via_bot =types .User ._parse (client ,users .get (message .via_bot_id ,None )),
            outgoing =message .out ,
            reply_markup =reply_markup ,
            reactions =reactions ,
            client =client 
            )

            if message .reply_to :
                parsed_message .reply_to_message_id =message .reply_to .reply_to_msg_id 
                parsed_message .reply_to_top_message_id =message .reply_to .reply_to_top_id 

                if replies :
                    try :
                        key =(parsed_message .chat .id ,parsed_message .reply_to_message_id )
                        reply_to_message =client .message_cache [key ]

                        if not reply_to_message :
                            reply_to_message =await client .get_messages (
                            parsed_message .chat .id ,
                            reply_to_message_ids =message .id ,
                            replies =replies -1 
                            )

                        parsed_message .reply_to_message =reply_to_message 
                    except MessageIdsEmpty :
                        pass 

            if not parsed_message .poll :
                client .message_cache [(parsed_message .chat .id ,parsed_message .id )]=parsed_message 

            return parsed_message 

    @property 
    def link (self )->str :
        if (
        self .chat .type in (enums .ChatType .GROUP ,enums .ChatType .SUPERGROUP ,enums .ChatType .CHANNEL )
        and self .chat .username 
        ):
            return f"https://t.me/{self .chat .username }/{self .id }"
        else :
            return f"https://t.me/c/{utils .get_channel_id (self .chat .id )}/{self .id }"

    async def get_media_group (self )->List ["types.Message"]:
        """"""

        return await self ._client .get_media_group (
        chat_id =self .chat .id ,
        message_id =self .id 
        )

    async def reply_text (
    self ,
    text :str ,
    quote :bool =None ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    entities :List ["types.MessageEntity"]=None ,
    disable_web_page_preview :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    protect_content :bool =None ,
    reply_markup =None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_message (
        chat_id =self .chat .id ,
        text =text ,
        parse_mode =parse_mode ,
        entities =entities ,
        disable_web_page_preview =disable_web_page_preview ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        schedule_date =schedule_date ,
        protect_content =protect_content ,
        reply_markup =reply_markup 
        )

    reply =reply_text 

    async def reply_animation (
    self ,
    animation :Union [str ,BinaryIO ],
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    duration :int =0 ,
    width :int =0 ,
    height :int =0 ,
    thumb :str =None ,
    disable_notification :bool =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    reply_to_message_id :int =None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_animation (
        chat_id =self .chat .id ,
        animation =animation ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        has_spoiler =has_spoiler ,
        duration =duration ,
        width =width ,
        height =height ,
        thumb =thumb ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_audio (
    self ,
    audio :Union [str ,BinaryIO ],
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    duration :int =0 ,
    performer :str =None ,
    title :str =None ,
    thumb :str =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_audio (
        chat_id =self .chat .id ,
        audio =audio ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        duration =duration ,
        performer =performer ,
        title =title ,
        thumb =thumb ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_cached_media (
    self ,
    file_id :str ,
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_cached_media (
        chat_id =self .chat .id ,
        file_id =file_id ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup 
        )

    async def reply_chat_action (self ,action :"enums.ChatAction")->bool :
        """"""
        return await self ._client .send_chat_action (
        chat_id =self .chat .id ,
        action =action 
        )

    async def reply_contact (
    self ,
    phone_number :str ,
    first_name :str ,
    quote :bool =None ,
    last_name :str ="",
    vcard :str ="",
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_contact (
        chat_id =self .chat .id ,
        phone_number =phone_number ,
        first_name =first_name ,
        last_name =last_name ,
        vcard =vcard ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup 
        )

    async def reply_document (
    self ,
    document :Union [str ,BinaryIO ],
    quote :bool =None ,
    thumb :str =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    file_name :str =None ,
    force_document :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_document (
        chat_id =self .chat .id ,
        document =document ,
        thumb =thumb ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        file_name =file_name ,
        force_document =force_document ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        schedule_date =schedule_date ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_game (
    self ,
    game_short_name :str ,
    quote :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_game (
        chat_id =self .chat .id ,
        game_short_name =game_short_name ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup 
        )

    async def reply_inline_bot_result (
    self ,
    query_id :int ,
    result_id :str ,
    quote :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_inline_bot_result (
        chat_id =self .chat .id ,
        query_id =query_id ,
        result_id =result_id ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id 
        )

    async def reply_location (
    self ,
    latitude :float ,
    longitude :float ,
    quote :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_location (
        chat_id =self .chat .id ,
        latitude =latitude ,
        longitude =longitude ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup 
        )

    async def reply_media_group (
    self ,
    media :List [Union ["types.InputMediaPhoto","types.InputMediaVideo"]],
    quote :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None 
    )->List ["types.Message"]:
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_media_group (
        chat_id =self .chat .id ,
        media =media ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id 
        )

    async def reply_photo (
    self ,
    photo :Union [str ,BinaryIO ],
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    ttl_seconds :int =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_photo (
        chat_id =self .chat .id ,
        photo =photo ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        has_spoiler =has_spoiler ,
        ttl_seconds =ttl_seconds ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_poll (
    self ,
    question :str ,
    options :List [str ],
    is_anonymous :bool =True ,
    type :"enums.PollType"=enums .PollType .REGULAR ,
    allows_multiple_answers :bool =None ,
    correct_option_id :int =None ,
    explanation :str =None ,
    explanation_parse_mode :"enums.ParseMode"=None ,
    explanation_entities :List ["types.MessageEntity"]=None ,
    open_period :int =None ,
    close_date :datetime =None ,
    is_closed :bool =None ,
    quote :bool =None ,
    disable_notification :bool =None ,
    protect_content :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_poll (
        chat_id =self .chat .id ,
        question =question ,
        options =options ,
        is_anonymous =is_anonymous ,
        type =type ,
        allows_multiple_answers =allows_multiple_answers ,
        correct_option_id =correct_option_id ,
        explanation =explanation ,
        explanation_parse_mode =explanation_parse_mode ,
        explanation_entities =explanation_entities ,
        open_period =open_period ,
        close_date =close_date ,
        is_closed =is_closed ,
        disable_notification =disable_notification ,
        protect_content =protect_content ,
        reply_to_message_id =reply_to_message_id ,
        schedule_date =schedule_date ,
        reply_markup =reply_markup 
        )

    async def reply_sticker (
    self ,
    sticker :Union [str ,BinaryIO ],
    quote :bool =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_sticker (
        chat_id =self .chat .id ,
        sticker =sticker ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_venue (
    self ,
    latitude :float ,
    longitude :float ,
    title :str ,
    address :str ,
    quote :bool =None ,
    foursquare_id :str ="",
    foursquare_type :str ="",
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None 
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_venue (
        chat_id =self .chat .id ,
        latitude =latitude ,
        longitude =longitude ,
        title =title ,
        address =address ,
        foursquare_id =foursquare_id ,
        foursquare_type =foursquare_type ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup 
        )

    async def reply_video (
    self ,
    video :Union [str ,BinaryIO ],
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    has_spoiler :bool =None ,
    ttl_seconds :int =None ,
    duration :int =0 ,
    width :int =0 ,
    height :int =0 ,
    thumb :str =None ,
    supports_streaming :bool =True ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_video (
        chat_id =self .chat .id ,
        video =video ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        has_spoiler =has_spoiler ,
        ttl_seconds =ttl_seconds ,
        duration =duration ,
        width =width ,
        height =height ,
        thumb =thumb ,
        supports_streaming =supports_streaming ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_video_note (
    self ,
    video_note :Union [str ,BinaryIO ],
    quote :bool =None ,
    duration :int =0 ,
    length :int =1 ,
    thumb :str =None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_video_note (
        chat_id =self .chat .id ,
        video_note =video_note ,
        duration =duration ,
        length =length ,
        thumb =thumb ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def reply_voice (
    self ,
    voice :Union [str ,BinaryIO ],
    quote :bool =None ,
    caption :str ="",
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    duration :int =0 ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=None ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->"Message":
        """"""
        if quote is None :
            quote =self .chat .type !=enums .ChatType .PRIVATE 

        if reply_to_message_id is None and quote :
            reply_to_message_id =self .id 

        return await self ._client .send_voice (
        chat_id =self .chat .id ,
        voice =voice ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        duration =duration ,
        disable_notification =disable_notification ,
        reply_to_message_id =reply_to_message_id ,
        reply_markup =reply_markup ,
        progress =progress ,
        progress_args =progress_args 
        )

    async def edit_text (
    self ,
    text :str ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    entities :List ["types.MessageEntity"]=None ,
    disable_web_page_preview :bool =None ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"Message":
        """"""
        return await self ._client .edit_message_text (
        chat_id =self .chat .id ,
        message_id =self .id ,
        text =text ,
        parse_mode =parse_mode ,
        entities =entities ,
        disable_web_page_preview =disable_web_page_preview ,
        reply_markup =reply_markup 
        )

    edit =edit_text 

    async def edit_caption (
    self ,
    caption :str ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"Message":
        """"""
        return await self ._client .edit_message_caption (
        chat_id =self .chat .id ,
        message_id =self .id ,
        caption =caption ,
        parse_mode =parse_mode ,
        caption_entities =caption_entities ,
        reply_markup =reply_markup 
        )

    async def edit_media (
    self ,
    media :"types.InputMedia",
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->"Message":
        """"""
        return await self ._client .edit_message_media (
        chat_id =self .chat .id ,
        message_id =self .id ,
        media =media ,
        reply_markup =reply_markup 
        )

    async def edit_reply_markup (self ,reply_markup :"types.InlineKeyboardMarkup"=None )->"Message":
        """"""
        return await self ._client .edit_message_reply_markup (
        chat_id =self .chat .id ,
        message_id =self .id ,
        reply_markup =reply_markup 
        )

    async def forward (
    self ,
    chat_id :Union [int ,str ],
    disable_notification :bool =None ,
    schedule_date :datetime =None 
    )->Union ["types.Message",List ["types.Message"]]:
        """"""
        return await self ._client .forward_messages (
        chat_id =chat_id ,
        from_chat_id =self .chat .id ,
        message_ids =self .id ,
        disable_notification =disable_notification ,
        schedule_date =schedule_date 
        )

    async def copy (
    self ,
    chat_id :Union [int ,str ],
    caption :str =None ,
    parse_mode :Optional ["enums.ParseMode"]=None ,
    caption_entities :List ["types.MessageEntity"]=None ,
    disable_notification :bool =None ,
    reply_to_message_id :int =None ,
    schedule_date :datetime =None ,
    protect_content :bool =None ,
    reply_markup :Union [
    "types.InlineKeyboardMarkup",
    "types.ReplyKeyboardMarkup",
    "types.ReplyKeyboardRemove",
    "types.ForceReply"
    ]=object 
    )->Union ["types.Message",List ["types.Message"]]:
        """"""
        if self .service :
            log .warning ("Service messages cannot be copied. chat_id: %s, message_id: %s",
            self .chat .id ,self .id )
        elif self .game and not await self ._client .storage .is_bot ():
            log .warning ("Users cannot send messages with Game media type. chat_id: %s, message_id: %s",
            self .chat .id ,self .id )
        elif self .empty :
            log .warning ("Empty messages cannot be copied.")
        elif self .text :
            return await self ._client .send_message (
            chat_id ,
            text =self .text ,
            entities =self .entities ,
            parse_mode =enums .ParseMode .DISABLED ,
            disable_web_page_preview =not self .web_page ,
            disable_notification =disable_notification ,
            reply_to_message_id =reply_to_message_id ,
            schedule_date =schedule_date ,
            protect_content =protect_content ,
            reply_markup =self .reply_markup if reply_markup is object else reply_markup 
            )
        elif self .media :
            send_media =partial (
            self ._client .send_cached_media ,
            chat_id =chat_id ,
            disable_notification =disable_notification ,
            reply_to_message_id =reply_to_message_id ,
            schedule_date =schedule_date ,
            protect_content =protect_content ,
            reply_markup =self .reply_markup if reply_markup is object else reply_markup 
            )

            if self .photo :
                file_id =self .photo .file_id 
            elif self .audio :
                file_id =self .audio .file_id 
            elif self .document :
                file_id =self .document .file_id 
            elif self .video :
                file_id =self .video .file_id 
            elif self .animation :
                file_id =self .animation .file_id 
            elif self .voice :
                file_id =self .voice .file_id 
            elif self .sticker :
                file_id =self .sticker .file_id 
            elif self .video_note :
                file_id =self .video_note .file_id 
            elif self .contact :
                return await self ._client .send_contact (
                chat_id ,
                phone_number =self .contact .phone_number ,
                first_name =self .contact .first_name ,
                last_name =self .contact .last_name ,
                vcard =self .contact .vcard ,
                disable_notification =disable_notification ,
                schedule_date =schedule_date 
                )
            elif self .location :
                return await self ._client .send_location (
                chat_id ,
                latitude =self .location .latitude ,
                longitude =self .location .longitude ,
                disable_notification =disable_notification ,
                schedule_date =schedule_date 
                )
            elif self .venue :
                return await self ._client .send_venue (
                chat_id ,
                latitude =self .venue .location .latitude ,
                longitude =self .venue .location .longitude ,
                title =self .venue .title ,
                address =self .venue .address ,
                foursquare_id =self .venue .foursquare_id ,
                foursquare_type =self .venue .foursquare_type ,
                disable_notification =disable_notification ,
                schedule_date =schedule_date 
                )
            elif self .poll :
                return await self ._client .send_poll (
                chat_id ,
                question =self .poll .question ,
                options =[opt .text for opt in self .poll .options ],
                disable_notification =disable_notification ,
                schedule_date =schedule_date 
                )
            elif self .game :
                return await self ._client .send_game (
                chat_id ,
                game_short_name =self .game .short_name ,
                disable_notification =disable_notification 
                )
            else :
                raise ValueError ("Unknown media type")

            if self .sticker or self .video_note :
                return await send_media (file_id =file_id )
            else :
                if caption is None :
                    caption =self .caption or ""
                    caption_entities =self .caption_entities 

                return await send_media (
                file_id =file_id ,
                caption =caption ,
                parse_mode =parse_mode ,
                caption_entities =caption_entities 
                )
        else :
            raise ValueError ("Can't copy this message")

    async def delete (self ,revoke :bool =True ):
        """"""
        return await self ._client .delete_messages (
        chat_id =self .chat .id ,
        message_ids =self .id ,
        revoke =revoke 
        )

    async def click (self ,x :Union [int ,str ]=0 ,y :int =None ,quote :bool =None ,timeout :int =10 ):
        """"""

        if isinstance (self .reply_markup ,types .ReplyKeyboardMarkup ):
            keyboard =self .reply_markup .keyboard 
            is_inline =False 
        elif isinstance (self .reply_markup ,types .InlineKeyboardMarkup ):
            keyboard =self .reply_markup .inline_keyboard 
            is_inline =True 
        else :
            raise ValueError ("The message doesn't contain any keyboard")

        if isinstance (x ,int )and y is None :
            try :
                button =[
                button 
                for row in keyboard 
                for button in row 
                ][x ]
            except IndexError :
                raise ValueError (f"The button at index {x } doesn't exist")
        elif isinstance (x ,int )and isinstance (y ,int ):
            try :
                button =keyboard [y ][x ]
            except IndexError :
                raise ValueError (f"The button at position ({x }, {y }) doesn't exist")
        elif isinstance (x ,str )and y is None :
            label =x .encode ("utf-16","surrogatepass").decode ("utf-16")

            try :
                button =[
                button 
                for row in keyboard 
                for button in row 
                if label ==button .text 
                ][0 ]
            except IndexError :
                raise ValueError (f"The button with label '{x }' doesn't exists")
        else :
            raise ValueError ("Invalid arguments")

        if is_inline :
            if button .callback_data :
                return await self ._client .request_callback_answer (
                chat_id =self .chat .id ,
                message_id =self .id ,
                callback_data =button .callback_data ,
                timeout =timeout 
                )
            elif button .url :
                return button .url 
            elif button .switch_inline_query :
                return button .switch_inline_query 
            elif button .switch_inline_query_current_chat :
                return button .switch_inline_query_current_chat 
            else :
                raise ValueError ("This button is not supported yet")
        else :
            await self .reply (button ,quote =quote )

    async def react (self ,emoji :str ="",big :bool =False )->bool :
        """"""

        return await self ._client .send_reaction (
        chat_id =self .chat .id ,
        message_id =self .id ,
        emoji =emoji ,
        big =big 
        )

    async def retract_vote (
    self ,
    )->"types.Poll":
        """"""

        return await self ._client .retract_vote (
        chat_id =self .chat .id ,
        message_id =self .id 
        )

    async def download (
    self ,
    file_name :str ="",
    in_memory :bool =False ,
    block :bool =True ,
    progress :Callable =None ,
    progress_args :tuple =()
    )->str :
        """"""
        return await self ._client .download_media (
        message =self ,
        file_name =file_name ,
        in_memory =in_memory ,
        block =block ,
        progress =progress ,
        progress_args =progress_args ,
        )

    async def vote (
    self ,
    option :int ,
    )->"types.Poll":
        """"""

        return await self ._client .vote_poll (
        chat_id =self .chat .id ,
        message_id =self .id ,
        options =option 
        )

    async def pin (self ,disable_notification :bool =False ,both_sides :bool =False )->"types.Message":
        """"""
        return await self ._client .pin_chat_message (
        chat_id =self .chat .id ,
        message_id =self .id ,
        disable_notification =disable_notification ,
        both_sides =both_sides 
        )

    async def unpin (self )->bool :
        """"""
        return await self ._client .unpin_chat_message (
        chat_id =self .chat .id ,
        message_id =self .id 
        )
