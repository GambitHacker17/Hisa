
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class MegagroupStats (TLObject ):
    """"""

    __slots__ :List [str ]=["period","members","messages","viewers","posters","growth_graph","members_graph","new_members_by_source_graph","languages_graph","messages_graph","actions_graph","top_hours_graph","weekdays_graph","top_posters","top_admins","top_inviters","users"]

    ID =0xef7ff916 
    QUALNAME ="types.stats.MegagroupStats"

    def __init__ (self ,*,period :"raw.base.StatsDateRangeDays",members :"raw.base.StatsAbsValueAndPrev",messages :"raw.base.StatsAbsValueAndPrev",viewers :"raw.base.StatsAbsValueAndPrev",posters :"raw.base.StatsAbsValueAndPrev",growth_graph :"raw.base.StatsGraph",members_graph :"raw.base.StatsGraph",new_members_by_source_graph :"raw.base.StatsGraph",languages_graph :"raw.base.StatsGraph",messages_graph :"raw.base.StatsGraph",actions_graph :"raw.base.StatsGraph",top_hours_graph :"raw.base.StatsGraph",weekdays_graph :"raw.base.StatsGraph",top_posters :List ["raw.base.StatsGroupTopPoster"],top_admins :List ["raw.base.StatsGroupTopAdmin"],top_inviters :List ["raw.base.StatsGroupTopInviter"],users :List ["raw.base.User"])->None :
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

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"MegagroupStats":

        period =TLObject .read (b )

        members =TLObject .read (b )

        messages =TLObject .read (b )

        viewers =TLObject .read (b )

        posters =TLObject .read (b )

        growth_graph =TLObject .read (b )

        members_graph =TLObject .read (b )

        new_members_by_source_graph =TLObject .read (b )

        languages_graph =TLObject .read (b )

        messages_graph =TLObject .read (b )

        actions_graph =TLObject .read (b )

        top_hours_graph =TLObject .read (b )

        weekdays_graph =TLObject .read (b )

        top_posters =TLObject .read (b )

        top_admins =TLObject .read (b )

        top_inviters =TLObject .read (b )

        users =TLObject .read (b )

        return MegagroupStats (period =period ,members =members ,messages =messages ,viewers =viewers ,posters =posters ,growth_graph =growth_graph ,members_graph =members_graph ,new_members_by_source_graph =new_members_by_source_graph ,languages_graph =languages_graph ,messages_graph =messages_graph ,actions_graph =actions_graph ,top_hours_graph =top_hours_graph ,weekdays_graph =weekdays_graph ,top_posters =top_posters ,top_admins =top_admins ,top_inviters =top_inviters ,users =users )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        b .write (self .period .write ())

        b .write (self .members .write ())

        b .write (self .messages .write ())

        b .write (self .viewers .write ())

        b .write (self .posters .write ())

        b .write (self .growth_graph .write ())

        b .write (self .members_graph .write ())

        b .write (self .new_members_by_source_graph .write ())

        b .write (self .languages_graph .write ())

        b .write (self .messages_graph .write ())

        b .write (self .actions_graph .write ())

        b .write (self .top_hours_graph .write ())

        b .write (self .weekdays_graph .write ())

        b .write (Vector (self .top_posters ))

        b .write (Vector (self .top_admins ))

        b .write (Vector (self .top_inviters ))

        b .write (Vector (self .users ))

        return b .getvalue ()
