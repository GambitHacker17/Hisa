
from ..rpc_error import RPCError 

class BadRequest (RPCError ):
    """"""
    CODE =400 
    """"""
    NAME =__doc__ 

class AboutTooLong (BadRequest ):
    """"""
    ID ="ABOUT_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class AccessTokenExpired (BadRequest ):
    """"""
    ID ="ACCESS_TOKEN_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class AccessTokenInvalid (BadRequest ):
    """"""
    ID ="ACCESS_TOKEN_INVALID"
    """"""
    MESSAGE =__doc__ 

class AdminsTooMuch (BadRequest ):
    """"""
    ID ="ADMINS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class AdminRankEmojiNotAllowed (BadRequest ):
    """"""
    ID ="ADMIN_RANK_EMOJI_NOT_ALLOWED"
    """"""
    MESSAGE =__doc__ 

class AdminRankInvalid (BadRequest ):
    """"""
    ID ="ADMIN_RANK_INVALID"
    """"""
    MESSAGE =__doc__ 

class AlbumPhotosTooMany (BadRequest ):
    """"""
    ID ="ALBUM_PHOTOS_TOO_MANY"
    """"""
    MESSAGE =__doc__ 

class ApiIdInvalid (BadRequest ):
    """"""
    ID ="API_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class ApiIdPublishedFlood (BadRequest ):
    """"""
    ID ="API_ID_PUBLISHED_FLOOD"
    """"""
    MESSAGE =__doc__ 

class ArticleTitleEmpty (BadRequest ):
    """"""
    ID ="ARTICLE_TITLE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class AudioTitleEmpty (BadRequest ):
    """"""
    ID ="AUDIO_TITLE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class AuthBytesInvalid (BadRequest ):
    """"""
    ID ="AUTH_BYTES_INVALID"
    """"""
    MESSAGE =__doc__ 

class AuthTokenAlreadyAccepted (BadRequest ):
    """"""
    ID ="AUTH_TOKEN_ALREADY_ACCEPTED"
    """"""
    MESSAGE =__doc__ 

class AuthTokenExpired (BadRequest ):
    """"""
    ID ="AUTH_TOKEN_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class AuthTokenInvalid (BadRequest ):
    """"""
    ID ="AUTH_TOKEN_INVALID"
    """"""
    MESSAGE =__doc__ 

class AutoarchiveNotAvailable (BadRequest ):
    """"""
    ID ="AUTOARCHIVE_NOT_AVAILABLE"
    """"""
    MESSAGE =__doc__ 

class BankCardNumberInvalid (BadRequest ):
    """"""
    ID ="BANK_CARD_NUMBER_INVALID"
    """"""
    MESSAGE =__doc__ 

class BannedRightsInvalid (BadRequest ):
    """"""
    ID ="BANNED_RIGHTS_INVALID"
    """"""
    MESSAGE =__doc__ 

class BasePortLocInvalid (BadRequest ):
    """"""
    ID ="BASE_PORT_LOC_INVALID"
    """"""
    MESSAGE =__doc__ 

class BotsTooMuch (BadRequest ):
    """"""
    ID ="BOTS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class BotChannelsNa (BadRequest ):
    """"""
    ID ="BOT_CHANNELS_NA"
    """"""
    MESSAGE =__doc__ 

class BotCommandDescriptionInvalid (BadRequest ):
    """"""
    ID ="BOT_COMMAND_DESCRIPTION_INVALID"
    """"""
    MESSAGE =__doc__ 

class BotDomainInvalid (BadRequest ):
    """"""
    ID ="BOT_DOMAIN_INVALID"
    """"""
    MESSAGE =__doc__ 

class BotGamesDisabled (BadRequest ):
    """"""
    ID ="BOT_GAMES_DISABLED"
    """"""
    MESSAGE =__doc__ 

class BotGroupsBlocked (BadRequest ):
    """"""
    ID ="BOT_GROUPS_BLOCKED"
    """"""
    MESSAGE =__doc__ 

class BotInlineDisabled (BadRequest ):
    """"""
    ID ="BOT_INLINE_DISABLED"
    """"""
    MESSAGE =__doc__ 

class BotInvalid (BadRequest ):
    """"""
    ID ="BOT_INVALID"
    """"""
    MESSAGE =__doc__ 

class BotMethodInvalid (BadRequest ):
    """"""
    ID ="BOT_METHOD_INVALID"
    """"""
    MESSAGE =__doc__ 

class BotMissing (BadRequest ):
    """"""
    ID ="BOT_MISSING"
    """"""
    MESSAGE =__doc__ 

class BotOnesideNotAvail (BadRequest ):
    """"""
    ID ="BOT_ONESIDE_NOT_AVAIL"
    """"""
    MESSAGE =__doc__ 

class BotPaymentsDisabled (BadRequest ):
    """"""
    ID ="BOT_PAYMENTS_DISABLED"
    """"""
    MESSAGE =__doc__ 

class BotPollsDisabled (BadRequest ):
    """"""
    ID ="BOT_POLLS_DISABLED"
    """"""
    MESSAGE =__doc__ 

class BotResponseTimeout (BadRequest ):
    """"""
    ID ="BOT_RESPONSE_TIMEOUT"
    """"""
    MESSAGE =__doc__ 

class BotScoreNotModified (BadRequest ):
    """"""
    ID ="BOT_SCORE_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class BroadcastIdInvalid (BadRequest ):
    """"""
    ID ="BROADCAST_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class BroadcastPublicVotersForbidden (BadRequest ):
    """"""
    ID ="BROADCAST_PUBLIC_VOTERS_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class BroadcastRequired (BadRequest ):
    """"""
    ID ="BROADCAST_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class ButtonDataInvalid (BadRequest ):
    """"""
    ID ="BUTTON_DATA_INVALID"
    """"""
    MESSAGE =__doc__ 

class ButtonTypeInvalid (BadRequest ):
    """"""
    ID ="BUTTON_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ButtonUrlInvalid (BadRequest ):
    """"""
    ID ="BUTTON_URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class ButtonUserPrivacyRestricted (BadRequest ):
    """"""
    ID ="BUTTON_USER_PRIVACY_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

class CallAlreadyAccepted (BadRequest ):
    """"""
    ID ="CALL_ALREADY_ACCEPTED"
    """"""
    MESSAGE =__doc__ 

class CallAlreadyDeclined (BadRequest ):
    """"""
    ID ="CALL_ALREADY_DECLINED"
    """"""
    MESSAGE =__doc__ 

class CallPeerInvalid (BadRequest ):
    """"""
    ID ="CALL_PEER_INVALID"
    """"""
    MESSAGE =__doc__ 

class CallProtocolFlagsInvalid (BadRequest ):
    """"""
    ID ="CALL_PROTOCOL_FLAGS_INVALID"
    """"""
    MESSAGE =__doc__ 

class CdnMethodInvalid (BadRequest ):
    """"""
    ID ="CDN_METHOD_INVALID"
    """"""
    MESSAGE =__doc__ 

class ChannelsAdminPublicTooMuch (BadRequest ):
    """"""
    ID ="CHANNELS_ADMIN_PUBLIC_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class ChannelsTooMuch (BadRequest ):
    """"""
    ID ="CHANNELS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class ChannelAddInvalid (BadRequest ):
    """"""
    ID ="CHANNEL_ADD_INVALID"
    """"""
    MESSAGE =__doc__ 

class ChannelBanned (BadRequest ):
    """"""
    ID ="CHANNEL_BANNED"
    """"""
    MESSAGE =__doc__ 

class ChannelInvalid (BadRequest ):
    """"""
    ID ="CHANNEL_INVALID"
    """"""
    MESSAGE =__doc__ 

class ChannelPrivate (BadRequest ):
    """"""
    ID ="CHANNEL_PRIVATE"
    """"""
    MESSAGE =__doc__ 

class ChannelTooLarge (BadRequest ):
    """"""
    ID ="CHANNEL_TOO_LARGE"
    """"""
    MESSAGE =__doc__ 

class ChatAboutNotModified (BadRequest ):
    """"""
    ID ="CHAT_ABOUT_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class ChatAboutTooLong (BadRequest ):
    """"""
    ID ="CHAT_ABOUT_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class ChatAdminRequired (BadRequest ):
    """"""
    ID ="CHAT_ADMIN_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class ChatForwardsRestricted (BadRequest ):
    """"""
    ID ="CHAT_FORWARDS_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

class ChatIdEmpty (BadRequest ):
    """"""
    ID ="CHAT_ID_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ChatIdInvalid (BadRequest ):
    """"""
    ID ="CHAT_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class ChatInvalid (BadRequest ):
    """"""
    ID ="CHAT_INVALID"
    """"""
    MESSAGE =__doc__ 

class ChatInvitePermanent (BadRequest ):
    """"""
    ID ="CHAT_INVITE_PERMANENT"
    """"""
    MESSAGE =__doc__ 

class ChatLinkExists (BadRequest ):
    """"""
    ID ="CHAT_LINK_EXISTS"
    """"""
    MESSAGE =__doc__ 

class ChatNotModified (BadRequest ):
    """"""
    ID ="CHAT_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class ChatRestricted (BadRequest ):
    """"""
    ID ="CHAT_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

class ChatSendInlineForbidden (BadRequest ):
    """"""
    ID ="CHAT_SEND_INLINE_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class ChatTitleEmpty (BadRequest ):
    """"""
    ID ="CHAT_TITLE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ChatTooBig (BadRequest ):
    """"""
    ID ="CHAT_TOO_BIG"
    """"""
    MESSAGE =__doc__ 

class CodeEmpty (BadRequest ):
    """"""
    ID ="CODE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class CodeHashInvalid (BadRequest ):
    """"""
    ID ="CODE_HASH_INVALID"
    """"""
    MESSAGE =__doc__ 

class CodeInvalid (BadRequest ):
    """"""
    ID ="CODE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ConnectionApiIdInvalid (BadRequest ):
    """"""
    ID ="CONNECTION_API_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class ConnectionAppVersionEmpty (BadRequest ):
    """"""
    ID ="CONNECTION_APP_VERSION_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ConnectionDeviceModelEmpty (BadRequest ):
    """"""
    ID ="CONNECTION_DEVICE_MODEL_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ConnectionLangPackInvalid (BadRequest ):
    """"""
    ID ="CONNECTION_LANG_PACK_INVALID"
    """"""
    MESSAGE =__doc__ 

class ConnectionLayerInvalid (BadRequest ):
    """"""
    ID ="CONNECTION_LAYER_INVALID"
    """"""
    MESSAGE =__doc__ 

class ConnectionNotInited (BadRequest ):
    """"""
    ID ="CONNECTION_NOT_INITED"
    """"""
    MESSAGE =__doc__ 

class ConnectionSystemEmpty (BadRequest ):
    """"""
    ID ="CONNECTION_SYSTEM_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ConnectionSystemLangCodeEmpty (BadRequest ):
    """"""
    ID ="CONNECTION_SYSTEM_LANG_CODE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ContactAddMissing (BadRequest ):
    """"""
    ID ="CONTACT_ADD_MISSING"
    """"""
    MESSAGE =__doc__ 

class ContactIdInvalid (BadRequest ):
    """"""
    ID ="CONTACT_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class ContactNameEmpty (BadRequest ):
    """"""
    ID ="CONTACT_NAME_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ContactReqMissing (BadRequest ):
    """"""
    ID ="CONTACT_REQ_MISSING"
    """"""
    MESSAGE =__doc__ 

class DataInvalid (BadRequest ):
    """"""
    ID ="DATA_INVALID"
    """"""
    MESSAGE =__doc__ 

class DataJsonInvalid (BadRequest ):
    """"""
    ID ="DATA_JSON_INVALID"
    """"""
    MESSAGE =__doc__ 

class DataTooLong (BadRequest ):
    """"""
    ID ="DATA_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class DateEmpty (BadRequest ):
    """"""
    ID ="DATE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class DcIdInvalid (BadRequest ):
    """"""
    ID ="DC_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class DhGAInvalid (BadRequest ):
    """"""
    ID ="DH_G_A_INVALID"
    """"""
    MESSAGE =__doc__ 

class DocumentInvalid (BadRequest ):
    """"""
    ID ="DOCUMENT_INVALID"
    """"""
    MESSAGE =__doc__ 

class EmailHashExpired (BadRequest ):
    """"""
    ID ="EMAIL_HASH_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class EmailInvalid (BadRequest ):
    """"""
    ID ="EMAIL_INVALID"
    """"""
    MESSAGE =__doc__ 

class EmailUnconfirmed (BadRequest ):
    """"""
    ID ="EMAIL_UNCONFIRMED"
    """"""
    MESSAGE =__doc__ 

class EmailUnconfirmed (BadRequest ):
    """"""
    ID ="EMAIL_UNCONFIRMED_X"
    """"""
    MESSAGE =__doc__ 

class EmailVerifyExpired (BadRequest ):
    """"""
    ID ="EMAIL_VERIFY_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class EmoticonEmpty (BadRequest ):
    """"""
    ID ="EMOTICON_EMPTY"
    """"""
    MESSAGE =__doc__ 

class EmoticonInvalid (BadRequest ):
    """"""
    ID ="EMOTICON_INVALID"
    """"""
    MESSAGE =__doc__ 

class EmoticonStickerpackMissing (BadRequest ):
    """"""
    ID ="EMOTICON_STICKERPACK_MISSING"
    """"""
    MESSAGE =__doc__ 

class EncryptedMessageInvalid (BadRequest ):
    """"""
    ID ="ENCRYPTED_MESSAGE_INVALID"
    """"""
    MESSAGE =__doc__ 

class EncryptionAlreadyAccepted (BadRequest ):
    """"""
    ID ="ENCRYPTION_ALREADY_ACCEPTED"
    """"""
    MESSAGE =__doc__ 

class EncryptionAlreadyDeclined (BadRequest ):
    """"""
    ID ="ENCRYPTION_ALREADY_DECLINED"
    """"""
    MESSAGE =__doc__ 

class EncryptionDeclined (BadRequest ):
    """"""
    ID ="ENCRYPTION_DECLINED"
    """"""
    MESSAGE =__doc__ 

class EncryptionIdInvalid (BadRequest ):
    """"""
    ID ="ENCRYPTION_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class EntitiesTooLong (BadRequest ):
    """"""
    ID ="ENTITIES_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class EntityBoundsInvalid (BadRequest ):
    """"""
    ID ="ENTITY_BOUNDS_INVALID"
    """"""
    MESSAGE =__doc__ 

class EntityMentionUserInvalid (BadRequest ):
    """"""
    ID ="ENTITY_MENTION_USER_INVALID"
    """"""
    MESSAGE =__doc__ 

class ErrorTextEmpty (BadRequest ):
    """"""
    ID ="ERROR_TEXT_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ExpireDateInvalid (BadRequest ):
    """"""
    ID ="EXPIRE_DATE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ExportCardInvalid (BadRequest ):
    """"""
    ID ="EXPORT_CARD_INVALID"
    """"""
    MESSAGE =__doc__ 

class ExternalUrlInvalid (BadRequest ):
    """"""
    ID ="EXTERNAL_URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class FieldNameEmpty (BadRequest ):
    """"""
    ID ="FIELD_NAME_EMPTY"
    """"""
    MESSAGE =__doc__ 

class FieldNameInvalid (BadRequest ):
    """"""
    ID ="FIELD_NAME_INVALID"
    """"""
    MESSAGE =__doc__ 

class FileIdInvalid (BadRequest ):
    """"""
    ID ="FILE_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class FileMigrate (BadRequest ):
    """"""
    ID ="FILE_MIGRATE_X"
    """"""
    MESSAGE =__doc__ 

class FilePartsInvalid (BadRequest ):
    """"""
    ID ="FILE_PARTS_INVALID"
    """"""
    MESSAGE =__doc__ 

class FilePartEmpty (BadRequest ):
    """"""
    ID ="FILE_PART_EMPTY"
    """"""
    MESSAGE =__doc__ 

class FilePartInvalid (BadRequest ):
    """"""
    ID ="FILE_PART_INVALID"
    """"""
    MESSAGE =__doc__ 

class FilePartLengthInvalid (BadRequest ):
    """"""
    ID ="FILE_PART_LENGTH_INVALID"
    """"""
    MESSAGE =__doc__ 

class FilePartSizeChanged (BadRequest ):
    """"""
    ID ="FILE_PART_SIZE_CHANGED"
    """"""
    MESSAGE =__doc__ 

class FilePartSizeInvalid (BadRequest ):
    """"""
    ID ="FILE_PART_SIZE_INVALID"
    """"""
    MESSAGE =__doc__ 

class FilePartTooBig (BadRequest ):
    """"""
    ID ="FILE_PART_TOO_BIG"
    """"""
    MESSAGE =__doc__ 

class FilePartMissing (BadRequest ):
    """"""
    ID ="FILE_PART_X_MISSING"
    """"""
    MESSAGE =__doc__ 

class FileReferenceEmpty (BadRequest ):
    """"""
    ID ="FILE_REFERENCE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class FileReferenceExpired (BadRequest ):
    """"""
    ID ="FILE_REFERENCE_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class FileReferenceInvalid (BadRequest ):
    """"""
    ID ="FILE_REFERENCE_INVALID"
    """"""
    MESSAGE =__doc__ 

class FilterIdInvalid (BadRequest ):
    """"""
    ID ="FILTER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class FirstnameInvalid (BadRequest ):
    """"""
    ID ="FIRSTNAME_INVALID"
    """"""
    MESSAGE =__doc__ 

class FolderIdEmpty (BadRequest ):
    """"""
    ID ="FOLDER_ID_EMPTY"
    """"""
    MESSAGE =__doc__ 

class FolderIdInvalid (BadRequest ):
    """"""
    ID ="FOLDER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class FreshChangeAdminsForbidden (BadRequest ):
    """"""
    ID ="FRESH_CHANGE_ADMINS_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class FromMessageBotDisabled (BadRequest ):
    """"""
    ID ="FROM_MESSAGE_BOT_DISABLED"
    """"""
    MESSAGE =__doc__ 

class FromPeerInvalid (BadRequest ):
    """"""
    ID ="FROM_PEER_INVALID"
    """"""
    MESSAGE =__doc__ 

class GameBotInvalid (BadRequest ):
    """"""
    ID ="GAME_BOT_INVALID"
    """"""
    MESSAGE =__doc__ 

class GeoPointInvalid (BadRequest ):
    """"""
    ID ="GEO_POINT_INVALID"
    """"""
    MESSAGE =__doc__ 

class GifContentTypeInvalid (BadRequest ):
    """"""
    ID ="GIF_CONTENT_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class GifIdInvalid (BadRequest ):
    """"""
    ID ="GIF_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class GraphInvalidReload (BadRequest ):
    """"""
    ID ="GRAPH_INVALID_RELOAD"
    """"""
    MESSAGE =__doc__ 

class GraphOutdatedReload (BadRequest ):
    """"""
    ID ="GRAPH_OUTDATED_RELOAD"
    """"""
    MESSAGE =__doc__ 

class GroupcallSsrcDuplicateMuch (BadRequest ):
    """"""
    ID ="GROUPCALL_SSRC_DUPLICATE_MUCH"
    """"""
    MESSAGE =__doc__ 

class GroupedMediaInvalid (BadRequest ):
    """"""
    ID ="GROUPED_MEDIA_INVALID"
    """"""
    MESSAGE =__doc__ 

class GroupCallInvalid (BadRequest ):
    """"""
    ID ="GROUP_CALL_INVALID"
    """"""
    MESSAGE =__doc__ 

class HashInvalid (BadRequest ):
    """"""
    ID ="HASH_INVALID"
    """"""
    MESSAGE =__doc__ 

class ImageProcessFailed (BadRequest ):
    """"""
    ID ="IMAGE_PROCESS_FAILED"
    """"""
    MESSAGE =__doc__ 

class ImportFileInvalid (BadRequest ):
    """"""
    ID ="IMPORT_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ImportFormatUnrecognized (BadRequest ):
    """"""
    ID ="IMPORT_FORMAT_UNRECOGNIZED"
    """"""
    MESSAGE =__doc__ 

class ImportIdInvalid (BadRequest ):
    """"""
    ID ="IMPORT_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class InlineResultExpired (BadRequest ):
    """"""
    ID ="INLINE_RESULT_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class InputConstructorInvalid (BadRequest ):
    """"""
    ID ="INPUT_CONSTRUCTOR_INVALID"
    """"""
    MESSAGE =__doc__ 

class InputFetchError (BadRequest ):
    """"""
    ID ="INPUT_FETCH_ERROR"
    """"""
    MESSAGE =__doc__ 

class InputFetchFail (BadRequest ):
    """"""
    ID ="INPUT_FETCH_FAIL"
    """"""
    MESSAGE =__doc__ 

class InputFilterInvalid (BadRequest ):
    """"""
    ID ="INPUT_FILTER_INVALID"
    """"""
    MESSAGE =__doc__ 

class InputLayerInvalid (BadRequest ):
    """"""
    ID ="INPUT_LAYER_INVALID"
    """"""
    MESSAGE =__doc__ 

class InputMethodInvalid (BadRequest ):
    """"""
    ID ="INPUT_METHOD_INVALID"
    """"""
    MESSAGE =__doc__ 

class InputRequestTooLong (BadRequest ):
    """"""
    ID ="INPUT_REQUEST_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class InputUserDeactivated (BadRequest ):
    """"""
    ID ="INPUT_USER_DEACTIVATED"
    """"""
    MESSAGE =__doc__ 

class InviteHashEmpty (BadRequest ):
    """"""
    ID ="INVITE_HASH_EMPTY"
    """"""
    MESSAGE =__doc__ 

class InviteHashExpired (BadRequest ):
    """"""
    ID ="INVITE_HASH_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class InviteHashInvalid (BadRequest ):
    """"""
    ID ="INVITE_HASH_INVALID"
    """"""
    MESSAGE =__doc__ 

class InviteRequestSent (BadRequest ):
    """"""
    ID ="INVITE_REQUEST_SENT"
    """"""
    MESSAGE =__doc__ 

class InviteRevokedMissing (BadRequest ):
    """"""
    ID ="INVITE_REVOKED_MISSING"
    """"""
    MESSAGE =__doc__ 

class LangPackInvalid (BadRequest ):
    """"""
    ID ="LANG_PACK_INVALID"
    """"""
    MESSAGE =__doc__ 

class LastnameInvalid (BadRequest ):
    """"""
    ID ="LASTNAME_INVALID"
    """"""
    MESSAGE =__doc__ 

class LimitInvalid (BadRequest ):
    """"""
    ID ="LIMIT_INVALID"
    """"""
    MESSAGE =__doc__ 

class LinkNotModified (BadRequest ):
    """"""
    ID ="LINK_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class LocationInvalid (BadRequest ):
    """"""
    ID ="LOCATION_INVALID"
    """"""
    MESSAGE =__doc__ 

class MaxIdInvalid (BadRequest ):
    """"""
    ID ="MAX_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class MaxQtsInvalid (BadRequest ):
    """"""
    ID ="MAX_QTS_INVALID"
    """"""
    MESSAGE =__doc__ 

class Md5ChecksumInvalid (BadRequest ):
    """"""
    ID ="MD5_CHECKSUM_INVALID"
    """"""
    MESSAGE =__doc__ 

class MediaCaptionTooLong (BadRequest ):
    """"""
    ID ="MEDIA_CAPTION_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class MediaEmpty (BadRequest ):
    """"""
    ID ="MEDIA_EMPTY"
    """"""
    MESSAGE =__doc__ 

class MediaInvalid (BadRequest ):
    """"""
    ID ="MEDIA_INVALID"
    """"""
    MESSAGE =__doc__ 

class MediaNewInvalid (BadRequest ):
    """"""
    ID ="MEDIA_NEW_INVALID"
    """"""
    MESSAGE =__doc__ 

class MediaPrevInvalid (BadRequest ):
    """"""
    ID ="MEDIA_PREV_INVALID"
    """"""
    MESSAGE =__doc__ 

class MegagroupIdInvalid (BadRequest ):
    """"""
    ID ="MEGAGROUP_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class MegagroupPrehistoryHidden (BadRequest ):
    """"""
    ID ="MEGAGROUP_PREHISTORY_HIDDEN"
    """"""
    MESSAGE =__doc__ 

class MegagroupRequired (BadRequest ):
    """"""
    ID ="MEGAGROUP_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class MessageEditTimeExpired (BadRequest ):
    """"""
    ID ="MESSAGE_EDIT_TIME_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class MessageEmpty (BadRequest ):
    """"""
    ID ="MESSAGE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class MessageIdsEmpty (BadRequest ):
    """"""
    ID ="MESSAGE_IDS_EMPTY"
    """"""
    MESSAGE =__doc__ 

class MessageIdInvalid (BadRequest ):
    """"""
    ID ="MESSAGE_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class MessageNotModified (BadRequest ):
    """"""
    ID ="MESSAGE_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class MessagePollClosed (BadRequest ):
    """"""
    ID ="MESSAGE_POLL_CLOSED"
    """"""
    MESSAGE =__doc__ 

class MessageTooLong (BadRequest ):
    """"""
    ID ="MESSAGE_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class MethodInvalid (BadRequest ):
    """"""
    ID ="METHOD_INVALID"
    """"""
    MESSAGE =__doc__ 

class MsgIdInvalid (BadRequest ):
    """"""
    ID ="MSG_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class MsgWaitFailed (BadRequest ):
    """"""
    ID ="MSG_WAIT_FAILED"
    """"""
    MESSAGE =__doc__ 

class MultiMediaTooLong (BadRequest ):
    """"""
    ID ="MULTI_MEDIA_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class NewSaltInvalid (BadRequest ):
    """"""
    ID ="NEW_SALT_INVALID"
    """"""
    MESSAGE =__doc__ 

class NewSettingsInvalid (BadRequest ):
    """"""
    ID ="NEW_SETTINGS_INVALID"
    """"""
    MESSAGE =__doc__ 

class NextOffsetInvalid (BadRequest ):
    """"""
    ID ="NEXT_OFFSET_INVALID"
    """"""
    MESSAGE =__doc__ 

class OffsetInvalid (BadRequest ):
    """"""
    ID ="OFFSET_INVALID"
    """"""
    MESSAGE =__doc__ 

class OffsetPeerIdInvalid (BadRequest ):
    """"""
    ID ="OFFSET_PEER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class OptionsTooMuch (BadRequest ):
    """"""
    ID ="OPTIONS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class OptionInvalid (BadRequest ):
    """"""
    ID ="OPTION_INVALID"
    """"""
    MESSAGE =__doc__ 

class PackShortNameInvalid (BadRequest ):
    """"""
    ID ="PACK_SHORT_NAME_INVALID"
    """"""
    MESSAGE =__doc__ 

class PackShortNameOccupied (BadRequest ):
    """"""
    ID ="PACK_SHORT_NAME_OCCUPIED"
    """"""
    MESSAGE =__doc__ 

class PackTitleInvalid (BadRequest ):
    """"""
    ID ="PACK_TITLE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ParticipantsTooFew (BadRequest ):
    """"""
    ID ="PARTICIPANTS_TOO_FEW"
    """"""
    MESSAGE =__doc__ 

class ParticipantVersionOutdated (BadRequest ):
    """"""
    ID ="PARTICIPANT_VERSION_OUTDATED"
    """"""
    MESSAGE =__doc__ 

class PasswordEmpty (BadRequest ):
    """"""
    ID ="PASSWORD_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PasswordHashInvalid (BadRequest ):
    """"""
    ID ="PASSWORD_HASH_INVALID"
    """"""
    MESSAGE =__doc__ 

class PasswordMissing (BadRequest ):
    """"""
    ID ="PASSWORD_MISSING"
    """"""
    MESSAGE =__doc__ 

class PasswordRecoveryNa (BadRequest ):
    """"""
    ID ="PASSWORD_RECOVERY_NA"
    """"""
    MESSAGE =__doc__ 

class PasswordRequired (BadRequest ):
    """"""
    ID ="PASSWORD_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class PasswordTooFresh (BadRequest ):
    """"""
    ID ="PASSWORD_TOO_FRESH_X"
    """"""
    MESSAGE =__doc__ 

class PaymentProviderInvalid (BadRequest ):
    """"""
    ID ="PAYMENT_PROVIDER_INVALID"
    """"""
    MESSAGE =__doc__ 

class PeerFlood (BadRequest ):
    """"""
    ID ="PEER_FLOOD"
    """"""
    MESSAGE =__doc__ 

class PeerIdInvalid (BadRequest ):
    """"""
    ID ="PEER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class PeerIdNotSupported (BadRequest ):
    """"""
    ID ="PEER_ID_NOT_SUPPORTED"
    """"""
    MESSAGE =__doc__ 

class PersistentTimestampEmpty (BadRequest ):
    """"""
    ID ="PERSISTENT_TIMESTAMP_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PersistentTimestampInvalid (BadRequest ):
    """"""
    ID ="PERSISTENT_TIMESTAMP_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhoneCodeEmpty (BadRequest ):
    """"""
    ID ="PHONE_CODE_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PhoneCodeExpired (BadRequest ):
    """"""
    ID ="PHONE_CODE_EXPIRED"
    """"""
    MESSAGE =__doc__ 

class PhoneCodeHashEmpty (BadRequest ):
    """"""
    ID ="PHONE_CODE_HASH_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PhoneCodeInvalid (BadRequest ):
    """"""
    ID ="PHONE_CODE_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberAppSignupForbidden (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_APP_SIGNUP_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberBanned (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_BANNED"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberFlood (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_FLOOD"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberInvalid (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberOccupied (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_OCCUPIED"
    """"""
    MESSAGE =__doc__ 

class PhoneNumberUnoccupied (BadRequest ):
    """"""
    ID ="PHONE_NUMBER_UNOCCUPIED"
    """"""
    MESSAGE =__doc__ 

class PhonePasswordProtected (BadRequest ):
    """"""
    ID ="PHONE_PASSWORD_PROTECTED"
    """"""
    MESSAGE =__doc__ 

class PhotoContentTypeInvalid (BadRequest ):
    """"""
    ID ="PHOTO_CONTENT_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhotoContentUrlEmpty (BadRequest ):
    """"""
    ID ="PHOTO_CONTENT_URL_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PhotoCropFileMissing (BadRequest ):
    """"""
    ID ="PHOTO_CROP_FILE_MISSING"
    """"""
    MESSAGE =__doc__ 

class PhotoCropSizeSmall (BadRequest ):
    """"""
    ID ="PHOTO_CROP_SIZE_SMALL"
    """"""
    MESSAGE =__doc__ 

class PhotoExtInvalid (BadRequest ):
    """"""
    ID ="PHOTO_EXT_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhotoFileMissing (BadRequest ):
    """"""
    ID ="PHOTO_FILE_MISSING"
    """"""
    MESSAGE =__doc__ 

class PhotoIdInvalid (BadRequest ):
    """"""
    ID ="PHOTO_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhotoInvalid (BadRequest ):
    """"""
    ID ="PHOTO_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhotoInvalidDimensions (BadRequest ):
    """"""
    ID ="PHOTO_INVALID_DIMENSIONS"
    """"""
    MESSAGE =__doc__ 

class PhotoSaveFileInvalid (BadRequest ):
    """"""
    ID ="PHOTO_SAVE_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class PhotoThumbUrlEmpty (BadRequest ):
    """"""
    ID ="PHOTO_THUMB_URL_EMPTY"
    """"""
    MESSAGE =__doc__ 

class PhotoThumbUrlInvalid (BadRequest ):
    """"""
    ID ="PHOTO_THUMB_URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class PinnedDialogsTooMuch (BadRequest ):
    """"""
    ID ="PINNED_DIALOGS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class PinRestricted (BadRequest ):
    """"""
    ID ="PIN_RESTRICTED"
    """"""
    MESSAGE =__doc__ 

class PollAnswersInvalid (BadRequest ):
    """"""
    ID ="POLL_ANSWERS_INVALID"
    """"""
    MESSAGE =__doc__ 

class PollOptionDuplicate (BadRequest ):
    """"""
    ID ="POLL_OPTION_DUPLICATE"
    """"""
    MESSAGE =__doc__ 

class PollOptionInvalid (BadRequest ):
    """"""
    ID ="POLL_OPTION_INVALID"
    """"""
    MESSAGE =__doc__ 

class PollQuestionInvalid (BadRequest ):
    """"""
    ID ="POLL_QUESTION_INVALID"
    """"""
    MESSAGE =__doc__ 

class PollUnsupported (BadRequest ):
    """"""
    ID ="POLL_UNSUPPORTED"
    """"""
    MESSAGE =__doc__ 

class PollVoteRequired (BadRequest ):
    """"""
    ID ="POLL_VOTE_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class PrivacyKeyInvalid (BadRequest ):
    """"""
    ID ="PRIVACY_KEY_INVALID"
    """"""
    MESSAGE =__doc__ 

class PrivacyTooLong (BadRequest ):
    """"""
    ID ="PRIVACY_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class PrivacyValueInvalid (BadRequest ):
    """"""
    ID ="PRIVACY_VALUE_INVALID"
    """"""
    MESSAGE =__doc__ 

class QueryIdEmpty (BadRequest ):
    """"""
    ID ="QUERY_ID_EMPTY"
    """"""
    MESSAGE =__doc__ 

class QueryIdInvalid (BadRequest ):
    """"""
    ID ="QUERY_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class QueryTooShort (BadRequest ):
    """"""
    ID ="QUERY_TOO_SHORT"
    """"""
    MESSAGE =__doc__ 

class QuizCorrectAnswersEmpty (BadRequest ):
    """"""
    ID ="QUIZ_CORRECT_ANSWERS_EMPTY"
    """"""
    MESSAGE =__doc__ 

class QuizCorrectAnswersTooMuch (BadRequest ):
    """"""
    ID ="QUIZ_CORRECT_ANSWERS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class QuizCorrectAnswerInvalid (BadRequest ):
    """"""
    ID ="QUIZ_CORRECT_ANSWER_INVALID"
    """"""
    MESSAGE =__doc__ 

class QuizMultipleInvalid (BadRequest ):
    """"""
    ID ="QUIZ_MULTIPLE_INVALID"
    """"""
    MESSAGE =__doc__ 

class RandomIdEmpty (BadRequest ):
    """"""
    ID ="RANDOM_ID_EMPTY"
    """"""
    MESSAGE =__doc__ 

class RandomIdInvalid (BadRequest ):
    """"""
    ID ="RANDOM_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class RandomLengthInvalid (BadRequest ):
    """"""
    ID ="RANDOM_LENGTH_INVALID"
    """"""
    MESSAGE =__doc__ 

class RangesInvalid (BadRequest ):
    """"""
    ID ="RANGES_INVALID"
    """"""
    MESSAGE =__doc__ 

class ReactionEmpty (BadRequest ):
    """"""
    ID ="REACTION_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ReactionInvalid (BadRequest ):
    """"""
    ID ="REACTION_INVALID"
    """"""
    MESSAGE =__doc__ 

class ReflectorNotAvailable (BadRequest ):
    """"""
    ID ="REFLECTOR_NOT_AVAILABLE"
    """"""
    MESSAGE =__doc__ 

class ReplyMarkupBuyEmpty (BadRequest ):
    """"""
    ID ="REPLY_MARKUP_BUY_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ReplyMarkupGameEmpty (BadRequest ):
    """"""
    ID ="REPLY_MARKUP_GAME_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ReplyMarkupInvalid (BadRequest ):
    """"""
    ID ="REPLY_MARKUP_INVALID"
    """"""
    MESSAGE =__doc__ 

class ReplyMarkupTooLong (BadRequest ):
    """"""
    ID ="REPLY_MARKUP_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class ResultsTooMuch (BadRequest ):
    """"""
    ID ="RESULTS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class ResultIdDuplicate (BadRequest ):
    """"""
    ID ="RESULT_ID_DUPLICATE"
    """"""
    MESSAGE =__doc__ 

class ResultIdEmpty (BadRequest ):
    """"""
    ID ="RESULT_ID_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ResultIdInvalid (BadRequest ):
    """"""
    ID ="RESULT_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class ResultTypeInvalid (BadRequest ):
    """"""
    ID ="RESULT_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class RevoteNotAllowed (BadRequest ):
    """"""
    ID ="REVOTE_NOT_ALLOWED"
    """"""
    MESSAGE =__doc__ 

class RsaDecryptFailed (BadRequest ):
    """"""
    ID ="RSA_DECRYPT_FAILED"
    """"""
    MESSAGE =__doc__ 

class ScheduleBotNotAllowed (BadRequest ):
    """"""
    ID ="SCHEDULE_BOT_NOT_ALLOWED"
    """"""
    MESSAGE =__doc__ 

class ScheduleDateInvalid (BadRequest ):
    """"""
    ID ="SCHEDULE_DATE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ScheduleDateTooLate (BadRequest ):
    """"""
    ID ="SCHEDULE_DATE_TOO_LATE"
    """"""
    MESSAGE =__doc__ 

class ScheduleStatusPrivate (BadRequest ):
    """"""
    ID ="SCHEDULE_STATUS_PRIVATE"
    """"""
    MESSAGE =__doc__ 

class ScheduleTooMuch (BadRequest ):
    """"""
    ID ="SCHEDULE_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class SearchQueryEmpty (BadRequest ):
    """"""
    ID ="SEARCH_QUERY_EMPTY"
    """"""
    MESSAGE =__doc__ 

class SecondsInvalid (BadRequest ):
    """"""
    ID ="SECONDS_INVALID"
    """"""
    MESSAGE =__doc__ 

class SendMessageMediaInvalid (BadRequest ):
    """"""
    ID ="SEND_MESSAGE_MEDIA_INVALID"
    """"""
    MESSAGE =__doc__ 

class SendMessageTypeInvalid (BadRequest ):
    """"""
    ID ="SEND_MESSAGE_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class SessionTooFresh (BadRequest ):
    """"""
    ID ="SESSION_TOO_FRESH_X"
    """"""
    MESSAGE =__doc__ 

class SettingsInvalid (BadRequest ):
    """"""
    ID ="SETTINGS_INVALID"
    """"""
    MESSAGE =__doc__ 

class Sha256HashInvalid (BadRequest ):
    """"""
    ID ="SHA256_HASH_INVALID"
    """"""
    MESSAGE =__doc__ 

class ShortnameOccupyFailed (BadRequest ):
    """"""
    ID ="SHORTNAME_OCCUPY_FAILED"
    """"""
    MESSAGE =__doc__ 

class SlowmodeMultiMsgsDisabled (BadRequest ):
    """"""
    ID ="SLOWMODE_MULTI_MSGS_DISABLED"
    """"""
    MESSAGE =__doc__ 

class SmsCodeCreateFailed (BadRequest ):
    """"""
    ID ="SMS_CODE_CREATE_FAILED"
    """"""
    MESSAGE =__doc__ 

class SrpIdInvalid (BadRequest ):
    """"""
    ID ="SRP_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class SrpPasswordChanged (BadRequest ):
    """"""
    ID ="SRP_PASSWORD_CHANGED"
    """"""
    MESSAGE =__doc__ 

class StartParamEmpty (BadRequest ):
    """"""
    ID ="START_PARAM_EMPTY"
    """"""
    MESSAGE =__doc__ 

class StartParamInvalid (BadRequest ):
    """"""
    ID ="START_PARAM_INVALID"
    """"""
    MESSAGE =__doc__ 

class StartParamTooLong (BadRequest ):
    """"""
    ID ="START_PARAM_TOO_LONG"
    """"""
    MESSAGE =__doc__ 

class StickersetInvalid (BadRequest ):
    """"""
    ID ="STICKERSET_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickersetNotModified (BadRequest ):
    """"""
    ID ="STICKERSET_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class StickersEmpty (BadRequest ):
    """"""
    ID ="STICKERS_EMPTY"
    """"""
    MESSAGE =__doc__ 

class StickersTooMuch (BadRequest ):
    """"""
    ID ="STICKERS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class StickerDocumentInvalid (BadRequest ):
    """"""
    ID ="STICKER_DOCUMENT_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickerEmojiInvalid (BadRequest ):
    """"""
    ID ="STICKER_EMOJI_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickerFileInvalid (BadRequest ):
    """"""
    ID ="STICKER_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickerIdInvalid (BadRequest ):
    """"""
    ID ="STICKER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickerInvalid (BadRequest ):
    """"""
    ID ="STICKER_INVALID"
    """"""
    MESSAGE =__doc__ 

class StickerPngDimensions (BadRequest ):
    """"""
    ID ="STICKER_PNG_DIMENSIONS"
    """"""
    MESSAGE =__doc__ 

class StickerPngNopng (BadRequest ):
    """"""
    ID ="STICKER_PNG_NOPNG"
    """"""
    MESSAGE =__doc__ 

class StickerTgsNotgs (BadRequest ):
    """"""
    ID ="STICKER_TGS_NOTGS"
    """"""
    MESSAGE =__doc__ 

class StickerThumbPngNopng (BadRequest ):
    """"""
    ID ="STICKER_THUMB_PNG_NOPNG"
    """"""
    MESSAGE =__doc__ 

class StickerVideoNowebm (BadRequest ):
    """"""
    ID ="STICKER_VIDEO_NOWEBM"
    """"""
    MESSAGE =__doc__ 

class TakeoutInvalid (BadRequest ):
    """"""
    ID ="TAKEOUT_INVALID"
    """"""
    MESSAGE =__doc__ 

class TakeoutRequired (BadRequest ):
    """"""
    ID ="TAKEOUT_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class TempAuthKeyEmpty (BadRequest ):
    """"""
    ID ="TEMP_AUTH_KEY_EMPTY"
    """"""
    MESSAGE =__doc__ 

class ThemeFileInvalid (BadRequest ):
    """"""
    ID ="THEME_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class ThemeFormatInvalid (BadRequest ):
    """"""
    ID ="THEME_FORMAT_INVALID"
    """"""
    MESSAGE =__doc__ 

class ThemeInvalid (BadRequest ):
    """"""
    ID ="THEME_INVALID"
    """"""
    MESSAGE =__doc__ 

class ThemeMimeInvalid (BadRequest ):
    """"""
    ID ="THEME_MIME_INVALID"
    """"""
    MESSAGE =__doc__ 

class TmpPasswordDisabled (BadRequest ):
    """"""
    ID ="TMP_PASSWORD_DISABLED"
    """"""
    MESSAGE =__doc__ 

class TmpPasswordInvalid (BadRequest ):
    """"""
    ID ="TMP_PASSWORD_INVALID"
    """"""
    MESSAGE =__doc__ 

class TokenInvalid (BadRequest ):
    """"""
    ID ="TOKEN_INVALID"
    """"""
    MESSAGE =__doc__ 

class TtlDaysInvalid (BadRequest ):
    """"""
    ID ="TTL_DAYS_INVALID"
    """"""
    MESSAGE =__doc__ 

class TtlMediaInvalid (BadRequest ):
    """"""
    ID ="TTL_MEDIA_INVALID"
    """"""
    MESSAGE =__doc__ 

class TypesEmpty (BadRequest ):
    """"""
    ID ="TYPES_EMPTY"
    """"""
    MESSAGE =__doc__ 

class TypeConstructorInvalid (BadRequest ):
    """"""
    ID ="TYPE_CONSTRUCTOR_INVALID"
    """"""
    MESSAGE =__doc__ 

class UntilDateInvalid (BadRequest ):
    """"""
    ID ="UNTIL_DATE_INVALID"
    """"""
    MESSAGE =__doc__ 

class UrlInvalid (BadRequest ):
    """"""
    ID ="URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class UsageLimitInvalid (BadRequest ):
    """"""
    ID ="USAGE_LIMIT_INVALID"
    """"""
    MESSAGE =__doc__ 

class UsernameInvalid (BadRequest ):
    """"""
    ID ="USERNAME_INVALID"
    """"""
    MESSAGE =__doc__ 

class UsernameNotModified (BadRequest ):
    """"""
    ID ="USERNAME_NOT_MODIFIED"
    """"""
    MESSAGE =__doc__ 

class UsernameNotOccupied (BadRequest ):
    """"""
    ID ="USERNAME_NOT_OCCUPIED"
    """"""
    MESSAGE =__doc__ 

class UsernameOccupied (BadRequest ):
    """"""
    ID ="USERNAME_OCCUPIED"
    """"""
    MESSAGE =__doc__ 

class UserpicUploadRequired (BadRequest ):
    """"""
    ID ="USERPIC_UPLOAD_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class UsersTooFew (BadRequest ):
    """"""
    ID ="USERS_TOO_FEW"
    """"""
    MESSAGE =__doc__ 

class UsersTooMuch (BadRequest ):
    """"""
    ID ="USERS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class UserAdminInvalid (BadRequest ):
    """"""
    ID ="USER_ADMIN_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserAlreadyParticipant (BadRequest ):
    """"""
    ID ="USER_ALREADY_PARTICIPANT"
    """"""
    MESSAGE =__doc__ 

class UserBannedInChannel (BadRequest ):
    """"""
    ID ="USER_BANNED_IN_CHANNEL"
    """"""
    MESSAGE =__doc__ 

class UserBlocked (BadRequest ):
    """"""
    ID ="USER_BLOCKED"
    """"""
    MESSAGE =__doc__ 

class UserBot (BadRequest ):
    """"""
    ID ="USER_BOT"
    """"""
    MESSAGE =__doc__ 

class UserBotInvalid (BadRequest ):
    """"""
    ID ="USER_BOT_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserBotRequired (BadRequest ):
    """"""
    ID ="USER_BOT_REQUIRED"
    """"""
    MESSAGE =__doc__ 

class UserChannelsTooMuch (BadRequest ):
    """"""
    ID ="USER_CHANNELS_TOO_MUCH"
    """"""
    MESSAGE =__doc__ 

class UserCreator (BadRequest ):
    """"""
    ID ="USER_CREATOR"
    """"""
    MESSAGE =__doc__ 

class UserIdInvalid (BadRequest ):
    """"""
    ID ="USER_ID_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserInvalid (BadRequest ):
    """"""
    ID ="USER_INVALID"
    """"""
    MESSAGE =__doc__ 

class UserIsBlocked (BadRequest ):
    """"""
    ID ="USER_IS_BLOCKED"
    """"""
    MESSAGE =__doc__ 

class UserIsBot (BadRequest ):
    """"""
    ID ="USER_IS_BOT"
    """"""
    MESSAGE =__doc__ 

class UserKicked (BadRequest ):
    """"""
    ID ="USER_KICKED"
    """"""
    MESSAGE =__doc__ 

class UserNotMutualContact (BadRequest ):
    """"""
    ID ="USER_NOT_MUTUAL_CONTACT"
    """"""
    MESSAGE =__doc__ 

class UserNotParticipant (BadRequest ):
    """"""
    ID ="USER_NOT_PARTICIPANT"
    """"""
    MESSAGE =__doc__ 

class VideoContentTypeInvalid (BadRequest ):
    """"""
    ID ="VIDEO_CONTENT_TYPE_INVALID"
    """"""
    MESSAGE =__doc__ 

class VideoFileInvalid (BadRequest ):
    """"""
    ID ="VIDEO_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class VoiceMessagesForbidden (BadRequest ):
    """"""
    ID ="VOICE_MESSAGES_FORBIDDEN"
    """"""
    MESSAGE =__doc__ 

class VolumeLocNotFound (BadRequest ):
    """"""
    ID ="VOLUME_LOC_NOT_FOUND"
    """"""
    MESSAGE =__doc__ 

class WallpaperFileInvalid (BadRequest ):
    """"""
    ID ="WALLPAPER_FILE_INVALID"
    """"""
    MESSAGE =__doc__ 

class WallpaperInvalid (BadRequest ):
    """"""
    ID ="WALLPAPER_INVALID"
    """"""
    MESSAGE =__doc__ 

class WallpaperMimeInvalid (BadRequest ):
    """"""
    ID ="WALLPAPER_MIME_INVALID"
    """"""
    MESSAGE =__doc__ 

class WcConvertUrlInvalid (BadRequest ):
    """"""
    ID ="WC_CONVERT_URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class WebdocumentInvalid (BadRequest ):
    """"""
    ID ="WEBDOCUMENT_INVALID"
    """"""
    MESSAGE =__doc__ 

class WebdocumentMimeInvalid (BadRequest ):
    """"""
    ID ="WEBDOCUMENT_MIME_INVALID"
    """"""
    MESSAGE =__doc__ 

class WebdocumentSizeTooBig (BadRequest ):
    """"""
    ID ="WEBDOCUMENT_SIZE_TOO_BIG"
    """"""
    MESSAGE =__doc__ 

class WebdocumentUrlEmpty (BadRequest ):
    """"""
    ID ="WEBDOCUMENT_URL_EMPTY"
    """"""
    MESSAGE =__doc__ 

class WebdocumentUrlInvalid (BadRequest ):
    """"""
    ID ="WEBDOCUMENT_URL_INVALID"
    """"""
    MESSAGE =__doc__ 

class WebpageCurlFailed (BadRequest ):
    """"""
    ID ="WEBPAGE_CURL_FAILED"
    """"""
    MESSAGE =__doc__ 

class WebpageMediaEmpty (BadRequest ):
    """"""
    ID ="WEBPAGE_MEDIA_EMPTY"
    """"""
    MESSAGE =__doc__ 

class YouBlockedUser (BadRequest ):
    """"""
    ID ="YOU_BLOCKED_USER"
    """"""
    MESSAGE =__doc__ 

