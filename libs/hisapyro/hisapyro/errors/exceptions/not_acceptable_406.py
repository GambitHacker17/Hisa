
from ..rpc_error import RPCError 

class NotAcceptable (RPCError ):
    """"""
    CODE =406 
    """"""
    NAME =__doc__ 

class AuthKeyDuplicated (NotAcceptable ):
    """"""
    ID ="AUTH_KEY_DUPLICATED"
    """"""
    MESSAGE =__doc__ 

class ChannelPrivate (NotAcceptable ):
    """"""
    ID ="CHANNEL_PRIVATE"
    """"""
    MESSAGE =__doc__ 

class FilerefUpgradeNeeded (NotAcceptable ):
    """"""
    ID ="FILEREF_UPGRADE_NEEDED"
    """"""
    MESSAGE =__doc__ 

class FreshChangeAdminsForbidden (NotAcceptable ):
    """"""
    ID ="FRESH_CHANGE_ADMINS_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class FreshChangePhoneForbidden (NotAcceptable ):
    """"""
    ID ="FRESH_CHANGE_PHONE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class FreshResetAuthorisationForbidden (NotAcceptable ):
    """"""
    ID ="FRESH_RESET_AUTHORISATION_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberInvalid (NotAcceptable ):
    """"""
    ID ="PHONE_NUMBER_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhonePasswordFlood (NotAcceptable ):
    """"""
    ID ="PHONE_PASSWORD_FLOOD"
    """"""
    MESSAGE =__doc__ 

class StickersetInvalid (NotAcceptable ):
    """"""
    ID ="STICKERSET_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickersetOwnerAnonymous (NotAcceptable ):
    """"""
    ID ="STICKERSET_OWNER_ANONYMOUS"
    """"""
    MESSAGE =__doc__ 

class UserpicUploadRequired (NotAcceptable ):
    """"""
    ID ="USERPIC_UPLOAD_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class UserRestricted (NotAcceptable ):
    """"""
    ID ="USER_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

