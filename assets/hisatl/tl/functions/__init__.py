""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
from .import account ,auth ,bots ,channels ,chatlists ,contacts ,folders ,help ,langpack ,messages ,payments ,phone ,photos ,premium ,stats ,stickers ,stories ,updates ,upload ,users 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputClientProxy ,TypeJSONValue ,TypeMessageRange ,TypeType ,TypeX 

class DestroyAuthKeyRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd1435160 
    SUBCLASS_OF_ID =0x8291e68e 

    def to_dict (self ):
        return {
        '_':'DestroyAuthKeyRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'`QC\xd1',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class DestroySessionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe7512126 
    SUBCLASS_OF_ID =0xaf0ce7bd 

    def __init__ (self ,session_id :int ):
        """"""
        self .session_id =session_id 

    def to_dict (self ):
        return {
        '_':'DestroySessionRequest',
        'session_id':self .session_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'&!Q\xe7',
        struct .pack ('<q',self .session_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _session_id =reader .read_long ()
        return cls (session_id =_session_id )

class GetFutureSaltsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb921bd04 
    SUBCLASS_OF_ID =0x1090f517 

    def __init__ (self ,num :int ):
        """"""
        self .num =num 

    def to_dict (self ):
        return {
        '_':'GetFutureSaltsRequest',
        'num':self .num 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x04\xbd!\xb9',
        struct .pack ('<i',self .num ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _num =reader .read_int ()
        return cls (num =_num )

class InitConnectionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc1cd5ea9 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,api_id :int ,device_model :str ,system_version :str ,app_version :str ,system_lang_code :str ,lang_pack :str ,lang_code :str ,query :'TypeX',proxy :Optional ['TypeInputClientProxy']=None ,params :Optional ['TypeJSONValue']=None ):
        """"""
        self .api_id =api_id 
        self .device_model =device_model 
        self .system_version =system_version 
        self .app_version =app_version 
        self .system_lang_code =system_lang_code 
        self .lang_pack =lang_pack 
        self .lang_code =lang_code 
        self .query =query 
        self .proxy =proxy 
        self .params =params 

    def to_dict (self ):
        return {
        '_':'InitConnectionRequest',
        'api_id':self .api_id ,
        'device_model':self .device_model ,
        'system_version':self .system_version ,
        'app_version':self .app_version ,
        'system_lang_code':self .system_lang_code ,
        'lang_pack':self .lang_pack ,
        'lang_code':self .lang_code ,
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query ,
        'proxy':self .proxy .to_dict ()if isinstance (self .proxy ,TLObject )else self .proxy ,
        'params':self .params .to_dict ()if isinstance (self .params ,TLObject )else self .params 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa9^\xcd\xc1',
        struct .pack ('<I',(0 if self .proxy is None or self .proxy is False else 1 )|(0 if self .params is None or self .params is False else 2 )),
        struct .pack ('<i',self .api_id ),
        self .serialize_bytes (self .device_model ),
        self .serialize_bytes (self .system_version ),
        self .serialize_bytes (self .app_version ),
        self .serialize_bytes (self .system_lang_code ),
        self .serialize_bytes (self .lang_pack ),
        self .serialize_bytes (self .lang_code ),
        b''if self .proxy is None or self .proxy is False else (self .proxy ._bytes ()),
        b''if self .params is None or self .params is False else (self .params ._bytes ()),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _api_id =reader .read_int ()
        _device_model =reader .tgread_string ()
        _system_version =reader .tgread_string ()
        _app_version =reader .tgread_string ()
        _system_lang_code =reader .tgread_string ()
        _lang_pack =reader .tgread_string ()
        _lang_code =reader .tgread_string ()
        if flags &1 :
            _proxy =reader .tgread_object ()
        else :
            _proxy =None 
        if flags &2 :
            _params =reader .tgread_object ()
        else :
            _params =None 
        _query =reader .tgread_object ()
        return cls (api_id =_api_id ,device_model =_device_model ,system_version =_system_version ,app_version =_app_version ,system_lang_code =_system_lang_code ,lang_pack =_lang_pack ,lang_code =_lang_code ,query =_query ,proxy =_proxy ,params =_params )

class InvokeAfterMsgRequest (TLRequest ):
    CONSTRUCTOR_ID =0xcb9f372d 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,msg_id :int ,query :'TypeX'):
        """"""
        self .msg_id =msg_id 
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeAfterMsgRequest',
        'msg_id':self .msg_id ,
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'-7\x9f\xcb',
        struct .pack ('<q',self .msg_id ),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _msg_id =reader .read_long ()
        _query =reader .tgread_object ()
        return cls (msg_id =_msg_id ,query =_query )

class InvokeAfterMsgsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3dc4b4f0 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,msg_ids :List [int ],query :'TypeX'):
        """"""
        self .msg_ids =msg_ids 
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeAfterMsgsRequest',
        'msg_ids':[]if self .msg_ids is None else self .msg_ids [:],
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf0\xb4\xc4=',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .msg_ids )),b''.join (struct .pack ('<q',x )for x in self .msg_ids ),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _msg_ids =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_long ()
            _msg_ids .append (_x )

        _query =reader .tgread_object ()
        return cls (msg_ids =_msg_ids ,query =_query )

class InvokeWithLayerRequest (TLRequest ):
    CONSTRUCTOR_ID =0xda9b0d0d 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,layer :int ,query :'TypeX'):
        """"""
        self .layer =layer 
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeWithLayerRequest',
        'layer':self .layer ,
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'\r\r\x9b\xda',
        struct .pack ('<i',self .layer ),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _layer =reader .read_int ()
        _query =reader .tgread_object ()
        return cls (layer =_layer ,query =_query )

class InvokeWithMessagesRangeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x365275f2 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,range :'TypeMessageRange',query :'TypeX'):
        """"""
        self .range =range 
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeWithMessagesRangeRequest',
        'range':self .range .to_dict ()if isinstance (self .range ,TLObject )else self .range ,
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf2uR6',
        self .range ._bytes (),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _range =reader .tgread_object ()
        _query =reader .tgread_object ()
        return cls (range =_range ,query =_query )

class InvokeWithTakeoutRequest (TLRequest ):
    CONSTRUCTOR_ID =0xaca9fd2e 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,takeout_id :int ,query :'TypeX'):
        """"""
        self .takeout_id =takeout_id 
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeWithTakeoutRequest',
        'takeout_id':self .takeout_id ,
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'.\xfd\xa9\xac',
        struct .pack ('<q',self .takeout_id ),
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _takeout_id =reader .read_long ()
        _query =reader .tgread_object ()
        return cls (takeout_id =_takeout_id ,query =_query )

class InvokeWithoutUpdatesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbf9459b7 
    SUBCLASS_OF_ID =0xb7b2364b 

    def __init__ (self ,query :'TypeX'):
        """"""
        self .query =query 

    def to_dict (self ):
        return {
        '_':'InvokeWithoutUpdatesRequest',
        'query':self .query .to_dict ()if isinstance (self .query ,TLObject )else self .query 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb7Y\x94\xbf',
        self .query ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _query =reader .tgread_object ()
        return cls (query =_query )

class PingRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7abe77ec 
    SUBCLASS_OF_ID =0x816aee71 

    def __init__ (self ,ping_id :int ):
        """"""
        self .ping_id =ping_id 

    def to_dict (self ):
        return {
        '_':'PingRequest',
        'ping_id':self .ping_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xecw\xbez',
        struct .pack ('<q',self .ping_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _ping_id =reader .read_long ()
        return cls (ping_id =_ping_id )

class PingDelayDisconnectRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf3427b8c 
    SUBCLASS_OF_ID =0x816aee71 

    def __init__ (self ,ping_id :int ,disconnect_delay :int ):
        """"""
        self .ping_id =ping_id 
        self .disconnect_delay =disconnect_delay 

    def to_dict (self ):
        return {
        '_':'PingDelayDisconnectRequest',
        'ping_id':self .ping_id ,
        'disconnect_delay':self .disconnect_delay 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8c{B\xf3',
        struct .pack ('<q',self .ping_id ),
        struct .pack ('<i',self .disconnect_delay ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _ping_id =reader .read_long ()
        _disconnect_delay =reader .read_int ()
        return cls (ping_id =_ping_id ,disconnect_delay =_disconnect_delay )

class ReqDHParamsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd712e4be 
    SUBCLASS_OF_ID =0xa6188d9e 

    def __init__ (self ,nonce :int ,server_nonce :int ,p :bytes ,q :bytes ,public_key_fingerprint :int ,encrypted_data :bytes ):
        """"""
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .p =p 
        self .q =q 
        self .public_key_fingerprint =public_key_fingerprint 
        self .encrypted_data =encrypted_data 

    def to_dict (self ):
        return {
        '_':'ReqDHParamsRequest',
        'nonce':self .nonce ,
        'server_nonce':self .server_nonce ,
        'p':self .p ,
        'q':self .q ,
        'public_key_fingerprint':self .public_key_fingerprint ,
        'encrypted_data':self .encrypted_data 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbe\xe4\x12\xd7',
        self .nonce .to_bytes (16 ,'little',signed =True ),
        self .server_nonce .to_bytes (16 ,'little',signed =True ),
        self .serialize_bytes (self .p ),
        self .serialize_bytes (self .q ),
        struct .pack ('<q',self .public_key_fingerprint ),
        self .serialize_bytes (self .encrypted_data ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _nonce =reader .read_large_int (bits =128 )
        _server_nonce =reader .read_large_int (bits =128 )
        _p =reader .tgread_bytes ()
        _q =reader .tgread_bytes ()
        _public_key_fingerprint =reader .read_long ()
        _encrypted_data =reader .tgread_bytes ()
        return cls (nonce =_nonce ,server_nonce =_server_nonce ,p =_p ,q =_q ,public_key_fingerprint =_public_key_fingerprint ,encrypted_data =_encrypted_data )

class ReqPqRequest (TLRequest ):
    CONSTRUCTOR_ID =0x60469778 
    SUBCLASS_OF_ID =0x786986b8 

    def __init__ (self ,nonce :int ):
        """"""
        self .nonce =nonce 

    def to_dict (self ):
        return {
        '_':'ReqPqRequest',
        'nonce':self .nonce 
        }

    def _bytes (self ):
        return b''.join ((
        b'x\x97F`',
        self .nonce .to_bytes (16 ,'little',signed =True ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _nonce =reader .read_large_int (bits =128 )
        return cls (nonce =_nonce )

class ReqPqMultiRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbe7e8ef1 
    SUBCLASS_OF_ID =0x786986b8 

    def __init__ (self ,nonce :int ):
        """"""
        self .nonce =nonce 

    def to_dict (self ):
        return {
        '_':'ReqPqMultiRequest',
        'nonce':self .nonce 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf1\x8e~\xbe',
        self .nonce .to_bytes (16 ,'little',signed =True ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _nonce =reader .read_large_int (bits =128 )
        return cls (nonce =_nonce )

class RpcDropAnswerRequest (TLRequest ):
    CONSTRUCTOR_ID =0x58e4a740 
    SUBCLASS_OF_ID =0x4bca7570 

    def __init__ (self ,req_msg_id :int ):
        """"""
        self .req_msg_id =req_msg_id 

    def to_dict (self ):
        return {
        '_':'RpcDropAnswerRequest',
        'req_msg_id':self .req_msg_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'@\xa7\xe4X',
        struct .pack ('<q',self .req_msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _req_msg_id =reader .read_long ()
        return cls (req_msg_id =_req_msg_id )

class SetClientDHParamsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf5045f1f 
    SUBCLASS_OF_ID =0x55dd6cdb 

    def __init__ (self ,nonce :int ,server_nonce :int ,encrypted_data :bytes ):
        """"""
        self .nonce =nonce 
        self .server_nonce =server_nonce 
        self .encrypted_data =encrypted_data 

    def to_dict (self ):
        return {
        '_':'SetClientDHParamsRequest',
        'nonce':self .nonce ,
        'server_nonce':self .server_nonce ,
        'encrypted_data':self .encrypted_data 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1f_\x04\xf5',
        self .nonce .to_bytes (16 ,'little',signed =True ),
        self .server_nonce .to_bytes (16 ,'little',signed =True ),
        self .serialize_bytes (self .encrypted_data ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _nonce =reader .read_large_int (bits =128 )
        _server_nonce =reader .read_large_int (bits =128 )
        _encrypted_data =reader .tgread_bytes ()
        return cls (nonce =_nonce ,server_nonce =_server_nonce ,encrypted_data =_encrypted_data )

