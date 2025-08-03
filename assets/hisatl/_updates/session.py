from typing import Optional ,Tuple 
from enum import IntEnum 
from ..tl .types import InputPeerUser ,InputPeerChat ,InputPeerChannel 

class SessionState :
    """"""
    __slots__ =('user_id','dc_id','bot','pts','qts','date','seq','takeout_id')

    def __init__ (
    self ,
    user_id :int ,
    dc_id :int ,
    bot :bool ,
    pts :int ,
    qts :int ,
    date :int ,
    seq :int ,
    takeout_id :Optional [int ]
    ):
        self .user_id =user_id 
        self .dc_id =dc_id 
        self .bot =bot 
        self .pts =pts 
        self .qts =qts 
        self .date =date 
        self .seq =seq 
        self .takeout_id =takeout_id 

    def __repr__ (self ):
        return repr ({k :getattr (self ,k )for k in self .__slots__ })

class ChannelState :
    """"""
    __slots__ =('channel_id','pts')

    def __init__ (
    self ,
    channel_id :int ,
    pts :int ,
    ):
        self .channel_id =channel_id 
        self .pts =pts 

    def __repr__ (self ):
        return repr ({k :getattr (self ,k )for k in self .__slots__ })

class EntityType (IntEnum ):
    """"""
    USER =ord ('U')
    BOT =ord ('B')
    GROUP =ord ('G')
    CHANNEL =ord ('C')
    MEGAGROUP =ord ('M')
    GIGAGROUP =ord ('E')

    def canonical (self ):
        """"""
        return _canon_entity_types [self ]

_canon_entity_types ={
EntityType .USER :EntityType .USER ,
EntityType .BOT :EntityType .USER ,
EntityType .GROUP :EntityType .GROUP ,
EntityType .CHANNEL :EntityType .CHANNEL ,
EntityType .MEGAGROUP :EntityType .CHANNEL ,
EntityType .GIGAGROUP :EntityType .CHANNEL ,
}

class Entity :
    """"""
    __slots__ =('ty','id','hash')

    def __init__ (
    self ,
    ty :EntityType ,
    id :int ,
    hash :int 
    ):
        self .ty =ty 
        self .id =id 
        self .hash =hash 

    @property 
    def is_user (self ):
        """"""
        return self .ty in (EntityType .USER ,EntityType .BOT )

    @property 
    def is_group (self ):
        """"""
        return self .ty in (EntityType .GROUP ,EntityType .MEGAGROUP )

    @property 
    def is_broadcast (self ):
        """"""
        return self .ty in (EntityType .CHANNEL ,EntityType .GIGAGROUP )

    @classmethod 
    def from_str (cls ,string :str ):
        """"""
        try :
            ty ,id ,hash =string .split ('.')
            ty ,id ,hash =ord (ty ),int (id ),int (hash )
        except AttributeError :
            raise TypeError (f'expected str, got {string!r}')from None 
        except (TypeError ,ValueError ):
            raise ValueError (f'malformed entity str (must be T.id.hash), got {string!r}')from None 

        return cls (EntityType (ty ),id ,hash )

    @classmethod 
    def from_bytes (cls ,blob ):
        """"""
        try :
            ty ,id ,hash =struct .unpack ('<Bqq',blob )
        except struct .error :
            raise ValueError (f'malformed entity data, got {string!r}')from None 

        return cls (EntityType (ty ),id ,hash )

    def __str__ (self ):
        return f'{chr (self .ty )}.{self .id }.{self .hash }'

    def __bytes__ (self ):
        return struct .pack ('<Bqq',self .ty ,self .id ,self .hash )

    def _as_input_peer (self ):
        if self .is_user :
            return InputPeerUser (self .id ,self .hash )
        elif self .ty ==EntityType .GROUP :
            return InputPeerChat (self .id )
        else :
            return InputPeerChannel (self .id ,self .hash )

    def __repr__ (self ):
        return repr ({k :getattr (self ,k )for k in self .__slots__ })
