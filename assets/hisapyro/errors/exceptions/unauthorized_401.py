
from ..rpc_error import RPCError 

class Unauthorized (RPCError ):
    """"""
    CODE =401 
    """"""
    NAME =__doc__ 

class ActiveUserRequired (Unauthorized ):
    """"""
    ID ="ACTIVE_USER_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class AuthKeyInvalid (Unauthorized ):
    """"""
    ID ="AUTH_KEY_INVALID"
    """"""
    MESSAGE =__doc__ 

class AuthKeyPermEmpty (Unauthorized ):
    """"""
    ID ="AUTH_KEY_PERM_EMPTY"
    """"""
    MESSAGE =__doc__ 

class AuthKeyUnregistered (Unauthorized ):
    """"""
    ID ="AUTH_KEY_UNREGISTERED"
    """"""
    MESSAGE =__doc__ 

class SessionExpired (Unauthorized ):
    """"""
    ID ="SESSION_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class SessionPasswordNeeded (Unauthorized ):
    """"""
    ID ="SESSION_PASSWORD_NEEDED"
    """"""
    MESSAGE =__doc__ 

class SessionRevoked (Unauthorized ):
    """"""
    ID ="SESSION_REVOKED"
    """"""
    MESSAGE =__doc__ 

class UserDeactivated (Unauthorized ):
    """"""
    ID ="USER_DEACTIVATED"
    """"""
    MESSAGE =__doc__ 

class UserDeactivatedBan (Unauthorized ):
    """"""
    ID ="USER_DEACTIVATED_BAN"
    """"""
    MESSAGE =__doc__ 

