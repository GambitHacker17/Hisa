
from ..rpc_error import RPCError 

class SeeOther (RPCError ):
    """"""
    CODE =303 
    """"""
    NAME =__doc__ 

class FileMigrate (SeeOther ):
    """"""
    ID ="FILE_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

class NetworkMigrate (SeeOther ):
    """"""
    ID ="NETWORK_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

class PhoneMigrate (SeeOther ):
    """"""
    ID ="PHONE_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

class StatsMigrate (SeeOther ):
    """"""
    ID ="STATS_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

class UserMigrate (SeeOther ):
    """"""
    ID ="USER_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

