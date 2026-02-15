import datetime 
import functools 

from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils 
from ..tl import types 
from ..tl .custom .sendergetter import SenderGetter 

def _requires_action (function ):
    @functools .wraps (function )
    def wrapped (self ):
        return None if self .action is None else function (self )

    return wrapped 

def _requires_status (function ):
    @functools .wraps (function )
    def wrapped (self ):
        return None if self .status is None else function (self )

    return wrapped 

@name_inner_event 
class UserUpdate (EventBuilder ):
    """"""
    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        if isinstance (update ,types .UpdateUserStatus ):
            return cls .Event (types .PeerUser (update .user_id ),
            status =update .status )
        elif isinstance (update ,types .UpdateChannelUserTyping ):
            return cls .Event (update .from_id ,
            chat_peer =types .PeerChannel (update .channel_id ),
            typing =update .action )
        elif isinstance (update ,types .UpdateChatUserTyping ):
            return cls .Event (update .from_id ,
            chat_peer =types .PeerChat (update .chat_id ),
            typing =update .action )
        elif isinstance (update ,types .UpdateUserTyping ):
            return cls .Event (update .user_id ,
            typing =update .action )

    class Event (EventCommon ,SenderGetter ):
        """"""
        def __init__ (self ,peer ,*,status =None ,chat_peer =None ,typing =None ):
            super ().__init__ (chat_peer or peer )
            SenderGetter .__init__ (self ,utils .get_peer_id (peer ))

            self .status =status 
            self .action =typing 

        def _set_client (self ,client ):
            super ()._set_client (client )
            self ._sender ,self ._input_sender =utils ._get_entity_pair (
            self .sender_id ,self ._entities ,client ._entity_cache )

        @property 
        def user (self ):
            """"""
            return self .sender 

        async def get_user (self ):
            """"""
            return await self .get_sender ()

        @property 
        def input_user (self ):
            """"""
            return self .input_sender 

        async def get_input_user (self ):
            """"""
            return await self .get_input_sender ()

        @property 
        def user_id (self ):
            """"""
            return self .sender_id 

        @property 
        @_requires_action 
        def typing (self ):
            """"""
            return isinstance (self .action ,types .SendMessageTypingAction )

        @property 
        @_requires_action 
        def uploading (self ):
            """"""
            return isinstance (self .action ,(
            types .SendMessageChooseContactAction ,
            types .SendMessageChooseStickerAction ,
            types .SendMessageUploadAudioAction ,
            types .SendMessageUploadDocumentAction ,
            types .SendMessageUploadPhotoAction ,
            types .SendMessageUploadRoundAction ,
            types .SendMessageUploadVideoAction 
            ))

        @property 
        @_requires_action 
        def recording (self ):
            """"""
            return isinstance (self .action ,(
            types .SendMessageRecordAudioAction ,
            types .SendMessageRecordRoundAction ,
            types .SendMessageRecordVideoAction 
            ))

        @property 
        @_requires_action 
        def playing (self ):
            """"""
            return isinstance (self .action ,types .SendMessageGamePlayAction )

        @property 
        @_requires_action 
        def cancel (self ):
            """"""
            return isinstance (self .action ,types .SendMessageCancelAction )

        @property 
        @_requires_action 
        def geo (self ):
            """"""
            return isinstance (self .action ,types .SendMessageGeoLocationAction )

        @property 
        @_requires_action 
        def audio (self ):
            """"""
            return isinstance (self .action ,(
            types .SendMessageRecordAudioAction ,
            types .SendMessageUploadAudioAction 
            ))

        @property 
        @_requires_action 
        def round (self ):
            """"""
            return isinstance (self .action ,(
            types .SendMessageRecordRoundAction ,
            types .SendMessageUploadRoundAction 
            ))

        @property 
        @_requires_action 
        def video (self ):
            """"""
            return isinstance (self .action ,(
            types .SendMessageRecordVideoAction ,
            types .SendMessageUploadVideoAction 
            ))

        @property 
        @_requires_action 
        def contact (self ):
            """"""
            return isinstance (self .action ,types .SendMessageChooseContactAction )

        @property 
        @_requires_action 
        def document (self ):
            """"""
            return isinstance (self .action ,types .SendMessageUploadDocumentAction )

        @property 
        @_requires_action 
        def sticker (self ):
            """"""
            return isinstance (self .action ,types .SendMessageChooseStickerAction )

        @property 
        @_requires_action 
        def photo (self ):
            """"""
            return isinstance (self .action ,types .SendMessageUploadPhotoAction )

        @property 
        @_requires_status 
        def last_seen (self ):
            """"""
            if isinstance (self .status ,types .UserStatusOffline ):
                return self .status .was_online 

        @property 
        @_requires_status 
        def until (self ):
            """"""
            if isinstance (self .status ,types .UserStatusOnline ):
                return self .status .expires 

        def _last_seen_delta (self ):
            if isinstance (self .status ,types .UserStatusOffline ):
                return datetime .datetime .now (tz =datetime .timezone .utc )-self .status .was_online 
            elif isinstance (self .status ,types .UserStatusOnline ):
                return datetime .timedelta (days =0 )
            elif isinstance (self .status ,types .UserStatusRecently ):
                return datetime .timedelta (days =1 )
            elif isinstance (self .status ,types .UserStatusLastWeek ):
                return datetime .timedelta (days =7 )
            elif isinstance (self .status ,types .UserStatusLastMonth ):
                return datetime .timedelta (days =30 )
            else :
                return datetime .timedelta (days =365 )

        @property 
        @_requires_status 
        def online (self ):
            """"""
            return self ._last_seen_delta ()<=datetime .timedelta (days =0 )

        @property 
        @_requires_status 
        def recently (self ):
            """"""
            return self ._last_seen_delta ()<=datetime .timedelta (days =1 )

        @property 
        @_requires_status 
        def within_weeks (self ):
            """"""
            return self ._last_seen_delta ()<=datetime .timedelta (days =7 )

        @property 
        @_requires_status 
        def within_months (self ):
            """"""
            return self ._last_seen_delta ()<=datetime .timedelta (days =30 )
