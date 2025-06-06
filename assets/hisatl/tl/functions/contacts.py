""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputContact ,TypeInputGeoPoint ,TypeInputPeer ,TypeInputUser ,TypeTopPeerCategory 

class AcceptContactRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf831a20f 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,id :'TypeInputUser'):
        """"""
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_user (await client .get_input_entity (self .id ))

    def to_dict (self ):
        return {
        '_':'AcceptContactRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x0f\xa21\xf8',
        self .id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _id =reader .tgread_object ()
        return cls (id =_id )

class AddContactRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe8f463d0 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,id :'TypeInputUser',first_name :str ,last_name :str ,phone :str ,add_phone_privacy_exception :Optional [bool ]=None ):
        """"""
        self .id =id 
        self .first_name =first_name 
        self .last_name =last_name 
        self .phone =phone 
        self .add_phone_privacy_exception =add_phone_privacy_exception 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_user (await client .get_input_entity (self .id ))

    def to_dict (self ):
        return {
        '_':'AddContactRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'first_name':self .first_name ,
        'last_name':self .last_name ,
        'phone':self .phone ,
        'add_phone_privacy_exception':self .add_phone_privacy_exception 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd0c\xf4\xe8',
        struct .pack ('<I',(0 if self .add_phone_privacy_exception is None or self .add_phone_privacy_exception is False else 1 )),
        self .id ._bytes (),
        self .serialize_bytes (self .first_name ),
        self .serialize_bytes (self .last_name ),
        self .serialize_bytes (self .phone ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _add_phone_privacy_exception =bool (flags &1 )
        _id =reader .tgread_object ()
        _first_name =reader .tgread_string ()
        _last_name =reader .tgread_string ()
        _phone =reader .tgread_string ()
        return cls (id =_id ,first_name =_first_name ,last_name =_last_name ,phone =_phone ,add_phone_privacy_exception =_add_phone_privacy_exception )

class BlockRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2e2e8734 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,id :'TypeInputPeer',my_stories_from :Optional [bool ]=None ):
        """"""
        self .id =id 
        self .my_stories_from =my_stories_from 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_peer (await client .get_input_entity (self .id ))

    def to_dict (self ):
        return {
        '_':'BlockRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'my_stories_from':self .my_stories_from 
        }

    def _bytes (self ):
        return b''.join ((
        b'4\x87..',
        struct .pack ('<I',(0 if self .my_stories_from is None or self .my_stories_from is False else 1 )),
        self .id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _my_stories_from =bool (flags &1 )
        _id =reader .tgread_object ()
        return cls (id =_id ,my_stories_from =_my_stories_from )

class BlockFromRepliesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x29a8962c 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,msg_id :int ,delete_message :Optional [bool ]=None ,delete_history :Optional [bool ]=None ,report_spam :Optional [bool ]=None ):
        """"""
        self .msg_id =msg_id 
        self .delete_message =delete_message 
        self .delete_history =delete_history 
        self .report_spam =report_spam 

    def to_dict (self ):
        return {
        '_':'BlockFromRepliesRequest',
        'msg_id':self .msg_id ,
        'delete_message':self .delete_message ,
        'delete_history':self .delete_history ,
        'report_spam':self .report_spam 
        }

    def _bytes (self ):
        return b''.join ((
        b',\x96\xa8)',
        struct .pack ('<I',(0 if self .delete_message is None or self .delete_message is False else 1 )|(0 if self .delete_history is None or self .delete_history is False else 2 )|(0 if self .report_spam is None or self .report_spam is False else 4 )),
        struct .pack ('<i',self .msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _delete_message =bool (flags &1 )
        _delete_history =bool (flags &2 )
        _report_spam =bool (flags &4 )
        _msg_id =reader .read_int ()
        return cls (msg_id =_msg_id ,delete_message =_delete_message ,delete_history =_delete_history ,report_spam =_report_spam )

class DeleteByPhonesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1013fd9e 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,phones :List [str ]):
        """"""
        self .phones =phones 

    def to_dict (self ):
        return {
        '_':'DeleteByPhonesRequest',
        'phones':[]if self .phones is None else self .phones [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9e\xfd\x13\x10',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .phones )),b''.join (self .serialize_bytes (x )for x in self .phones ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _phones =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _phones .append (_x )

        return cls (phones =_phones )

class DeleteContactsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x96a0e00 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,id :List ['TypeInputUser']):
        """"""
        self .id =id 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_user (await client .get_input_entity (_x )))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'DeleteContactsRequest',
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x00\x0ej\t',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (x ._bytes ()for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _id .append (_x )

        return cls (id =_id )

class EditCloseFriendsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xba6705f0 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,id :List [int ]):
        """"""
        self .id =id 

    def to_dict (self ):
        return {
        '_':'EditCloseFriendsRequest',
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf0\x05g\xba',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<q',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_long ()
            _id .append (_x )

        return cls (id =_id )

class ExportContactTokenRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf8654027 
    SUBCLASS_OF_ID =0x86ddbed1 

    def to_dict (self ):
        return {
        '_':'ExportContactTokenRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b"'@e\xf8",
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetBlockedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9a868f80 
    SUBCLASS_OF_ID =0xffba4f4f 

    def __init__ (self ,offset :int ,limit :int ,my_stories_from :Optional [bool ]=None ):
        """"""
        self .offset =offset 
        self .limit =limit 
        self .my_stories_from =my_stories_from 

    def to_dict (self ):
        return {
        '_':'GetBlockedRequest',
        'offset':self .offset ,
        'limit':self .limit ,
        'my_stories_from':self .my_stories_from 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x80\x8f\x86\x9a',
        struct .pack ('<I',(0 if self .my_stories_from is None or self .my_stories_from is False else 1 )),
        struct .pack ('<i',self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _my_stories_from =bool (flags &1 )
        _offset =reader .read_int ()
        _limit =reader .read_int ()
        return cls (offset =_offset ,limit =_limit ,my_stories_from =_my_stories_from )

class GetContactIDsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7adc669d 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetContactIDsRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9df\xdcz',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

class GetContactsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5dd69e12 
    SUBCLASS_OF_ID =0x38be25f6 

    def __init__ (self ,hash :int ):
        """"""
        self .hash =hash 

    def to_dict (self ):
        return {
        '_':'GetContactsRequest',
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x12\x9e\xd6]',
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        return cls (hash =_hash )

class GetLocatedRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd348bc44 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,geo_point :'TypeInputGeoPoint',background :Optional [bool ]=None ,self_expires :Optional [int ]=None ):
        """"""
        self .geo_point =geo_point 
        self .background =background 
        self .self_expires =self_expires 

    def to_dict (self ):
        return {
        '_':'GetLocatedRequest',
        'geo_point':self .geo_point .to_dict ()if isinstance (self .geo_point ,TLObject )else self .geo_point ,
        'background':self .background ,
        'self_expires':self .self_expires 
        }

    def _bytes (self ):
        return b''.join ((
        b'D\xbcH\xd3',
        struct .pack ('<I',(0 if self .background is None or self .background is False else 2 )|(0 if self .self_expires is None or self .self_expires is False else 1 )),
        self .geo_point ._bytes (),
        b''if self .self_expires is None or self .self_expires is False else (struct .pack ('<i',self .self_expires )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _background =bool (flags &2 )
        _geo_point =reader .tgread_object ()
        if flags &1 :
            _self_expires =reader .read_int ()
        else :
            _self_expires =None 
        return cls (geo_point =_geo_point ,background =_background ,self_expires =_self_expires )

class GetSavedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x82f1e39f 
    SUBCLASS_OF_ID =0x975dbef 

    def to_dict (self ):
        return {
        '_':'GetSavedRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9f\xe3\xf1\x82',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetStatusesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc4a353ee 
    SUBCLASS_OF_ID =0xdf815c90 

    def to_dict (self ):
        return {
        '_':'GetStatusesRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeeS\xa3\xc4',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetTopPeersRequest (TLRequest ):
    CONSTRUCTOR_ID =0x973478b6 
    SUBCLASS_OF_ID =0x9ee8bb88 

    def __init__ (self ,offset :int ,limit :int ,hash :int ,correspondents :Optional [bool ]=None ,bots_pm :Optional [bool ]=None ,bots_inline :Optional [bool ]=None ,phone_calls :Optional [bool ]=None ,forward_users :Optional [bool ]=None ,forward_chats :Optional [bool ]=None ,groups :Optional [bool ]=None ,channels :Optional [bool ]=None ):
        """"""
        self .offset =offset 
        self .limit =limit 
        self .hash =hash 
        self .correspondents =correspondents 
        self .bots_pm =bots_pm 
        self .bots_inline =bots_inline 
        self .phone_calls =phone_calls 
        self .forward_users =forward_users 
        self .forward_chats =forward_chats 
        self .groups =groups 
        self .channels =channels 

    def to_dict (self ):
        return {
        '_':'GetTopPeersRequest',
        'offset':self .offset ,
        'limit':self .limit ,
        'hash':self .hash ,
        'correspondents':self .correspondents ,
        'bots_pm':self .bots_pm ,
        'bots_inline':self .bots_inline ,
        'phone_calls':self .phone_calls ,
        'forward_users':self .forward_users ,
        'forward_chats':self .forward_chats ,
        'groups':self .groups ,
        'channels':self .channels 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb6x4\x97',
        struct .pack ('<I',(0 if self .correspondents is None or self .correspondents is False else 1 )|(0 if self .bots_pm is None or self .bots_pm is False else 2 )|(0 if self .bots_inline is None or self .bots_inline is False else 4 )|(0 if self .phone_calls is None or self .phone_calls is False else 8 )|(0 if self .forward_users is None or self .forward_users is False else 16 )|(0 if self .forward_chats is None or self .forward_chats is False else 32 )|(0 if self .groups is None or self .groups is False else 1024 )|(0 if self .channels is None or self .channels is False else 32768 )),
        struct .pack ('<i',self .offset ),
        struct .pack ('<i',self .limit ),
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _correspondents =bool (flags &1 )
        _bots_pm =bool (flags &2 )
        _bots_inline =bool (flags &4 )
        _phone_calls =bool (flags &8 )
        _forward_users =bool (flags &16 )
        _forward_chats =bool (flags &32 )
        _groups =bool (flags &1024 )
        _channels =bool (flags &32768 )
        _offset =reader .read_int ()
        _limit =reader .read_int ()
        _hash =reader .read_long ()
        return cls (offset =_offset ,limit =_limit ,hash =_hash ,correspondents =_correspondents ,bots_pm =_bots_pm ,bots_inline =_bots_inline ,phone_calls =_phone_calls ,forward_users =_forward_users ,forward_chats =_forward_chats ,groups =_groups ,channels =_channels )

class ImportContactTokenRequest (TLRequest ):
    CONSTRUCTOR_ID =0x13005788 
    SUBCLASS_OF_ID =0x2da17977 

    def __init__ (self ,token :str ):
        """"""
        self .token =token 

    def to_dict (self ):
        return {
        '_':'ImportContactTokenRequest',
        'token':self .token 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x88W\x00\x13',
        self .serialize_bytes (self .token ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _token =reader .tgread_string ()
        return cls (token =_token )

class ImportContactsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2c800be5 
    SUBCLASS_OF_ID =0x8172ad93 

    def __init__ (self ,contacts :List ['TypeInputContact']):
        """"""
        self .contacts =contacts 

    def to_dict (self ):
        return {
        '_':'ImportContactsRequest',
        'contacts':[]if self .contacts is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .contacts ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe5\x0b\x80,',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .contacts )),b''.join (x ._bytes ()for x in self .contacts ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _contacts =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _contacts .append (_x )

        return cls (contacts =_contacts )

class ResetSavedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x879537f1 
    SUBCLASS_OF_ID =0xf5b399ac 

    def to_dict (self ):
        return {
        '_':'ResetSavedRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf17\x95\x87',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ResetTopPeerRatingRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1ae373ac 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,category :'TypeTopPeerCategory',peer :'TypeInputPeer'):
        """"""
        self .category =category 
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ResetTopPeerRatingRequest',
        'category':self .category .to_dict ()if isinstance (self .category ,TLObject )else self .category ,
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xacs\xe3\x1a',
        self .category ._bytes (),
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _category =reader .tgread_object ()
        _peer =reader .tgread_object ()
        return cls (category =_category ,peer =_peer )

class ResolvePhoneRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8af94344 
    SUBCLASS_OF_ID =0xf065b3a8 

    def __init__ (self ,phone :str ):
        """"""
        self .phone =phone 

    def to_dict (self ):
        return {
        '_':'ResolvePhoneRequest',
        'phone':self .phone 
        }

    def _bytes (self ):
        return b''.join ((
        b'DC\xf9\x8a',
        self .serialize_bytes (self .phone ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _phone =reader .tgread_string ()
        return cls (phone =_phone )

class ResolveUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf93ccba3 
    SUBCLASS_OF_ID =0xf065b3a8 

    def __init__ (self ,username :str ):
        """"""
        self .username =username 

    def to_dict (self ):
        return {
        '_':'ResolveUsernameRequest',
        'username':self .username 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa3\xcb<\xf9',
        self .serialize_bytes (self .username ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _username =reader .tgread_string ()
        return cls (username =_username )

class SearchRequest (TLRequest ):
    CONSTRUCTOR_ID =0x11f812d8 
    SUBCLASS_OF_ID =0x4386a2e3 

    def __init__ (self ,q :str ,limit :int ):
        """"""
        self .q =q 
        self .limit =limit 

    def to_dict (self ):
        return {
        '_':'SearchRequest',
        'q':self .q ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd8\x12\xf8\x11',
        self .serialize_bytes (self .q ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _q =reader .tgread_string ()
        _limit =reader .read_int ()
        return cls (q =_q ,limit =_limit )

class SetBlockedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x94c65c76 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,id :List ['TypeInputPeer'],limit :int ,my_stories_from :Optional [bool ]=None ):
        """"""
        self .id =id 
        self .limit =limit 
        self .my_stories_from =my_stories_from 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'SetBlockedRequest',
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ],
        'limit':self .limit ,
        'my_stories_from':self .my_stories_from 
        }

    def _bytes (self ):
        return b''.join ((
        b'v\\\xc6\x94',
        struct .pack ('<I',(0 if self .my_stories_from is None or self .my_stories_from is False else 1 )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (x ._bytes ()for x in self .id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _my_stories_from =bool (flags &1 )
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _id .append (_x )

        _limit =reader .read_int ()
        return cls (id =_id ,limit =_limit ,my_stories_from =_my_stories_from )

class ToggleTopPeersRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8514bdda 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,enabled :bool ):
        """"""
        self .enabled =enabled 

    def to_dict (self ):
        return {
        '_':'ToggleTopPeersRequest',
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xda\xbd\x14\x85',
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _enabled =reader .tgread_bool ()
        return cls (enabled =_enabled )

class UnblockRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb550d328 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,id :'TypeInputPeer',my_stories_from :Optional [bool ]=None ):
        """"""
        self .id =id 
        self .my_stories_from =my_stories_from 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_peer (await client .get_input_entity (self .id ))

    def to_dict (self ):
        return {
        '_':'UnblockRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'my_stories_from':self .my_stories_from 
        }

    def _bytes (self ):
        return b''.join ((
        b'(\xd3P\xb5',
        struct .pack ('<I',(0 if self .my_stories_from is None or self .my_stories_from is False else 1 )),
        self .id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _my_stories_from =bool (flags &1 )
        _id =reader .tgread_object ()
        return cls (id =_id ,my_stories_from =_my_stories_from )

