
from ..rpc_error import RPCError 

class Forbidden (RPCError ):
    """"""
    CODE =403 
    """"""
    NAME =__doc__ 

class BroadcastForbidden (Forbidden ):
    """"""
    ID ="BROADCAST_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChannelPublicGroupNa (Forbidden ):
    """"""
    ID ="CHANNEL_PUBLIC_GROUP_NA"
    """"""
    MESSAGE =__doc__ 

class ChatAdminInviteRequired (Forbidden ):
    """"""
    ID ="CHAT_ADMIN_INVITE_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class ChatAdminRequired (Forbidden ):
    """"""
    ID ="CHAT_ADMIN_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class ChatForbidden (Forbidden ):
    """"""
    ID ="CHAT_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatSendGifsForbidden (Forbidden ):
    """"""
    ID ="CHAT_SEND_GIFS_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatSendInlineForbidden (Forbidden ):
    """"""
    ID ="CHAT_SEND_INLINE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatSendMediaForbidden (Forbidden ):
    """"""
    ID ="CHAT_SEND_MEDIA_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatSendPollForbidden (Forbidden ):
    """"""
    ID ="CHAT_SEND_POLL_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatSendStickersForbidden (Forbidden ):
    """"""
    ID ="CHAT_SEND_STICKERS_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatWriteForbidden (Forbidden ):
    """"""
    ID ="CHAT_WRITE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class EditBotInviteForbidden (Forbidden ):
    """"""
    ID ="EDIT_BOT_INVITE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class InlineBotRequired (Forbidden ):
    """"""
    ID ="INLINE_BOT_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class MessageAuthorRequired (Forbidden ):
    """"""
    ID ="MESSAGE_AUTHOR_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class MessageDeleteForbidden (Forbidden ):
    """"""
    ID ="MESSAGE_DELETE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class PollVoteRequired (Forbidden ):
    """"""
    ID ="POLL_VOTE_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class PremiumAccountRequired (Forbidden ):
    """"""
    ID ="PREMIUM_ACCOUNT_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class RightForbidden (Forbidden ):
    """"""
    ID ="RIGHT_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class SensitiveChangeForbidden (Forbidden ):
    """"""
    ID ="SENSITIVE_CHANGE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class TakeoutRequired (Forbidden ):
    """"""
    ID ="TAKEOUT_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class UserBotInvalid (Forbidden ):
    """"""
    ID ="USER_BOT_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserChannelsTooMuch (Forbidden ):
    """"""
    ID ="USER_CHANNELS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class UserInvalid (Forbidden ):
    """"""
    ID ="USER_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserIsBlocked (Forbidden ):
    """"""
    ID ="USER_IS_BLOCKED"
    """"""
    MESSAGE =__doc__ 

class UserNotMutualContact (Forbidden ):
    """"""
    ID ="USER_NOT_MUTUAL_CONTACT"
    """"""
    MESSAGE =__doc__ 

class UserPrivacyRestricted (Forbidden ):
    """"""
    ID ="USER_PRIVACY_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

class UserRestricted (Forbidden ):
    """"""
    ID ="USER_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

