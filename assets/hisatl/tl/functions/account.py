""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeAccountDaysTTL ,TypeAutoDownloadSettings ,TypeAutoSaveSettings ,TypeBaseTheme ,TypeCodeSettings ,TypeEmailVerification ,TypeEmailVerifyPurpose ,TypeEmojiStatus ,TypeGlobalPrivacySettings ,TypeInputCheckPasswordSRP ,TypeInputDocument ,TypeInputFile ,TypeInputNotifyPeer ,TypeInputPeer ,TypeInputPeerNotifySettings ,TypeInputPhoto ,TypeInputPrivacyKey ,TypeInputPrivacyRule ,TypeInputSecureValue ,TypeInputTheme ,TypeInputThemeSettings ,TypeInputWallPaper ,TypeReportReason ,TypeSecureCredentialsEncrypted ,TypeSecureValueHash ,TypeSecureValueType ,TypeWallPaperSettings 
    from ...tl .types .account import TypePasswordInputSettings 

class AcceptAuthorizationRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf3ed4c73 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,bot_id :int ,scope :str ,public_key :str ,value_hashes :List ['TypeSecureValueHash'],credentials :'TypeSecureCredentialsEncrypted'):
        """"""
        self .bot_id =bot_id 
        self .scope =scope 
        self .public_key =public_key 
        self .value_hashes =value_hashes 
        self .credentials =credentials 

    def to_dict (self ):
        return {
        '_':'AcceptAuthorizationRequest',
        'bot_id':self .bot_id ,
        'scope':self .scope ,
        'public_key':self .public_key ,
        'value_hashes':[]if self .value_hashes is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .value_hashes ],
        'credentials':self .credentials .to_dict ()if isinstance (self .credentials ,TLObject )else self .credentials 
        }

    def _bytes (self ):
        return b''.join ((
        b'sL\xed\xf3',
        struct .pack ('<q',self .bot_id ),
        self .serialize_bytes (self .scope ),
        self .serialize_bytes (self .public_key ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .value_hashes )),b''.join (x ._bytes ()for x in self .value_hashes ),
        self .credentials ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot_id =reader .read_long ()
        _scope =reader .tgread_string ()
        _public_key =reader .tgread_string ()
        reader .read_int ()
        _value_hashes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _value_hashes .append (_x )

        _credentials =reader .tgread_object ()
        return cls (bot_id =_bot_id ,scope =_scope ,public_key =_public_key ,value_hashes =_value_hashes ,credentials =_credentials )

class CancelPasswordEmailRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc1cbd5b6 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'CancelPasswordEmailRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb6\xd5\xcb\xc1',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ChangeAuthorizationSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x40f48462 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,hash :int ,confirmed :Optional [bool ]=None ,encrypted_requests_disabled :Optional [bool ]=None ,call_requests_disabled :Optional [bool ]=None ):
        """"""
        self .hash =hash 
        self .confirmed =confirmed 
        self .encrypted_requests_disabled =encrypted_requests_disabled 
        self .call_requests_disabled =call_requests_disabled 

    def to_dict (self ):
        return {
        '_':'ChangeAuthorizationSettingsRequest',
        'hash':self .hash ,
        'confirmed':self .confirmed ,
        'encrypted_requests_disabled':self .encrypted_requests_disabled ,
        'call_requests_disabled':self .call_requests_disabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'b\x84\xf4@',
        struct .pack ('<I',(0 if self .confirmed is None or self .confirmed is False else 8 )|(0 if self .encrypted_requests_disabled is None else 1 )|(0 if self .call_requests_disabled is None else 2 )),
        struct .pack ('<q',self .hash ),
        b''if self .encrypted_requests_disabled is None else (b'\xb5ur\x99'if self .encrypted_requests_disabled else b'7\x97y\xbc'),
        b''if self .call_requests_disabled is None else (b'\xb5ur\x99'if self .call_requests_disabled else b'7\x97y\xbc'),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _confirmed =bool (flags &8 )
        _hash =reader .read_long ()
        if flags &1 :
            _encrypted_requests_disabled =reader .tgread_bool ()
        else :
            _encrypted_requests_disabled =None 
        if flags &2 :
            _call_requests_disabled =reader .tgread_bool ()
        else :
            _call_requests_disabled =None 
        return cls (hash =_hash ,confirmed =_confirmed ,encrypted_requests_disabled =_encrypted_requests_disabled ,call_requests_disabled =_call_requests_disabled )

class ChangePhoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x70c32edb 
    SUBCLASS_OF_ID =0x2da17977 

    def __init__ (self ,phone_number :str ,phone_code_hash :str ,phone_code :str ):
        """"""
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .phone_code =phone_code 

    def to_dict (self ):
        return {
        '_':'ChangePhoneRequest',
        'phone_number':self .phone_number ,
        'phone_code_hash':self .phone_code_hash ,
        'phone_code':self .phone_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdb.\xc3p',
        self .serialize_bytes (self .phone_number ),
        self .serialize_bytes (self .phone_code_hash ),
        self .serialize_bytes (self .phone_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_number =reader .tgread_string ()
        _phone_code_hash =reader .tgread_string ()
        _phone_code =reader .tgread_string ()
        return cls (phone_number =_phone_number ,phone_code_hash =_phone_code_hash ,phone_code =_phone_code )

class CheckUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2714d86c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,username :str ):
        """"""
        self .username =username 

    def to_dict (self ):
        return {
        '_':'CheckUsernameRequest',
        'username':self .username 
        }

    def _bytes (self ):
        return b''.join ((
        b"l\xd8\x14'",
        self .serialize_bytes (self .username ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _username =reader .tgread_string ()
        return cls (username =_username )

class ClearRecentEmojiStatusesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x18201aae 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ClearRecentEmojiStatusesRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xae\x1a \x18',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ConfirmPasswordEmailRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8fdf1920 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,code :str ):
        """"""
        self .code =code 

    def to_dict (self ):
        return {
        '_':'ConfirmPasswordEmailRequest',
        'code':self .code 
        }

    def _bytes (self ):
        return b''.join ((
        b' \x19\xdf\x8f',
        self .serialize_bytes (self .code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _code =reader .tgread_string ()
        return cls (code =_code )

class ConfirmPhoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5f2178c3 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,phone_code_hash :str ,phone_code :str ):
        """"""
        self .phone_code_hash =phone_code_hash 
        self .phone_code =phone_code 

    def to_dict (self ):
        return {
        '_':'ConfirmPhoneRequest',
        'phone_code_hash':self .phone_code_hash ,
        'phone_code':self .phone_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc3x!_',
        self .serialize_bytes (self .phone_code_hash ),
        self .serialize_bytes (self .phone_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_code_hash =reader .tgread_string ()
        _phone_code =reader .tgread_string ()
        return cls (phone_code_hash =_phone_code_hash ,phone_code =_phone_code )

class CreateThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x652e4400 
    SUBCLASS_OF_ID =0x56b4c80c 

    def __init__ (self ,slug :str ,title :str ,document :Optional ['TypeInputDocument']=None ,settings :Optional [List ['TypeInputThemeSettings']]=None ):
        """"""
        self .slug =slug 
        self .title =title 
        self .document =document 
        self .settings =settings 

    async def resolve (self ,client ,utils ):
        if self .document :
            self .document =utils .get_input_document (self .document )

    def to_dict (self ):
        return {
        '_':'CreateThemeRequest',
        'slug':self .slug ,
        'title':self .title ,
        'document':self .document .to_dict ()if isinstance (self .document ,TLObject )else self .document ,
        'settings':[]if self .settings is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .settings ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x00D.e',
        struct .pack ('<I',(0 if self .document is None or self .document is False else 4 )|(0 if self .settings is None or self .settings is False else 8 )),
        self .serialize_bytes (self .slug ),
        self .serialize_bytes (self .title ),
        b''if self .document is None or self .document is False else (self .document ._bytes ()),
        b''if self .settings is None or self .settings is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .settings )),b''.join (x ._bytes ()for x in self .settings ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _slug =reader .tgread_string ()
        _title =reader .tgread_string ()
        if flags &4 :
            _document =reader .tgread_object ()
        else :
            _document =None 
        if flags &8 :
            reader .read_int ()
            _settings =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _settings .append (_x )

        else :
            _settings =None 
        return cls (slug =_slug ,title =_title ,document =_document ,settings =_settings )

class DeclinePasswordResetRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4c9409f6 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'DeclinePasswordResetRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf6\t\x94L',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class DeleteAccountRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa2c0cf74 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,reason :str ,password :Optional ['TypeInputCheckPasswordSRP']=None ):
        """"""
        self .reason =reason 
        self .password =password 

    def to_dict (self ):
        return {
        '_':'DeleteAccountRequest',
        'reason':self .reason ,
        'password':self .password .to_dict ()if isinstance (self .password ,TLObject )else self .password 
        }

    def _bytes (self ):
        return b''.join ((
        b't\xcf\xc0\xa2',
        struct .pack ('<I',(0 if self .password is None or self .password is False else 1 )),
        self .serialize_bytes (self .reason ),
        b''if self .password is None or self .password is False else (self .password ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _reason =reader .tgread_string ()
        if flags &1 :
            _password =reader .tgread_object ()
        else :
            _password =None 
        return cls (reason =_reason ,password =_password )

class DeleteAutoSaveExceptionsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x53bc0020 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'DeleteAutoSaveExceptionsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b' \x00\xbcS',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class DeleteSecureValueRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb880bc4b 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,types :List ['TypeSecureValueType']):
        """"""
        self .types =types 

    def to_dict (self ):
        return {
        '_':'DeleteSecureValueRequest',
        'types':[]if self .types is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .types ]
        }

    def _bytes (self ):
        return b''.join ((
        b'K\xbc\x80\xb8',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .types )),b''.join (x ._bytes ()for x in self .types ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _types =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _types .append (_x )

        return cls (types =_types )

class FinishTakeoutSessionRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1d2652ee 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,success :Optional [bool ]=None ):
        """"""
        self .success =success 

    def to_dict (self ):
        return {
        '_':'FinishTakeoutSessionRequest',
        'success':self .success 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeeR&\x1d',
        struct .pack ('<I',(0 if self .success is None or self .success is False else 1 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _success =bool (flags &1 )
        return cls (success =_success )

class GetAccountTTLRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8fc711d 
    SUBCLASS_OF_ID =0xbaa39d88 

    def to_dict (self ):
        return {
        '_':'GetAccountTTLRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1dq\xfc\x08',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetAllSecureValuesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb288bc7d 
    SUBCLASS_OF_ID =0xe82e4121 

    def to_dict (self ):
        return {
        '_':'GetAllSecureValuesRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'}\xbc\x88\xb2',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetAuthorizationFormRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa929597a 
    SUBCLASS_OF_ID =0x78049a94 

    def __init__ (self ,bot_id :int ,scope :str ,public_key :str ):
        """"""
        self .bot_id =bot_id 
        self .scope =scope 
        self .public_key =public_key 

    def to_dict (self ):
        return {
        '_':'GetAuthorizationFormRequest',
        'bot_id':self .bot_id ,
        'scope':self .scope ,
        'public_key':self .public_key 
        }

    def _bytes (self ):
        return b''.join ((
        b'zY)\xa9',
        struct .pack ('<q',self .bot_id ),
        self .serialize_bytes (self .scope ),
        self .serialize_bytes (self .public_key ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot_id =reader .read_long ()
        _scope =reader .tgread_string ()
        _public_key =reader .tgread_string ()
        return cls (bot_id =_bot_id ,scope =_scope ,public_key =_public_key )

class GetAuthorizationsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe320c158 
    SUBCLASS_OF_ID =0xbf5e0ff 

    def to_dict (self ):
        return {
        '_':'GetAuthorizationsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'X\xc1 \xe3',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetAutoDownloadSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x56da0b3f 
    SUBCLASS_OF_ID =0x2fb85921 

    def to_dict (self ):
        return {
        '_':'GetAutoDownloadSettingsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'?\x0b\xdaV',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetAutoSaveSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xadcbbcda 
    SUBCLASS_OF_ID =0x48cf2f02 

    def to_dict (self ):
        return {
        '_':'GetAutoSaveSettingsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xda\xbc\xcb\xad',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetChatThemesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd638de89 
    SUBCLASS_OF_ID =0x7fc52204 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetChatThemesRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x89\xde8\xd6',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetContactSignUpNotificationRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9f07c728 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'GetContactSignUpNotificationRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'(\xc7\x07\x9f',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetContentSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8b9b4dae 
    SUBCLASS_OF_ID =0xae3ff891 

    def to_dict (self ):
        return {
        '_':'GetContentSettingsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xaeM\x9b\x8b',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetDefaultBackgroundEmojisRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa60ab9ce 
    SUBCLASS_OF_ID =0xbcef6aba 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetDefaultBackgroundEmojisRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xce\xb9\n\xa6',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetDefaultEmojiStatusesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd6753386 
    SUBCLASS_OF_ID =0xd3e005ca 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetDefaultEmojiStatusesRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x863u\xd6',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetDefaultGroupPhotoEmojisRequest (TLRequest ):
    CONSTRUCTOR_ID =0x915860ae 
    SUBCLASS_OF_ID =0xbcef6aba 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetDefaultGroupPhotoEmojisRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xae`X\x91',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetDefaultProfilePhotoEmojisRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe2750328 
    SUBCLASS_OF_ID =0xbcef6aba 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetDefaultProfilePhotoEmojisRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'(\x03u\xe2',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetGlobalPrivacySettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xeb2b4cf6 
    SUBCLASS_OF_ID =0xc90e5770 

    def to_dict (self ):
        return {
        '_':'GetGlobalPrivacySettingsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf6L+\xeb',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetMultiWallPapersRequest (TLRequest ):
    CONSTRUCTOR_ID =0x65ad71dc 
    SUBCLASS_OF_ID =0x8ec35283 

    def __init__ (self ,wallpapers :List ['TypeInputWallPaper']):
        """"""
        self .wallpapers =wallpapers 

    def to_dict (self ):
        return {
        '_':'GetMultiWallPapersRequest',
        'wallpapers':[]if self .wallpapers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .wallpapers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdcq\xade',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .wallpapers )),b''.join (x ._bytes ()for x in self .wallpapers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _wallpapers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _wallpapers .append (_x )

        return cls (wallpapers =_wallpapers )

class GetNotifyExceptionsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x53577479 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,compare_sound :Optional [bool ]=None ,compare_stories :Optional [bool ]=None ,peer :Optional ['TypeInputNotifyPeer']=None ):
        """"""
        self .compare_sound =compare_sound 
        self .compare_stories =compare_stories 
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        if self .peer :
            self .peer =await client ._get_input_notify (self .peer )

    def to_dict (self ):
        return {
        '_':'GetNotifyExceptionsRequest',
        'compare_sound':self .compare_sound ,
        'compare_stories':self .compare_stories ,
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'ytWS',
        struct .pack ('<I',(0 if self .compare_sound is None or self .compare_sound is False else 2 )|(0 if self .compare_stories is None or self .compare_stories is False else 4 )|(0 if self .peer is None or self .peer is False else 1 )),
        b''if self .peer is None or self .peer is False else (self .peer ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _compare_sound =bool (flags &2 )
        _compare_stories =bool (flags &4 )
        if flags &1 :
            _peer =reader .tgread_object ()
        else :
            _peer =None 
        return cls (compare_sound =_compare_sound ,compare_stories =_compare_stories ,peer =_peer )

class GetNotifySettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x12b3ad31 
    SUBCLASS_OF_ID =0xcf20c074 

    def __init__ (self ,peer :'TypeInputNotifyPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =await client ._get_input_notify (self .peer )

    def to_dict (self ):
        return {
        '_':'GetNotifySettingsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'1\xad\xb3\x12',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class GetPasswordRequest (TLRequest ):
    CONSTRUCTOR_ID =0x548a30f5 
    SUBCLASS_OF_ID =0x53a211a3 

    def to_dict (self ):
        return {
        '_':'GetPasswordRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf50\x8aT',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetPasswordSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9cd4eaf9 
    SUBCLASS_OF_ID =0xd23fb078 

    def __init__ (self ,password :'TypeInputCheckPasswordSRP'):
        """"""
        self .password =password 

    def to_dict (self ):
        return {
        '_':'GetPasswordSettingsRequest',
        'password':self .password .to_dict ()if isinstance (self .password ,TLObject )else self .password 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9\xea\xd4\x9c',
        self .password ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _password =reader .tgread_object ()
        return cls (password =_password )

class GetPrivacyRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdadbc950 
    SUBCLASS_OF_ID =0xb55aba82 

    def __init__ (self ,key :'TypeInputPrivacyKey'):
        """"""
        self .key =key 

    def to_dict (self ):
        return {
        '_':'GetPrivacyRequest',
        'key':self .key .to_dict ()if isinstance (self .key ,TLObject )else self .key 
        }

    def _bytes (self ):
        return b''.join ((
        b'P\xc9\xdb\xda',
        self .key ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _key =reader .tgread_object ()
        return cls (key =_key )

class GetRecentEmojiStatusesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf578105 
    SUBCLASS_OF_ID =0xd3e005ca 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetRecentEmojiStatusesRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x05\x81W\x0f',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetSavedRingtonesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe1902288 
    SUBCLASS_OF_ID =0x27bcc95e 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetSavedRingtonesRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x88"\x90\xe1',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetSecureValueRequest (TLRequest ):
    CONSTRUCTOR_ID =0x73665bc2 
    SUBCLASS_OF_ID =0xe82e4121 

    def __init__ (self ,types :List ['TypeSecureValueType']):
        """"""
        self .types =types 

    def to_dict (self ):
        return {
        '_':'GetSecureValueRequest',
        'types':[]if self .types is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .types ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc2[fs',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .types )),b''.join (x ._bytes ()for x in self .types ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _types =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _types .append (_x )

        return cls (types =_types )

class GetThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3a5869ec 
    SUBCLASS_OF_ID =0x56b4c80c 

    def __init__ (self ,format :str ,theme :'TypeInputTheme'):
        """"""
        self .format =format 
        self .theme =theme 

    def to_dict (self ):
        return {
        '_':'GetThemeRequest',
        'format':self .format ,
        'theme':self .theme .to_dict ()if isinstance (self .theme ,TLObject )else self .theme 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeciX:',
        self .serialize_bytes (self .format ),
        self .theme ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _format =reader .tgread_string ()
        _theme =reader .tgread_object ()
        return cls (format =_format ,theme =_theme )

class GetThemesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7206e458 
    SUBCLASS_OF_ID =0x7fc52204 

    def __init__ (self ,format :str ,hash :int ):
        """"""
        self .format =format 
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetThemesRequest',
        'format':self .format ,
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'X\xe4\x06r',
        self .serialize_bytes (self .format ),
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _format =reader .tgread_string ()
        _hash =reader .read_long ()
        return cls (format =_format ,hash =_hash )

class GetTmpPasswordRequest (TLRequest ):
    CONSTRUCTOR_ID =0x449e0b51 
    SUBCLASS_OF_ID =0xb064992d 

    def __init__ (self ,password :'TypeInputCheckPasswordSRP',period :int ):
        """"""
        self .password =password 
        self .period =period 

    def to_dict (self ):
        return {
        '_':'GetTmpPasswordRequest',
        'password':self .password .to_dict ()if isinstance (self .password ,TLObject )else self .password ,
        'period':self .period 
        }

    def _bytes (self ):
        return b''.join ((
        b'Q\x0b\x9eD',
        self .password ._bytes (),
        struct .pack ('<i',self .period ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _password =reader .tgread_object ()
        _period =reader .read_int ()
        return cls (password =_password ,period =_period )

class GetWallPaperRequest (TLRequest ):
    CONSTRUCTOR_ID =0xfc8ddbea 
    SUBCLASS_OF_ID =0x96a2c98b 

    def __init__ (self ,wallpaper :'TypeInputWallPaper'):
        """"""
        self .wallpaper =wallpaper 

    def to_dict (self ):
        return {
        '_':'GetWallPaperRequest',
        'wallpaper':self .wallpaper .to_dict ()if isinstance (self .wallpaper ,TLObject )else self .wallpaper 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xea\xdb\x8d\xfc',
        self .wallpaper ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _wallpaper =reader .tgread_object ()
        return cls (wallpaper =_wallpaper )

class GetWallPapersRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7967d36 
    SUBCLASS_OF_ID =0xa2c548fd 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetWallPapersRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'6}\x96\x07',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetWebAuthorizationsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x182e6d6f 
    SUBCLASS_OF_ID =0x9a365b32 

    def to_dict (self ):
        return {
        '_':'GetWebAuthorizationsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'om.\x18',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class InitTakeoutSessionRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8ef3eab0 
    SUBCLASS_OF_ID =0x843ebe85 

    def __init__ (self ,contacts :Optional [bool ]=None ,message_users :Optional [bool ]=None ,message_chats :Optional [bool ]=None ,message_megagroups :Optional [bool ]=None ,message_channels :Optional [bool ]=None ,files :Optional [bool ]=None ,file_max_size :Optional [int ]=None ):
        """"""
        self .contacts =contacts 
        self .message_users =message_users 
        self .message_chats =message_chats 
        self .message_megagroups =message_megagroups 
        self .message_channels =message_channels 
        self .files =files 
        self .file_max_size =file_max_size 

    def to_dict (self ):
        return {
        '_':'InitTakeoutSessionRequest',
        'contacts':self .contacts ,
        'message_users':self .message_users ,
        'message_chats':self .message_chats ,
        'message_megagroups':self .message_megagroups ,
        'message_channels':self .message_channels ,
        'files':self .files ,
        'file_max_size':self .file_max_size 
        }

    def _bytes (self ):
        assert ((self .files or self .files is not None )and (self .file_max_size or self .file_max_size is not None ))or ((self .files is None or self .files is False )and (self .file_max_size is None or self .file_max_size is False )),'files, file_max_size parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'\xb0\xea\xf3\x8e',
        struct .pack ('<I',(0 if self .contacts is None or self .contacts is False else 1 )|(0 if self .message_users is None or self .message_users is False else 2 )|(0 if self .message_chats is None or self .message_chats is False else 4 )|(0 if self .message_megagroups is None or self .message_megagroups is False else 8 )|(0 if self .message_channels is None or self .message_channels is False else 16 )|(0 if self .files is None or self .files is False else 32 )|(0 if self .file_max_size is None or self .file_max_size is False else 32 )),
        b''if self .file_max_size is None or self .file_max_size is False else (struct .pack ('<q',self .file_max_size )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _contacts =bool (flags &1 )
        _message_users =bool (flags &2 )
        _message_chats =bool (flags &4 )
        _message_megagroups =bool (flags &8 )
        _message_channels =bool (flags &16 )
        _files =bool (flags &32 )
        if flags &32 :
            _file_max_size =reader .read_long ()
        else :
            _file_max_size =None 
        return cls (contacts =_contacts ,message_users =_message_users ,message_chats =_message_chats ,message_megagroups =_message_megagroups ,message_channels =_message_channels ,files =_files ,file_max_size =_file_max_size )

class InstallThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc727bb3b 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,dark :Optional [bool ]=None ,theme :Optional ['TypeInputTheme']=None ,format :Optional [str ]=None ,base_theme :Optional ['TypeBaseTheme']=None ):
        """"""
        self .dark =dark 
        self .theme =theme 
        self .format =format 
        self .base_theme =base_theme 

    def to_dict (self ):
        return {
        '_':'InstallThemeRequest',
        'dark':self .dark ,
        'theme':self .theme .to_dict ()if isinstance (self .theme ,TLObject )else self .theme ,
        'format':self .format ,
        'base_theme':self .base_theme .to_dict ()if isinstance (self .base_theme ,TLObject )else self .base_theme 
        }

    def _bytes (self ):
        return b''.join ((
        b";\xbb'\xc7",
        struct .pack ('<I',(0 if self .dark is None or self .dark is False else 1 )|(0 if self .theme is None or self .theme is False else 2 )|(0 if self .format is None or self .format is False else 4 )|(0 if self .base_theme is None or self .base_theme is False else 8 )),
        b''if self .theme is None or self .theme is False else (self .theme ._bytes ()),
        b''if self .format is None or self .format is False else (self .serialize_bytes (self .format )),
        b''if self .base_theme is None or self .base_theme is False else (self .base_theme ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _dark =bool (flags &1 )
        if flags &2 :
            _theme =reader .tgread_object ()
        else :
            _theme =None 
        if flags &4 :
            _format =reader .tgread_string ()
        else :
            _format =None 
        if flags &8 :
            _base_theme =reader .tgread_object ()
        else :
            _base_theme =None 
        return cls (dark =_dark ,theme =_theme ,format =_format ,base_theme =_base_theme )

class InstallWallPaperRequest (TLRequest ):
    CONSTRUCTOR_ID =0xfeed5769 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,wallpaper :'TypeInputWallPaper',settings :'TypeWallPaperSettings'):
        """"""
        self .wallpaper =wallpaper 
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'InstallWallPaperRequest',
        'wallpaper':self .wallpaper .to_dict ()if isinstance (self .wallpaper ,TLObject )else self .wallpaper ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'iW\xed\xfe',
        self .wallpaper ._bytes (),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _wallpaper =reader .tgread_object ()
        _settings =reader .tgread_object ()
        return cls (wallpaper =_wallpaper ,settings =_settings )

class InvalidateSignInCodesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xca8ae8ba 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,codes :List [str ]):
        """"""
        self .codes =codes 

    def to_dict (self ):
        return {
        '_':'InvalidateSignInCodesRequest',
        'codes':[]if self .codes is None else self .codes [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xba\xe8\x8a\xca',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .codes )),b''.join (self .serialize_bytes (x )for x in self .codes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _codes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _codes .append (_x )

        return cls (codes =_codes )

class RegisterDeviceRequest (TLRequest ):
    CONSTRUCTOR_ID =0xec86017a 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,token_type :int ,token :str ,app_sandbox :bool ,secret :bytes ,other_uids :List [int ],no_muted :Optional [bool ]=None ):
        """"""
        self .token_type =token_type 
        self .token =token 
        self .app_sandbox =app_sandbox 
        self .secret =secret 
        self .other_uids =other_uids 
        self .no_muted =no_muted 

    def to_dict (self ):
        return {
        '_':'RegisterDeviceRequest',
        'token_type':self .token_type ,
        'token':self .token ,
        'app_sandbox':self .app_sandbox ,
        'secret':self .secret ,
        'other_uids':[]if self .other_uids is None else self .other_uids [:],
        'no_muted':self .no_muted 
        }

    def _bytes (self ):
        return b''.join ((
        b'z\x01\x86\xec',
        struct .pack ('<I',(0 if self .no_muted is None or self .no_muted is False else 1 )),
        struct .pack ('<i',self .token_type ),
        self .serialize_bytes (self .token ),
        b'\xb5ur\x99'if self .app_sandbox else b'7\x97y\xbc',
        self .serialize_bytes (self .secret ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .other_uids )),b''.join (struct .pack ('<q',x )for x in self .other_uids ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _no_muted =bool (flags &1 )
        _token_type =reader .read_int ()
        _token =reader .tgread_string ()
        _app_sandbox =reader .tgread_bool ()
        _secret =reader .tgread_bytes ()
        reader .read_int ()
        _other_uids =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_long ()
            _other_uids .append (_x )

        return cls (token_type =_token_type ,token =_token ,app_sandbox =_app_sandbox ,secret =_secret ,other_uids =_other_uids ,no_muted =_no_muted )

class ReorderUsernamesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xef500eab 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,order :List [str ]):
        """"""
        self .order =order 

    def to_dict (self ):
        return {
        '_':'ReorderUsernamesRequest',
        'order':[]if self .order is None else self .order [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xab\x0eP\xef',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .order )),b''.join (self .serialize_bytes (x )for x in self .order ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _order =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _order .append (_x )

        return cls (order =_order )

class ReportPeerRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc5ba3d86 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',reason :'TypeReportReason',message :str ):
        """"""
        self .peer =peer 
        self .reason =reason 
        self .message =message 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ReportPeerRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'reason':self .reason .to_dict ()if isinstance (self .reason ,TLObject )else self .reason ,
        'message':self .message 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x86=\xba\xc5',
        self .peer ._bytes (),
        self .reason ._bytes (),
        self .serialize_bytes (self .message ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _reason =reader .tgread_object ()
        _message =reader .tgread_string ()
        return cls (peer =_peer ,reason =_reason ,message =_message )

class ReportProfilePhotoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xfa8cc6f5 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',photo_id :'TypeInputPhoto',reason :'TypeReportReason',message :str ):
        """"""
        self .peer =peer 
        self .photo_id =photo_id 
        self .reason =reason 
        self .message =message 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))
        self .photo_id =utils .get_input_photo (self .photo_id )

    def to_dict (self ):
        return {
        '_':'ReportProfilePhotoRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'photo_id':self .photo_id .to_dict ()if isinstance (self .photo_id ,TLObject )else self .photo_id ,
        'reason':self .reason .to_dict ()if isinstance (self .reason ,TLObject )else self .reason ,
        'message':self .message 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf5\xc6\x8c\xfa',
        self .peer ._bytes (),
        self .photo_id ._bytes (),
        self .reason ._bytes (),
        self .serialize_bytes (self .message ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _photo_id =reader .tgread_object ()
        _reason =reader .tgread_object ()
        _message =reader .tgread_string ()
        return cls (peer =_peer ,photo_id =_photo_id ,reason =_reason ,message =_message )

class ResendPasswordEmailRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7a7f2a15 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ResendPasswordEmailRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x15*\x7fz',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetAuthorizationRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdf77f3bc 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'ResetAuthorizationRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbc\xf3w\xdf',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class ResetNotifySettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdb7e1747 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ResetNotifySettingsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'G\x17~\xdb',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetPasswordRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9308ce1b 
    SUBCLASS_OF_ID =0x49507416 

    def to_dict (self ):
        return {
        '_':'ResetPasswordRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1b\xce\x08\x93',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetWallPapersRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbb3b9804 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ResetWallPapersRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x04\x98;\xbb',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetWebAuthorizationRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2d01b9ef 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'ResetWebAuthorizationRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xef\xb9\x01-',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class ResetWebAuthorizationsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x682d2594 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ResetWebAuthorizationsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x94%-h',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SaveAutoDownloadSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x76f36233 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,settings :'TypeAutoDownloadSettings',low :Optional [bool ]=None ,high :Optional [bool ]=None ):
        """"""
        self .settings =settings 
        self .low =low 
        self .high =high 

    def to_dict (self ):
        return {
        '_':'SaveAutoDownloadSettingsRequest',
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings ,
        'low':self .low ,
        'high':self .high 
        }

    def _bytes (self ):
        return b''.join ((
        b'3b\xf3v',
        struct .pack ('<I',(0 if self .low is None or self .low is False else 1 )|(0 if self .high is None or self .high is False else 2 )),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _low =bool (flags &1 )
        _high =bool (flags &2 )
        _settings =reader .tgread_object ()
        return cls (settings =_settings ,low =_low ,high =_high )

class SaveAutoSaveSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd69b8361 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,settings :'TypeAutoSaveSettings',users :Optional [bool ]=None ,chats :Optional [bool ]=None ,broadcasts :Optional [bool ]=None ,peer :Optional ['TypeInputPeer']=None ):
        """"""
        self .settings =settings 
        self .users =users 
        self .chats =chats 
        self .broadcasts =broadcasts 
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        if self .peer :
            self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'SaveAutoSaveSettingsRequest',
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings ,
        'users':self .users ,
        'chats':self .chats ,
        'broadcasts':self .broadcasts ,
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'a\x83\x9b\xd6',
        struct .pack ('<I',(0 if self .users is None or self .users is False else 1 )|(0 if self .chats is None or self .chats is False else 2 )|(0 if self .broadcasts is None or self .broadcasts is False else 4 )|(0 if self .peer is None or self .peer is False else 8 )),
        b''if self .peer is None or self .peer is False else (self .peer ._bytes ()),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _users =bool (flags &1 )
        _chats =bool (flags &2 )
        _broadcasts =bool (flags &4 )
        if flags &8 :
            _peer =reader .tgread_object ()
        else :
            _peer =None 
        _settings =reader .tgread_object ()
        return cls (settings =_settings ,users =_users ,chats =_chats ,broadcasts =_broadcasts ,peer =_peer )

class SaveRingtoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3dea5b03 
    SUBCLASS_OF_ID =0xb1e28424 

    def __init__ (self ,id :'TypeInputDocument',unsave :bool ):
        """"""
        self .id =id 
        self .unsave =unsave 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_document (self .id )

    def to_dict (self ):
        return {
        '_':'SaveRingtoneRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'unsave':self .unsave 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x03[\xea=',
        self .id ._bytes (),
        b'\xb5ur\x99'if self .unsave else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _id =reader .tgread_object ()
        _unsave =reader .tgread_bool ()
        return cls (id =_id ,unsave =_unsave )

class SaveSecureValueRequest (TLRequest ):
    CONSTRUCTOR_ID =0x899fe31d 
    SUBCLASS_OF_ID =0x51138ae 

    def __init__ (self ,value :'TypeInputSecureValue',secure_secret_id :int ):
        """"""
        self .value =value 
        self .secure_secret_id =secure_secret_id 

    def to_dict (self ):
        return {
        '_':'SaveSecureValueRequest',
        'value':self .value .to_dict ()if isinstance (self .value ,TLObject )else self .value ,
        'secure_secret_id':self .secure_secret_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1d\xe3\x9f\x89',
        self .value ._bytes (),
        struct .pack ('<q',self .secure_secret_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _value =reader .tgread_object ()
        _secure_secret_id =reader .read_long ()
        return cls (value =_value ,secure_secret_id =_secure_secret_id )

class SaveThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf257106c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,theme :'TypeInputTheme',unsave :bool ):
        """"""
        self .theme =theme 
        self .unsave =unsave 

    def to_dict (self ):
        return {
        '_':'SaveThemeRequest',
        'theme':self .theme .to_dict ()if isinstance (self .theme ,TLObject )else self .theme ,
        'unsave':self .unsave 
        }

    def _bytes (self ):
        return b''.join ((
        b'l\x10W\xf2',
        self .theme ._bytes (),
        b'\xb5ur\x99'if self .unsave else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _theme =reader .tgread_object ()
        _unsave =reader .tgread_bool ()
        return cls (theme =_theme ,unsave =_unsave )

class SaveWallPaperRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6c5a5b37 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,wallpaper :'TypeInputWallPaper',unsave :bool ,settings :'TypeWallPaperSettings'):
        """"""
        self .wallpaper =wallpaper 
        self .unsave =unsave 
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'SaveWallPaperRequest',
        'wallpaper':self .wallpaper .to_dict ()if isinstance (self .wallpaper ,TLObject )else self .wallpaper ,
        'unsave':self .unsave ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'7[Zl',
        self .wallpaper ._bytes (),
        b'\xb5ur\x99'if self .unsave else b'7\x97y\xbc',
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _wallpaper =reader .tgread_object ()
        _unsave =reader .tgread_bool ()
        _settings =reader .tgread_object ()
        return cls (wallpaper =_wallpaper ,unsave =_unsave ,settings =_settings )

class SendChangePhoneCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x82574ae5 
    SUBCLASS_OF_ID =0x6ce87081 

    def __init__ (self ,phone_number :str ,settings :'TypeCodeSettings'):
        """"""
        self .phone_number =phone_number 
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'SendChangePhoneCodeRequest',
        'phone_number':self .phone_number ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe5JW\x82',
        self .serialize_bytes (self .phone_number ),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_number =reader .tgread_string ()
        _settings =reader .tgread_object ()
        return cls (phone_number =_phone_number ,settings =_settings )

class SendConfirmPhoneCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1b3faa88 
    SUBCLASS_OF_ID =0x6ce87081 

    def __init__ (self ,hash :str ,settings :'TypeCodeSettings'):
        """"""
        self .hash =hash 
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'SendConfirmPhoneCodeRequest',
        'hash':self .hash ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x88\xaa?\x1b',
        self .serialize_bytes (self .hash ),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .tgread_string ()
        _settings =reader .tgread_object ()
        return cls (hash =_hash ,settings =_settings )

class SendVerifyEmailCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x98e037bb 
    SUBCLASS_OF_ID =0x69f3c06e 

    def __init__ (self ,purpose :'TypeEmailVerifyPurpose',email :str ):
        """"""
        self .purpose =purpose 
        self .email =email 

    def to_dict (self ):
        return {
        '_':'SendVerifyEmailCodeRequest',
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose ,
        'email':self .email 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbb7\xe0\x98',
        self .purpose ._bytes (),
        self .serialize_bytes (self .email ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _purpose =reader .tgread_object ()
        _email =reader .tgread_string ()
        return cls (purpose =_purpose ,email =_email )

class SendVerifyPhoneCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa5a356f9 
    SUBCLASS_OF_ID =0x6ce87081 

    def __init__ (self ,phone_number :str ,settings :'TypeCodeSettings'):
        """"""
        self .phone_number =phone_number 
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'SendVerifyPhoneCodeRequest',
        'phone_number':self .phone_number ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9V\xa3\xa5',
        self .serialize_bytes (self .phone_number ),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_number =reader .tgread_string ()
        _settings =reader .tgread_object ()
        return cls (phone_number =_phone_number ,settings =_settings )

class SetAccountTTLRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2442485e 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,ttl :'TypeAccountDaysTTL'):
        """"""
        self .ttl =ttl 

    def to_dict (self ):
        return {
        '_':'SetAccountTTLRequest',
        'ttl':self .ttl .to_dict ()if isinstance (self .ttl ,TLObject )else self .ttl 
        }

    def _bytes (self ):
        return b''.join ((
        b'^HB$',
        self .ttl ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _ttl =reader .tgread_object ()
        return cls (ttl =_ttl )

class SetAuthorizationTTLRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbf899aa0 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,authorization_ttl_days :int ):
        """"""
        self .authorization_ttl_days =authorization_ttl_days 

    def to_dict (self ):
        return {
        '_':'SetAuthorizationTTLRequest',
        'authorization_ttl_days':self .authorization_ttl_days 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0\x9a\x89\xbf',
        struct .pack ('<i',self .authorization_ttl_days ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _authorization_ttl_days =reader .read_int ()
        return cls (authorization_ttl_days =_authorization_ttl_days )

class SetContactSignUpNotificationRequest (TLRequest ):
    CONSTRUCTOR_ID =0xcff43f61 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,silent :bool ):
        """"""
        self .silent =silent 

    def to_dict (self ):
        return {
        '_':'SetContactSignUpNotificationRequest',
        'silent':self .silent 
        }

    def _bytes (self ):
        return b''.join ((
        b'a?\xf4\xcf',
        b'\xb5ur\x99'if self .silent else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _silent =reader .tgread_bool ()
        return cls (silent =_silent )

class SetContentSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb574b16b 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,sensitive_enabled :Optional [bool ]=None ):
        """"""
        self .sensitive_enabled =sensitive_enabled 

    def to_dict (self ):
        return {
        '_':'SetContentSettingsRequest',
        'sensitive_enabled':self .sensitive_enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'k\xb1t\xb5',
        struct .pack ('<I',(0 if self .sensitive_enabled is None or self .sensitive_enabled is False else 1 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _sensitive_enabled =bool (flags &1 )
        return cls (sensitive_enabled =_sensitive_enabled )

class SetGlobalPrivacySettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1edaaac2 
    SUBCLASS_OF_ID =0xc90e5770 

    def __init__ (self ,settings :'TypeGlobalPrivacySettings'):
        """"""
        self .settings =settings 

    def to_dict (self ):
        return {
        '_':'SetGlobalPrivacySettingsRequest',
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc2\xaa\xda\x1e',
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _settings =reader .tgread_object ()
        return cls (settings =_settings )

class SetPrivacyRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc9f81ce8 
    SUBCLASS_OF_ID =0xb55aba82 

    def __init__ (self ,key :'TypeInputPrivacyKey',rules :List ['TypeInputPrivacyRule']):
        """"""
        self .key =key 
        self .rules =rules 

    def to_dict (self ):
        return {
        '_':'SetPrivacyRequest',
        'key':self .key .to_dict ()if isinstance (self .key ,TLObject )else self .key ,
        'rules':[]if self .rules is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .rules ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe8\x1c\xf8\xc9',
        self .key ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .rules )),b''.join (x ._bytes ()for x in self .rules ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _key =reader .tgread_object ()
        reader .read_int ()
        _rules =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _rules .append (_x )

        return cls (key =_key ,rules =_rules )

class ToggleUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x58d6b376 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,username :str ,active :bool ):
        """"""
        self .username =username 
        self .active =active 

    def to_dict (self ):
        return {
        '_':'ToggleUsernameRequest',
        'username':self .username ,
        'active':self .active 
        }

    def _bytes (self ):
        return b''.join ((
        b'v\xb3\xd6X',
        self .serialize_bytes (self .username ),
        b'\xb5ur\x99'if self .active else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _username =reader .tgread_string ()
        _active =reader .tgread_bool ()
        return cls (username =_username ,active =_active )

class UnregisterDeviceRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6a0d3206 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,token_type :int ,token :str ,other_uids :List [int ]):
        """"""
        self .token_type =token_type 
        self .token =token 
        self .other_uids =other_uids 

    def to_dict (self ):
        return {
        '_':'UnregisterDeviceRequest',
        'token_type':self .token_type ,
        'token':self .token ,
        'other_uids':[]if self .other_uids is None else self .other_uids [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x062\rj',
        struct .pack ('<i',self .token_type ),
        self .serialize_bytes (self .token ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .other_uids )),b''.join (struct .pack ('<q',x )for x in self .other_uids ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _token_type =reader .read_int ()
        _token =reader .tgread_string ()
        reader .read_int ()
        _other_uids =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_long ()
            _other_uids .append (_x )

        return cls (token_type =_token_type ,token =_token ,other_uids =_other_uids )

class UpdateColorRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa001cc43 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,color :int ,background_emoji_id :Optional [int ]=None ):
        """"""
        self .color =color 
        self .background_emoji_id =background_emoji_id 

    def to_dict (self ):
        return {
        '_':'UpdateColorRequest',
        'color':self .color ,
        'background_emoji_id':self .background_emoji_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'C\xcc\x01\xa0',
        struct .pack ('<I',(0 if self .background_emoji_id is None or self .background_emoji_id is False else 1 )),
        struct .pack ('<i',self .color ),
        b''if self .background_emoji_id is None or self .background_emoji_id is False else (struct .pack ('<q',self .background_emoji_id )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _color =reader .read_int ()
        if flags &1 :
            _background_emoji_id =reader .read_long ()
        else :
            _background_emoji_id =None 
        return cls (color =_color ,background_emoji_id =_background_emoji_id )

class UpdateDeviceLockedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x38df3532 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,period :int ):
        """"""
        self .period =period 

    def to_dict (self ):
        return {
        '_':'UpdateDeviceLockedRequest',
        'period':self .period 
        }

    def _bytes (self ):
        return b''.join ((
        b'25\xdf8',
        struct .pack ('<i',self .period ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _period =reader .read_int ()
        return cls (period =_period )

class UpdateEmojiStatusRequest (TLRequest ):
    CONSTRUCTOR_ID =0xfbd3de6b 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,emoji_status :'TypeEmojiStatus'):
        """"""
        self .emoji_status =emoji_status 

    def to_dict (self ):
        return {
        '_':'UpdateEmojiStatusRequest',
        'emoji_status':self .emoji_status .to_dict ()if isinstance (self .emoji_status ,TLObject )else self .emoji_status 
        }

    def _bytes (self ):
        return b''.join ((
        b'k\xde\xd3\xfb',
        self .emoji_status ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _emoji_status =reader .tgread_object ()
        return cls (emoji_status =_emoji_status )

class UpdateNotifySettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x84be5b93 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputNotifyPeer',settings :'TypeInputPeerNotifySettings'):
        """"""
        self .peer =peer 
        self .settings =settings 

    async def resolve (self ,client ,utils ):
        self .peer =await client ._get_input_notify (self .peer )

    def to_dict (self ):
        return {
        '_':'UpdateNotifySettingsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x93[\xbe\x84',
        self .peer ._bytes (),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _settings =reader .tgread_object ()
        return cls (peer =_peer ,settings =_settings )

class UpdatePasswordSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa59b102f 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,password :'TypeInputCheckPasswordSRP',new_settings :'TypePasswordInputSettings'):
        """"""
        self .password =password 
        self .new_settings =new_settings 

    def to_dict (self ):
        return {
        '_':'UpdatePasswordSettingsRequest',
        'password':self .password .to_dict ()if isinstance (self .password ,TLObject )else self .password ,
        'new_settings':self .new_settings .to_dict ()if isinstance (self .new_settings ,TLObject )else self .new_settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'/\x10\x9b\xa5',
        self .password ._bytes (),
        self .new_settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _password =reader .tgread_object ()
        _new_settings =reader .tgread_object ()
        return cls (password =_password ,new_settings =_new_settings )

class UpdateProfileRequest (TLRequest ):
    CONSTRUCTOR_ID =0x78515775 
    SUBCLASS_OF_ID =0x2da17977 

    def __init__ (self ,first_name :Optional [str ]=None ,last_name :Optional [str ]=None ,about :Optional [str ]=None ):
        """"""
        self .first_name =first_name 
        self .last_name =last_name 
        self .about =about 

    def to_dict (self ):
        return {
        '_':'UpdateProfileRequest',
        'first_name':self .first_name ,
        'last_name':self .last_name ,
        'about':self .about 
        }

    def _bytes (self ):
        return b''.join ((
        b'uWQx',
        struct .pack ('<I',(0 if self .first_name is None or self .first_name is False else 1 )|(0 if self .last_name is None or self .last_name is False else 2 )|(0 if self .about is None or self .about is False else 4 )),
        b''if self .first_name is None or self .first_name is False else (self .serialize_bytes (self .first_name )),
        b''if self .last_name is None or self .last_name is False else (self .serialize_bytes (self .last_name )),
        b''if self .about is None or self .about is False else (self .serialize_bytes (self .about )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _first_name =reader .tgread_string ()
        else :
            _first_name =None 
        if flags &2 :
            _last_name =reader .tgread_string ()
        else :
            _last_name =None 
        if flags &4 :
            _about =reader .tgread_string ()
        else :
            _about =None 
        return cls (first_name =_first_name ,last_name =_last_name ,about =_about )

class UpdateStatusRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6628562c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,offline :bool ):
        """"""
        self .offline =offline 

    def to_dict (self ):
        return {
        '_':'UpdateStatusRequest',
        'offline':self .offline 
        }

    def _bytes (self ):
        return b''.join ((
        b',V(f',
        b'\xb5ur\x99'if self .offline else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _offline =reader .tgread_bool ()
        return cls (offline =_offline )

class UpdateThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2bf40ccc 
    SUBCLASS_OF_ID =0x56b4c80c 

    def __init__ (self ,format :str ,theme :'TypeInputTheme',slug :Optional [str ]=None ,title :Optional [str ]=None ,document :Optional ['TypeInputDocument']=None ,settings :Optional [List ['TypeInputThemeSettings']]=None ):
        """"""
        self .format =format 
        self .theme =theme 
        self .slug =slug 
        self .title =title 
        self .document =document 
        self .settings =settings 

    async def resolve (self ,client ,utils ):
        if self .document :
            self .document =utils .get_input_document (self .document )

    def to_dict (self ):
        return {
        '_':'UpdateThemeRequest',
        'format':self .format ,
        'theme':self .theme .to_dict ()if isinstance (self .theme ,TLObject )else self .theme ,
        'slug':self .slug ,
        'title':self .title ,
        'document':self .document .to_dict ()if isinstance (self .document ,TLObject )else self .document ,
        'settings':[]if self .settings is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .settings ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcc\x0c\xf4+',
        struct .pack ('<I',(0 if self .slug is None or self .slug is False else 1 )|(0 if self .title is None or self .title is False else 2 )|(0 if self .document is None or self .document is False else 4 )|(0 if self .settings is None or self .settings is False else 8 )),
        self .serialize_bytes (self .format ),
        self .theme ._bytes (),
        b''if self .slug is None or self .slug is False else (self .serialize_bytes (self .slug )),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        b''if self .document is None or self .document is False else (self .document ._bytes ()),
        b''if self .settings is None or self .settings is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .settings )),b''.join (x ._bytes ()for x in self .settings ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _format =reader .tgread_string ()
        _theme =reader .tgread_object ()
        if flags &1 :
            _slug =reader .tgread_string ()
        else :
            _slug =None 
        if flags &2 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        if flags &4 :
            _document =reader .tgread_object ()
        else :
            _document =None 
        if flags &8 :
            reader .read_int ()
            _settings =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _settings .append (_x )

        else :
            _settings =None 
        return cls (format =_format ,theme =_theme ,slug =_slug ,title =_title ,document =_document ,settings =_settings )

class UpdateUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3e0bdd7c 
    SUBCLASS_OF_ID =0x2da17977 

    def __init__ (self ,username :str ):
        """"""
        self .username =username 

    def to_dict (self ):
        return {
        '_':'UpdateUsernameRequest',
        'username':self .username 
        }

    def _bytes (self ):
        return b''.join ((
        b'|\xdd\x0b>',
        self .serialize_bytes (self .username ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _username =reader .tgread_string ()
        return cls (username =_username )

class UploadRingtoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x831a83a2 
    SUBCLASS_OF_ID =0x211fe820 

    def __init__ (self ,file :'TypeInputFile',file_name :str ,mime_type :str ):
        """"""
        self .file =file 
        self .file_name =file_name 
        self .mime_type =mime_type 

    def to_dict (self ):
        return {
        '_':'UploadRingtoneRequest',
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file ,
        'file_name':self .file_name ,
        'mime_type':self .mime_type 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa2\x83\x1a\x83',
        self .file ._bytes (),
        self .serialize_bytes (self .file_name ),
        self .serialize_bytes (self .mime_type ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _file =reader .tgread_object ()
        _file_name =reader .tgread_string ()
        _mime_type =reader .tgread_string ()
        return cls (file =_file ,file_name =_file_name ,mime_type =_mime_type )

class UploadThemeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1c3db333 
    SUBCLASS_OF_ID =0x211fe820 

    def __init__ (self ,file :'TypeInputFile',file_name :str ,mime_type :str ,thumb :Optional ['TypeInputFile']=None ):
        """"""
        self .file =file 
        self .file_name =file_name 
        self .mime_type =mime_type 
        self .thumb =thumb 

    def to_dict (self ):
        return {
        '_':'UploadThemeRequest',
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file ,
        'file_name':self .file_name ,
        'mime_type':self .mime_type ,
        'thumb':self .thumb .to_dict ()if isinstance (self .thumb ,TLObject )else self .thumb 
        }

    def _bytes (self ):
        return b''.join ((
        b'3\xb3=\x1c',
        struct .pack ('<I',(0 if self .thumb is None or self .thumb is False else 1 )),
        self .file ._bytes (),
        b''if self .thumb is None or self .thumb is False else (self .thumb ._bytes ()),
        self .serialize_bytes (self .file_name ),
        self .serialize_bytes (self .mime_type ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _file =reader .tgread_object ()
        if flags &1 :
            _thumb =reader .tgread_object ()
        else :
            _thumb =None 
        _file_name =reader .tgread_string ()
        _mime_type =reader .tgread_string ()
        return cls (file =_file ,file_name =_file_name ,mime_type =_mime_type ,thumb =_thumb )

class UploadWallPaperRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe39a8f03 
    SUBCLASS_OF_ID =0x96a2c98b 

    def __init__ (self ,file :'TypeInputFile',mime_type :str ,settings :'TypeWallPaperSettings',for_chat :Optional [bool ]=None ):
        """"""
        self .file =file 
        self .mime_type =mime_type 
        self .settings =settings 
        self .for_chat =for_chat 

    def to_dict (self ):
        return {
        '_':'UploadWallPaperRequest',
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file ,
        'mime_type':self .mime_type ,
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings ,
        'for_chat':self .for_chat 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x03\x8f\x9a\xe3',
        struct .pack ('<I',(0 if self .for_chat is None or self .for_chat is False else 1 )),
        self .file ._bytes (),
        self .serialize_bytes (self .mime_type ),
        self .settings ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _for_chat =bool (flags &1 )
        _file =reader .tgread_object ()
        _mime_type =reader .tgread_string ()
        _settings =reader .tgread_object ()
        return cls (file =_file ,mime_type =_mime_type ,settings =_settings ,for_chat =_for_chat )

class VerifyEmailRequest (TLRequest ):
    CONSTRUCTOR_ID =0x32da4cf 
    SUBCLASS_OF_ID =0x64833188 

    def __init__ (self ,purpose :'TypeEmailVerifyPurpose',verification :'TypeEmailVerification'):
        """"""
        self .purpose =purpose 
        self .verification =verification 

    def to_dict (self ):
        return {
        '_':'VerifyEmailRequest',
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose ,
        'verification':self .verification .to_dict ()if isinstance (self .verification ,TLObject )else self .verification 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcf\xa4-\x03',
        self .purpose ._bytes (),
        self .verification ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _purpose =reader .tgread_object ()
        _verification =reader .tgread_object ()
        return cls (purpose =_purpose ,verification =_verification )

class VerifyPhoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4dd3a7f6 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,phone_number :str ,phone_code_hash :str ,phone_code :str ):
        """"""
        self .phone_number =phone_number 
        self .phone_code_hash =phone_code_hash 
        self .phone_code =phone_code 

    def to_dict (self ):
        return {
        '_':'VerifyPhoneRequest',
        'phone_number':self .phone_number ,
        'phone_code_hash':self .phone_code_hash ,
        'phone_code':self .phone_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf6\xa7\xd3M',
        self .serialize_bytes (self .phone_number ),
        self .serialize_bytes (self .phone_code_hash ),
        self .serialize_bytes (self .phone_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone_number =reader .tgread_string ()
        _phone_code_hash =reader .tgread_string ()
        _phone_code =reader .tgread_string ()
        return cls (phone_number =_phone_number ,phone_code_hash =_phone_code_hash ,phone_code =_phone_code )

