
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class BroadcastStats (TLObject ):
    """"""

    __slots__ :List [str ]=["period","followers","views_per_post","shares_per_post","enabled_notifications","growth_graph","followers_graph","mute_graph","top_hours_graph","interactions_graph","iv_interactions_graph","views_by_source_graph","new_followers_by_source_graph","languages_graph","recent_message_interactions"]

    ID =0xbdf78394 
    QUALNAME ="types.stats.BroadcastStats"

    def __init__ (self ,*,period :"raw.base.StatsDateRangeDays",followers :"raw.base.StatsAbsValueAndPrev",views_per_post :"raw.base.StatsAbsValueAndPrev",shares_per_post :"raw.base.StatsAbsValueAndPrev",enabled_notifications :"raw.base.StatsPercentValue",growth_graph :"raw.base.StatsGraph",followers_graph :"raw.base.StatsGraph",mute_graph :"raw.base.StatsGraph",top_hours_graph :"raw.base.StatsGraph",interactions_graph :"raw.base.StatsGraph",iv_interactions_graph :"raw.base.StatsGraph",views_by_source_graph :"raw.base.StatsGraph",new_followers_by_source_graph :"raw.base.StatsGraph",languages_graph :"raw.base.StatsGraph",recent_message_interactions :List ["raw.base.MessageInteractionCounters"])->None :
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

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"BroadcastStats":

        period =TLObject .read (b )

        followers =TLObject .read (b )

        views_per_post =TLObject .read (b )

        shares_per_post =TLObject .read (b )

        enabled_notifications =TLObject .read (b )

        growth_graph =TLObject .read (b )

        followers_graph =TLObject .read (b )

        mute_graph =TLObject .read (b )

        top_hours_graph =TLObject .read (b )

        interactions_graph =TLObject .read (b )

        iv_interactions_graph =TLObject .read (b )

        views_by_source_graph =TLObject .read (b )

        new_followers_by_source_graph =TLObject .read (b )

        languages_graph =TLObject .read (b )

        recent_message_interactions =TLObject .read (b )

        return BroadcastStats (period =period ,followers =followers ,views_per_post =views_per_post ,shares_per_post =shares_per_post ,enabled_notifications =enabled_notifications ,growth_graph =growth_graph ,followers_graph =followers_graph ,mute_graph =mute_graph ,top_hours_graph =top_hours_graph ,interactions_graph =interactions_graph ,iv_interactions_graph =iv_interactions_graph ,views_by_source_graph =views_by_source_graph ,new_followers_by_source_graph =new_followers_by_source_graph ,languages_graph =languages_graph ,recent_message_interactions =recent_message_interactions )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .period .write ())

        b .write (self .followers .write ())

        b .write (self .views_per_post .write ())

        b .write (self .shares_per_post .write ())

        b .write (self .enabled_notifications .write ())

        b .write (self .growth_graph .write ())

        b .write (self .followers_graph .write ())

        b .write (self .mute_graph .write ())

        b .write (self .top_hours_graph .write ())

        b .write (self .interactions_graph .write ())

        b .write (self .iv_interactions_graph .write ())

        b .write (self .views_by_source_graph .write ())

        b .write (self .new_followers_by_source_graph .write ())

        b .write (self .languages_graph .write ())

        b .write (Vector (self .recent_message_interactions ))

        return b .getvalue ()
