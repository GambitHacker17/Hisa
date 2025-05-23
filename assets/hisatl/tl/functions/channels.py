""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChannelAdminLogEventsFilter ,TypeChannelParticipantsFilter ,TypeChatAdminRights ,TypeChatBannedRights ,TypeInputChannel ,TypeInputChatPhoto ,TypeInputCheckPasswordSRP ,TypeInputGeoPoint ,TypeInputMessage ,TypeInputPeer ,TypeInputStickerSet ,TypeInputUser 

class CheckUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x10e6bd2c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',username :str ):
        """"""
        self .channel =channel 
        self .username =username 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'CheckUsernameRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'username':self .username 
        }

    def _bytes (self ):
        return b''.join ((
        b',\xbd\xe6\x10',
        self .channel ._bytes (),
        self .serialize_bytes (self .username ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _username =reader .tgread_string ()
        return cls (channel =_channel ,username =_username )

class ClickSponsoredMessageRequest (TLRequest ):
    CONSTRUCTOR_ID =0x18afbc93 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',random_id :bytes =None ):
        """"""
        self .channel =channel 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (4 ),'big',signed =True )

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ClickSponsoredMessageRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'random_id':self .random_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x93\xbc\xaf\x18',
        self .channel ._bytes (),
        self .serialize_bytes (self .random_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _random_id =reader .tgread_bytes ()
        return cls (channel =_channel ,random_id =_random_id )

class ConvertToGigagroupRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb290c69 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ConvertToGigagroupRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'i\x0c)\x0b',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class CreateChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0x91006707 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,title :str ,about :str ,broadcast :Optional [bool ]=None ,megagroup :Optional [bool ]=None ,for_import :Optional [bool ]=None ,forum :Optional [bool ]=None ,geo_point :Optional ['TypeInputGeoPoint']=None ,address :Optional [str ]=None ,ttl_period :Optional [int ]=None ):
        """"""
        self .title =title 
        self .about =about 
        self .broadcast =broadcast 
        self .megagroup =megagroup 
        self .for_import =for_import 
        self .forum =forum 
        self .geo_point =geo_point 
        self .address =address 
        self .ttl_period =ttl_period 

    def to_dict (self ):
        return {
        '_':'CreateChannelRequest',
        'title':self .title ,
        'about':self .about ,
        'broadcast':self .broadcast ,
        'megagroup':self .megagroup ,
        'for_import':self .for_import ,
        'forum':self .forum ,
        'geo_point':self .geo_point .to_dict ()if isinstance (self .geo_point ,TLObject )else self .geo_point ,
        'address':self .address ,
        'ttl_period':self .ttl_period 
        }

    def _bytes (self ):
        assert ((self .geo_point or self .geo_point is not None )and (self .address or self .address is not None ))or ((self .geo_point is None or self .geo_point is False )and (self .address is None or self .address is False )),'geo_point, address parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'\x07g\x00\x91',
        struct .pack ('<I',(0 if self .broadcast is None or self .broadcast is False else 1 )|(0 if self .megagroup is None or self .megagroup is False else 2 )|(0 if self .for_import is None or self .for_import is False else 8 )|(0 if self .forum is None or self .forum is False else 32 )|(0 if self .geo_point is None or self .geo_point is False else 4 )|(0 if self .address is None or self .address is False else 4 )|(0 if self .ttl_period is None or self .ttl_period is False else 16 )),
        self .serialize_bytes (self .title ),
        self .serialize_bytes (self .about ),
        b''if self .geo_point is None or self .geo_point is False else (self .geo_point ._bytes ()),
        b''if self .address is None or self .address is False else (self .serialize_bytes (self .address )),
        b''if self .ttl_period is None or self .ttl_period is False else (struct .pack ('<i',self .ttl_period )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _broadcast =bool (flags &1 )
        _megagroup =bool (flags &2 )
        _for_import =bool (flags &8 )
        _forum =bool (flags &32 )
        _title =reader .tgread_string ()
        _about =reader .tgread_string ()
        if flags &4 :
            _geo_point =reader .tgread_object ()
        else :
            _geo_point =None 
        if flags &4 :
            _address =reader .tgread_string ()
        else :
            _address =None 
        if flags &16 :
            _ttl_period =reader .read_int ()
        else :
            _ttl_period =None 
        return cls (title =_title ,about =_about ,broadcast =_broadcast ,megagroup =_megagroup ,for_import =_for_import ,forum =_forum ,geo_point =_geo_point ,address =_address ,ttl_period =_ttl_period )

class CreateForumTopicRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf40c0224 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',title :str ,icon_color :Optional [int ]=None ,icon_emoji_id :Optional [int ]=None ,random_id :int =None ,send_as :Optional ['TypeInputPeer']=None ):
        """"""
        self .channel =channel 
        self .title =title 
        self .icon_color =icon_color 
        self .icon_emoji_id =icon_emoji_id 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (8 ),'big',signed =True )
        self .send_as =send_as 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        if self .send_as :
            self .send_as =utils .get_input_peer (await client .get_input_entity (self .send_as ))

    def to_dict (self ):
        return {
        '_':'CreateForumTopicRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'title':self .title ,
        'icon_color':self .icon_color ,
        'icon_emoji_id':self .icon_emoji_id ,
        'random_id':self .random_id ,
        'send_as':self .send_as .to_dict ()if isinstance (self .send_as ,TLObject )else self .send_as 
        }

    def _bytes (self ):
        return b''.join ((
        b'$\x02\x0c\xf4',
        struct .pack ('<I',(0 if self .icon_color is None or self .icon_color is False else 1 )|(0 if self .icon_emoji_id is None or self .icon_emoji_id is False else 8 )|(0 if self .send_as is None or self .send_as is False else 4 )),
        self .channel ._bytes (),
        self .serialize_bytes (self .title ),
        b''if self .icon_color is None or self .icon_color is False else (struct .pack ('<i',self .icon_color )),
        b''if self .icon_emoji_id is None or self .icon_emoji_id is False else (struct .pack ('<q',self .icon_emoji_id )),
        struct .pack ('<q',self .random_id ),
        b''if self .send_as is None or self .send_as is False else (self .send_as ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _channel =reader .tgread_object ()
        _title =reader .tgread_string ()
        if flags &1 :
            _icon_color =reader .read_int ()
        else :
            _icon_color =None 
        if flags &8 :
            _icon_emoji_id =reader .read_long ()
        else :
            _icon_emoji_id =None 
        _random_id =reader .read_long ()
        if flags &4 :
            _send_as =reader .tgread_object ()
        else :
            _send_as =None 
        return cls (channel =_channel ,title =_title ,icon_color =_icon_color ,icon_emoji_id =_icon_emoji_id ,random_id =_random_id ,send_as =_send_as )

class DeactivateAllUsernamesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa245dd3 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'DeactivateAllUsernamesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd3]$\n',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class DeleteChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc0111fe3 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'DeleteChannelRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe3\x1f\x11\xc0',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class DeleteHistoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9baa9647 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',max_id :int ,for_everyone :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .max_id =max_id 
        self .for_everyone =for_everyone 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'DeleteHistoryRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'max_id':self .max_id ,
        'for_everyone':self .for_everyone 
        }

    def _bytes (self ):
        return b''.join ((
        b'G\x96\xaa\x9b',
        struct .pack ('<I',(0 if self .for_everyone is None or self .for_everyone is False else 1 )),
        self .channel ._bytes (),
        struct .pack ('<i',self .max_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _for_everyone =bool (flags &1 )
        _channel =reader .tgread_object ()
        _max_id =reader .read_int ()
        return cls (channel =_channel ,max_id =_max_id ,for_everyone =_for_everyone )

class DeleteMessagesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x84c1fd4e 
    SUBCLASS_OF_ID =0xced3c06e 

    def __init__ (self ,channel :'TypeInputChannel',id :List [int ]):
        """"""
        self .channel =channel 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'DeleteMessagesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'N\xfd\xc1\x84',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (channel =_channel ,id =_id )

class DeleteParticipantHistoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0x367544db 
    SUBCLASS_OF_ID =0x2c49c116 

    def __init__ (self ,channel :'TypeInputChannel',participant :'TypeInputPeer'):
        """"""
        self .channel =channel 
        self .participant =participant 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .participant =utils .get_input_peer (await client .get_input_entity (self .participant ))

    def to_dict (self ):
        return {
        '_':'DeleteParticipantHistoryRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdbDu6',
        self .channel ._bytes (),
        self .participant ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _participant =reader .tgread_object ()
        return cls (channel =_channel ,participant =_participant )

class DeleteTopicHistoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0x34435f2d 
    SUBCLASS_OF_ID =0x2c49c116 

    def __init__ (self ,channel :'TypeInputChannel',top_msg_id :int ):
        """"""
        self .channel =channel 
        self .top_msg_id =top_msg_id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'DeleteTopicHistoryRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'top_msg_id':self .top_msg_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'-_C4',
        self .channel ._bytes (),
        struct .pack ('<i',self .top_msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _top_msg_id =reader .read_int ()
        return cls (channel =_channel ,top_msg_id =_top_msg_id )

class EditAdminRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd33c8902 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',user_id :'TypeInputUser',admin_rights :'TypeChatAdminRights',rank :str ):
        """"""
        self .channel =channel 
        self .user_id =user_id 
        self .admin_rights =admin_rights 
        self .rank =rank 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'EditAdminRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'admin_rights':self .admin_rights .to_dict ()if isinstance (self .admin_rights ,TLObject )else self .admin_rights ,
        'rank':self .rank 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x02\x89<\xd3',
        self .channel ._bytes (),
        self .user_id ._bytes (),
        self .admin_rights ._bytes (),
        self .serialize_bytes (self .rank ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _user_id =reader .tgread_object ()
        _admin_rights =reader .tgread_object ()
        _rank =reader .tgread_string ()
        return cls (channel =_channel ,user_id =_user_id ,admin_rights =_admin_rights ,rank =_rank )

class EditBannedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x96e6cd81 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',participant :'TypeInputPeer',banned_rights :'TypeChatBannedRights'):
        """"""
        self .channel =channel 
        self .participant =participant 
        self .banned_rights =banned_rights 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .participant =utils .get_input_peer (await client .get_input_entity (self .participant ))

    def to_dict (self ):
        return {
        '_':'EditBannedRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant ,
        'banned_rights':self .banned_rights .to_dict ()if isinstance (self .banned_rights ,TLObject )else self .banned_rights 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x81\xcd\xe6\x96',
        self .channel ._bytes (),
        self .participant ._bytes (),
        self .banned_rights ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _participant =reader .tgread_object ()
        _banned_rights =reader .tgread_object ()
        return cls (channel =_channel ,participant =_participant ,banned_rights =_banned_rights )

class EditCreatorRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8f38cd1f 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',user_id :'TypeInputUser',password :'TypeInputCheckPasswordSRP'):
        """"""
        self .channel =channel 
        self .user_id =user_id 
        self .password =password 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'EditCreatorRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'password':self .password .to_dict ()if isinstance (self .password ,TLObject )else self .password 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1f\xcd8\x8f',
        self .channel ._bytes (),
        self .user_id ._bytes (),
        self .password ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _user_id =reader .tgread_object ()
        _password =reader .tgread_object ()
        return cls (channel =_channel ,user_id =_user_id ,password =_password )

class EditForumTopicRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf4dfa185 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',topic_id :int ,title :Optional [str ]=None ,icon_emoji_id :Optional [int ]=None ,closed :Optional [bool ]=None ,hidden :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .topic_id =topic_id 
        self .title =title 
        self .icon_emoji_id =icon_emoji_id 
        self .closed =closed 
        self .hidden =hidden 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'EditForumTopicRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'topic_id':self .topic_id ,
        'title':self .title ,
        'icon_emoji_id':self .icon_emoji_id ,
        'closed':self .closed ,
        'hidden':self .hidden 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x85\xa1\xdf\xf4',
        struct .pack ('<I',(0 if self .title is None or self .title is False else 1 )|(0 if self .icon_emoji_id is None or self .icon_emoji_id is False else 2 )|(0 if self .closed is None else 4 )|(0 if self .hidden is None else 8 )),
        self .channel ._bytes (),
        struct .pack ('<i',self .topic_id ),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        b''if self .icon_emoji_id is None or self .icon_emoji_id is False else (struct .pack ('<q',self .icon_emoji_id )),
        b''if self .closed is None else (b'\xb5ur\x99'if self .closed else b'7\x97y\xbc'),
        b''if self .hidden is None else (b'\xb5ur\x99'if self .hidden else b'7\x97y\xbc'),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _channel =reader .tgread_object ()
        _topic_id =reader .read_int ()
        if flags &1 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        if flags &2 :
            _icon_emoji_id =reader .read_long ()
        else :
            _icon_emoji_id =None 
        if flags &4 :
            _closed =reader .tgread_bool ()
        else :
            _closed =None 
        if flags &8 :
            _hidden =reader .tgread_bool ()
        else :
            _hidden =None 
        return cls (channel =_channel ,topic_id =_topic_id ,title =_title ,icon_emoji_id =_icon_emoji_id ,closed =_closed ,hidden =_hidden )

class EditLocationRequest (TLRequest ):
    CONSTRUCTOR_ID =0x58e63f6d 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',geo_point :'TypeInputGeoPoint',address :str ):
        """"""
        self .channel =channel 
        self .geo_point =geo_point 
        self .address =address 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'EditLocationRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'geo_point':self .geo_point .to_dict ()if isinstance (self .geo_point ,TLObject )else self .geo_point ,
        'address':self .address 
        }

    def _bytes (self ):
        return b''.join ((
        b'm?\xe6X',
        self .channel ._bytes (),
        self .geo_point ._bytes (),
        self .serialize_bytes (self .address ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _geo_point =reader .tgread_object ()
        _address =reader .tgread_string ()
        return cls (channel =_channel ,geo_point =_geo_point ,address =_address )

class EditPhotoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf12e57c9 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',photo :'TypeInputChatPhoto'):
        """"""
        self .channel =channel 
        self .photo =photo 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .photo =utils .get_input_chat_photo (self .photo )

    def to_dict (self ):
        return {
        '_':'EditPhotoRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'photo':self .photo .to_dict ()if isinstance (self .photo ,TLObject )else self .photo 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc9W.\xf1',
        self .channel ._bytes (),
        self .photo ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _photo =reader .tgread_object ()
        return cls (channel =_channel ,photo =_photo )

class EditTitleRequest (TLRequest ):
    CONSTRUCTOR_ID =0x566decd0 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',title :str ):
        """"""
        self .channel =channel 
        self .title =title 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'EditTitleRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'title':self .title 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd0\xecmV',
        self .channel ._bytes (),
        self .serialize_bytes (self .title ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _title =reader .tgread_string ()
        return cls (channel =_channel ,title =_title )

class ExportMessageLinkRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe63fadeb 
    SUBCLASS_OF_ID =0xdee644cc 

    def __init__ (self ,channel :'TypeInputChannel',id :int ,grouped :Optional [bool ]=None ,thread :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .id =id 
        self .grouped =grouped 
        self .thread =thread 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ExportMessageLinkRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'id':self .id ,
        'grouped':self .grouped ,
        'thread':self .thread 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeb\xad?\xe6',
        struct .pack ('<I',(0 if self .grouped is None or self .grouped is False else 1 )|(0 if self .thread is None or self .thread is False else 2 )),
        self .channel ._bytes (),
        struct .pack ('<i',self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _grouped =bool (flags &1 )
        _thread =bool (flags &2 )
        _channel =reader .tgread_object ()
        _id =reader .read_int ()
        return cls (channel =_channel ,id =_id ,grouped =_grouped ,thread =_thread )

class GetAdminLogRequest (TLRequest ):
    CONSTRUCTOR_ID =0x33ddf480 
    SUBCLASS_OF_ID =0x51f076bc 

    def __init__ (self ,channel :'TypeInputChannel',q :str ,max_id :int ,min_id :int ,limit :int ,events_filter :Optional ['TypeChannelAdminLogEventsFilter']=None ,admins :Optional [List ['TypeInputUser']]=None ):
        """"""
        self .channel =channel 
        self .q =q 
        self .max_id =max_id 
        self .min_id =min_id 
        self .limit =limit 
        self .events_filter =events_filter 
        self .admins =admins 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        if self .admins :
            _tmp =[]
            for _x in self .admins :
                _tmp .append (utils .get_input_user (await client .get_input_entity (_x )))

            self .admins =_tmp 

    def to_dict (self ):
        return {
        '_':'GetAdminLogRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'q':self .q ,
        'max_id':self .max_id ,
        'min_id':self .min_id ,
        'limit':self .limit ,
        'events_filter':self .events_filter .to_dict ()if isinstance (self .events_filter ,TLObject )else self .events_filter ,
        'admins':[]if self .admins is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .admins ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x80\xf4\xdd3',
        struct .pack ('<I',(0 if self .events_filter is None or self .events_filter is False else 1 )|(0 if self .admins is None or self .admins is False else 2 )),
        self .channel ._bytes (),
        self .serialize_bytes (self .q ),
        b''if self .events_filter is None or self .events_filter is False else (self .events_filter ._bytes ()),
        b''if self .admins is None or self .admins is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .admins )),b''.join (x ._bytes ()for x in self .admins ))),
        struct .pack ('<q',self .max_id ),
        struct .pack ('<q',self .min_id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _channel =reader .tgread_object ()
        _q =reader .tgread_string ()
        if flags &1 :
            _events_filter =reader .tgread_object ()
        else :
            _events_filter =None 
        if flags &2 :
            reader .read_int ()
            _admins =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _admins .append (_x )

        else :
            _admins =None 
        _max_id =reader .read_long ()
        _min_id =reader .read_long ()
        _limit =reader .read_int ()
        return cls (channel =_channel ,q =_q ,max_id =_max_id ,min_id =_min_id ,limit =_limit ,events_filter =_events_filter ,admins =_admins )

class GetAdminedPublicChannelsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf8b036af 
    SUBCLASS_OF_ID =0x99d5cb14 

    def __init__ (self ,by_location :Optional [bool ]=None ,check_limit :Optional [bool ]=None ):
        """"""
        self .by_location =by_location 
        self .check_limit =check_limit 

    def to_dict (self ):
        return {
        '_':'GetAdminedPublicChannelsRequest',
        'by_location':self .by_location ,
        'check_limit':self .check_limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xaf6\xb0\xf8',
        struct .pack ('<I',(0 if self .by_location is None or self .by_location is False else 1 )|(0 if self .check_limit is None or self .check_limit is False else 2 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _by_location =bool (flags &1 )
        _check_limit =bool (flags &2 )
        return cls (by_location =_by_location ,check_limit =_check_limit )

class GetChannelsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa7f6bbb 
    SUBCLASS_OF_ID =0x99d5cb14 

    def __init__ (self ,id :List ['TypeInputChannel']):
        """"""
        self .id =id 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_channel (await client .get_input_entity (_x )))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'GetChannelsRequest',
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbbk\x7f\n',
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

class GetForumTopicsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xde560d1 
    SUBCLASS_OF_ID =0x8e1d3e1e 

    def __init__ (self ,channel :'TypeInputChannel',offset_date :Optional [datetime ],offset_id :int ,offset_topic :int ,limit :int ,q :Optional [str ]=None ):
        """"""
        self .channel =channel 
        self .offset_date =offset_date 
        self .offset_id =offset_id 
        self .offset_topic =offset_topic 
        self .limit =limit 
        self .q =q 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetForumTopicsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'offset_date':self .offset_date ,
        'offset_id':self .offset_id ,
        'offset_topic':self .offset_topic ,
        'limit':self .limit ,
        'q':self .q 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd1`\xe5\r',
        struct .pack ('<I',(0 if self .q is None or self .q is False else 1 )),
        self .channel ._bytes (),
        b''if self .q is None or self .q is False else (self .serialize_bytes (self .q )),
        self .serialize_datetime (self .offset_date ),
        struct .pack ('<i',self .offset_id ),
        struct .pack ('<i',self .offset_topic ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _channel =reader .tgread_object ()
        if flags &1 :
            _q =reader .tgread_string ()
        else :
            _q =None 
        _offset_date =reader .tgread_date ()
        _offset_id =reader .read_int ()
        _offset_topic =reader .read_int ()
        _limit =reader .read_int ()
        return cls (channel =_channel ,offset_date =_offset_date ,offset_id =_offset_id ,offset_topic =_offset_topic ,limit =_limit ,q =_q )

class GetForumTopicsByIDRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb0831eb9 
    SUBCLASS_OF_ID =0x8e1d3e1e 

    def __init__ (self ,channel :'TypeInputChannel',topics :List [int ]):
        """"""
        self .channel =channel 
        self .topics =topics 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetForumTopicsByIDRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'topics':[]if self .topics is None else self .topics [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb9\x1e\x83\xb0',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .topics )),b''.join (struct .pack ('<i',x )for x in self .topics ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _topics =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _topics .append (_x )

        return cls (channel =_channel ,topics =_topics )

class GetFullChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8736a09 
    SUBCLASS_OF_ID =0x225a5109 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetFullChannelRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\tjs\x08',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class GetGroupsForDiscussionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf5dad378 
    SUBCLASS_OF_ID =0x99d5cb14 

    def to_dict (self ):
        return {
        '_':'GetGroupsForDiscussionRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'x\xd3\xda\xf5',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetInactiveChannelsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x11e831ee 
    SUBCLASS_OF_ID =0x8bf3d7d4 

    def to_dict (self ):
        return {
        '_':'GetInactiveChannelsRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xee1\xe8\x11',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetLeftChannelsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8341ecc0 
    SUBCLASS_OF_ID =0x99d5cb14 

    def __init__ (self ,offset :int ):
        """"""
        self .offset =offset 

    def to_dict (self ):
        return {
        '_':'GetLeftChannelsRequest',
        'offset':self .offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc0\xecA\x83',
        struct .pack ('<i',self .offset ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _offset =reader .read_int ()
        return cls (offset =_offset )

class GetMessagesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xad8c9a23 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,channel :'TypeInputChannel',id :List ['TypeInputMessage']):
        """"""
        self .channel =channel 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_message (_x ))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'GetMessagesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ]
        }

    def _bytes (self ):
        return b''.join ((
        b'#\x9a\x8c\xad',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (x ._bytes ()for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _id .append (_x )

        return cls (channel =_channel ,id =_id )

class GetParticipantRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa0ab6cc6 
    SUBCLASS_OF_ID =0x6658151a 

    def __init__ (self ,channel :'TypeInputChannel',participant :'TypeInputPeer'):
        """"""
        self .channel =channel 
        self .participant =participant 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .participant =utils .get_input_peer (await client .get_input_entity (self .participant ))

    def to_dict (self ):
        return {
        '_':'GetParticipantRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc6l\xab\xa0',
        self .channel ._bytes (),
        self .participant ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _participant =reader .tgread_object ()
        return cls (channel =_channel ,participant =_participant )

class GetParticipantsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x77ced9d0 
    SUBCLASS_OF_ID =0xe60a6e64 

    def __init__ (self ,channel :'TypeInputChannel',filter :'TypeChannelParticipantsFilter',offset :int ,limit :int ,hash :int ):
        """"""
        self .channel =channel 
        self .filter =filter 
        self .offset =offset 
        self .limit =limit 
        self .hash =hash 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetParticipantsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'filter':self .filter .to_dict ()if isinstance (self .filter ,TLObject )else self .filter ,
        'offset':self .offset ,
        'limit':self .limit ,
        'hash':self .hash 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd0\xd9\xcew',
        self .channel ._bytes (),
        self .filter ._bytes (),
        struct .pack ('<i',self .offset ),
        struct .pack ('<i',self .limit ),
        struct .pack ('<q',self .hash ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _filter =reader .tgread_object ()
        _offset =reader .read_int ()
        _limit =reader .read_int ()
        _hash =reader .read_long ()
        return cls (channel =_channel ,filter =_filter ,offset =_offset ,limit =_limit ,hash =_hash )

class GetSendAsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdc770ee 
    SUBCLASS_OF_ID =0x38cb8d21 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetSendAsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeep\xc7\r',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class GetSponsoredMessagesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xec210fbf 
    SUBCLASS_OF_ID =0x7f4169e0 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'GetSponsoredMessagesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbf\x0f!\xec',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class InviteToChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0x199f3a6c 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',users :List ['TypeInputUser']):
        """"""
        self .channel =channel 
        self .users =users 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        _tmp =[]
        for _x in self .users :
            _tmp .append (utils .get_input_user (await client .get_input_entity (_x )))

        self .users =_tmp 

    def to_dict (self ):
        return {
        '_':'InviteToChannelRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'l:\x9f\x19',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (channel =_channel ,users =_users )

class JoinChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0x24b524c5 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'JoinChannelRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc5$\xb5$',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class LeaveChannelRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf836aa95 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel'):
        """"""
        self .channel =channel 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'LeaveChannelRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x95\xaa6\xf8',
        self .channel ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        return cls (channel =_channel )

class ReadHistoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0xcc104937 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',max_id :int ):
        """"""
        self .channel =channel 
        self .max_id =max_id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ReadHistoryRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'max_id':self .max_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'7I\x10\xcc',
        self .channel ._bytes (),
        struct .pack ('<i',self .max_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _max_id =reader .read_int ()
        return cls (channel =_channel ,max_id =_max_id )

class ReadMessageContentsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xeab5dc38 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',id :List [int ]):
        """"""
        self .channel =channel 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ReadMessageContentsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'8\xdc\xb5\xea',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (channel =_channel ,id =_id )

class ReorderPinnedForumTopicsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2950a18f 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',order :List [int ],force :Optional [bool ]=None ):
        """"""
        self .channel =channel 
        self .order =order 
        self .force =force 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ReorderPinnedForumTopicsRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'order':[]if self .order is None else self .order [:],
        'force':self .force 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8f\xa1P)',
        struct .pack ('<I',(0 if self .force is None or self .force is False else 1 )),
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .order )),b''.join (struct .pack ('<i',x )for x in self .order ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _force =bool (flags &1 )
        _channel =reader .tgread_object ()
        reader .read_int ()
        _order =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _order .append (_x )

        return cls (channel =_channel ,order =_order ,force =_force )

class ReorderUsernamesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb45ced1d 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',order :List [str ]):
        """"""
        self .channel =channel 
        self .order =order 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ReorderUsernamesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'order':[]if self .order is None else self .order [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1d\xed\\\xb4',
        self .channel ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .order )),b''.join (self .serialize_bytes (x )for x in self .order ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        reader .read_int ()
        _order =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_string ()
            _order .append (_x )

        return cls (channel =_channel ,order =_order )

class ReportAntiSpamFalsePositiveRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa850a693 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',msg_id :int ):
        """"""
        self .channel =channel 
        self .msg_id =msg_id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ReportAntiSpamFalsePositiveRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'msg_id':self .msg_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x93\xa6P\xa8',
        self .channel ._bytes (),
        struct .pack ('<i',self .msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _msg_id =reader .read_int ()
        return cls (channel =_channel ,msg_id =_msg_id )

class ReportSpamRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf44a8315 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',participant :'TypeInputPeer',id :List [int ]):
        """"""
        self .channel =channel 
        self .participant =participant 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))
        self .participant =utils .get_input_peer (await client .get_input_entity (self .participant ))

    def to_dict (self ):
        return {
        '_':'ReportSpamRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'participant':self .participant .to_dict ()if isinstance (self .participant ,TLObject )else self .participant ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x15\x83J\xf4',
        self .channel ._bytes (),
        self .participant ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _participant =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (channel =_channel ,participant =_participant ,id =_id )

class SetDiscussionGroupRequest (TLRequest ):
    CONSTRUCTOR_ID =0x40582bb2 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,broadcast :'TypeInputChannel',group :'TypeInputChannel'):
        """"""
        self .broadcast =broadcast 
        self .group =group 

    async def resolve (self ,client ,utils ):
        self .broadcast =utils .get_input_channel (await client .get_input_entity (self .broadcast ))
        self .group =utils .get_input_channel (await client .get_input_entity (self .group ))

    def to_dict (self ):
        return {
        '_':'SetDiscussionGroupRequest',
        'broadcast':self .broadcast .to_dict ()if isinstance (self .broadcast ,TLObject )else self .broadcast ,
        'group':self .group .to_dict ()if isinstance (self .group ,TLObject )else self .group 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb2+X@',
        self .broadcast ._bytes (),
        self .group ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _broadcast =reader .tgread_object ()
        _group =reader .tgread_object ()
        return cls (broadcast =_broadcast ,group =_group )

class SetStickersRequest (TLRequest ):
    CONSTRUCTOR_ID =0xea8ca4f9 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',stickerset :'TypeInputStickerSet'):
        """"""
        self .channel =channel 
        self .stickerset =stickerset 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'SetStickersRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'stickerset':self .stickerset .to_dict ()if isinstance (self .stickerset ,TLObject )else self .stickerset 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9\xa4\x8c\xea',
        self .channel ._bytes (),
        self .stickerset ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _stickerset =reader .tgread_object ()
        return cls (channel =_channel ,stickerset =_stickerset )

class ToggleAntiSpamRequest (TLRequest ):
    CONSTRUCTOR_ID =0x68f3e4eb 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleAntiSpamRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeb\xe4\xf3h',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleForumRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa4298b29 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleForumRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b')\x8b)\xa4',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleJoinRequestRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4c2985b6 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleJoinRequestRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb6\x85)L',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleJoinToSendRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe4cb9580 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleJoinToSendRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x80\x95\xcb\xe4',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleParticipantsHiddenRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6a6e7854 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleParticipantsHiddenRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'Txnj',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class TogglePreHistoryHiddenRequest (TLRequest ):
    CONSTRUCTOR_ID =0xeabbb94c 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'TogglePreHistoryHiddenRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'L\xb9\xbb\xea',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleSignaturesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1f69b606 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',enabled :bool ):
        """"""
        self .channel =channel 
        self .enabled =enabled 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleSignaturesRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'enabled':self .enabled 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x06\xb6i\x1f',
        self .channel ._bytes (),
        b'\xb5ur\x99'if self .enabled else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _enabled =reader .tgread_bool ()
        return cls (channel =_channel ,enabled =_enabled )

class ToggleSlowModeRequest (TLRequest ):
    CONSTRUCTOR_ID =0xedd49ef0 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',seconds :int ):
        """"""
        self .channel =channel 
        self .seconds =seconds 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleSlowModeRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'seconds':self .seconds 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf0\x9e\xd4\xed',
        self .channel ._bytes (),
        struct .pack ('<i',self .seconds ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _seconds =reader .read_int ()
        return cls (channel =_channel ,seconds =_seconds )

class ToggleUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x50f24105 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',username :str ,active :bool ):
        """"""
        self .channel =channel 
        self .username =username 
        self .active =active 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ToggleUsernameRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'username':self .username ,
        'active':self .active 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x05A\xf2P',
        self .channel ._bytes (),
        self .serialize_bytes (self .username ),
        b'\xb5ur\x99'if self .active else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _username =reader .tgread_string ()
        _active =reader .tgread_bool ()
        return cls (channel =_channel ,username =_username ,active =_active )

class UpdateColorRequest (TLRequest ):
    CONSTRUCTOR_ID =0x621a201f 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',color :int ,background_emoji_id :Optional [int ]=None ):
        """"""
        self .channel =channel 
        self .color =color 
        self .background_emoji_id =background_emoji_id 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'UpdateColorRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'color':self .color ,
        'background_emoji_id':self .background_emoji_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x1f \x1ab',
        struct .pack ('<I',(0 if self .background_emoji_id is None or self .background_emoji_id is False else 1 )),
        self .channel ._bytes (),
        struct .pack ('<i',self .color ),
        b''if self .background_emoji_id is None or self .background_emoji_id is False else (struct .pack ('<q',self .background_emoji_id )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _channel =reader .tgread_object ()
        _color =reader .read_int ()
        if flags &1 :
            _background_emoji_id =reader .read_long ()
        else :
            _background_emoji_id =None 
        return cls (channel =_channel ,color =_color ,background_emoji_id =_background_emoji_id )

class UpdatePinnedForumTopicRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6c2d9026 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,channel :'TypeInputChannel',topic_id :int ,pinned :bool ):
        """"""
        self .channel =channel 
        self .topic_id =topic_id 
        self .pinned =pinned 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'UpdatePinnedForumTopicRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'topic_id':self .topic_id ,
        'pinned':self .pinned 
        }

    def _bytes (self ):
        return b''.join ((
        b'&\x90-l',
        self .channel ._bytes (),
        struct .pack ('<i',self .topic_id ),
        b'\xb5ur\x99'if self .pinned else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _topic_id =reader .read_int ()
        _pinned =reader .tgread_bool ()
        return cls (channel =_channel ,topic_id =_topic_id ,pinned =_pinned )

class UpdateUsernameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x3514b3de 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',username :str ):
        """"""
        self .channel =channel 
        self .username =username 

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'UpdateUsernameRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'username':self .username 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xde\xb3\x145',
        self .channel ._bytes (),
        self .serialize_bytes (self .username ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _username =reader .tgread_string ()
        return cls (channel =_channel ,username =_username )

class ViewSponsoredMessageRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbeaedb94 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,channel :'TypeInputChannel',random_id :bytes =None ):
        """"""
        self .channel =channel 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (4 ),'big',signed =True )

    async def resolve (self ,client ,utils ):
        self .channel =utils .get_input_channel (await client .get_input_entity (self .channel ))

    def to_dict (self ):
        return {
        '_':'ViewSponsoredMessageRequest',
        'channel':self .channel .to_dict ()if isinstance (self .channel ,TLObject )else self .channel ,
        'random_id':self .random_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x94\xdb\xae\xbe',
        self .channel ._bytes (),
        self .serialize_bytes (self .random_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _channel =reader .tgread_object ()
        _random_id =reader .tgread_bytes ()
        return cls (channel =_channel ,random_id =_random_id )

