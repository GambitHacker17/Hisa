""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputMedia ,TypeInputPeer ,TypeInputPrivacyRule ,TypeMediaArea ,TypeMessageEntity ,TypeReaction ,TypeReportReason 

class ActivateStealthModeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x57bbd166 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,past :Optional [bool ]=None ,future :Optional [bool ]=None ):
        """"""
        self .past =past 
        self .future =future 

    def to_dict (self ):
        return {
        '_':'ActivateStealthModeRequest',
        'past':self .past ,
        'future':self .future 
        }

    def _bytes (self ):
        return b''.join ((
        b'f\xd1\xbbW',
        struct .pack ('<I',(0 if self .past is None or self .past is False else 1 )|(0 if self .future is None or self .future is False else 2 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _past =bool (flags &1 )
        _future =bool (flags &2 )
        return cls (past =_past ,future =_future )

class CanSendStoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0xc7dfdfdd 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'CanSendStoryRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdd\xdf\xdf\xc7',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class DeleteStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xae59db5f 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ]):
        """"""
        self .peer =peer 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'DeleteStoriesRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'_\xdbY\xae',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (peer =_peer ,id =_id )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

class EditStoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb583ba46 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPeer',id :int ,media :Optional ['TypeInputMedia']=None ,media_areas :Optional [List ['TypeMediaArea']]=None ,caption :Optional [str ]=None ,entities :Optional [List ['TypeMessageEntity']]=None ,privacy_rules :Optional [List ['TypeInputPrivacyRule']]=None ):
        """"""
        self .peer =peer 
        self .id =id 
        self .media =media 
        self .media_areas =media_areas 
        self .caption =caption 
        self .entities =entities 
        self .privacy_rules =privacy_rules 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))
        if self .media :
            self .media =utils .get_input_media (self .media )

    def to_dict (self ):
        return {
        '_':'EditStoryRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':self .id ,
        'media':self .media .to_dict ()if isinstance (self .media ,TLObject )else self .media ,
        'media_areas':[]if self .media_areas is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .media_areas ],
        'caption':self .caption ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ],
        'privacy_rules':[]if self .privacy_rules is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .privacy_rules ]
        }

    def _bytes (self ):
        assert ((self .caption or self .caption is not None )and (self .entities or self .entities is not None ))or ((self .caption is None or self .caption is False )and (self .entities is None or self .entities is False )),'caption, entities parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'F\xba\x83\xb5',
        struct .pack ('<I',(0 if self .media is None or self .media is False else 1 )|(0 if self .media_areas is None or self .media_areas is False else 8 )|(0 if self .caption is None or self .caption is False else 2 )|(0 if self .entities is None or self .entities is False else 2 )|(0 if self .privacy_rules is None or self .privacy_rules is False else 4 )),
        self .peer ._bytes (),
        struct .pack ('<i',self .id ),
        b''if self .media is None or self .media is False else (self .media ._bytes ()),
        b''if self .media_areas is None or self .media_areas is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .media_areas )),b''.join (x ._bytes ()for x in self .media_areas ))),
        b''if self .caption is None or self .caption is False else (self .serialize_bytes (self .caption )),
        b''if self .entities is None or self .entities is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ))),
        b''if self .privacy_rules is None or self .privacy_rules is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .privacy_rules )),b''.join (x ._bytes ()for x in self .privacy_rules ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _peer =reader .tgread_object ()
        _id =reader .read_int ()
        if flags &1 :
            _media =reader .tgread_object ()
        else :
            _media =None 
        if flags &8 :
            reader .read_int ()
            _media_areas =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _media_areas .append (_x )

        else :
            _media_areas =None 
        if flags &2 :
            _caption =reader .tgread_string ()
        else :
            _caption =None 
        if flags &2 :
            reader .read_int ()
            _entities =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _entities .append (_x )

        else :
            _entities =None 
        if flags &4 :
            reader .read_int ()
            _privacy_rules =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _privacy_rules .append (_x )

        else :
            _privacy_rules =None 
        return cls (peer =_peer ,id =_id ,media =_media ,media_areas =_media_areas ,caption =_caption ,entities =_entities ,privacy_rules =_privacy_rules )

class ExportStoryLinkRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7b8def20 
    SUBCLASS_OF_ID =0xfc541a6 

    def __init__ (self ,peer :'TypeInputPeer',id :int ):
        """"""
        self .peer =peer 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ExportStoryLinkRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':self .id 
        }

    def _bytes (self ):
        return b''.join ((
        b' \xef\x8d{',
        self .peer ._bytes (),
        struct .pack ('<i',self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _id =reader .read_int ()
        return cls (peer =_peer ,id =_id )

class GetAllReadPeerStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9b5ae7f9 
    SUBCLASS_OF_ID =0x8af52aac 

    def to_dict (self ):
        return {
        '_':'GetAllReadPeerStoriesRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf9\xe7Z\x9b',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetAllStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xeeb0d625 
    SUBCLASS_OF_ID =0x7e60d0cd 

    def __init__ (self ,next :Optional [bool ]=None ,hidden :Optional [bool ]=None ,state :Optional [str ]=None ):
        """"""
        self .next =next 
        self .hidden =hidden 
        self .state =state 

    def to_dict (self ):
        return {
        '_':'GetAllStoriesRequest',
        'next':self .next ,
        'hidden':self .hidden ,
        'state':self .state 
        }

    def _bytes (self ):
        return b''.join ((
        b'%\xd6\xb0\xee',
        struct .pack ('<I',(0 if self .next is None or self .next is False else 2 )|(0 if self .hidden is None or self .hidden is False else 4 )|(0 if self .state is None or self .state is False else 1 )),
        b''if self .state is None or self .state is False else (self .serialize_bytes (self .state )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _next =bool (flags &2 )
        _hidden =bool (flags &4 )
        if flags &1 :
            _state =reader .tgread_string ()
        else :
            _state =None 
        return cls (next =_next ,hidden =_hidden ,state =_state )

class GetChatsToSendRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa56a8b60 
    SUBCLASS_OF_ID =0x99d5cb14 

    def to_dict (self ):
        return {
        '_':'GetChatsToSendRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'`\x8bj\xa5',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class GetPeerMaxIDsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x535983c3 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,id :List ['TypeInputPeer']):
        """"""
        self .id =id 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_peer (await client .get_input_entity (_x )))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'GetPeerMaxIDsRequest',
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc3\x83YS',
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

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

class GetPeerStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2c4ada50 
    SUBCLASS_OF_ID =0x9d56cfd0 

    def __init__ (self ,peer :'TypeInputPeer'):
        """"""
        self .peer =peer 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetPeerStoriesRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer 
        }

    def _bytes (self ):
        return b''.join ((
        b'P\xdaJ,',
        self .peer ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        return cls (peer =_peer )

class GetPinnedStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5821a5dc 
    SUBCLASS_OF_ID =0x251c0c2c 

    def __init__ (self ,peer :'TypeInputPeer',offset_id :int ,limit :int ):
        """"""
        self .peer =peer 
        self .offset_id =offset_id 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetPinnedStoriesRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'offset_id':self .offset_id ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdc\xa5!X',
        self .peer ._bytes (),
        struct .pack ('<i',self .offset_id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _offset_id =reader .read_int ()
        _limit =reader .read_int ()
        return cls (peer =_peer ,offset_id =_offset_id ,limit =_limit )

class GetStoriesArchiveRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb4352016 
    SUBCLASS_OF_ID =0x251c0c2c 

    def __init__ (self ,peer :'TypeInputPeer',offset_id :int ,limit :int ):
        """"""
        self .peer =peer 
        self .offset_id =offset_id 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetStoriesArchiveRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'offset_id':self .offset_id ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x16 5\xb4',
        self .peer ._bytes (),
        struct .pack ('<i',self .offset_id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _offset_id =reader .read_int ()
        _limit =reader .read_int ()
        return cls (peer =_peer ,offset_id =_offset_id ,limit =_limit )

class GetStoriesByIDRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5774ca74 
    SUBCLASS_OF_ID =0x251c0c2c 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ]):
        """"""
        self .peer =peer 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetStoriesByIDRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b't\xcatW',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (peer =_peer ,id =_id )

class GetStoriesViewsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x28e16cc8 
    SUBCLASS_OF_ID =0x4b3fc4ba 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ]):
        """"""
        self .peer =peer 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetStoriesViewsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc8l\xe1(',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (peer =_peer ,id =_id )

class GetStoryViewsListRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7ed23c57 
    SUBCLASS_OF_ID =0xb9437560 

    def __init__ (self ,peer :'TypeInputPeer',id :int ,offset :str ,limit :int ,just_contacts :Optional [bool ]=None ,reactions_first :Optional [bool ]=None ,q :Optional [str ]=None ):
        """"""
        self .peer =peer 
        self .id =id 
        self .offset =offset 
        self .limit =limit 
        self .just_contacts =just_contacts 
        self .reactions_first =reactions_first 
        self .q =q 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetStoryViewsListRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':self .id ,
        'offset':self .offset ,
        'limit':self .limit ,
        'just_contacts':self .just_contacts ,
        'reactions_first':self .reactions_first ,
        'q':self .q 
        }

    def _bytes (self ):
        return b''.join ((
        b'W<\xd2~',
        struct .pack ('<I',(0 if self .just_contacts is None or self .just_contacts is False else 1 )|(0 if self .reactions_first is None or self .reactions_first is False else 4 )|(0 if self .q is None or self .q is False else 2 )),
        self .peer ._bytes (),
        b''if self .q is None or self .q is False else (self .serialize_bytes (self .q )),
        struct .pack ('<i',self .id ),
        self .serialize_bytes (self .offset ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _just_contacts =bool (flags &1 )
        _reactions_first =bool (flags &4 )
        _peer =reader .tgread_object ()
        if flags &2 :
            _q =reader .tgread_string ()
        else :
            _q =None 
        _id =reader .read_int ()
        _offset =reader .tgread_string ()
        _limit =reader .read_int ()
        return cls (peer =_peer ,id =_id ,offset =_offset ,limit =_limit ,just_contacts =_just_contacts ,reactions_first =_reactions_first ,q =_q )

class IncrementStoryViewsRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb2028afb 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ]):
        """"""
        self .peer =peer 
        self .id =id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'IncrementStoryViewsRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfb\x8a\x02\xb2',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        return cls (peer =_peer ,id =_id )

class ReadStoriesRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa556dac8 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,peer :'TypeInputPeer',max_id :int ):
        """"""
        self .peer =peer 
        self .max_id =max_id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ReadStoriesRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'max_id':self .max_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc8\xdaV\xa5',
        self .peer ._bytes (),
        struct .pack ('<i',self .max_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _max_id =reader .read_int ()
        return cls (peer =_peer ,max_id =_max_id )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

class ReportRequest (TLRequest ):
    CONSTRUCTOR_ID =0x1923fa8c 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ],reason :'TypeReportReason',message :str ):
        """"""
        self .peer =peer 
        self .id =id 
        self .reason =reason 
        self .message =message 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'ReportRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:],
        'reason':self .reason .to_dict ()if isinstance (self .reason ,TLObject )else self .reason ,
        'message':self .message 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x8c\xfa#\x19',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        self .reason ._bytes (),
        self .serialize_bytes (self .message ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        _reason =reader .tgread_object ()
        _message =reader .tgread_string ()
        return cls (peer =_peer ,id =_id ,reason =_reason ,message =_message )

class SendReactionRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7fd736b2 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPeer',story_id :int ,reaction :'TypeReaction',add_to_recent :Optional [bool ]=None ):
        """"""
        self .peer =peer 
        self .story_id =story_id 
        self .reaction =reaction 
        self .add_to_recent =add_to_recent 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'SendReactionRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'story_id':self .story_id ,
        'reaction':self .reaction .to_dict ()if isinstance (self .reaction ,TLObject )else self .reaction ,
        'add_to_recent':self .add_to_recent 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb26\xd7\x7f',
        struct .pack ('<I',(0 if self .add_to_recent is None or self .add_to_recent is False else 1 )),
        self .peer ._bytes (),
        struct .pack ('<i',self .story_id ),
        self .reaction ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _add_to_recent =bool (flags &1 )
        _peer =reader .tgread_object ()
        _story_id =reader .read_int ()
        _reaction =reader .tgread_object ()
        return cls (peer =_peer ,story_id =_story_id ,reaction =_reaction ,add_to_recent =_add_to_recent )

class SendStoryRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbcb73644 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPeer',media :'TypeInputMedia',privacy_rules :List ['TypeInputPrivacyRule'],pinned :Optional [bool ]=None ,noforwards :Optional [bool ]=None ,media_areas :Optional [List ['TypeMediaArea']]=None ,caption :Optional [str ]=None ,entities :Optional [List ['TypeMessageEntity']]=None ,random_id :int =None ,period :Optional [int ]=None ):
        """"""
        self .peer =peer 
        self .media =media 
        self .privacy_rules =privacy_rules 
        self .pinned =pinned 
        self .noforwards =noforwards 
        self .media_areas =media_areas 
        self .caption =caption 
        self .entities =entities 
        self .random_id =random_id if random_id is not None else int .from_bytes (os .urandom (8 ),'big',signed =True )
        self .period =period 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))
        self .media =utils .get_input_media (self .media )

    def to_dict (self ):
        return {
        '_':'SendStoryRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'media':self .media .to_dict ()if isinstance (self .media ,TLObject )else self .media ,
        'privacy_rules':[]if self .privacy_rules is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .privacy_rules ],
        'pinned':self .pinned ,
        'noforwards':self .noforwards ,
        'media_areas':[]if self .media_areas is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .media_areas ],
        'caption':self .caption ,
        'entities':[]if self .entities is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .entities ],
        'random_id':self .random_id ,
        'period':self .period 
        }

    def _bytes (self ):
        return b''.join ((
        b'D6\xb7\xbc',
        struct .pack ('<I',(0 if self .pinned is None or self .pinned is False else 4 )|(0 if self .noforwards is None or self .noforwards is False else 16 )|(0 if self .media_areas is None or self .media_areas is False else 32 )|(0 if self .caption is None or self .caption is False else 1 )|(0 if self .entities is None or self .entities is False else 2 )|(0 if self .period is None or self .period is False else 8 )),
        self .peer ._bytes (),
        self .media ._bytes (),
        b''if self .media_areas is None or self .media_areas is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .media_areas )),b''.join (x ._bytes ()for x in self .media_areas ))),
        b''if self .caption is None or self .caption is False else (self .serialize_bytes (self .caption )),
        b''if self .entities is None or self .entities is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .entities )),b''.join (x ._bytes ()for x in self .entities ))),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .privacy_rules )),b''.join (x ._bytes ()for x in self .privacy_rules ),
        struct .pack ('<q',self .random_id ),
        b''if self .period is None or self .period is False else (struct .pack ('<i',self .period )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _pinned =bool (flags &4 )
        _noforwards =bool (flags &16 )
        _peer =reader .tgread_object ()
        _media =reader .tgread_object ()
        if flags &32 :
            reader .read_int ()
            _media_areas =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _media_areas .append (_x )

        else :
            _media_areas =None 
        if flags &1 :
            _caption =reader .tgread_string ()
        else :
            _caption =None 
        if flags &2 :
            reader .read_int ()
            _entities =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _entities .append (_x )

        else :
            _entities =None 
        reader .read_int ()
        _privacy_rules =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _privacy_rules .append (_x )

        _random_id =reader .read_long ()
        if flags &8 :
            _period =reader .read_int ()
        else :
            _period =None 
        return cls (peer =_peer ,media =_media ,privacy_rules =_privacy_rules ,pinned =_pinned ,noforwards =_noforwards ,media_areas =_media_areas ,caption =_caption ,entities =_entities ,random_id =_random_id ,period =_period )

class ToggleAllStoriesHiddenRequest (TLRequest ):
    CONSTRUCTOR_ID =0x7c2557c4 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,hidden :bool ):
        """"""
        self .hidden =hidden 

    def to_dict (self ):
        return {
        '_':'ToggleAllStoriesHiddenRequest',
        'hidden':self .hidden 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc4W%|',
        b'\xb5ur\x99'if self .hidden else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hidden =reader .tgread_bool ()
        return cls (hidden =_hidden )

class TogglePeerStoriesHiddenRequest (TLRequest ):
    CONSTRUCTOR_ID =0xbd0415c4 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,peer :'TypeInputPeer',hidden :bool ):
        """"""
        self .peer =peer 
        self .hidden =hidden 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'TogglePeerStoriesHiddenRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'hidden':self .hidden 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc4\x15\x04\xbd',
        self .peer ._bytes (),
        b'\xb5ur\x99'if self .hidden else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _hidden =reader .tgread_bool ()
        return cls (peer =_peer ,hidden =_hidden )

class TogglePinnedRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9a75a1ef 
    SUBCLASS_OF_ID =0x5026710f 

    def __init__ (self ,peer :'TypeInputPeer',id :List [int ],pinned :bool ):
        """"""
        self .peer =peer 
        self .id =id 
        self .pinned =pinned 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'TogglePinnedRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'id':[]if self .id is None else self .id [:],
        'pinned':self .pinned 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xef\xa1u\x9a',
        self .peer ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (struct .pack ('<i',x )for x in self .id ),
        b'\xb5ur\x99'if self .pinned else b'7\x97y\xbc',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _id .append (_x )

        _pinned =reader .tgread_bool ()
        return cls (peer =_peer ,id =_id ,pinned =_pinned )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_int ()for _ in range (reader .read_int ())]

