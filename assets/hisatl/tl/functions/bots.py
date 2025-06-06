""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeBotCommand ,TypeBotCommandScope ,TypeBotMenuButton ,TypeChatAdminRights ,TypeDataJSON ,TypeInputUser 

class AllowSendMessageRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf132e3ef 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,bot :'TypeInputUser'):
        """"""
        self .bot =bot 

    async def resolve (self ,client ,utils ):
        self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'AllowSendMessageRequest',
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xef\xe32\xf1',
        self .bot ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot =reader .tgread_object ()
        return cls (bot =_bot )

class AnswerWebhookJSONQueryRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe6213f4d 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,query_id :int ,data :'TypeDataJSON'):
        """"""
        self .query_id =query_id 
        self .data =data 

    def to_dict (self ):
        return {
        '_':'AnswerWebhookJSONQueryRequest',
        'query_id':self .query_id ,
        'data':self .data .to_dict ()if isinstance (self .data ,TLObject )else self .data 
        }

    def _bytes (self ):
        return b''.join ((
        b'M?!\xe6',
        struct .pack ('<q',self .query_id ),
        self .data ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _query_id =reader .read_long ()
        _data =reader .tgread_object ()
        return cls (query_id =_query_id ,data =_data )

class CanSendMessageRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1359f4e6 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,bot :'TypeInputUser'):
        """"""
        self .bot =bot 

    async def resolve (self ,client ,utils ):
        self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'CanSendMessageRequest',
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe6\xf4Y\x13',
        self .bot ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot =reader .tgread_object ()
        return cls (bot =_bot )

class GetBotCommandsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe34c0dd6 
    SUBCLASS_OF_ID =0xfae91529 

    def __init__ (self ,scope :'TypeBotCommandScope',lang_code :str ):
        """"""
        self .scope =scope 
        self .lang_code =lang_code 

    def to_dict (self ):
        return {
        '_':'GetBotCommandsRequest',
        'scope':self .scope .to_dict ()if isinstance (self .scope ,TLObject )else self .scope ,
        'lang_code':self .lang_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd6\rL\xe3',
        self .scope ._bytes (),
        self .serialize_bytes (self .lang_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _scope =reader .tgread_object ()
        _lang_code =reader .tgread_string ()
        return cls (scope =_scope ,lang_code =_lang_code )

class GetBotInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdcd914fd 
    SUBCLASS_OF_ID =0xca7b2235 

    def __init__ (self ,lang_code :str ,bot :Optional ['TypeInputUser']=None ):
        """"""
        self .lang_code =lang_code 
        self .bot =bot 

    async def resolve (self ,client ,utils ):
        if self .bot :
            self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'GetBotInfoRequest',
        'lang_code':self .lang_code ,
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfd\x14\xd9\xdc',
        struct .pack ('<I',(0 if self .bot is None or self .bot is False else 1 )),
        b''if self .bot is None or self .bot is False else (self .bot ._bytes ()),
        self .serialize_bytes (self .lang_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _bot =reader .tgread_object ()
        else :
            _bot =None 
        _lang_code =reader .tgread_string ()
        return cls (lang_code =_lang_code ,bot =_bot )

class GetBotMenuButtonRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9c60eb28 
    SUBCLASS_OF_ID =0x4c71bd3c 

    def __init__ (self ,user_id :'TypeInputUser'):
        """"""
        self .user_id =user_id 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'GetBotMenuButtonRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'(\xeb`\x9c',
        self .user_id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _user_id =reader .tgread_object ()
        return cls (user_id =_user_id )

class InvokeWebViewCustomMethodRequest (TLRequest ):
    CONSTRUCTOR_ID =0x87fc5e7 
    SUBCLASS_OF_ID =0xad0352e8 

    def __init__ (self ,bot :'TypeInputUser',custom_method :str ,params :'TypeDataJSON'):
        """"""
        self .bot =bot 
        self .custom_method =custom_method 
        self .params =params 

    async def resolve (self ,client ,utils ):
        self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'InvokeWebViewCustomMethodRequest',
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot ,
        'custom_method':self .custom_method ,
        'params':self .params .to_dict ()if isinstance (self .params ,TLObject )else self .params 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe7\xc5\x7f\x08',
        self .bot ._bytes (),
        self .serialize_bytes (self .custom_method ),
        self .params ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot =reader .tgread_object ()
        _custom_method =reader .tgread_string ()
        _params =reader .tgread_object ()
        return cls (bot =_bot ,custom_method =_custom_method ,params =_params )

class ReorderUsernamesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9709b1c2 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,bot :'TypeInputUser',order :List [str ]):
        """"""
        self .bot =bot 
        self .order =order 

    async def resolve (self ,client ,utils ):
        self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'ReorderUsernamesRequest',
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot ,
        'order':[]if self .order is None else self .order [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc2\xb1\t\x97',
        self .bot ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .order )),b''.join (self .serialize_bytes (x )for x in self .order ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot =reader .tgread_object ()
        reader .read_int ()
        _order =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _order .append (_x )

        return cls (bot =_bot ,order =_order )

class ResetBotCommandsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3d8de0f9 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,scope :'TypeBotCommandScope',lang_code :str ):
        """"""
        self .scope =scope 
        self .lang_code =lang_code 

    def to_dict (self ):
        return {
        '_':'ResetBotCommandsRequest',
        'scope':self .scope .to_dict ()if isinstance (self .scope ,TLObject )else self .scope ,
        'lang_code':self .lang_code 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9\xe0\x8d=',
        self .scope ._bytes (),
        self .serialize_bytes (self .lang_code ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _scope =reader .tgread_object ()
        _lang_code =reader .tgread_string ()
        return cls (scope =_scope ,lang_code =_lang_code )

class SendCustomRequestRequest (TLRequest ):
    CONSTRUCTOR_ID =0xaa2769ed 
    SUBCLASS_OF_ID =0xad0352e8 

    def __init__ (self ,custom_method :str ,params :'TypeDataJSON'):
        """"""
        self .custom_method =custom_method 
        self .params =params 

    def to_dict (self ):
        return {
        '_':'SendCustomRequestRequest',
        'custom_method':self .custom_method ,
        'params':self .params .to_dict ()if isinstance (self .params ,TLObject )else self .params 
        }

    def _bytes (self ):
        return b''.join ((
        b"\xedi'\xaa",
        self .serialize_bytes (self .custom_method ),
        self .params ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _custom_method =reader .tgread_string ()
        _params =reader .tgread_object ()
        return cls (custom_method =_custom_method ,params =_params )

class SetBotBroadcastDefaultAdminRightsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x788464e1 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,admin_rights :'TypeChatAdminRights'):
        """"""
        self .admin_rights =admin_rights 

    def to_dict (self ):
        return {
        '_':'SetBotBroadcastDefaultAdminRightsRequest',
        'admin_rights':self .admin_rights .to_dict ()if isinstance (self .admin_rights ,TLObject )else self .admin_rights 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe1d\x84x',
        self .admin_rights ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _admin_rights =reader .tgread_object ()
        return cls (admin_rights =_admin_rights )

class SetBotCommandsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x517165a 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,scope :'TypeBotCommandScope',lang_code :str ,commands :List ['TypeBotCommand']):
        """"""
        self .scope =scope 
        self .lang_code =lang_code 
        self .commands =commands 

    def to_dict (self ):
        return {
        '_':'SetBotCommandsRequest',
        'scope':self .scope .to_dict ()if isinstance (self .scope ,TLObject )else self .scope ,
        'lang_code':self .lang_code ,
        'commands':[]if self .commands is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .commands ]
        }

    def _bytes (self ):
        return b''.join ((
        b'Z\x16\x17\x05',
        self .scope ._bytes (),
        self .serialize_bytes (self .lang_code ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .commands )),b''.join (x ._bytes ()for x in self .commands ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _scope =reader .tgread_object ()
        _lang_code =reader .tgread_string ()
        reader .read_int ()
        _commands =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _commands .append (_x )

        return cls (scope =_scope ,lang_code =_lang_code ,commands =_commands )

class SetBotGroupDefaultAdminRightsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x925ec9ea 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,admin_rights :'TypeChatAdminRights'):
        """"""
        self .admin_rights =admin_rights 

    def to_dict (self ):
        return {
        '_':'SetBotGroupDefaultAdminRightsRequest',
        'admin_rights':self .admin_rights .to_dict ()if isinstance (self .admin_rights ,TLObject )else self .admin_rights 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xea\xc9^\x92',
        self .admin_rights ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _admin_rights =reader .tgread_object ()
        return cls (admin_rights =_admin_rights )

class SetBotInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x10cf3123 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,lang_code :str ,bot :Optional ['TypeInputUser']=None ,name :Optional [str ]=None ,about :Optional [str ]=None ,description :Optional [str ]=None ):
        """"""
        self .lang_code =lang_code 
        self .bot =bot 
        self .name =name 
        self .about =about 
        self .description =description 

    async def resolve (self ,client ,utils ):
        if self .bot :
            self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'SetBotInfoRequest',
        'lang_code':self .lang_code ,
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot ,
        'name':self .name ,
        'about':self .about ,
        'description':self .description 
        }

    def _bytes (self ):
        return b''.join ((
        b'#1\xcf\x10',
        struct .pack ('<I',(0 if self .bot is None or self .bot is False else 4 )|(0 if self .name is None or self .name is False else 8 )|(0 if self .about is None or self .about is False else 1 )|(0 if self .description is None or self .description is False else 2 )),
        b''if self .bot is None or self .bot is False else (self .bot ._bytes ()),
        self .serialize_bytes (self .lang_code ),
        b''if self .name is None or self .name is False else (self .serialize_bytes (self .name )),
        b''if self .about is None or self .about is False else (self .serialize_bytes (self .about )),
        b''if self .description is None or self .description is False else (self .serialize_bytes (self .description )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &4 :
            _bot =reader .tgread_object ()
        else :
            _bot =None 
        _lang_code =reader .tgread_string ()
        if flags &8 :
            _name =reader .tgread_string ()
        else :
            _name =None 
        if flags &1 :
            _about =reader .tgread_string ()
        else :
            _about =None 
        if flags &2 :
            _description =reader .tgread_string ()
        else :
            _description =None 
        return cls (lang_code =_lang_code ,bot =_bot ,name =_name ,about =_about ,description =_description )

class SetBotMenuButtonRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4504d54f 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,user_id :'TypeInputUser',button :'TypeBotMenuButton'):
        """"""
        self .user_id =user_id 
        self .button =button 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'SetBotMenuButtonRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'button':self .button .to_dict ()if isinstance (self .button ,TLObject )else self .button 
        }

    def _bytes (self ):
        return b''.join ((
        b'O\xd5\x04E',
        self .user_id ._bytes (),
        self .button ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _user_id =reader .tgread_object ()
        _button =reader .tgread_object ()
        return cls (user_id =_user_id ,button =_button )

class ToggleUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x53ca973 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,bot :'TypeInputUser',username :str ,active :bool ):
        """"""
        self .bot =bot 
        self .username =username 
        self .active =active 

    async def resolve (self ,client ,utils ):
        self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'ToggleUsernameRequest',
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot ,
        'username':self .username ,
        'active':self .active 
        }

    def _bytes (self ):
        return b''.join ((
        b's\xa9<\x05',
        self .bot ._bytes (),
        self .serialize_bytes (self .username ),
        b'\xb5ur\x99'if self .active else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _bot =reader .tgread_object ()
        _username =reader .tgread_string ()
        _active =reader .tgread_bool ()
        return cls (bot =_bot ,username =_username ,active =_active )

