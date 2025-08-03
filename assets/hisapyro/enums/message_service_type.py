
from enum import auto 

from .auto_name import AutoName 

class MessageServiceType (AutoName ):
    """"""

    NEW_CHAT_MEMBERS =auto ()
    "New members join"

    LEFT_CHAT_MEMBERS =auto ()
    "Left chat members"

    NEW_CHAT_TITLE =auto ()
    "New chat title"

    NEW_CHAT_PHOTO =auto ()
    "New chat photo"

    DELETE_CHAT_PHOTO =auto ()
    "Deleted chat photo"

    GROUP_CHAT_CREATED =auto ()
    "Group chat created"

    CHANNEL_CHAT_CREATED =auto ()
    "Channel chat created"

    MIGRATE_TO_CHAT_ID =auto ()
    "Migrated to chat id"

    MIGRATE_FROM_CHAT_ID =auto ()
    "Migrated from chat id"

    PINNED_MESSAGE =auto ()
    "Pinned message"

    GAME_HIGH_SCORE =auto ()
    "Game high score"

    VIDEO_CHAT_STARTED =auto ()
    "Video chat started"

    VIDEO_CHAT_ENDED =auto ()
    "Video chat ended"

    VIDEO_CHAT_SCHEDULED =auto ()
    "Video chat scheduled"

    VIDEO_CHAT_MEMBERS_INVITED =auto ()
    "Video chat members invited"

    WEB_APP_DATA =auto ()
    "Web app data"
