""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeMessageInteractionCounters ,TypeStatsAbsValueAndPrev ,TypeStatsDateRangeDays ,TypeStatsGraph ,TypeStatsGroupTopAdmin ,TypeStatsGroupTopInviter ,TypeStatsGroupTopPoster ,TypeStatsPercentValue ,TypeUser 

class BroadcastStats (TLObject ):
    CONSTRUCTOR_ID =0xbdf78394 
    SUBCLASS_OF_ID =0x7ff25428 

    def __init__ (self ,period :'TypeStatsDateRangeDays',followers :'TypeStatsAbsValueAndPrev',views_per_post :'TypeStatsAbsValueAndPrev',shares_per_post :'TypeStatsAbsValueAndPrev',enabled_notifications :'TypeStatsPercentValue',growth_graph :'TypeStatsGraph',followers_graph :'TypeStatsGraph',mute_graph :'TypeStatsGraph',top_hours_graph :'TypeStatsGraph',interactions_graph :'TypeStatsGraph',iv_interactions_graph :'TypeStatsGraph',views_by_source_graph :'TypeStatsGraph',new_followers_by_source_graph :'TypeStatsGraph',languages_graph :'TypeStatsGraph',recent_message_interactions :List ['TypeMessageInteractionCounters']):
        """"""
        self .period =period 
        self .followers =followers 
        self .views_per_post =views_per_post 
        self .shares_per_post =shares_per_post 
        self .enabled_notifications =enabled_notifications 
        self .growth_graph =growth_graph 
        self .followers_graph =followers_graph 
        self .mute_graph =mute_graph 
        self .top_hours_graph =top_hours_graph 
        self .interactions_graph =interactions_graph 
        self .iv_interactions_graph =iv_interactions_graph 
        self .views_by_source_graph =views_by_source_graph 
        self .new_followers_by_source_graph =new_followers_by_source_graph 
        self .languages_graph =languages_graph 
        self .recent_message_interactions =recent_message_interactions 

    def to_dict (self ):
        return {
        '_':'BroadcastStats',
        'period':self .period .to_dict ()if isinstance (self .period ,TLObject )else self .period ,
        'followers':self .followers .to_dict ()if isinstance (self .followers ,TLObject )else self .followers ,
        'views_per_post':self .views_per_post .to_dict ()if isinstance (self .views_per_post ,TLObject )else self .views_per_post ,
        'shares_per_post':self .shares_per_post .to_dict ()if isinstance (self .shares_per_post ,TLObject )else self .shares_per_post ,
        'enabled_notifications':self .enabled_notifications .to_dict ()if isinstance (self .enabled_notifications ,TLObject )else self .enabled_notifications ,
        'growth_graph':self .growth_graph .to_dict ()if isinstance (self .growth_graph ,TLObject )else self .growth_graph ,
        'followers_graph':self .followers_graph .to_dict ()if isinstance (self .followers_graph ,TLObject )else self .followers_graph ,
        'mute_graph':self .mute_graph .to_dict ()if isinstance (self .mute_graph ,TLObject )else self .mute_graph ,
        'top_hours_graph':self .top_hours_graph .to_dict ()if isinstance (self .top_hours_graph ,TLObject )else self .top_hours_graph ,
        'interactions_graph':self .interactions_graph .to_dict ()if isinstance (self .interactions_graph ,TLObject )else self .interactions_graph ,
        'iv_interactions_graph':self .iv_interactions_graph .to_dict ()if isinstance (self .iv_interactions_graph ,TLObject )else self .iv_interactions_graph ,
        'views_by_source_graph':self .views_by_source_graph .to_dict ()if isinstance (self .views_by_source_graph ,TLObject )else self .views_by_source_graph ,
        'new_followers_by_source_graph':self .new_followers_by_source_graph .to_dict ()if isinstance (self .new_followers_by_source_graph ,TLObject )else self .new_followers_by_source_graph ,
        'languages_graph':self .languages_graph .to_dict ()if isinstance (self .languages_graph ,TLObject )else self .languages_graph ,
        'recent_message_interactions':[]if self .recent_message_interactions is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .recent_message_interactions ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x94\x83\xf7\xbd',
        self .period ._bytes (),
        self .followers ._bytes (),
        self .views_per_post ._bytes (),
        self .shares_per_post ._bytes (),
        self .enabled_notifications ._bytes (),
        self .growth_graph ._bytes (),
        self .followers_graph ._bytes (),
        self .mute_graph ._bytes (),
        self .top_hours_graph ._bytes (),
        self .interactions_graph ._bytes (),
        self .iv_interactions_graph ._bytes (),
        self .views_by_source_graph ._bytes (),
        self .new_followers_by_source_graph ._bytes (),
        self .languages_graph ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .recent_message_interactions )),b''.join (x ._bytes ()for x in self .recent_message_interactions ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _period =reader .tgread_object ()
        _followers =reader .tgread_object ()
        _views_per_post =reader .tgread_object ()
        _shares_per_post =reader .tgread_object ()
        _enabled_notifications =reader .tgread_object ()
        _growth_graph =reader .tgread_object ()
        _followers_graph =reader .tgread_object ()
        _mute_graph =reader .tgread_object ()
        _top_hours_graph =reader .tgread_object ()
        _interactions_graph =reader .tgread_object ()
        _iv_interactions_graph =reader .tgread_object ()
        _views_by_source_graph =reader .tgread_object ()
        _new_followers_by_source_graph =reader .tgread_object ()
        _languages_graph =reader .tgread_object ()
        reader .read_int ()
        _recent_message_interactions =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _recent_message_interactions .append (_x )

        return cls (period =_period ,followers =_followers ,views_per_post =_views_per_post ,shares_per_post =_shares_per_post ,enabled_notifications =_enabled_notifications ,growth_graph =_growth_graph ,followers_graph =_followers_graph ,mute_graph =_mute_graph ,top_hours_graph =_top_hours_graph ,interactions_graph =_interactions_graph ,iv_interactions_graph =_iv_interactions_graph ,views_by_source_graph =_views_by_source_graph ,new_followers_by_source_graph =_new_followers_by_source_graph ,languages_graph =_languages_graph ,recent_message_interactions =_recent_message_interactions )

class MegagroupStats (TLObject ):
    CONSTRUCTOR_ID =0xef7ff916 
    SUBCLASS_OF_ID =0x5b59be8d 

    def __init__ (self ,period :'TypeStatsDateRangeDays',members :'TypeStatsAbsValueAndPrev',messages :'TypeStatsAbsValueAndPrev',viewers :'TypeStatsAbsValueAndPrev',posters :'TypeStatsAbsValueAndPrev',growth_graph :'TypeStatsGraph',members_graph :'TypeStatsGraph',new_members_by_source_graph :'TypeStatsGraph',languages_graph :'TypeStatsGraph',messages_graph :'TypeStatsGraph',actions_graph :'TypeStatsGraph',top_hours_graph :'TypeStatsGraph',weekdays_graph :'TypeStatsGraph',top_posters :List ['TypeStatsGroupTopPoster'],top_admins :List ['TypeStatsGroupTopAdmin'],top_inviters :List ['TypeStatsGroupTopInviter'],users :List ['TypeUser']):
        """"""
        self .period =period 
        self .members =members 
        self .messages =messages 
        self .viewers =viewers 
        self .posters =posters 
        self .growth_graph =growth_graph 
        self .members_graph =members_graph 
        self .new_members_by_source_graph =new_members_by_source_graph 
        self .languages_graph =languages_graph 
        self .messages_graph =messages_graph 
        self .actions_graph =actions_graph 
        self .top_hours_graph =top_hours_graph 
        self .weekdays_graph =weekdays_graph 
        self .top_posters =top_posters 
        self .top_admins =top_admins 
        self .top_inviters =top_inviters 
        self .users =users 

    def to_dict (self ):
        return {
        '_':'MegagroupStats',
        'period':self .period .to_dict ()if isinstance (self .period ,TLObject )else self .period ,
        'members':self .members .to_dict ()if isinstance (self .members ,TLObject )else self .members ,
        'messages':self .messages .to_dict ()if isinstance (self .messages ,TLObject )else self .messages ,
        'viewers':self .viewers .to_dict ()if isinstance (self .viewers ,TLObject )else self .viewers ,
        'posters':self .posters .to_dict ()if isinstance (self .posters ,TLObject )else self .posters ,
        'growth_graph':self .growth_graph .to_dict ()if isinstance (self .growth_graph ,TLObject )else self .growth_graph ,
        'members_graph':self .members_graph .to_dict ()if isinstance (self .members_graph ,TLObject )else self .members_graph ,
        'new_members_by_source_graph':self .new_members_by_source_graph .to_dict ()if isinstance (self .new_members_by_source_graph ,TLObject )else self .new_members_by_source_graph ,
        'languages_graph':self .languages_graph .to_dict ()if isinstance (self .languages_graph ,TLObject )else self .languages_graph ,
        'messages_graph':self .messages_graph .to_dict ()if isinstance (self .messages_graph ,TLObject )else self .messages_graph ,
        'actions_graph':self .actions_graph .to_dict ()if isinstance (self .actions_graph ,TLObject )else self .actions_graph ,
        'top_hours_graph':self .top_hours_graph .to_dict ()if isinstance (self .top_hours_graph ,TLObject )else self .top_hours_graph ,
        'weekdays_graph':self .weekdays_graph .to_dict ()if isinstance (self .weekdays_graph ,TLObject )else self .weekdays_graph ,
        'top_posters':[]if self .top_posters is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .top_posters ],
        'top_admins':[]if self .top_admins is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .top_admins ],
        'top_inviters':[]if self .top_inviters is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .top_inviters ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x16\xf9\x7f\xef',
        self .period ._bytes (),
        self .members ._bytes (),
        self .messages ._bytes (),
        self .viewers ._bytes (),
        self .posters ._bytes (),
        self .growth_graph ._bytes (),
        self .members_graph ._bytes (),
        self .new_members_by_source_graph ._bytes (),
        self .languages_graph ._bytes (),
        self .messages_graph ._bytes (),
        self .actions_graph ._bytes (),
        self .top_hours_graph ._bytes (),
        self .weekdays_graph ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .top_posters )),b''.join (x ._bytes ()for x in self .top_posters ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .top_admins )),b''.join (x ._bytes ()for x in self .top_admins ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .top_inviters )),b''.join (x ._bytes ()for x in self .top_inviters ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _period =reader .tgread_object ()
        _members =reader .tgread_object ()
        _messages =reader .tgread_object ()
        _viewers =reader .tgread_object ()
        _posters =reader .tgread_object ()
        _growth_graph =reader .tgread_object ()
        _members_graph =reader .tgread_object ()
        _new_members_by_source_graph =reader .tgread_object ()
        _languages_graph =reader .tgread_object ()
        _messages_graph =reader .tgread_object ()
        _actions_graph =reader .tgread_object ()
        _top_hours_graph =reader .tgread_object ()
        _weekdays_graph =reader .tgread_object ()
        reader .read_int ()
        _top_posters =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _top_posters .append (_x )

        reader .read_int ()
        _top_admins =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _top_admins .append (_x )

        reader .read_int ()
        _top_inviters =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _top_inviters .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (period =_period ,members =_members ,messages =_messages ,viewers =_viewers ,posters =_posters ,growth_graph =_growth_graph ,members_graph =_members_graph ,new_members_by_source_graph =_new_members_by_source_graph ,languages_graph =_languages_graph ,messages_graph =_messages_graph ,actions_graph =_actions_graph ,top_hours_graph =_top_hours_graph ,weekdays_graph =_weekdays_graph ,top_posters =_top_posters ,top_admins =_top_admins ,top_inviters =_top_inviters ,users =_users )

class MessageStats (TLObject ):
    CONSTRUCTOR_ID =0x8999f295 
    SUBCLASS_OF_ID =0x9604a322 

    def __init__ (self ,views_graph :'TypeStatsGraph'):
        """"""
        self .views_graph =views_graph 

    def to_dict (self ):
        return {
        '_':'MessageStats',
        'views_graph':self .views_graph .to_dict ()if isinstance (self .views_graph ,TLObject )else self .views_graph 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x95\xf2\x99\x89',
        self .views_graph ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _views_graph =reader .tgread_object ()
        return cls (views_graph =_views_graph )

