""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeAvailableReaction ,TypeBotApp ,TypeBotInlineResult ,TypeChat ,TypeChatAdminWithInvites ,TypeChatFull ,TypeChatInviteImporter ,TypeDialog ,TypeDocument ,TypeEmojiGroup ,TypeEncryptedFile ,TypeExportedChatInvite ,TypeForumTopic ,TypeHighScore ,TypeInlineBotSwitchPM ,TypeInlineBotWebView ,TypeMessage ,TypeMessagePeerReaction ,TypeMessagePeerVote ,TypeMessageViews ,TypeMessagesFilter ,TypePeerSettings ,TypeReaction ,TypeSearchResultsCalendarPeriod ,TypeSearchResultsPosition ,TypeSponsoredMessage ,TypeStickerKeyword ,TypeStickerPack ,TypeStickerSet ,TypeStickerSetCovered ,TypeTextWithEntities ,TypeUser ,TypeWebPage 
    from ...tl .types .updates import TypeState 

class AffectedFoundMessages (TLObject ):
    CONSTRUCTOR_ID =0xef8d3e6c 
    SUBCLASS_OF_ID =0xf817652e 

    def __init__ (self ,pts :int ,pts_count :int ,offset :int ,messages :List [int ]):
        """"""
        self .pts =pts 
        self .pts_count =pts_count 
        self .offset =offset 
        self .messages =messages 

    def to_dict (self ):
        return {
        '_':'AffectedFoundMessages',
        'pts':self .pts ,
        'pts_count':self .pts_count ,
        'offset':self .offset ,
        'messages':[]if self .messages is None else self .messages [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'l>\x8d\xef',
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .pts_count ),
        struct .pack ('<i',self .offset ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (struct .pack ('<i',x )for x in self .messages ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pts =reader .read_int ()
        _pts_count =reader .read_int ()
        _offset =reader .read_int ()
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _messages .append (_x )

        return cls (pts =_pts ,pts_count =_pts_count ,offset =_offset ,messages =_messages )

class AffectedHistory (TLObject ):
    CONSTRUCTOR_ID =0xb45c69d1 
    SUBCLASS_OF_ID =0x2c49c116 

    def __init__ (self ,pts :int ,pts_count :int ,offset :int ):
        """"""
        self .pts =pts 
        self .pts_count =pts_count 
        self .offset =offset 

    def to_dict (self ):
        return {
        '_':'AffectedHistory',
        'pts':self .pts ,
        'pts_count':self .pts_count ,
        'offset':self .offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd1i\\\xb4',
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .pts_count ),
        struct .pack ('<i',self .offset ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pts =reader .read_int ()
        _pts_count =reader .read_int ()
        _offset =reader .read_int ()
        return cls (pts =_pts ,pts_count =_pts_count ,offset =_offset )

class AffectedMessages (TLObject ):
    CONSTRUCTOR_ID =0x84d19185 
    SUBCLASS_OF_ID =0xced3c06e 

    def __init__ (self ,pts :int ,pts_count :int ):
        """"""
        self .pts =pts 
        self .pts_count =pts_count 

    def to_dict (self ):
        return {
        '_':'AffectedMessages',
        'pts':self .pts ,
        'pts_count':self .pts_count 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x85\x91\xd1\x84',
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .pts_count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pts =reader .read_int ()
        _pts_count =reader .read_int ()
        return cls (pts =_pts ,pts_count =_pts_count )

class AllStickers (TLObject ):
    CONSTRUCTOR_ID =0xcdbbcebb 
    SUBCLASS_OF_ID =0x45834829 

    def __init__ (self ,hash :int ,sets :List ['TypeStickerSet']):
        """"""
        self .hash =hash 
        self .sets =sets 

    def to_dict (self ):
        return {
        '_':'AllStickers',
        'hash':self .hash ,
        'sets':[]if self .sets is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .sets ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbb\xce\xbb\xcd',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sets )),b''.join (x ._bytes ()for x in self .sets ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _sets =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _sets .append (_x )

        return cls (hash =_hash ,sets =_sets )

class AllStickersNotModified (TLObject ):
    CONSTRUCTOR_ID =0xe86602c3 
    SUBCLASS_OF_ID =0x45834829 

    def to_dict (self ):
        return {
        '_':'AllStickersNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc3\x02f\xe8',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ArchivedStickers (TLObject ):
    CONSTRUCTOR_ID =0x4fcba9c8 
    SUBCLASS_OF_ID =0x7296d771 

    def __init__ (self ,count :int ,sets :List ['TypeStickerSetCovered']):
        """"""
        self .count =count 
        self .sets =sets 

    def to_dict (self ):
        return {
        '_':'ArchivedStickers',
        'count':self .count ,
        'sets':[]if self .sets is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .sets ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc8\xa9\xcbO',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sets )),b''.join (x ._bytes ()for x in self .sets ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _sets =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _sets .append (_x )

        return cls (count =_count ,sets =_sets )

class AvailableReactions (TLObject ):
    CONSTRUCTOR_ID =0x768e3aad 
    SUBCLASS_OF_ID =0xe426ad82 

    def __init__ (self ,hash :int ,reactions :List ['TypeAvailableReaction']):
        """"""
        self .hash =hash 
        self .reactions =reactions 

    def to_dict (self ):
        return {
        '_':'AvailableReactions',
        'hash':self .hash ,
        'reactions':[]if self .reactions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .reactions ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xad:\x8ev',
        struct .pack ('<i',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .reactions )),b''.join (x ._bytes ()for x in self .reactions ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        reader .read_int ()
        _reactions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _reactions .append (_x )

        return cls (hash =_hash ,reactions =_reactions )

class AvailableReactionsNotModified (TLObject ):
    CONSTRUCTOR_ID =0x9f071957 
    SUBCLASS_OF_ID =0xe426ad82 

    def to_dict (self ):
        return {
        '_':'AvailableReactionsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'W\x19\x07\x9f',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class BotApp (TLObject ):
    CONSTRUCTOR_ID =0xeb50adf5 
    SUBCLASS_OF_ID =0x8f7243a7 

    def __init__ (self ,app :'TypeBotApp',inactive :Optional [bool ]=None ,request_write_access :Optional [bool ]=None ,has_settings :Optional [bool ]=None ):
        """"""
        self .app =app 
        self .inactive =inactive 
        self .request_write_access =request_write_access 
        self .has_settings =has_settings 

    def to_dict (self ):
        return {
        '_':'BotApp',
        'app':self .app .to_dict ()if isinstance (self .app ,TLObject )else self .app ,
        'inactive':self .inactive ,
        'request_write_access':self .request_write_access ,
        'has_settings':self .has_settings 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf5\xadP\xeb',
        struct .pack ('<I',(0 if self .inactive is None or self .inactive is False else 1 )|(0 if self .request_write_access is None or self .request_write_access is False else 2 )|(0 if self .has_settings is None or self .has_settings is False else 4 )),
        self .app ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _inactive =bool (flags &1 )
        _request_write_access =bool (flags &2 )
        _has_settings =bool (flags &4 )
        _app =reader .tgread_object ()
        return cls (app =_app ,inactive =_inactive ,request_write_access =_request_write_access ,has_settings =_has_settings )

class BotCallbackAnswer (TLObject ):
    CONSTRUCTOR_ID =0x36585ea4 
    SUBCLASS_OF_ID =0x6c4dd18c 

    def __init__ (self ,cache_time :int ,alert :Optional [bool ]=None ,has_url :Optional [bool ]=None ,native_ui :Optional [bool ]=None ,message :Optional [str ]=None ,url :Optional [str ]=None ):
        """"""
        self .cache_time =cache_time 
        self .alert =alert 
        self .has_url =has_url 
        self .native_ui =native_ui 
        self .message =message 
        self .url =url 

    def to_dict (self ):
        return {
        '_':'BotCallbackAnswer',
        'cache_time':self .cache_time ,
        'alert':self .alert ,
        'has_url':self .has_url ,
        'native_ui':self .native_ui ,
        'message':self .message ,
        'url':self .url 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa4^X6',
        struct .pack ('<I',(0 if self .alert is None or self .alert is False else 2 )|(0 if self .has_url is None or self .has_url is False else 8 )|(0 if self .native_ui is None or self .native_ui is False else 16 )|(0 if self .message is None or self .message is False else 1 )|(0 if self .url is None or self .url is False else 4 )),
        b''if self .message is None or self .message is False else (self .serialize_bytes (self .message )),
        b''if self .url is None or self .url is False else (self .serialize_bytes (self .url )),
        struct .pack ('<i',self .cache_time ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _alert =bool (flags &2 )
        _has_url =bool (flags &8 )
        _native_ui =bool (flags &16 )
        if flags &1 :
            _message =reader .tgread_string ()
        else :
            _message =None 
        if flags &4 :
            _url =reader .tgread_string ()
        else :
            _url =None 
        _cache_time =reader .read_int ()
        return cls (cache_time =_cache_time ,alert =_alert ,has_url =_has_url ,native_ui =_native_ui ,message =_message ,url =_url )

class BotResults (TLObject ):
    CONSTRUCTOR_ID =0xe021f2f6 
    SUBCLASS_OF_ID =0x3ed4d9c9 

    def __init__ (self ,query_id :int ,results :List ['TypeBotInlineResult'],cache_time :int ,users :List ['TypeUser'],gallery :Optional [bool ]=None ,next_offset :Optional [str ]=None ,switch_pm :Optional ['TypeInlineBotSwitchPM']=None ,switch_webview :Optional ['TypeInlineBotWebView']=None ):
        """"""
        self .query_id =query_id 
        self .results =results 
        self .cache_time =cache_time 
        self .users =users 
        self .gallery =gallery 
        self .next_offset =next_offset 
        self .switch_pm =switch_pm 
        self .switch_webview =switch_webview 

    def to_dict (self ):
        return {
        '_':'BotResults',
        'query_id':self .query_id ,
        'results':[]if self .results is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .results ],
        'cache_time':self .cache_time ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'gallery':self .gallery ,
        'next_offset':self .next_offset ,
        'switch_pm':self .switch_pm .to_dict ()if isinstance (self .switch_pm ,TLObject )else self .switch_pm ,
        'switch_webview':self .switch_webview .to_dict ()if isinstance (self .switch_webview ,TLObject )else self .switch_webview 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf6\xf2!\xe0',
        struct .pack ('<I',(0 if self .gallery is None or self .gallery is False else 1 )|(0 if self .next_offset is None or self .next_offset is False else 2 )|(0 if self .switch_pm is None or self .switch_pm is False else 4 )|(0 if self .switch_webview is None or self .switch_webview is False else 8 )),
        struct .pack ('<q',self .query_id ),
        b''if self .next_offset is None or self .next_offset is False else (self .serialize_bytes (self .next_offset )),
        b''if self .switch_pm is None or self .switch_pm is False else (self .switch_pm ._bytes ()),
        b''if self .switch_webview is None or self .switch_webview is False else (self .switch_webview ._bytes ()),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .results )),b''.join (x ._bytes ()for x in self .results ),
        struct .pack ('<i',self .cache_time ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _gallery =bool (flags &1 )
        _query_id =reader .read_long ()
        if flags &2 :
            _next_offset =reader .tgread_string ()
        else :
            _next_offset =None 
        if flags &4 :
            _switch_pm =reader .tgread_object ()
        else :
            _switch_pm =None 
        if flags &8 :
            _switch_webview =reader .tgread_object ()
        else :
            _switch_webview =None 
        reader .read_int ()
        _results =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _results .append (_x )

        _cache_time =reader .read_int ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (query_id =_query_id ,results =_results ,cache_time =_cache_time ,users =_users ,gallery =_gallery ,next_offset =_next_offset ,switch_pm =_switch_pm ,switch_webview =_switch_webview )

class ChannelMessages (TLObject ):
    CONSTRUCTOR_ID =0xc776ba4e 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,pts :int ,count :int ,messages :List ['TypeMessage'],topics :List ['TypeForumTopic'],chats :List ['TypeChat'],users :List ['TypeUser'],inexact :Optional [bool ]=None ,offset_id_offset :Optional [int ]=None ):
        """"""
        self .pts =pts 
        self .count =count 
        self .messages =messages 
        self .topics =topics 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .offset_id_offset =offset_id_offset 

    def to_dict (self ):
        return {
        '_':'ChannelMessages',
        'pts':self .pts ,
        'count':self .count ,
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'topics':[]if self .topics is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .topics ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'inexact':self .inexact ,
        'offset_id_offset':self .offset_id_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'N\xbav\xc7',
        struct .pack ('<I',(0 if self .inexact is None or self .inexact is False else 2 )|(0 if self .offset_id_offset is None or self .offset_id_offset is False else 4 )),
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .count ),
        b''if self .offset_id_offset is None or self .offset_id_offset is False else (struct .pack ('<i',self .offset_id_offset )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .topics )),b''.join (x ._bytes ()for x in self .topics ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _inexact =bool (flags &2 )
        _pts =reader .read_int ()
        _count =reader .read_int ()
        if flags &4 :
            _offset_id_offset =reader .read_int ()
        else :
            _offset_id_offset =None 
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

        reader .read_int ()
        _topics =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _topics .append (_x )

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

        return cls (pts =_pts ,count =_count ,messages =_messages ,topics =_topics ,chats =_chats ,users =_users ,inexact =_inexact ,offset_id_offset =_offset_id_offset )

class ChatAdminsWithInvites (TLObject ):
    CONSTRUCTOR_ID =0xb69b72d7 
    SUBCLASS_OF_ID =0x8f5bad2b 

    def __init__ (self ,admins :List ['TypeChatAdminWithInvites'],users :List ['TypeUser']):
        """"""
        self .admins =admins 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChatAdminsWithInvites',
        'admins':[]if self .admins is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .admins ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd7r\x9b\xb6',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .admins )),b''.join (x ._bytes ()for x in self .admins ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _admins =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _admins .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (admins =_admins ,users =_users )

class ChatFull (TLObject ):
    CONSTRUCTOR_ID =0xe5d7d19c 
    SUBCLASS_OF_ID =0x225a5109 

    def __init__ (self ,full_chat :'TypeChatFull',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .full_chat =full_chat 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChatFull',
        'full_chat':self .full_chat .to_dict ()if isinstance (self .full_chat ,TLObject )else self .full_chat ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x9c\xd1\xd7\xe5',
        self .full_chat ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _full_chat =reader .tgread_object ()
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

        return cls (full_chat =_full_chat ,chats =_chats ,users =_users )

class ChatInviteImporters (TLObject ):
    CONSTRUCTOR_ID =0x81b6b00a 
    SUBCLASS_OF_ID =0xd9bc8aa6 

    def __init__ (self ,count :int ,importers :List ['TypeChatInviteImporter'],users :List ['TypeUser']):
        """"""
        self .count =count 
        self .importers =importers 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ChatInviteImporters',
        'count':self .count ,
        'importers':[]if self .importers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .importers ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\n\xb0\xb6\x81',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .importers )),b''.join (x ._bytes ()for x in self .importers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _importers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _importers .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (count =_count ,importers =_importers ,users =_users )

class Chats (TLObject ):
    CONSTRUCTOR_ID =0x64ff9fd5 
    SUBCLASS_OF_ID =0x99d5cb14 

    def __init__ (self ,chats :List ['TypeChat']):
        """"""
        self .chats =chats 

    def to_dict (self ):
        return {
        '_':'Chats',
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd5\x9f\xffd',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        return cls (chats =_chats )

class ChatsSlice (TLObject ):
    CONSTRUCTOR_ID =0x9cd81144 
    SUBCLASS_OF_ID =0x99d5cb14 

    def __init__ (self ,count :int ,chats :List ['TypeChat']):
        """"""
        self .count =count 
        self .chats =chats 

    def to_dict (self ):
        return {
        '_':'ChatsSlice',
        'count':self .count ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ]
        }

    def _bytes (self ):
        return b''.join ((
        b'D\x11\xd8\x9c',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        return cls (count =_count ,chats =_chats )

class CheckedHistoryImportPeer (TLObject ):
    CONSTRUCTOR_ID =0xa24de717 
    SUBCLASS_OF_ID =0xb84bb337 

    def __init__ (self ,confirm_text :str ):
        """"""
        self .confirm_text =confirm_text 

    def to_dict (self ):
        return {
        '_':'CheckedHistoryImportPeer',
        'confirm_text':self .confirm_text 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x17\xe7M\xa2',
        self .serialize_bytes (self .confirm_text ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _confirm_text =reader .tgread_string ()
        return cls (confirm_text =_confirm_text )

class DhConfig (TLObject ):
    CONSTRUCTOR_ID =0x2c221edd 
    SUBCLASS_OF_ID =0xe488ed8b 

    def __init__ (self ,g :int ,p :bytes ,version :int ,random :bytes ):
        """"""
        self .g =g 
        self .p =p 
        self .version =version 
        self .random =random 

    def to_dict (self ):
        return {
        '_':'DhConfig',
        'g':self .g ,
        'p':self .p ,
        'version':self .version ,
        'random':self .random 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdd\x1e",',
        struct .pack ('<i',self .g ),
        self .serialize_bytes (self .p ),
        struct .pack ('<i',self .version ),
        self .serialize_bytes (self .random ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _g =reader .read_int ()
        _p =reader .tgread_bytes ()
        _version =reader .read_int ()
        _random =reader .tgread_bytes ()
        return cls (g =_g ,p =_p ,version =_version ,random =_random )

class DhConfigNotModified (TLObject ):
    CONSTRUCTOR_ID =0xc0e24635 
    SUBCLASS_OF_ID =0xe488ed8b 

    def __init__ (self ,random :bytes ):
        """"""
        self .random =random 

    def to_dict (self ):
        return {
        '_':'DhConfigNotModified',
        'random':self .random 
        }

    def _bytes (self ):
        return b''.join ((
        b'5F\xe2\xc0',
        self .serialize_bytes (self .random ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _random =reader .tgread_bytes ()
        return cls (random =_random )

class Dialogs (TLObject ):
    CONSTRUCTOR_ID =0x15ba6c40 
    SUBCLASS_OF_ID =0xe1b52ee 

    def __init__ (self ,dialogs :List ['TypeDialog'],messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .dialogs =dialogs 
        self .messages =messages 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'Dialogs',
        'dialogs':[]if self .dialogs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .dialogs ],
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'@l\xba\x15',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .dialogs )),b''.join (x ._bytes ()for x in self .dialogs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _dialogs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _dialogs .append (_x )

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (dialogs =_dialogs ,messages =_messages ,chats =_chats ,users =_users )

class DialogsNotModified (TLObject ):
    CONSTRUCTOR_ID =0xf0e3e596 
    SUBCLASS_OF_ID =0xe1b52ee 

    def __init__ (self ,count :int ):
        """"""
        self .count =count 

    def to_dict (self ):
        return {
        '_':'DialogsNotModified',
        'count':self .count 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x96\xe5\xe3\xf0',
        struct .pack ('<i',self .count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        return cls (count =_count )

class DialogsSlice (TLObject ):
    CONSTRUCTOR_ID =0x71e094f3 
    SUBCLASS_OF_ID =0xe1b52ee 

    def __init__ (self ,count :int ,dialogs :List ['TypeDialog'],messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .count =count 
        self .dialogs =dialogs 
        self .messages =messages 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'DialogsSlice',
        'count':self .count ,
        'dialogs':[]if self .dialogs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .dialogs ],
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf3\x94\xe0q',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .dialogs )),b''.join (x ._bytes ()for x in self .dialogs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _dialogs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _dialogs .append (_x )

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (count =_count ,dialogs =_dialogs ,messages =_messages ,chats =_chats ,users =_users )

class DiscussionMessage (TLObject ):
    CONSTRUCTOR_ID =0xa6341782 
    SUBCLASS_OF_ID =0x53f8e3e8 

    def __init__ (self ,messages :List ['TypeMessage'],unread_count :int ,chats :List ['TypeChat'],users :List ['TypeUser'],max_id :Optional [int ]=None ,read_inbox_max_id :Optional [int ]=None ,read_outbox_max_id :Optional [int ]=None ):
        """"""
        self .messages =messages 
        self .unread_count =unread_count 
        self .chats =chats 
        self .users =users 
        self .max_id =max_id 
        self .read_inbox_max_id =read_inbox_max_id 
        self .read_outbox_max_id =read_outbox_max_id 

    def to_dict (self ):
        return {
        '_':'DiscussionMessage',
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'unread_count':self .unread_count ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'max_id':self .max_id ,
        'read_inbox_max_id':self .read_inbox_max_id ,
        'read_outbox_max_id':self .read_outbox_max_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x82\x174\xa6',
        struct .pack ('<I',(0 if self .max_id is None or self .max_id is False else 1 )|(0 if self .read_inbox_max_id is None or self .read_inbox_max_id is False else 2 )|(0 if self .read_outbox_max_id is None or self .read_outbox_max_id is False else 4 )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b''if self .max_id is None or self .max_id is False else (struct .pack ('<i',self .max_id )),
        b''if self .read_inbox_max_id is None or self .read_inbox_max_id is False else (struct .pack ('<i',self .read_inbox_max_id )),
        b''if self .read_outbox_max_id is None or self .read_outbox_max_id is False else (struct .pack ('<i',self .read_outbox_max_id )),
        struct .pack ('<i',self .unread_count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

        if flags &1 :
            _max_id =reader .read_int ()
        else :
            _max_id =None 
        if flags &2 :
            _read_inbox_max_id =reader .read_int ()
        else :
            _read_inbox_max_id =None 
        if flags &4 :
            _read_outbox_max_id =reader .read_int ()
        else :
            _read_outbox_max_id =None 
        _unread_count =reader .read_int ()
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

        return cls (messages =_messages ,unread_count =_unread_count ,chats =_chats ,users =_users ,max_id =_max_id ,read_inbox_max_id =_read_inbox_max_id ,read_outbox_max_id =_read_outbox_max_id )

class EmojiGroups (TLObject ):
    CONSTRUCTOR_ID =0x881fb94b 
    SUBCLASS_OF_ID =0x7eca55d9 

    def __init__ (self ,hash :int ,groups :List ['TypeEmojiGroup']):
        """"""
        self .hash =hash 
        self .groups =groups 

    def to_dict (self ):
        return {
        '_':'EmojiGroups',
        'hash':self .hash ,
        'groups':[]if self .groups is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .groups ]
        }

    def _bytes (self ):
        return b''.join ((
        b'K\xb9\x1f\x88',
        struct .pack ('<i',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .groups )),b''.join (x ._bytes ()for x in self .groups ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_int ()
        reader .read_int ()
        _groups =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _groups .append (_x )

        return cls (hash =_hash ,groups =_groups )

class EmojiGroupsNotModified (TLObject ):
    CONSTRUCTOR_ID =0x6fb4ad87 
    SUBCLASS_OF_ID =0x7eca55d9 

    def to_dict (self ):
        return {
        '_':'EmojiGroupsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x87\xad\xb4o',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class ExportedChatInvite (TLObject ):
    CONSTRUCTOR_ID =0x1871be50 
    SUBCLASS_OF_ID =0x82dcd4ca 

    def __init__ (self ,invite :'TypeExportedChatInvite',users :List ['TypeUser']):
        """"""
        self .invite =invite 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ExportedChatInvite',
        'invite':self .invite .to_dict ()if isinstance (self .invite ,TLObject )else self .invite ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'P\xbeq\x18',
        self .invite ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _invite =reader .tgread_object ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (invite =_invite ,users =_users )

class ExportedChatInviteReplaced (TLObject ):
    CONSTRUCTOR_ID =0x222600ef 
    SUBCLASS_OF_ID =0x82dcd4ca 

    def __init__ (self ,invite :'TypeExportedChatInvite',new_invite :'TypeExportedChatInvite',users :List ['TypeUser']):
        """"""
        self .invite =invite 
        self .new_invite =new_invite 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ExportedChatInviteReplaced',
        'invite':self .invite .to_dict ()if isinstance (self .invite ,TLObject )else self .invite ,
        'new_invite':self .new_invite .to_dict ()if isinstance (self .new_invite ,TLObject )else self .new_invite ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xef\x00&"',
        self .invite ._bytes (),
        self .new_invite ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _invite =reader .tgread_object ()
        _new_invite =reader .tgread_object ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (invite =_invite ,new_invite =_new_invite ,users =_users )

class ExportedChatInvites (TLObject ):
    CONSTRUCTOR_ID =0xbdc62dcc 
    SUBCLASS_OF_ID =0x603d3871 

    def __init__ (self ,count :int ,invites :List ['TypeExportedChatInvite'],users :List ['TypeUser']):
        """"""
        self .count =count 
        self .invites =invites 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'ExportedChatInvites',
        'count':self .count ,
        'invites':[]if self .invites is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .invites ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcc-\xc6\xbd',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .invites )),b''.join (x ._bytes ()for x in self .invites ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _invites =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _invites .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (count =_count ,invites =_invites ,users =_users )

class FavedStickers (TLObject ):
    CONSTRUCTOR_ID =0x2cb51097 
    SUBCLASS_OF_ID =0x8e736fb9 

    def __init__ (self ,hash :int ,packs :List ['TypeStickerPack'],stickers :List ['TypeDocument']):
        """"""
        self .hash =hash 
        self .packs =packs 
        self .stickers =stickers 

    def to_dict (self ):
        return {
        '_':'FavedStickers',
        'hash':self .hash ,
        'packs':[]if self .packs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .packs ],
        'stickers':[]if self .stickers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .stickers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x97\x10\xb5,',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .packs )),b''.join (x ._bytes ()for x in self .packs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .stickers )),b''.join (x ._bytes ()for x in self .stickers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _packs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _packs .append (_x )

        reader .read_int ()
        _stickers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _stickers .append (_x )

        return cls (hash =_hash ,packs =_packs ,stickers =_stickers )

class FavedStickersNotModified (TLObject ):
    CONSTRUCTOR_ID =0x9e8fa6d3 
    SUBCLASS_OF_ID =0x8e736fb9 

    def to_dict (self ):
        return {
        '_':'FavedStickersNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd3\xa6\x8f\x9e',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class FeaturedStickers (TLObject ):
    CONSTRUCTOR_ID =0xbe382906 
    SUBCLASS_OF_ID =0x2614b722 

    def __init__ (self ,hash :int ,count :int ,sets :List ['TypeStickerSetCovered'],unread :List [int ],premium :Optional [bool ]=None ):
        """"""
        self .hash =hash 
        self .count =count 
        self .sets =sets 
        self .unread =unread 
        self .premium =premium 

    def to_dict (self ):
        return {
        '_':'FeaturedStickers',
        'hash':self .hash ,
        'count':self .count ,
        'sets':[]if self .sets is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .sets ],
        'unread':[]if self .unread is None else self .unread [:],
        'premium':self .premium 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x06)8\xbe',
        struct .pack ('<I',(0 if self .premium is None or self .premium is False else 1 )),
        struct .pack ('<q',self .hash ),
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sets )),b''.join (x ._bytes ()for x in self .sets ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .unread )),b''.join (struct .pack ('<q',x )for x in self .unread ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _premium =bool (flags &1 )
        _hash =reader .read_long ()
        _count =reader .read_int ()
        reader .read_int ()
        _sets =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _sets .append (_x )

        reader .read_int ()
        _unread =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_long ()
            _unread .append (_x )

        return cls (hash =_hash ,count =_count ,sets =_sets ,unread =_unread ,premium =_premium )

class FeaturedStickersNotModified (TLObject ):
    CONSTRUCTOR_ID =0xc6dc0c66 
    SUBCLASS_OF_ID =0x2614b722 

    def __init__ (self ,count :int ):
        """"""
        self .count =count 

    def to_dict (self ):
        return {
        '_':'FeaturedStickersNotModified',
        'count':self .count 
        }

    def _bytes (self ):
        return b''.join ((
        b'f\x0c\xdc\xc6',
        struct .pack ('<i',self .count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        return cls (count =_count )

class ForumTopics (TLObject ):
    CONSTRUCTOR_ID =0x367617d3 
    SUBCLASS_OF_ID =0x8e1d3e1e 

    def __init__ (self ,count :int ,topics :List ['TypeForumTopic'],messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],pts :int ,order_by_create_date :Optional [bool ]=None ):
        """"""
        self .count =count 
        self .topics =topics 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .pts =pts 
        self .order_by_create_date =order_by_create_date 

    def to_dict (self ):
        return {
        '_':'ForumTopics',
        'count':self .count ,
        'topics':[]if self .topics is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .topics ],
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'pts':self .pts ,
        'order_by_create_date':self .order_by_create_date 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd3\x17v6',
        struct .pack ('<I',(0 if self .order_by_create_date is None or self .order_by_create_date is False else 1 )),
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .topics )),b''.join (x ._bytes ()for x in self .topics ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        struct .pack ('<i',self .pts ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _order_by_create_date =bool (flags &1 )
        _count =reader .read_int ()
        reader .read_int ()
        _topics =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _topics .append (_x )

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        _pts =reader .read_int ()
        return cls (count =_count ,topics =_topics ,messages =_messages ,chats =_chats ,users =_users ,pts =_pts ,order_by_create_date =_order_by_create_date )

class FoundStickerSets (TLObject ):
    CONSTRUCTOR_ID =0x8af09dd2 
    SUBCLASS_OF_ID =0x40df361 

    def __init__ (self ,hash :int ,sets :List ['TypeStickerSetCovered']):
        """"""
        self .hash =hash 
        self .sets =sets 

    def to_dict (self ):
        return {
        '_':'FoundStickerSets',
        'hash':self .hash ,
        'sets':[]if self .sets is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .sets ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd2\x9d\xf0\x8a',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sets )),b''.join (x ._bytes ()for x in self .sets ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _sets =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _sets .append (_x )

        return cls (hash =_hash ,sets =_sets )

class FoundStickerSetsNotModified (TLObject ):
    CONSTRUCTOR_ID =0xd54b65d 
    SUBCLASS_OF_ID =0x40df361 

    def to_dict (self ):
        return {
        '_':'FoundStickerSetsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b']\xb6T\r',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class HighScores (TLObject ):
    CONSTRUCTOR_ID =0x9a3bfd99 
    SUBCLASS_OF_ID =0x6ccd95fd 

    def __init__ (self ,scores :List ['TypeHighScore'],users :List ['TypeUser']):
        """"""
        self .scores =scores 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'HighScores',
        'scores':[]if self .scores is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .scores ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x99\xfd;\x9a',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .scores )),b''.join (x ._bytes ()for x in self .scores ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _scores =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _scores .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (scores =_scores ,users =_users )

class HistoryImport (TLObject ):
    CONSTRUCTOR_ID =0x1662af0b 
    SUBCLASS_OF_ID =0xb18bb50a 

    def __init__ (self ,id :int ):
        """"""
        self .id =id 

    def to_dict (self ):
        return {
        '_':'HistoryImport',
        'id':self .id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x0b\xafb\x16',
        struct .pack ('<q',self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _id =reader .read_long ()
        return cls (id =_id )

class HistoryImportParsed (TLObject ):
    CONSTRUCTOR_ID =0x5e0fb7b9 
    SUBCLASS_OF_ID =0x5bb2720b 

    def __init__ (self ,pm :Optional [bool ]=None ,group :Optional [bool ]=None ,title :Optional [str ]=None ):
        """"""
        self .pm =pm 
        self .group =group 
        self .title =title 

    def to_dict (self ):
        return {
        '_':'HistoryImportParsed',
        'pm':self .pm ,
        'group':self .group ,
        'title':self .title 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb9\xb7\x0f^',
        struct .pack ('<I',(0 if self .pm is None or self .pm is False else 1 )|(0 if self .group is None or self .group is False else 2 )|(0 if self .title is None or self .title is False else 4 )),
        b''if self .title is None or self .title is False else (self .serialize_bytes (self .title )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _pm =bool (flags &1 )
        _group =bool (flags &2 )
        if flags &4 :
            _title =reader .tgread_string ()
        else :
            _title =None 
        return cls (pm =_pm ,group =_group ,title =_title )

class InactiveChats (TLObject ):
    CONSTRUCTOR_ID =0xa927fec5 
    SUBCLASS_OF_ID =0x8bf3d7d4 

    def __init__ (self ,dates :List [int ],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .dates =dates 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'InactiveChats',
        'dates':[]if self .dates is None else self .dates [:],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b"\xc5\xfe'\xa9",
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .dates )),b''.join (struct .pack ('<i',x )for x in self .dates ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _dates =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _dates .append (_x )

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

        return cls (dates =_dates ,chats =_chats ,users =_users )

class MessageEditData (TLObject ):
    CONSTRUCTOR_ID =0x26b5dde6 
    SUBCLASS_OF_ID =0xfb47949d 

    def __init__ (self ,caption :Optional [bool ]=None ):
        """"""
        self .caption =caption 

    def to_dict (self ):
        return {
        '_':'MessageEditData',
        'caption':self .caption 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xe6\xdd\xb5&',
        struct .pack ('<I',(0 if self .caption is None or self .caption is False else 1 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _caption =bool (flags &1 )
        return cls (caption =_caption )

class MessageReactionsList (TLObject ):
    CONSTRUCTOR_ID =0x31bd492d 
    SUBCLASS_OF_ID =0x60fce5e6 

    def __init__ (self ,count :int ,reactions :List ['TypeMessagePeerReaction'],chats :List ['TypeChat'],users :List ['TypeUser'],next_offset :Optional [str ]=None ):
        """"""
        self .count =count 
        self .reactions =reactions 
        self .chats =chats 
        self .users =users 
        self .next_offset =next_offset 

    def to_dict (self ):
        return {
        '_':'MessageReactionsList',
        'count':self .count ,
        'reactions':[]if self .reactions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .reactions ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'next_offset':self .next_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'-I\xbd1',
        struct .pack ('<I',(0 if self .next_offset is None or self .next_offset is False else 1 )),
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .reactions )),b''.join (x ._bytes ()for x in self .reactions ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        b''if self .next_offset is None or self .next_offset is False else (self .serialize_bytes (self .next_offset )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _count =reader .read_int ()
        reader .read_int ()
        _reactions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _reactions .append (_x )

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

        if flags &1 :
            _next_offset =reader .tgread_string ()
        else :
            _next_offset =None 
        return cls (count =_count ,reactions =_reactions ,chats =_chats ,users =_users ,next_offset =_next_offset )

class MessageViews (TLObject ):
    CONSTRUCTOR_ID =0xb6c4f543 
    SUBCLASS_OF_ID =0xafb5eb9c 

    def __init__ (self ,views :List ['TypeMessageViews'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .views =views 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'MessageViews',
        'views':[]if self .views is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .views ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'C\xf5\xc4\xb6',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .views )),b''.join (x ._bytes ()for x in self .views ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _views =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _views .append (_x )

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

        return cls (views =_views ,chats =_chats ,users =_users )

class Messages (TLObject ):
    CONSTRUCTOR_ID =0x8c718e87 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .messages =messages 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'Messages',
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x87\x8eq\x8c',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (messages =_messages ,chats =_chats ,users =_users )

class MessagesNotModified (TLObject ):
    CONSTRUCTOR_ID =0x74535f21 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,count :int ):
        """"""
        self .count =count 

    def to_dict (self ):
        return {
        '_':'MessagesNotModified',
        'count':self .count 
        }

    def _bytes (self ):
        return b''.join ((
        b'!_St',
        struct .pack ('<i',self .count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        return cls (count =_count )

class MessagesSlice (TLObject ):
    CONSTRUCTOR_ID =0x3a54685e 
    SUBCLASS_OF_ID =0xd4b40b5e 

    def __init__ (self ,count :int ,messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],inexact :Optional [bool ]=None ,next_rate :Optional [int ]=None ,offset_id_offset :Optional [int ]=None ):
        """"""
        self .count =count 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .next_rate =next_rate 
        self .offset_id_offset =offset_id_offset 

    def to_dict (self ):
        return {
        '_':'MessagesSlice',
        'count':self .count ,
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'inexact':self .inexact ,
        'next_rate':self .next_rate ,
        'offset_id_offset':self .offset_id_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'^hT:',
        struct .pack ('<I',(0 if self .inexact is None or self .inexact is False else 2 )|(0 if self .next_rate is None or self .next_rate is False else 1 )|(0 if self .offset_id_offset is None or self .offset_id_offset is False else 4 )),
        struct .pack ('<i',self .count ),
        b''if self .next_rate is None or self .next_rate is False else (struct .pack ('<i',self .next_rate )),
        b''if self .offset_id_offset is None or self .offset_id_offset is False else (struct .pack ('<i',self .offset_id_offset )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _inexact =bool (flags &2 )
        _count =reader .read_int ()
        if flags &1 :
            _next_rate =reader .read_int ()
        else :
            _next_rate =None 
        if flags &4 :
            _offset_id_offset =reader .read_int ()
        else :
            _offset_id_offset =None 
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (count =_count ,messages =_messages ,chats =_chats ,users =_users ,inexact =_inexact ,next_rate =_next_rate ,offset_id_offset =_offset_id_offset )

class PeerDialogs (TLObject ):
    CONSTRUCTOR_ID =0x3371c354 
    SUBCLASS_OF_ID =0x3ac70132 

    def __init__ (self ,dialogs :List ['TypeDialog'],messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],state :'TypeState'):
        """"""
        self .dialogs =dialogs 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .state =state 

    def to_dict (self ):
        return {
        '_':'PeerDialogs',
        'dialogs':[]if self .dialogs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .dialogs ],
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'state':self .state .to_dict ()if isinstance (self .state ,TLObject )else self .state 
        }

    def _bytes (self ):
        return b''.join ((
        b'T\xc3q3',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .dialogs )),b''.join (x ._bytes ()for x in self .dialogs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        self .state ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _dialogs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _dialogs .append (_x )

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        _state =reader .tgread_object ()
        return cls (dialogs =_dialogs ,messages =_messages ,chats =_chats ,users =_users ,state =_state )

class PeerSettings (TLObject ):
    CONSTRUCTOR_ID =0x6880b94d 
    SUBCLASS_OF_ID =0x65a2f7a1 

    def __init__ (self ,settings :'TypePeerSettings',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .settings =settings 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'PeerSettings',
        'settings':self .settings .to_dict ()if isinstance (self .settings ,TLObject )else self .settings ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'M\xb9\x80h',
        self .settings ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _settings =reader .tgread_object ()
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

        return cls (settings =_settings ,chats =_chats ,users =_users )

class Reactions (TLObject ):
    CONSTRUCTOR_ID =0xeafdf716 
    SUBCLASS_OF_ID =0xadc38324 

    def __init__ (self ,hash :int ,reactions :List ['TypeReaction']):
        """"""
        self .hash =hash 
        self .reactions =reactions 

    def to_dict (self ):
        return {
        '_':'Reactions',
        'hash':self .hash ,
        'reactions':[]if self .reactions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .reactions ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x16\xf7\xfd\xea',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .reactions )),b''.join (x ._bytes ()for x in self .reactions ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _reactions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _reactions .append (_x )

        return cls (hash =_hash ,reactions =_reactions )

class ReactionsNotModified (TLObject ):
    CONSTRUCTOR_ID =0xb06fdbdf 
    SUBCLASS_OF_ID =0xadc38324 

    def to_dict (self ):
        return {
        '_':'ReactionsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xdf\xdbo\xb0',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class RecentStickers (TLObject ):
    CONSTRUCTOR_ID =0x88d37c56 
    SUBCLASS_OF_ID =0xf76f8683 

    def __init__ (self ,hash :int ,packs :List ['TypeStickerPack'],stickers :List ['TypeDocument'],dates :List [int ]):
        """"""
        self .hash =hash 
        self .packs =packs 
        self .stickers =stickers 
        self .dates =dates 

    def to_dict (self ):
        return {
        '_':'RecentStickers',
        'hash':self .hash ,
        'packs':[]if self .packs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .packs ],
        'stickers':[]if self .stickers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .stickers ],
        'dates':[]if self .dates is None else self .dates [:]
        }

    def _bytes (self ):
        return b''.join ((
        b'V|\xd3\x88',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .packs )),b''.join (x ._bytes ()for x in self .packs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .stickers )),b''.join (x ._bytes ()for x in self .stickers ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .dates )),b''.join (struct .pack ('<i',x )for x in self .dates ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _packs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _packs .append (_x )

        reader .read_int ()
        _stickers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _stickers .append (_x )

        reader .read_int ()
        _dates =[]
        for _ in range (reader .read_int ()):
            _x =reader .read_int ()
            _dates .append (_x )

        return cls (hash =_hash ,packs =_packs ,stickers =_stickers ,dates =_dates )

class RecentStickersNotModified (TLObject ):
    CONSTRUCTOR_ID =0xb17f890 
    SUBCLASS_OF_ID =0xf76f8683 

    def to_dict (self ):
        return {
        '_':'RecentStickersNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x90\xf8\x17\x0b',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SavedGifs (TLObject ):
    CONSTRUCTOR_ID =0x84a02a0d 
    SUBCLASS_OF_ID =0xa68b61f5 

    def __init__ (self ,hash :int ,gifs :List ['TypeDocument']):
        """"""
        self .hash =hash 
        self .gifs =gifs 

    def to_dict (self ):
        return {
        '_':'SavedGifs',
        'hash':self .hash ,
        'gifs':[]if self .gifs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .gifs ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\r*\xa0\x84',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .gifs )),b''.join (x ._bytes ()for x in self .gifs ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _gifs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _gifs .append (_x )

        return cls (hash =_hash ,gifs =_gifs )

class SavedGifsNotModified (TLObject ):
    CONSTRUCTOR_ID =0xe8025ca2 
    SUBCLASS_OF_ID =0xa68b61f5 

    def to_dict (self ):
        return {
        '_':'SavedGifsNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa2\\\x02\xe8',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class SearchCounter (TLObject ):
    CONSTRUCTOR_ID =0xe844ebff 
    SUBCLASS_OF_ID =0xd6a7bfa2 

    def __init__ (self ,filter :'TypeMessagesFilter',count :int ,inexact :Optional [bool ]=None ):
        """"""
        self .filter =filter 
        self .count =count 
        self .inexact =inexact 

    def to_dict (self ):
        return {
        '_':'SearchCounter',
        'filter':self .filter .to_dict ()if isinstance (self .filter ,TLObject )else self .filter ,
        'count':self .count ,
        'inexact':self .inexact 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xff\xebD\xe8',
        struct .pack ('<I',(0 if self .inexact is None or self .inexact is False else 2 )),
        self .filter ._bytes (),
        struct .pack ('<i',self .count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _inexact =bool (flags &2 )
        _filter =reader .tgread_object ()
        _count =reader .read_int ()
        return cls (filter =_filter ,count =_count ,inexact =_inexact )

class SearchResultsCalendar (TLObject ):
    CONSTRUCTOR_ID =0x147ee23c 
    SUBCLASS_OF_ID =0x92c5640f 

    def __init__ (self ,count :int ,min_date :Optional [datetime ],min_msg_id :int ,periods :List ['TypeSearchResultsCalendarPeriod'],messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],inexact :Optional [bool ]=None ,offset_id_offset :Optional [int ]=None ):
        """"""
        self .count =count 
        self .min_date =min_date 
        self .min_msg_id =min_msg_id 
        self .periods =periods 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .inexact =inexact 
        self .offset_id_offset =offset_id_offset 

    def to_dict (self ):
        return {
        '_':'SearchResultsCalendar',
        'count':self .count ,
        'min_date':self .min_date ,
        'min_msg_id':self .min_msg_id ,
        'periods':[]if self .periods is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .periods ],
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'inexact':self .inexact ,
        'offset_id_offset':self .offset_id_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'<\xe2~\x14',
        struct .pack ('<I',(0 if self .inexact is None or self .inexact is False else 1 )|(0 if self .offset_id_offset is None or self .offset_id_offset is False else 2 )),
        struct .pack ('<i',self .count ),
        self .serialize_datetime (self .min_date ),
        struct .pack ('<i',self .min_msg_id ),
        b''if self .offset_id_offset is None or self .offset_id_offset is False else (struct .pack ('<i',self .offset_id_offset )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .periods )),b''.join (x ._bytes ()for x in self .periods ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _inexact =bool (flags &1 )
        _count =reader .read_int ()
        _min_date =reader .tgread_date ()
        _min_msg_id =reader .read_int ()
        if flags &2 :
            _offset_id_offset =reader .read_int ()
        else :
            _offset_id_offset =None 
        reader .read_int ()
        _periods =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _periods .append (_x )

        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (count =_count ,min_date =_min_date ,min_msg_id =_min_msg_id ,periods =_periods ,messages =_messages ,chats =_chats ,users =_users ,inexact =_inexact ,offset_id_offset =_offset_id_offset )

class SearchResultsPositions (TLObject ):
    CONSTRUCTOR_ID =0x53b22baf 
    SUBCLASS_OF_ID =0xd963708d 

    def __init__ (self ,count :int ,positions :List ['TypeSearchResultsPosition']):
        """"""
        self .count =count 
        self .positions =positions 

    def to_dict (self ):
        return {
        '_':'SearchResultsPositions',
        'count':self .count ,
        'positions':[]if self .positions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .positions ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xaf+\xb2S',
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .positions )),b''.join (x ._bytes ()for x in self .positions ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _count =reader .read_int ()
        reader .read_int ()
        _positions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _positions .append (_x )

        return cls (count =_count ,positions =_positions )

class SentEncryptedFile (TLObject ):
    CONSTRUCTOR_ID =0x9493ff32 
    SUBCLASS_OF_ID =0xc99e3e50 

    def __init__ (self ,date :Optional [datetime ],file :'TypeEncryptedFile'):
        """"""
        self .date =date 
        self .file =file 

    def to_dict (self ):
        return {
        '_':'SentEncryptedFile',
        'date':self .date ,
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file 
        }

    def _bytes (self ):
        return b''.join ((
        b'2\xff\x93\x94',
        self .serialize_datetime (self .date ),
        self .file ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _date =reader .tgread_date ()
        _file =reader .tgread_object ()
        return cls (date =_date ,file =_file )

class SentEncryptedMessage (TLObject ):
    CONSTRUCTOR_ID =0x560f8935 
    SUBCLASS_OF_ID =0xc99e3e50 

    def __init__ (self ,date :Optional [datetime ]):
        """"""
        self .date =date 

    def to_dict (self ):
        return {
        '_':'SentEncryptedMessage',
        'date':self .date 
        }

    def _bytes (self ):
        return b''.join ((
        b'5\x89\x0fV',
        self .serialize_datetime (self .date ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _date =reader .tgread_date ()
        return cls (date =_date )

class SponsoredMessages (TLObject ):
    CONSTRUCTOR_ID =0xc9ee1d87 
    SUBCLASS_OF_ID =0x7f4169e0 

    def __init__ (self ,messages :List ['TypeSponsoredMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],posts_between :Optional [int ]=None ):
        """"""
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .posts_between =posts_between 

    def to_dict (self ):
        return {
        '_':'SponsoredMessages',
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'posts_between':self .posts_between 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x87\x1d\xee\xc9',
        struct .pack ('<I',(0 if self .posts_between is None or self .posts_between is False else 1 )),
        b''if self .posts_between is None or self .posts_between is False else (struct .pack ('<i',self .posts_between )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _posts_between =reader .read_int ()
        else :
            _posts_between =None 
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

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

        return cls (messages =_messages ,chats =_chats ,users =_users ,posts_between =_posts_between )

class SponsoredMessagesEmpty (TLObject ):
    CONSTRUCTOR_ID =0x1839490f 
    SUBCLASS_OF_ID =0x7f4169e0 

    def to_dict (self ):
        return {
        '_':'SponsoredMessagesEmpty'
        }

    def _bytes (self ):
        return b''.join ((
        b'\x0fI9\x18',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class StickerSet (TLObject ):
    CONSTRUCTOR_ID =0x6e153f16 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,set :'TypeStickerSet',packs :List ['TypeStickerPack'],keywords :List ['TypeStickerKeyword'],documents :List ['TypeDocument']):
        """"""
        self .set =set 
        self .packs =packs 
        self .keywords =keywords 
        self .documents =documents 

    def to_dict (self ):
        return {
        '_':'StickerSet',
        'set':self .set .to_dict ()if isinstance (self .set ,TLObject )else self .set ,
        'packs':[]if self .packs is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .packs ],
        'keywords':[]if self .keywords is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .keywords ],
        'documents':[]if self .documents is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .documents ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x16?\x15n',
        self .set ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .packs )),b''.join (x ._bytes ()for x in self .packs ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .keywords )),b''.join (x ._bytes ()for x in self .keywords ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .documents )),b''.join (x ._bytes ()for x in self .documents ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _set =reader .tgread_object ()
        reader .read_int ()
        _packs =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _packs .append (_x )

        reader .read_int ()
        _keywords =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _keywords .append (_x )

        reader .read_int ()
        _documents =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _documents .append (_x )

        return cls (set =_set ,packs =_packs ,keywords =_keywords ,documents =_documents )

class StickerSetInstallResultArchive (TLObject ):
    CONSTRUCTOR_ID =0x35e410a8 
    SUBCLASS_OF_ID =0x67cb3fe8 

    def __init__ (self ,sets :List ['TypeStickerSetCovered']):
        """"""
        self .sets =sets 

    def to_dict (self ):
        return {
        '_':'StickerSetInstallResultArchive',
        'sets':[]if self .sets is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .sets ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa8\x10\xe45',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .sets )),b''.join (x ._bytes ()for x in self .sets ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _sets =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _sets .append (_x )

        return cls (sets =_sets )

class StickerSetInstallResultSuccess (TLObject ):
    CONSTRUCTOR_ID =0x38641628 
    SUBCLASS_OF_ID =0x67cb3fe8 

    def to_dict (self ):
        return {
        '_':'StickerSetInstallResultSuccess'
        }

    def _bytes (self ):
        return b''.join ((
        b'(\x16d8',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class StickerSetNotModified (TLObject ):
    CONSTRUCTOR_ID =0xd3f924eb 
    SUBCLASS_OF_ID =0x9b704a5a 

    def to_dict (self ):
        return {
        '_':'StickerSetNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'\xeb$\xf9\xd3',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class Stickers (TLObject ):
    CONSTRUCTOR_ID =0x30a6ec7e 
    SUBCLASS_OF_ID =0xd73bb9de 

    def __init__ (self ,hash :int ,stickers :List ['TypeDocument']):
        """"""
        self .hash =hash 
        self .stickers =stickers 

    def to_dict (self ):
        return {
        '_':'Stickers',
        'hash':self .hash ,
        'stickers':[]if self .stickers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .stickers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'~\xec\xa60',
        struct .pack ('<q',self .hash ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .stickers )),b''.join (x ._bytes ()for x in self .stickers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _hash =reader .read_long ()
        reader .read_int ()
        _stickers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _stickers .append (_x )

        return cls (hash =_hash ,stickers =_stickers )

class StickersNotModified (TLObject ):
    CONSTRUCTOR_ID =0xf1749a22 
    SUBCLASS_OF_ID =0xd73bb9de 

    def to_dict (self ):
        return {
        '_':'StickersNotModified'
        }

    def _bytes (self ):
        return b''.join ((
        b'"\x9at\xf1',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class TranscribedAudio (TLObject ):
    CONSTRUCTOR_ID =0x93752c52 
    SUBCLASS_OF_ID =0x21b24936 

    def __init__ (self ,transcription_id :int ,text :str ,pending :Optional [bool ]=None ):
        """"""
        self .transcription_id =transcription_id 
        self .text =text 
        self .pending =pending 

    def to_dict (self ):
        return {
        '_':'TranscribedAudio',
        'transcription_id':self .transcription_id ,
        'text':self .text ,
        'pending':self .pending 
        }

    def _bytes (self ):
        return b''.join ((
        b'R,u\x93',
        struct .pack ('<I',(0 if self .pending is None or self .pending is False else 1 )),
        struct .pack ('<q',self .transcription_id ),
        self .serialize_bytes (self .text ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _pending =bool (flags &1 )
        _transcription_id =reader .read_long ()
        _text =reader .tgread_string ()
        return cls (transcription_id =_transcription_id ,text =_text ,pending =_pending )

class TranslateResult (TLObject ):
    CONSTRUCTOR_ID =0x33db32f8 
    SUBCLASS_OF_ID =0x24243e8 

    def __init__ (self ,result :List ['TypeTextWithEntities']):
        """"""
        self .result =result 

    def to_dict (self ):
        return {
        '_':'TranslateResult',
        'result':[]if self .result is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .result ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xf82\xdb3',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .result )),b''.join (x ._bytes ()for x in self .result ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _result =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _result .append (_x )

        return cls (result =_result )

class VotesList (TLObject ):
    CONSTRUCTOR_ID =0x4899484e 
    SUBCLASS_OF_ID =0xc2199885 

    def __init__ (self ,count :int ,votes :List ['TypeMessagePeerVote'],chats :List ['TypeChat'],users :List ['TypeUser'],next_offset :Optional [str ]=None ):
        """"""
        self .count =count 
        self .votes =votes 
        self .chats =chats 
        self .users =users 
        self .next_offset =next_offset 

    def to_dict (self ):
        return {
        '_':'VotesList',
        'count':self .count ,
        'votes':[]if self .votes is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .votes ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'next_offset':self .next_offset 
        }

    def _bytes (self ):
        return b''.join ((
        b'NH\x99H',
        struct .pack ('<I',(0 if self .next_offset is None or self .next_offset is False else 1 )),
        struct .pack ('<i',self .count ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .votes )),b''.join (x ._bytes ()for x in self .votes ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        b''if self .next_offset is None or self .next_offset is False else (self .serialize_bytes (self .next_offset )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _count =reader .read_int ()
        reader .read_int ()
        _votes =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _votes .append (_x )

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

        if flags &1 :
            _next_offset =reader .tgread_string ()
        else :
            _next_offset =None 
        return cls (count =_count ,votes =_votes ,chats =_chats ,users =_users ,next_offset =_next_offset )

class WebPage (TLObject ):
    CONSTRUCTOR_ID =0xfd5e12bd 
    SUBCLASS_OF_ID =0x2cf8b154 

    def __init__ (self ,webpage :'TypeWebPage',chats :List ['TypeChat'],users :List ['TypeUser']):
        """"""
        self .webpage =webpage 
        self .chats =chats 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'WebPage',
        'webpage':self .webpage .to_dict ()if isinstance (self .webpage ,TLObject )else self .webpage ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbd\x12^\xfd',
        self .webpage ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _webpage =reader .tgread_object ()
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

        return cls (webpage =_webpage ,chats =_chats ,users =_users )

