""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeAuthorization ,TypeAutoDownloadSettings ,TypeAutoSaveException ,TypeAutoSaveSettings ,TypeChat ,TypeDocument ,TypeEmojiStatus ,TypePasswordKdfAlgo ,TypePrivacyRule ,TypeSecurePasswordKdfAlgo ,TypeSecureRequiredType ,TypeSecureSecretSettings ,TypeSecureValue ,TypeSecureValueError ,TypeTheme ,TypeUser ,TypeWallPaper ,TypeWebAuthorization 
    from ...tl .types .auth import TypeSentCode 

class AuthorizationForm (TLObject ):
    CONSTRUCTOR_ID =0xad2e1cd8 
    SUBCLASS_OF_ID =0x78049a94 

    def __init__ (self ,required_types :List ['TypeSecureRequiredType'],values :List ['TypeSecureValue'],errors :List ['TypeSecureValueError'],users :List ['TypeUser'],privacy_policy_url :Optional [str ]=None ):
        """"""
        self .required_types =required_types 
        self .values =values 
        self .errors =errors 
        self .users =users 
        self .privacy_policy_url =privacy_policy_url 

    def to_dict (self ):
        return {
        '_':'AuthorizationForm',
        'required_types':[]if self .required_types is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .required_types ],
        'values':[]if self .values is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .values ],
        'errors':[]if self .errors is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .errors ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'privacy_policy_url':self .privacy_policy_url 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd8\x1c.\xad',
        struct .pack ('<I',(0 if self .privacy_policy_url is None or self .privacy_policy_url is False else 1 )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .required_types )),b''.join (x ._bytes ()for x in self .required_types ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .values )),b''.join (x ._bytes ()for x in self .values ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .errors )),b''.join (x ._bytes ()for x in self .errors ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        b''if self .privacy_policy_url is None or self .privacy_policy_url is False else (self .serialize_bytes (self .privacy_policy_url )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        reader .read_int ()
        _required_types =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _required_types .append (_x )

        reader .read_int ()
        _values =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _values .append (_x )

        reader .read_int ()
        _errors =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _errors .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        if flags &1 :
            _privacy_policy_url =reader .tgread_string ()
        else :
            _privacy_policy_url =None 
        return cls (required_types =_required_types ,values =_values ,errors =_errors ,users =_users ,privacy_policy_url =_privacy_policy_url )

class Authorizations (TLObject ):
    CONSTRUCTOR_ID =0x4bff8ea0 
    SUBCLASS_OF_ID =0xbf5e0ff 

    def __init__ (self ,authorization_ttl_days :int ,authorizations :List ['TypeAuthorization']):
        """"""
        self .authorization_ttl_days =authorization_ttl_days 
        self .authorizations =authorizations 

    def to_dict (self ):
        return {
        '_':'Authorizations',
        'authorization_ttl_days':self .authorization_ttl_days ,
        'authorizations':[]if self .authorizations is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .authorizations ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0\x8e\xffK',
        struct .pack ('<i',self .authorization_ttl_days ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .authorizations )),b''.join (x ._bytes ()for x in self .authorizations ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _authorization_ttl_days =reader .read_int ()
        reader .read_int ()
        _authorizations =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _authorizations .append (_x )

        return cls (authorization_ttl_days =_authorization_ttl_days ,authorizations =_authorizations )

class AutoDownloadSettings (TLObject ):
    CONSTRUCTOR_ID =0x63cacf26 
    SUBCLASS_OF_ID =0x2fb85921 

    def __init__ (self ,low :'TypeAutoDownloadSettings',medium :'TypeAutoDownloadSettings',high :'TypeAutoDownloadSettings'):
        """"""
        self .low =low 
        self .medium =medium 
        self .high =high 

    def to_dict (self ):
        return {
        '_':'AutoDownloadSettings',
        'low':self .low .to_dict ()if isinstance (self .low ,TLObject )else self .low ,
        'medium':self .medium .to_dict ()if isinstance (self .medium ,TLObject )else self .medium ,
        'high':self .high .to_dict ()if isinstance (self .high ,TLObject )else self .high 
        }

    def _bytes (self ):
        return b''.join ((
        b'&\xcf\xcac',
        self .low ._bytes (),
        self .medium ._bytes (),
        self .high ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _low =reader .tgread_object ()
        _medium =reader .tgread_object ()
        _high =reader .tgread_object ()
        return cls (low =_low ,medium =_medium ,high =_high )

class AutoSaveSettings (TLObject ):
    CONSTRUCTOR_ID =0x4c3e069d 
    SUBCLASS_OF_ID =0x48cf2f02 

    def __init__ (self ,users_settings :'TypeAutoSaveSettings',chats_settings :'TypeAutoSaveSettings',broadcasts_settings :'TypeAutoSaveSettings',exceptions :List ['TypeAutoSaveException'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .users_settings =users_settings 
        self .chats_settings =chats_settings 
        self .broadcasts_settings =broadcasts_settings 
        self .exceptions =exceptions 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'AutoSaveSettings',
        'users_settings':self .users_settings .to_dict ()if isinstance (self .users_settings ,TLObject )else self .users_settings ,
        'chats_settings':self .chats_settings .to_dict ()if isinstance (self .chats_settings ,TLObject )else self .chats_settings ,
        'broadcasts_settings':self .broadcasts_settings .to_dict ()if isinstance (self .broadcasts_settings ,TLObject )else self .broadcasts_settings ,
        'exceptions':[]if self .exceptions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .exceptions ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9d\x06>L',
        self .users_settings ._bytes (),
        self .chats_settings ._bytes (),
        self .broadcasts_settings ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .exceptions )),b''.join (x ._bytes ()for x in self .exceptions ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _users_settings =reader .tgread_object ()
        _chats_settings =reader .tgread_object ()
        _broadcasts_settings =reader .tgread_object ()
        reader .read_int ()
        _exceptions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _exceptions .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (users_settings =_users_settings ,chats_settings =_chats_settings ,broadcasts_settings =_broadcasts_settings ,exceptions =_exceptions ,chats =_chats ,users =_users )

class ContentSettings (TLObject ):
    CONSTRUCTOR_ID =0x57e28221 
    SUBCLASS_OF_ID =0xae3ff891 

    def __init__ (self ,sensitive_enabled :Optional [bool ]=None ,sensitive_can_change :Optional [bool ]=None ):
        """"""
        self .sensitive_enabled =sensitive_enabled 
        self .sensitive_can_change =sensitive_can_change 

    def to_dict (self ):
        return {
        '_':'ContentSettings',
        'sensitive_enabled':self .sensitive_enabled ,
        'sensitive_can_change':self .sensitive_can_change 
        }

    def _bytes (self ):
        return b''.join ((
        b'!\x82\xe2W',
        struct .pack ('<I',(0 if self .sensitive_enabled is None or self .sensitive_enabled is False else 1 )|(0 if self .sensitive_can_change is None or self .sensitive_can_change is False else 2 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _sensitive_enabled =bool (flags &1 )
        _sensitive_can_change =bool (flags &2 )
        return cls (sensitive_enabled =_sensitive_enabled ,sensitive_can_change =_sensitive_can_change )

class EmailVerified (TLObject ):
    CONSTRUCTOR_ID =0x2b96cd1b 
    SUBCLASS_OF_ID =0x64833188 

    def __init__ (self ,email :str ):
        """"""
        self .email =email 

    def to_dict (self ):
        return {
        '_':'EmailVerified',
        'email':self .email 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1b\xcd\x96+',
        self .serialize_bytes (self .email ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _email =reader .tgread_string ()
        return cls (email =_email )

class EmailVerifiedLogin (TLObject ):
    CONSTRUCTOR_ID =0xe1bb0d61 
    SUBCLASS_OF_ID =0x64833188 

    def __init__ (self ,email :str ,sent_code :'TypeSentCode'):
        """"""
        self .email =email 
        self .sent_code =sent_code 

    def to_dict (self ):
        return {
        '_':'EmailVerifiedLogin',
        'email':self .email ,
        'sent_code':self .sent_code .to_dict ()if isinstance (self .sent_code ,TLObject )else self .sent_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'a\r\xbb\xe1',
        self .serialize_bytes (self .email ),
        self .sent_code ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _email =reader .tgread_string ()
        _sent_code =reader .tgread_object ()
        return cls (email =_email ,sent_code =_sent_code )

class EmojiStatuses (TLObject ):
    CONSTRUCTOR_ID =0x90c467d1 
    SUBCLASS_OF_ID =0xd3e005ca 

    def __init__ (self ,hash :int ,statuses :List ['TypeEmojiStatus']):
        """"""
        self .hash =hash 
        self .statuses =statuses 

    def to_dict (self ):
        return {
        '_':'EmojiStatuses',
        'hash':self .hash ,
        'statuses':[]if self .statuses is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .statuses ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd1g\xc4\x90',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .statuses )),b''.join (x ._bytes ()for x in self .statuses ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _statuses =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _statuses .append (_x )

        return cls (hash =_hash ,statuses =_statuses )

class EmojiStatusesNotModified (TLObject ):
    CONSTRUCTOR_ID =0xd08ce645 
    SUBCLASS_OF_ID =0xd3e005ca 

    def to_dict (self ):
        return {
        '_':'EmojiStatusesNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'E\xe6\x8c\xd0',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class Password (TLObject ):
    CONSTRUCTOR_ID =0x957b50fb 
    SUBCLASS_OF_ID =0x53a211a3 

    def __init__ (self ,new_algo :'TypePasswordKdfAlgo',new_secure_algo :'TypeSecurePasswordKdfAlgo',secure_random :bytes ,has_recovery :Optional [bool ]=None ,has_secure_values :Optional [bool ]=None ,has_password :Optional [bool ]=None ,current_algo :Optional ['TypePasswordKdfAlgo']=None ,srp_B :Optional [bytes ]=None ,srp_id :Optional [int ]=None ,hint :Optional [str ]=None ,email_unconfirmed_pattern :Optional [str ]=None ,pending_reset_date :Optional [datetime ]=None ,login_email_pattern :Optional [str ]=None ):
        """"""
        self .new_algo =new_algo 
        self .new_secure_algo =new_secure_algo 
        self .secure_random =secure_random 
        self .has_recovery =has_recovery 
        self .has_secure_values =has_secure_values 
        self .has_password =has_password 
        self .current_algo =current_algo 
        self .srp_B =srp_B 
        self .srp_id =srp_id 
        self .hint =hint 
        self .email_unconfirmed_pattern =email_unconfirmed_pattern 
        self .pending_reset_date =pending_reset_date 
        self .login_email_pattern =login_email_pattern 

    def to_dict (self ):
        return {
        '_':'Password',
        'new_algo':self .new_algo .to_dict ()if isinstance (self .new_algo ,TLObject )else self .new_algo ,
        'new_secure_algo':self .new_secure_algo .to_dict ()if isinstance (self .new_secure_algo ,TLObject )else self .new_secure_algo ,
        'secure_random':self .secure_random ,
        'has_recovery':self .has_recovery ,
        'has_secure_values':self .has_secure_values ,
        'has_password':self .has_password ,
        'current_algo':self .current_algo .to_dict ()if isinstance (self .current_algo ,TLObject )else self .current_algo ,
        'srp_B':self .srp_B ,
        'srp_id':self .srp_id ,
        'hint':self .hint ,
        'email_unconfirmed_pattern':self .email_unconfirmed_pattern ,
        'pending_reset_date':self .pending_reset_date ,
        'login_email_pattern':self .login_email_pattern 
        }

    def _bytes (self ):
        assert ((self .has_password or self .has_password is not None )and (self .current_algo or self .current_algo is not None )and (self .srp_B or self .srp_B is not None )and (self .srp_id or self .srp_id is not None ))or ((self .has_password is None or self .has_password is False )and (self .current_algo is None or self .current_algo is False )and (self .srp_B is None or self .srp_B is False )and (self .srp_id is None or self .srp_id is False )),'has_password, current_algo, srp_B, srp_id parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'\xfbP{\x95',
        struct .pack ('<I',(0 if self .has_recovery is None or self .has_recovery is False else 1 )|(0 if self .has_secure_values is None or self .has_secure_values is False else 2 )|(0 if self .has_password is None or self .has_password is False else 4 )|(0 if self .current_algo is None or self .current_algo is False else 4 )|(0 if self .srp_B is None or self .srp_B is False else 4 )|(0 if self .srp_id is None or self .srp_id is False else 4 )|(0 if self .hint is None or self .hint is False else 8 )|(0 if self .email_unconfirmed_pattern is None or self .email_unconfirmed_pattern is False else 16 )|(0 if self .pending_reset_date is None or self .pending_reset_date is False else 32 )|(0 if self .login_email_pattern is None or self .login_email_pattern is False else 64 )),
        b''if self .current_algo is None or self .current_algo is False else (self .current_algo ._bytes ()),
        b''if self .srp_B is None or self .srp_B is False else (self .serialize_bytes (self .srp_B )),
        b''if self .srp_id is None or self .srp_id is False else (struct .pack ('<q',self .srp_id )),
        b''if self .hint is None or self .hint is False else (self .serialize_bytes (self .hint )),
        b''if self .email_unconfirmed_pattern is None or self .email_unconfirmed_pattern is False else (self .serialize_bytes (self .email_unconfirmed_pattern )),
        self .new_algo ._bytes (),
        self .new_secure_algo ._bytes (),
        self .serialize_bytes (self .secure_random ),
        b''if self .pending_reset_date is None or self .pending_reset_date is False else (self .serialize_datetime (self .pending_reset_date )),
        b''if self .login_email_pattern is None or self .login_email_pattern is False else (self .serialize_bytes (self .login_email_pattern )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _has_recovery =bool (flags &1 )
        _has_secure_values =bool (flags &2 )
        _has_password =bool (flags &4 )
        if flags &4 :
            _current_algo =reader .tgread_object ()
        else :
            _current_algo =None 
        if flags &4 :
            _srp_B =reader .tgread_bytes ()
        else :
            _srp_B =None 
        if flags &4 :
            _srp_id =reader .read_long ()
        else :
            _srp_id =None 
        if flags &8 :
            _hint =reader .tgread_string ()
        else :
            _hint =None 
        if flags &16 :
            _email_unconfirmed_pattern =reader .tgread_string ()
        else :
            _email_unconfirmed_pattern =None 
        _new_algo =reader .tgread_object ()
        _new_secure_algo =reader .tgread_object ()
        _secure_random =reader .tgread_bytes ()
        if flags &32 :
            _pending_reset_date =reader .tgread_date ()
        else :
            _pending_reset_date =None 
        if flags &64 :
            _login_email_pattern =reader .tgread_string ()
        else :
            _login_email_pattern =None 
        return cls (new_algo =_new_algo ,new_secure_algo =_new_secure_algo ,secure_random =_secure_random ,has_recovery =_has_recovery ,has_secure_values =_has_secure_values ,has_password =_has_password ,current_algo =_current_algo ,srp_B =_srp_B ,srp_id =_srp_id ,hint =_hint ,email_unconfirmed_pattern =_email_unconfirmed_pattern ,pending_reset_date =_pending_reset_date ,login_email_pattern =_login_email_pattern )

class PasswordInputSettings (TLObject ):
    CONSTRUCTOR_ID =0xc23727c9 
    SUBCLASS_OF_ID =0xc426ca6 

    def __init__ (self ,new_algo :Optional ['TypePasswordKdfAlgo']=None ,new_password_hash :Optional [bytes ]=None ,hint :Optional [str ]=None ,email :Optional [str ]=None ,new_secure_settings :Optional ['TypeSecureSecretSettings']=None ):
        """"""
        self .new_algo =new_algo 
        self .new_password_hash =new_password_hash 
        self .hint =hint 
        self .email =email 
        self .new_secure_settings =new_secure_settings 

    def to_dict (self ):
        return {
        '_':'PasswordInputSettings',
        'new_algo':self .new_algo .to_dict ()if isinstance (self .new_algo ,TLObject )else self .new_algo ,
        'new_password_hash':self .new_password_hash ,
        'hint':self .hint ,
        'email':self .email ,
        'new_secure_settings':self .new_secure_settings .to_dict ()if isinstance (self .new_secure_settings ,TLObject )else self .new_secure_settings 
        }

    def _bytes (self ):
        assert ((self .new_algo or self .new_algo is not None )and (self .new_password_hash or self .new_password_hash is not None )and (self .hint or self .hint is not None ))or ((self .new_algo is None or self .new_algo is False )and (self .new_password_hash is None or self .new_password_hash is False )and (self .hint is None or self .hint is False )),'new_algo, new_password_hash, hint parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b"\xc9'7\xc2",
        struct .pack ('<I',(0 if self .new_algo is None or self .new_algo is False else 1 )|(0 if self .new_password_hash is None or self .new_password_hash is False else 1 )|(0 if self .hint is None or self .hint is False else 1 )|(0 if self .email is None or self .email is False else 2 )|(0 if self .new_secure_settings is None or self .new_secure_settings is False else 4 )),
        b''if self .new_algo is None or self .new_algo is False else (self .new_algo ._bytes ()),
        b''if self .new_password_hash is None or self .new_password_hash is False else (self .serialize_bytes (self .new_password_hash )),
        b''if self .hint is None or self .hint is False else (self .serialize_bytes (self .hint )),
        b''if self .email is None or self .email is False else (self .serialize_bytes (self .email )),
        b''if self .new_secure_settings is None or self .new_secure_settings is False else (self .new_secure_settings ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _new_algo =reader .tgread_object ()
        else :
            _new_algo =None 
        if flags &1 :
            _new_password_hash =reader .tgread_bytes ()
        else :
            _new_password_hash =None 
        if flags &1 :
            _hint =reader .tgread_string ()
        else :
            _hint =None 
        if flags &2 :
            _email =reader .tgread_string ()
        else :
            _email =None 
        if flags &4 :
            _new_secure_settings =reader .tgread_object ()
        else :
            _new_secure_settings =None 
        return cls (new_algo =_new_algo ,new_password_hash =_new_password_hash ,hint =_hint ,email =_email ,new_secure_settings =_new_secure_settings )

class PasswordSettings (TLObject ):
    CONSTRUCTOR_ID =0x9a5c33e5 
    SUBCLASS_OF_ID =0xd23fb078 

    def __init__ (self ,email :Optional [str ]=None ,secure_settings :Optional ['TypeSecureSecretSettings']=None ):
        """"""
        self .email =email 
        self .secure_settings =secure_settings 

    def to_dict (self ):
        return {
        '_':'PasswordSettings',
        'email':self .email ,
        'secure_settings':self .secure_settings .to_dict ()if isinstance (self .secure_settings ,TLObject )else self .secure_settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe53\\\x9a',
        struct .pack ('<I',(0 if self .email is None or self .email is False else 1 )|(0 if self .secure_settings is None or self .secure_settings is False else 2 )),
        b''if self .email is None or self .email is False else (self .serialize_bytes (self .email )),
        b''if self .secure_settings is None or self .secure_settings is False else (self .secure_settings ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _email =reader .tgread_string ()
        else :
            _email =None 
        if flags &2 :
            _secure_settings =reader .tgread_object ()
        else :
            _secure_settings =None 
        return cls (email =_email ,secure_settings =_secure_settings )

class PrivacyRules (TLObject ):
    CONSTRUCTOR_ID =0x50a04e45 
    SUBCLASS_OF_ID =0xb55aba82 

    def __init__ (self ,rules :List ['TypePrivacyRule'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .rules =rules 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'PrivacyRules',
        'rules':[]if self .rules is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .rules ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'EN\xa0P',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .rules )),b''.join (x ._bytes ()for x in self .rules ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _rules =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _rules .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (rules =_rules ,chats =_chats ,users =_users )

class ResetPasswordFailedWait (TLObject ):
    CONSTRUCTOR_ID =0xe3779861 
    SUBCLASS_OF_ID =0x49507416 

    def __init__ (self ,retry_date :Optional [datetime ]):
        """"""
        self .retry_date =retry_date 

    def to_dict (self ):
        return {
        '_':'ResetPasswordFailedWait',
        'retry_date':self .retry_date 
        }

    def _bytes (self ):
        return b''.join ((
        b'a\x98w\xe3',
        self .serialize_datetime (self .retry_date ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _retry_date =reader .tgread_date ()
        return cls (retry_date =_retry_date )

class ResetPasswordOk (TLObject ):
    CONSTRUCTOR_ID =0xe926d63e 
    SUBCLASS_OF_ID =0x49507416 

    def to_dict (self ):
        return {
        '_':'ResetPasswordOk'
        }

    def _bytes (self ):
        return b''.join ((
        b'>\xd6&\xe9',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetPasswordRequestedWait (TLObject ):
    CONSTRUCTOR_ID =0xe9effc7d 
    SUBCLASS_OF_ID =0x49507416 

    def __init__ (self ,until_date :Optional [datetime ]):
        """"""
        self .until_date =until_date 

    def to_dict (self ):
        return {
        '_':'ResetPasswordRequestedWait',
        'until_date':self .until_date 
        }

    def _bytes (self ):
        return b''.join ((
        b'}\xfc\xef\xe9',
        self .serialize_datetime (self .until_date ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _until_date =reader .tgread_date ()
        return cls (until_date =_until_date )

class SavedRingtone (TLObject ):
    CONSTRUCTOR_ID =0xb7263f6d 
    SUBCLASS_OF_ID =0xb1e28424 

    def to_dict (self ):
        return {
        '_':'SavedRingtone'
        }

    def _bytes (self ):
        return b''.join ((
        b'm?&\xb7',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SavedRingtoneConverted (TLObject ):
    CONSTRUCTOR_ID =0x1f307eb7 
    SUBCLASS_OF_ID =0xb1e28424 

    def __init__ (self ,document :'TypeDocument'):
        """"""
        self .document =document 

    def to_dict (self ):
        return {
        '_':'SavedRingtoneConverted',
        'document':self .document .to_dict ()if isinstance (self .document ,TLObject )else self .document 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb7~0\x1f',
        self .document ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _document =reader .tgread_object ()
        return cls (document =_document )

class SavedRingtones (TLObject ):
    CONSTRUCTOR_ID =0xc1e92cc5 
    SUBCLASS_OF_ID =0x27bcc95e 

    def __init__ (self ,hash :int ,ringtones :List ['TypeDocument']):
        """"""
        self .hash =hash 
        self .ringtones =ringtones 

    def to_dict (self ):
        return {
        '_':'SavedRingtones',
        'hash':self .hash ,
        'ringtones':[]if self .ringtones is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .ringtones ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc5,\xe9\xc1',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .ringtones )),b''.join (x ._bytes ()for x in self .ringtones ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _ringtones =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _ringtones .append (_x )

        return cls (hash =_hash ,ringtones =_ringtones )

class SavedRingtonesNotModified (TLObject ):
    CONSTRUCTOR_ID =0xfbf6e8b1 
    SUBCLASS_OF_ID =0x27bcc95e 

    def to_dict (self ):
        return {
        '_':'SavedRingtonesNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb1\xe8\xf6\xfb',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SentEmailCode (TLObject ):
    CONSTRUCTOR_ID =0x811f854f 
    SUBCLASS_OF_ID =0x69f3c06e 

    def __init__ (self ,email_pattern :str ,length :int ):
        """"""
        self .email_pattern =email_pattern 
        self .length =length 

    def to_dict (self ):
        return {
        '_':'SentEmailCode',
        'email_pattern':self .email_pattern ,
        'length':self .length 
        }

    def _bytes (self ):
        return b''.join ((
        b'O\x85\x1f\x81',
        self .serialize_bytes (self .email_pattern ),
        struct .pack ('<i',self .length ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _email_pattern =reader .tgread_string ()
        _length =reader .read_int ()
        return cls (email_pattern =_email_pattern ,length =_length )

class Takeout (TLObject ):
    CONSTRUCTOR_ID =0x4dba4501 
    SUBCLASS_OF_ID =0x843ebe85 

    def __init__ (self ,id :int ):
        """"""
        self .id =id 

    def to_dict (self ):
        return {
        '_':'Takeout',
        'id':self .id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x01E\xbaM',
        struct .pack ('<q',self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _id =reader .read_long ()
        return cls (id =_id )

class Themes (TLObject ):
    CONSTRUCTOR_ID =0x9a3d8c6d 
    SUBCLASS_OF_ID =0x7fc52204 

    def __init__ (self ,hash :int ,themes :List ['TypeTheme']):
        """"""
        self .hash =hash 
        self .themes =themes 

    def to_dict (self ):
        return {
        '_':'Themes',
        'hash':self .hash ,
        'themes':[]if self .themes is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .themes ]
        }

    def _bytes (self ):
        return b''.join ((
        b'm\x8c=\x9a',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .themes )),b''.join (x ._bytes ()for x in self .themes ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _themes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _themes .append (_x )

        return cls (hash =_hash ,themes =_themes )

class ThemesNotModified (TLObject ):
    CONSTRUCTOR_ID =0xf41eb622 
    SUBCLASS_OF_ID =0x7fc52204 

    def to_dict (self ):
        return {
        '_':'ThemesNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'"\xb6\x1e\xf4',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class TmpPassword (TLObject ):
    CONSTRUCTOR_ID =0xdb64fd34 
    SUBCLASS_OF_ID =0xb064992d 

    def __init__ (self ,tmp_password :bytes ,valid_until :Optional [datetime ]):
        """"""
        self .tmp_password =tmp_password 
        self .valid_until =valid_until 

    def to_dict (self ):
        return {
        '_':'TmpPassword',
        'tmp_password':self .tmp_password ,
        'valid_until':self .valid_until 
        }

    def _bytes (self ):
        return b''.join ((
        b'4\xfdd\xdb',
        self .serialize_bytes (self .tmp_password ),
        self .serialize_datetime (self .valid_until ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _tmp_password =reader .tgread_bytes ()
        _valid_until =reader .tgread_date ()
        return cls (tmp_password =_tmp_password ,valid_until =_valid_until )

class WallPapers (TLObject ):
    CONSTRUCTOR_ID =0xcdc3858c 
    SUBCLASS_OF_ID =0xa2c548fd 

    def __init__ (self ,hash :int ,wallpapers :List ['TypeWallPaper']):
        """"""
        self .hash =hash 
        self .wallpapers =wallpapers 

    def to_dict (self ):
        return {
        '_':'WallPapers',
        'hash':self .hash ,
        'wallpapers':[]if self .wallpapers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .wallpapers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8c\x85\xc3\xcd',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .wallpapers )),b''.join (x ._bytes ()for x in self .wallpapers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _wallpapers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _wallpapers .append (_x )

        return cls (hash =_hash ,wallpapers =_wallpapers )

class WallPapersNotModified (TLObject ):
    CONSTRUCTOR_ID =0x1c199183 
    SUBCLASS_OF_ID =0xa2c548fd 

    def to_dict (self ):
        return {
        '_':'WallPapersNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x83\x91\x19\x1c',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class WebAuthorizations (TLObject ):
    CONSTRUCTOR_ID =0xed56c9fc 
    SUBCLASS_OF_ID =0x9a365b32 

    def __init__ (self ,authorizations :List ['TypeWebAuthorization'],users :List ['TypeUser']):
        """"""
        self .authorizations =authorizations 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'WebAuthorizations',
        'authorizations':[]if self .authorizations is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .authorizations ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfc\xc9V\xed',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .authorizations )),b''.join (x ._bytes ()for x in self .authorizations ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _authorizations =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _authorizations .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (authorizations =_authorizations ,users =_users )

