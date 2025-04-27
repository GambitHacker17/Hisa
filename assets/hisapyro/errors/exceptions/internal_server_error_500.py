
from ..rpc_error import RPCError 

class InternalServerError (RPCError ):
    """"""
    CODE =500 
    """"""
    NAME =__doc__ 

class ApiCallError (InternalServerError ):
    """"""
    ID ="API_CALL_ERROR"
    """"""
    MESSAGE =__doc__ 

class AuthRestart (InternalServerError ):
    """"""
    ID ="AUTH_RESTART"
    """"""
    MESSAGE =__doc__ 

class CallOccupyFailed (InternalServerError ):
    """"""
    ID ="CALL_OCCUPY_FAILED"
    """"""
    MESSAGE =__doc__ 

class ChatIdGenerateFailed (InternalServerError ):
    """"""
    ID ="CHAT_ID_GENERATE_FAILED"
    """"""
    MESSAGE =__doc__ 

class ChatOccupyLocFailed (InternalServerError ):
    """"""
    ID ="CHAT_OCCUPY_LOC_FAILED"
    """"""
    MESSAGE =__doc__ 

class ChatOccupyUsernameFailed (InternalServerError ):
    """"""
    ID ="CHAT_OCCUPY_USERNAME_FAILED"
    """"""
    MESSAGE =__doc__ 

class ChpCallFail (InternalServerError ):
    """"""
    ID ="CHP_CALL_FAIL"
    """"""
    MESSAGE =__doc__ 

class EncryptionOccupyAdminFailed (InternalServerError ):
    """"""
    ID ="ENCRYPTION_OCCUPY_ADMIN_FAILED"
    """"""
    MESSAGE =__doc__ 

class EncryptionOccupyFailed (InternalServerError ):
    """"""
    ID ="ENCRYPTION_OCCUPY_FAILED"
    """"""
    MESSAGE =__doc__ 

class FolderDeacAutofixAll (InternalServerError ):
    """"""
    ID ="FOLDER_DEAC_AUTOFIX_ALL"
    """"""
    MESSAGE =__doc__ 

class GroupcallAddParticipantsFailed (InternalServerError ):
    """"""
    ID ="GROUPCALL_ADD_PARTICIPANTS_FAILED"
    """"""
    MESSAGE =__doc__ 

class GroupedIdOccupyFailed (InternalServerError ):
    """"""
    ID ="GROUPED_ID_OCCUPY_FAILED"
    """"""
    MESSAGE =__doc__ 

class HistoryGetFailed (InternalServerError ):
    """"""
    ID ="HISTORY_GET_FAILED"
    """"""
    MESSAGE =__doc__ 

class ImageEngineDown (InternalServerError ):
    """"""
    ID ="IMAGE_ENGINE_DOWN"
    """"""
    MESSAGE =__doc__ 

class InterdcCallError (InternalServerError ):
    """"""
    ID ="INTERDC_X_CALL_ERROR"
    """"""
    MESSAGE =__doc__ 

class InterdcCallRichError (InternalServerError ):
    """"""
    ID ="INTERDC_X_CALL_RICH_ERROR"
    """"""
    MESSAGE =__doc__ 

class MemberFetchFailed (InternalServerError ):
    """"""
    ID ="MEMBER_FETCH_FAILED"
    """"""
    MESSAGE =__doc__ 

class MemberNoLocation (InternalServerError ):
    """"""
    ID ="MEMBER_NO_LOCATION"
    """"""
    MESSAGE =__doc__ 

class MemberOccupyPrimaryLocFailed (InternalServerError ):
    """"""
    ID ="MEMBER_OCCUPY_PRIMARY_LOC_FAILED"
    """"""
    MESSAGE =__doc__ 

class MemberOccupyUsernameFailed (InternalServerError ):
    """"""
    ID ="MEMBER_OCCUPY_USERNAME_FAILED"
    """"""
    MESSAGE =__doc__ 

class MsgidDecreaseRetry (InternalServerError ):
    """"""
    ID ="MSGID_DECREASE_RETRY"
    """"""
    MESSAGE =__doc__ 

class MsgRangeUnsync (InternalServerError ):
    """"""
    ID ="MSG_RANGE_UNSYNC"
    """"""
    MESSAGE =__doc__ 

class MtSendQueueTooLong (InternalServerError ):
    """"""
    ID ="MT_SEND_QUEUE_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class NeedChatInvalid (InternalServerError ):
    """"""
    ID ="NEED_CHAT_INVALID"
    """"""
    MESSAGE =__doc__ 

class NeedMemberInvalid (InternalServerError ):
    """"""
    ID ="NEED_MEMBER_INVALID"
    """"""
    MESSAGE =__doc__ 

class NoWorkersRunning (InternalServerError ):
    """"""
    ID ="No workers running"
    """"""
    MESSAGE =__doc__ 

class ParticipantCallFailed (InternalServerError ):
    """"""
    ID ="PARTICIPANT_CALL_FAILED"
    """"""
    MESSAGE =__doc__ 

class PersistentTimestampOutdated (InternalServerError ):
    """"""
    ID ="PERSISTENT_TIMESTAMP_OUTDATED"
    """"""
    MESSAGE =__doc__ 

class PhotoCreateFailed (InternalServerError ):
    """"""
    ID ="PHOTO_CREATE_FAILED"
    """"""
    MESSAGE =__doc__ 

class PostponedTimeout (InternalServerError ):
    """"""
    ID ="POSTPONED_TIMEOUT"
    """"""
    MESSAGE =__doc__ 

class PtsChangeEmpty (InternalServerError ):
    """"""
    ID ="PTS_CHANGE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class RandomIdDuplicate (InternalServerError ):
    """"""
    ID ="RANDOM_ID_DUPLICATE"
    """"""
    MESSAGE =__doc__ 

class RegIdGenerateFailed (InternalServerError ):
    """"""
    ID ="REG_ID_GENERATE_FAILED"
    """"""
    MESSAGE =__doc__ 

class RpcCallFail (InternalServerError ):
    """"""
    ID ="RPC_CALL_FAIL"
    """"""
    MESSAGE =__doc__ 

class RpcConnectFailed (InternalServerError ):
    """"""
    ID ="RPC_CONNECT_FAILED"
    """"""
    MESSAGE =__doc__ 

class RpcMcgetFail (InternalServerError ):
    """"""
    ID ="RPC_MCGET_FAIL"
    """"""
    MESSAGE =__doc__ 

class SignInFailed (InternalServerError ):
    """"""
    ID ="SIGN_IN_FAILED"
    """"""
    MESSAGE =__doc__ 

class StorageCheckFailed (InternalServerError ):
    """"""
    ID ="STORAGE_CHECK_FAILED"
    """"""
    MESSAGE =__doc__ 

class StoreInvalidScalarType (InternalServerError ):
    """"""
    ID ="STORE_INVALID_SCALAR_TYPE"
    """"""
    MESSAGE =__doc__ 

class UnknownMethod (InternalServerError ):
    """"""
    ID ="UNKNOWN_METHOD"
    """"""
    MESSAGE =__doc__ 

class UploadNoVolume (InternalServerError ):
    """"""
    ID ="UPLOAD_NO_VOLUME"
    """"""
    MESSAGE =__doc__ 

class VolumeLocNotFound (InternalServerError ):
    """"""
    ID ="VOLUME_LOC_NOT_FOUND"
    """"""
    MESSAGE =__doc__ 

class WorkerBusyTooLongRetry (InternalServerError ):
    """"""
    ID ="WORKER_BUSY_TOO_LONG_RETRY"
    """"""
    MESSAGE =__doc__ 

class WpIdGenerateFailed (InternalServerError ):
    """"""
    ID ="WP_ID_GENERATE_FAILED"
    """"""
    MESSAGE =__doc__ 

