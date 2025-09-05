
from hisapyro import raw 
from .auto_name import AutoName 

class ChatMembersFilter (AutoName ):
    """"""

    SEARCH =raw .types .ChannelParticipantsSearch 
    "Search for members"

    BANNED =raw .types .ChannelParticipantsKicked 
    "Banned members"

    RESTRICTED =raw .types .ChannelParticipantsBanned 
    "Restricted members"

    BOTS =raw .types .ChannelParticipantsBots 
    "Bots"

    RECENT =raw .types .ChannelParticipantsRecent 
    "Recently active members"

    ADMINISTRATORS =raw .types .ChannelParticipantsAdmins 
    "Administrators"
