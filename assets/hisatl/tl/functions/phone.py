""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeDataJSON ,TypeInputFile ,TypeInputGroupCall ,TypeInputPeer ,TypeInputPhoneCall ,TypeInputUser ,TypePhoneCallDiscardReason ,TypePhoneCallProtocol 

class AcceptCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3bd2b4a0 
    SUBCLASS_OF_ID =0xd48afe4f 

    def __init__ (self ,peer :'TypeInputPhoneCall',g_b :bytes ,protocol :'TypePhoneCallProtocol'):
        """"""
        self .peer =peer 
        self .g_b =g_b 
        self .protocol =protocol 

    def to_dict (self ):
        return {
        '_':'AcceptCallRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'g_b':self .g_b ,
        'protocol':self .protocol .to_dict ()if isinstance (self .protocol ,TLObject )else self .protocol 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0\xb4\xd2;',
        self .peer ._bytes (),
        self .serialize_bytes (self .g_b ),
        self .protocol ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _g_b =reader .tgread_bytes ()
        _protocol =reader .tgread_object ()
        return cls (peer =_peer ,g_b =_g_b ,protocol =_protocol )

class CheckGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb59cf977 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,call :'TypeInputGroupCall',sources :List [int ]):
        """"""
        self .call =call 
        self .sources =sources 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'CheckGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'sources':[]if self .sources is None else self .sources [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'w\xf9\x9c\xb5',
        self .call ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sources )),b''.join (struct .pack ('<i',x )for x in self .sources ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        reader .read_int ()
        _sources =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _sources .append (_x )

        return cls (call =_call ,sources =_sources )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

class ConfirmCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2efe1722 
    SUBCLASS_OF_ID =0xd48afe4f 

    def __init__ (self ,peer :'TypeInputPhoneCall',g_a :bytes ,key_fingerprint :int ,protocol :'TypePhoneCallProtocol'):
        """"""
        self .peer =peer 
        self .g_a =g_a 
        self .key_fingerprint =key_fingerprint 
        self .protocol =protocol 

    def to_dict (self ):
        return {
        '_':'ConfirmCallRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'g_a':self .g_a ,
        'key_fingerprint':self .key_fingerprint ,
        'protocol':self .protocol .to_dict ()if isinstance (self .protocol ,TLObject )else self .protocol 
        }

    def _bytes (self ):
        return b''.join ((
        b'"\x17\xfe.',
        self .peer ._bytes (),
        self .serialize_bytes (self .g_a ),
        struct .pack ('<q',self .key_fingerprint ),
        self .protocol ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _g_a =reader .tgread_bytes ()
        _key_fingerprint =reader .read_long ()
        _protocol =reader .tgread_object ()
        return cls (peer =_peer ,g_a =_g_a ,key_fingerprint =_key_fingerprint ,protocol =_protocol )

class CreateGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x48cdc6d8 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPeer',rtmp_stream :Optional [bool ]=None ,random_id :int =None ,title :Optional [str ]=None ,schedule_date :Optional [datetime ]=None ):
        """"""
        self .peer =peer 
        self .rtmp_stream =rtmp_stream 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (4 ),'big',signed =True )
        self .title =title 
        self .schedule_date =schedule_date 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'CreateGroupCallRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'rtmp_stream':self .rtmp_stream ,
        'random_id':self .random_id ,
        'title':self .title ,
        'schedule_date':self .schedule_date 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd8\xc6\xcdH',
        struct .pack ('<I',(0 if self .rtmp_stream is None or self .rtmp_stream is False else 4 )|(0 if self .title is None or self .title is False else 1 )|(0 if self .schedule_date is None or self .schedule_date is False else 2 )),
        self .peer ._bytes (),
        struct .pack ('<i',self .random_id ),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        b''if self .schedule_date is None or self .schedule_date is False else (self .serialize_datetime (self .schedule_date )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _rtmp_stream =bool (flags &4 )
        _peer =reader .tgread_object ()
        _random_id =reader .read_int ()
        if flags &1 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        if flags &2 :
            _schedule_date =reader .tgread_date ()
        else :
            _schedule_date =None 
        return cls (peer =_peer ,rtmp_stream =_rtmp_stream ,random_id =_random_id ,title =_title ,schedule_date =_schedule_date )

class DiscardCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb2cbc1c0 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPhoneCall',duration :int ,reason :'TypePhoneCallDiscardReason',connection_id :int ,video :Optional [bool ]=None ):
        """"""
        self .peer =peer 
        self .duration =duration 
        self .reason =reason 
        self .connection_id =connection_id 
        self .video =video 

    def to_dict (self ):
        return {
        '_':'DiscardCallRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'duration':self .duration ,
        'reason':self .reason .to_dict ()if isinstance (self .reason ,TLObject )else self .reason ,
        'connection_id':self .connection_id ,
        'video':self .video 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc0\xc1\xcb\xb2',
        struct .pack ('<I',(0 if self .video is None or self .video is False else 1 )),
        self .peer ._bytes (),
        struct .pack ('<i',self .duration ),
        self .reason ._bytes (),
        struct .pack ('<q',self .connection_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _video =bool (flags &1 )
        _peer =reader .tgread_object ()
        _duration =reader .read_int ()
        _reason =reader .tgread_object ()
        _connection_id =reader .read_long ()
        return cls (peer =_peer ,duration =_duration ,reason =_reason ,connection_id =_connection_id ,video =_video )

class DiscardGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7a777135 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall'):
        """"""
        self .call =call 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'DiscardGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call 
        }

    def _bytes (self ):
        return b''.join ((
        b'5qwz',
        self .call ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        return cls (call =_call )

class EditGroupCallParticipantRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa5273abf 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',participant :'TypeInputPeer',muted :Optional [bool ]=None ,volume :Optional [int ]=None ,raise_hand :Optional [bool ]=None ,video_stopped :Optional [bool ]=None ,video_paused :Optional [bool ]=None ,presentation_paused :Optional [bool ]=None ):
        """"""
        self .call =call 
        self .participant =participant 
        self .muted =muted 
        self .volume =volume 
        self .raise_hand =raise_hand 
        self .video_stopped =video_stopped 
        self .video_paused =video_paused 
        self .presentation_paused =presentation_paused 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )
        self .participant =utils .get_input_peer (await client .get_input_entity (self .participant ))

    def to_dict (self ):
        return {
        '_':'EditGroupCallParticipantRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant ,
        'muted':self .muted ,
        'volume':self .volume ,
        'raise_hand':self .raise_hand ,
        'video_stopped':self .video_stopped ,
        'video_paused':self .video_paused ,
        'presentation_paused':self .presentation_paused 
        }

    def _bytes (self ):
        return b''.join ((
        b"\xbf:'\xa5",
        struct .pack ('<I',(0 if self .muted is None else 1 )|(0 if self .volume is None or self .volume is False else 2 )|(0 if self .raise_hand is None else 4 )|(0 if self .video_stopped is None else 8 )|(0 if self .video_paused is None else 16 )|(0 if self .presentation_paused is None else 32 )),
        self .call ._bytes (),
        self .participant ._bytes (),
        b''if self .muted is None else (b'\xb5ur\x99'if self .muted else b'7\x97y\xbc'),
        b''if self .volume is None or self .volume is False else (struct .pack ('<i',self .volume )),
        b''if self .raise_hand is None else (b'\xb5ur\x99'if self .raise_hand else b'7\x97y\xbc'),
        b''if self .video_stopped is None else (b'\xb5ur\x99'if self .video_stopped else b'7\x97y\xbc'),
        b''if self .video_paused is None else (b'\xb5ur\x99'if self .video_paused else b'7\x97y\xbc'),
        b''if self .presentation_paused is None else (b'\xb5ur\x99'if self .presentation_paused else b'7\x97y\xbc'),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _call =reader .tgread_object ()
        _participant =reader .tgread_object ()
        if flags &1 :
            _muted =reader .tgread_bool ()
        else :
            _muted =None 
        if flags &2 :
            _volume =reader .read_int ()
        else :
            _volume =None 
        if flags &4 :
            _raise_hand =reader .tgread_bool ()
        else :
            _raise_hand =None 
        if flags &8 :
            _video_stopped =reader .tgread_bool ()
        else :
            _video_stopped =None 
        if flags &16 :
            _video_paused =reader .tgread_bool ()
        else :
            _video_paused =None 
        if flags &32 :
            _presentation_paused =reader .tgread_bool ()
        else :
            _presentation_paused =None 
        return cls (call =_call ,participant =_participant ,muted =_muted ,volume =_volume ,raise_hand =_raise_hand ,video_stopped =_video_stopped ,video_paused =_video_paused ,presentation_paused =_presentation_paused )

class EditGroupCallTitleRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1ca6ac0a 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',title :str ):
        """"""
        self .call =call 
        self .title =title 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'EditGroupCallTitleRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'title':self .title 
        }

    def _bytes (self ):
        return b''.join ((
        b'\n\xac\xa6\x1c',
        self .call ._bytes (),
        self .serialize_bytes (self .title ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        _title =reader .tgread_string ()
        return cls (call =_call ,title =_title )

class ExportGroupCallInviteRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe6aa647f 
    SUBCLASS_OF_ID =0x3b3bfe8f 

    def __init__ (self ,call :'TypeInputGroupCall',can_self_unmute :Optional [bool ]=None ):
        """"""
        self .call =call 
        self .can_self_unmute =can_self_unmute 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'ExportGroupCallInviteRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'can_self_unmute':self .can_self_unmute 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x7fd\xaa\xe6',
        struct .pack ('<I',(0 if self .can_self_unmute is None or self .can_self_unmute is False else 1 )),
        self .call ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _can_self_unmute =bool (flags &1 )
        _call =reader .tgread_object ()
        return cls (call =_call ,can_self_unmute =_can_self_unmute )

class GetCallConfigRequest (TLRequest ):
    CONSTRUCTOR_ID =0x55451fa9 
    SUBCLASS_OF_ID =0xad0352e8 

    def to_dict (self ):
        return {
        '_':'GetCallConfigRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa9\x1fEU',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x41845db 
    SUBCLASS_OF_ID =0x304116be 

    def __init__ (self ,call :'TypeInputGroupCall',limit :int ):
        """"""
        self .call =call 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'GetGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdbE\x18\x04',
        self .call ._bytes (),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        _limit =reader .read_int ()
        return cls (call =_call ,limit =_limit )

class GetGroupCallJoinAsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xef7c213a 
    SUBCLASS_OF_ID =0xb4b770fb 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetGroupCallJoinAsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b':!|\xef',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class GetGroupCallStreamChannelsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1ab21940 
    SUBCLASS_OF_ID =0x9157c5e4 

    def __init__ (self ,call :'TypeInputGroupCall'):
        """"""
        self .call =call 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'GetGroupCallStreamChannelsRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call 
        }

    def _bytes (self ):
        return b''.join ((
        b'@\x19\xb2\x1a',
        self .call ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        return cls (call =_call )

class GetGroupCallStreamRtmpUrlRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdeb3abbf 
    SUBCLASS_OF_ID =0xd1f515cb 

    def __init__ (self ,peer :'TypeInputPeer',revoke :bool ):
        """"""
        self .peer =peer 
        self .revoke =revoke 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetGroupCallStreamRtmpUrlRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'revoke':self .revoke 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbf\xab\xb3\xde',
        self .peer ._bytes (),
        b'\xb5ur\x99'if self .revoke else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _revoke =reader .tgread_bool ()
        return cls (peer =_peer ,revoke =_revoke )

class GetGroupParticipantsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc558d8ab 
    SUBCLASS_OF_ID =0x72d304f4 

    def __init__ (self ,call :'TypeInputGroupCall',ids :List ['TypeInputPeer'],sources :List [int ],offset :str ,limit :int ):
        """"""
        self .call =call 
        self .ids =ids 
        self .sources =sources 
        self .offset =offset 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )
        _tmp =[]
        for _x in self .ids :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .ids =_tmp 

    def to_dict (self ):
        return {
        '_':'GetGroupParticipantsRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'ids':[]if self .ids is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .ids ],
        'sources':[]if self .sources is None else self .sources [:],
        'offset':self .offset ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xab\xd8X\xc5',
        self .call ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .ids )),b''.join (x ._bytes ()for x in self .ids ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sources )),b''.join (struct .pack ('<i',x )for x in self .sources ),
        self .serialize_bytes (self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        reader .read_int ()
        _ids =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _ids .append (_x )

        reader .read_int ()
        _sources =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _sources .append (_x )

        _offset =reader .tgread_string ()
        _limit =reader .read_int ()
        return cls (call =_call ,ids =_ids ,sources =_sources ,offset =_offset ,limit =_limit )

class InviteToGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7b393160 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',users :List ['TypeInputUser']):
        """"""
        self .call =call 
        self .users =users 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )
        _tmp =[]
        for _x in self .users :
            _tmp .append (utils .get_input_user (await client .get_input_entity (_x )))

        self .users =_tmp 

    def to_dict (self ):
        return {
        '_':'InviteToGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'`19{',
        self .call ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (call =_call ,users =_users )

class JoinGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb132ff7b 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',join_as :'TypeInputPeer',params :'TypeDataJSON',muted :Optional [bool ]=None ,video_stopped :Optional [bool ]=None ,invite_hash :Optional [str ]=None ):
        """"""
        self .call =call 
        self .join_as =join_as 
        self .params =params 
        self .muted =muted 
        self .video_stopped =video_stopped 
        self .invite_hash =invite_hash 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )
        self .join_as =utils .get_input_peer (await client .get_input_entity (self .join_as ))

    def to_dict (self ):
        return {
        '_':'JoinGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'join_as':self .join_as .to_dict ()if isinstance (self .join_as ,TLObject )else self .join_as ,
        'params':self .params .to_dict ()if isinstance (self .params ,TLObject )else self .params ,
        'muted':self .muted ,
        'video_stopped':self .video_stopped ,
        'invite_hash':self .invite_hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'{\xff2\xb1',
        struct .pack ('<I',(0 if self .muted is None or self .muted is False else 1 )|(0 if self .video_stopped is None or self .video_stopped is False else 4 )|(0 if self .invite_hash is None or self .invite_hash is False else 2 )),
        self .call ._bytes (),
        self .join_as ._bytes (),
        b''if self .invite_hash is None or self .invite_hash is False else (self .serialize_bytes (self .invite_hash )),
        self .params ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _muted =bool (flags &1 )
        _video_stopped =bool (flags &4 )
        _call =reader .tgread_object ()
        _join_as =reader .tgread_object ()
        if flags &2 :
            _invite_hash =reader .tgread_string ()
        else :
            _invite_hash =None 
        _params =reader .tgread_object ()
        return cls (call =_call ,join_as =_join_as ,params =_params ,muted =_muted ,video_stopped =_video_stopped ,invite_hash =_invite_hash )

class JoinGroupCallPresentationRequest (TLRequest ):
    CONSTRUCTOR_ID =0xcbea6bc4 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',params :'TypeDataJSON'):
        """"""
        self .call =call 
        self .params =params 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'JoinGroupCallPresentationRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'params':self .params .to_dict ()if isinstance (self .params ,TLObject )else self .params 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc4k\xea\xcb',
        self .call ._bytes (),
        self .params ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        _params =reader .tgread_object ()
        return cls (call =_call ,params =_params )

class LeaveGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x500377f9 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',source :int ):
        """"""
        self .call =call 
        self .source =source 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'LeaveGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'source':self .source 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9w\x03P',
        self .call ._bytes (),
        struct .pack ('<i',self .source ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        _source =reader .read_int ()
        return cls (call =_call ,source =_source )

class LeaveGroupCallPresentationRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1c50d144 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall'):
        """"""
        self .call =call 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'LeaveGroupCallPresentationRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call 
        }

    def _bytes (self ):
        return b''.join ((
        b'D\xd1P\x1c',
        self .call ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        return cls (call =_call )

class ReceivedCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x17d54f61 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPhoneCall'):
        """"""
        self .peer =peer 

    def to_dict (self ):
        return {
        '_':'ReceivedCallRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'aO\xd5\x17',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class RequestCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x42ff96ed 
    SUBCLASS_OF_ID =0xd48afe4f 

    def __init__ (self ,user_id :'TypeInputUser',g_a_hash :bytes ,protocol :'TypePhoneCallProtocol',video :Optional [bool ]=None ,random_id :int =None ):
        """"""
        self .user_id =user_id 
        self .g_a_hash =g_a_hash 
        self .protocol =protocol 
        self .video =video 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (4 ),'big',signed =True )

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'RequestCallRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'g_a_hash':self .g_a_hash ,
        'protocol':self .protocol .to_dict ()if isinstance (self .protocol ,TLObject )else self .protocol ,
        'video':self .video ,
        'random_id':self .random_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xed\x96\xffB',
        struct .pack ('<I',(0 if self .video is None or self .video is False else 1 )),
        self .user_id ._bytes (),
        struct .pack ('<i',self .random_id ),
        self .serialize_bytes (self .g_a_hash ),
        self .protocol ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _video =bool (flags &1 )
        _user_id =reader .tgread_object ()
        _random_id =reader .read_int ()
        _g_a_hash =reader .tgread_bytes ()
        _protocol =reader .tgread_object ()
        return cls (user_id =_user_id ,g_a_hash =_g_a_hash ,protocol =_protocol ,video =_video ,random_id =_random_id )

class SaveCallDebugRequest (TLRequest ):
    CONSTRUCTOR_ID =0x277add7e 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPhoneCall',debug :'TypeDataJSON'):
        """"""
        self .peer =peer 
        self .debug =debug 

    def to_dict (self ):
        return {
        '_':'SaveCallDebugRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'debug':self .debug .to_dict ()if isinstance (self .debug ,TLObject )else self .debug 
        }

    def _bytes (self ):
        return b''.join ((
        b"~\xddz'",
        self .peer ._bytes (),
        self .debug ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _debug =reader .tgread_object ()
        return cls (peer =_peer ,debug =_debug )

class SaveCallLogRequest (TLRequest ):
    CONSTRUCTOR_ID =0x41248786 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPhoneCall',file :'TypeInputFile'):
        """"""
        self .peer =peer 
        self .file =file 

    def to_dict (self ):
        return {
        '_':'SaveCallLogRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x86\x87$A',
        self .peer ._bytes (),
        self .file ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _file =reader .tgread_object ()
        return cls (peer =_peer ,file =_file )

class SaveDefaultGroupCallJoinAsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x575e1f8c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',join_as :'TypeInputPeer'):
        """"""
        self .peer =peer 
        self .join_as =join_as 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))
        self .join_as =utils .get_input_peer (await client .get_input_entity (self .join_as ))

    def to_dict (self ):
        return {
        '_':'SaveDefaultGroupCallJoinAsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'join_as':self .join_as .to_dict ()if isinstance (self .join_as ,TLObject )else self .join_as 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8c\x1f^W',
        self .peer ._bytes (),
        self .join_as ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _join_as =reader .tgread_object ()
        return cls (peer =_peer ,join_as =_join_as )

class SendSignalingDataRequest (TLRequest ):
    CONSTRUCTOR_ID =0xff7a9383 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPhoneCall',data :bytes ):
        """"""
        self .peer =peer 
        self .data =data 

    def to_dict (self ):
        return {
        '_':'SendSignalingDataRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'data':self .data 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x83\x93z\xff',
        self .peer ._bytes (),
        self .serialize_bytes (self .data ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _data =reader .tgread_bytes ()
        return cls (peer =_peer ,data =_data )

class SetCallRatingRequest (TLRequest ):
    CONSTRUCTOR_ID =0x59ead627 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPhoneCall',rating :int ,comment :str ,user_initiative :Optional [bool ]=None ):
        """"""
        self .peer =peer 
        self .rating =rating 
        self .comment =comment 
        self .user_initiative =user_initiative 

    def to_dict (self ):
        return {
        '_':'SetCallRatingRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'rating':self .rating ,
        'comment':self .comment ,
        'user_initiative':self .user_initiative 
        }

    def _bytes (self ):
        return b''.join ((
        b"'\xd6\xeaY",
        struct .pack ('<I',(0 if self .user_initiative is None or self .user_initiative is False else 1 )),
        self .peer ._bytes (),
        struct .pack ('<i',self .rating ),
        self .serialize_bytes (self .comment ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _user_initiative =bool (flags &1 )
        _peer =reader .tgread_object ()
        _rating =reader .read_int ()
        _comment =reader .tgread_string ()
        return cls (peer =_peer ,rating =_rating ,comment =_comment ,user_initiative =_user_initiative )

class StartScheduledGroupCallRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5680e342 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall'):
        """"""
        self .call =call 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'StartScheduledGroupCallRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call 
        }

    def _bytes (self ):
        return b''.join ((
        b'B\xe3\x80V',
        self .call ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        return cls (call =_call )

class ToggleGroupCallRecordRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf128c708 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',start :Optional [bool ]=None ,video :Optional [bool ]=None ,title :Optional [str ]=None ,video_portrait :Optional [bool ]=None ):
        """"""
        self .call =call 
        self .start =start 
        self .video =video 
        self .title =title 
        self .video_portrait =video_portrait 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'ToggleGroupCallRecordRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'start':self .start ,
        'video':self .video ,
        'title':self .title ,
        'video_portrait':self .video_portrait 
        }

    def _bytes (self ):
        assert ((self .video or self .video is not None )and (self .video_portrait or self .video_portrait is not None ))or ((self .video is None or self .video is False )and (self .video_portrait is None or self .video_portrait is False )),'video, video_portrait parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'\x08\xc7(\xf1',
        struct .pack ('<I',(0 if self .start is None or self .start is False else 1 )|(0 if self .video is None or self .video is False else 4 )|(0 if self .title is None or self .title is False else 2 )|(0 if self .video_portrait is None else 4 )),
        self .call ._bytes (),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        b''if self .video_portrait is None else (b'\xb5ur\x99'if self .video_portrait else b'7\x97y\xbc'),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _start =bool (flags &1 )
        _video =bool (flags &4 )
        _call =reader .tgread_object ()
        if flags &2 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        if flags &4 :
            _video_portrait =reader .tgread_bool ()
        else :
            _video_portrait =None 
        return cls (call =_call ,start =_start ,video =_video ,title =_title ,video_portrait =_video_portrait )

class ToggleGroupCallSettingsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x74bbb43d 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',reset_invite_hash :Optional [bool ]=None ,join_muted :Optional [bool ]=None ):
        """"""
        self .call =call 
        self .reset_invite_hash =reset_invite_hash 
        self .join_muted =join_muted 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'ToggleGroupCallSettingsRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'reset_invite_hash':self .reset_invite_hash ,
        'join_muted':self .join_muted 
        }

    def _bytes (self ):
        return b''.join ((
        b'=\xb4\xbbt',
        struct .pack ('<I',(0 if self .reset_invite_hash is None or self .reset_invite_hash is False else 2 )|(0 if self .join_muted is None else 1 )),
        self .call ._bytes (),
        b''if self .join_muted is None else (b'\xb5ur\x99'if self .join_muted else b'7\x97y\xbc'),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _reset_invite_hash =bool (flags &2 )
        _call =reader .tgread_object ()
        if flags &1 :
            _join_muted =reader .tgread_bool ()
        else :
            _join_muted =None 
        return cls (call =_call ,reset_invite_hash =_reset_invite_hash ,join_muted =_join_muted )

class ToggleGroupCallStartSubscriptionRequest (TLRequest ):
    CONSTRUCTOR_ID =0x219c34e6 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,call :'TypeInputGroupCall',subscribed :bool ):
        """"""
        self .call =call 
        self .subscribed =subscribed 

    async def resolve (self ,client ,utils ):
        self .call =utils .get_input_group_call (self .call )

    def to_dict (self ):
        return {
        '_':'ToggleGroupCallStartSubscriptionRequest',
        'call':self .call .to_dict ()if isinstance (self .call ,TLObject )else self .call ,
        'subscribed':self .subscribed 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe64\x9c!',
        self .call ._bytes (),
        b'\xb5ur\x99'if self .subscribed else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _call =reader .tgread_object ()
        _subscribed =reader .tgread_bool ()
        return cls (call =_call ,subscribed =_subscribed )

