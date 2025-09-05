""""""
import asyncio 
import datetime 
import time 
import logging 
from enum import Enum 
from .session import SessionState ,ChannelState 
from ..tl import types as tl ,functions as fn 
from ..helpers import get_running_loop 

NO_SEQ =0 

BOT_CHANNEL_DIFF_LIMIT =100000 
USER_CHANNEL_DIFF_LIMIT =100 

POSSIBLE_GAP_TIMEOUT =0.5 

NO_UPDATES_TIMEOUT =15 *60 

ENTRY_ACCOUNT =object ()

ENTRY_SECRET =object ()

LOG_LEVEL_TRACE =(logging .DEBUG -logging .NOTSET )//2 

_sentinel =object ()

def next_updates_deadline ():
    return get_running_loop ().time ()+NO_UPDATES_TIMEOUT 

class GapError (ValueError ):
    def __repr__ (self ):
        return 'GapError()'

class PrematureEndReason (Enum ):
    TEMPORARY_SERVER_ISSUES ='tmp'
    BANNED ='ban'

class PtsInfo :
    __slots__ =('pts','pts_count','entry')

    def __init__ (
    self ,
    pts :int ,
    pts_count :int ,
    entry :object 
    ):
        self .pts =pts 
        self .pts_count =pts_count 
        self .entry =entry 

    @classmethod 
    def from_update (cls ,update ):
        pts =getattr (update ,'pts',None )
        if pts :
            pts_count =getattr (update ,'pts_count',None )or 0 
            try :
                entry =update .message .peer_id .channel_id 
            except AttributeError :
                entry =getattr (update ,'channel_id',None )or ENTRY_ACCOUNT 
            return cls (pts =pts ,pts_count =pts_count ,entry =entry )

        qts =getattr (update ,'qts',None )
        if qts :
            pts_count =1 if isinstance (update ,tl .UpdateNewEncryptedMessage )else 0 
            return cls (pts =qts ,pts_count =pts_count ,entry =ENTRY_SECRET )

        return None 

    def __repr__ (self ):
        if self .entry is ENTRY_ACCOUNT :
            entry ='ENTRY_ACCOUNT'
        elif self .entry is ENTRY_SECRET :
            entry ='ENTRY_SECRET'
        else :
            entry =self .entry 
        return f'PtsInfo(pts={self .pts }, pts_count={self .pts_count }, entry={entry })'

class State :
    __slots__ =('pts','deadline')

    def __init__ (
    self ,

    pts :int ,

    deadline :float 
    ):
        self .pts =pts 
        self .deadline =deadline 

    def __repr__ (self ):
        return f'State(pts={self .pts }, deadline={self .deadline })'

class PossibleGap :
    __slots__ =('deadline','updates')

    def __init__ (
    self ,
    deadline :float ,

    updates :list 
    ):
        self .deadline =deadline 
        self .updates =updates 

    def __repr__ (self ):
        return f'PossibleGap(deadline={self .deadline }, update_count={len (self .updates )})'

class MessageBox :
    __slots__ =('_log','map','date','seq','next_deadline','possible_gaps','getting_diff_for','reset_deadlines_for')

    def __init__ (
    self ,
    log ,

    map :dict =_sentinel ,

    date :datetime .datetime =datetime .datetime (*time .gmtime (0 )[:6 ]).replace (tzinfo =datetime .timezone .utc ),
    seq :int =NO_SEQ ,

    next_deadline :object =None ,

    possible_gaps :dict =_sentinel ,

    getting_diff_for :set =_sentinel ,

    reset_deadlines_for :set =_sentinel 
    ):
        self ._log =log 
        self .map ={}if map is _sentinel else map 
        self .date =date 
        self .seq =seq 
        self .next_deadline =next_deadline 
        self .possible_gaps ={}if possible_gaps is _sentinel else possible_gaps 
        self .getting_diff_for =set ()if getting_diff_for is _sentinel else getting_diff_for 
        self .reset_deadlines_for =set ()if reset_deadlines_for is _sentinel else reset_deadlines_for 

        if __debug__ :

            self ._trace ('ENTRY_ACCOUNT = %r; ENTRY_SECRET = %r',ENTRY_ACCOUNT ,ENTRY_SECRET )
            self ._trace ('Created new MessageBox with map = %r, date = %r, seq = %r',self .map ,self .date ,self .seq )

    def _trace (self ,msg ,*args ,**kwargs ):

        self ._log .log (LOG_LEVEL_TRACE ,msg ,*args ,**kwargs )

    def load (self ,session_state ,channel_states ):
        """"""
        if __debug__ :
            self ._trace ('Loading MessageBox with session_state = %r, channel_states = %r',session_state ,channel_states )

        deadline =next_updates_deadline ()

        self .map .clear ()
        if session_state .pts !=NO_SEQ :
            self .map [ENTRY_ACCOUNT ]=State (pts =session_state .pts ,deadline =deadline )
        if session_state .qts !=NO_SEQ :
            self .map [ENTRY_SECRET ]=State (pts =session_state .qts ,deadline =deadline )
        self .map .update ((s .channel_id ,State (pts =s .pts ,deadline =deadline ))for s in channel_states )

        self .date =datetime .datetime .fromtimestamp (session_state .date ).replace (tzinfo =datetime .timezone .utc )
        self .seq =session_state .seq 
        self .next_deadline =ENTRY_ACCOUNT 

    def session_state (self ):
        """"""
        return dict (
        pts =self .map [ENTRY_ACCOUNT ].pts if ENTRY_ACCOUNT in self .map else NO_SEQ ,
        qts =self .map [ENTRY_SECRET ].pts if ENTRY_SECRET in self .map else NO_SEQ ,
        date =self .date ,
        seq =self .seq ,
        ),{id :state .pts for id ,state in self .map .items ()if isinstance (id ,int )}

    def is_empty (self )->bool :
        """"""
        return ENTRY_ACCOUNT not in self .map 

    def check_deadlines (self ):
        """"""
        now =get_running_loop ().time ()

        if self .getting_diff_for :
            return now 

        deadline =next_updates_deadline ()

        if self .possible_gaps :
            deadline =min (deadline ,*(gap .deadline for gap in self .possible_gaps .values ()))
        elif self .next_deadline in self .map :
            deadline =min (deadline ,self .map [self .next_deadline ].deadline )

        if now >=deadline :

            self .getting_diff_for .update (entry for entry ,gap in self .possible_gaps .items ()if now >gap .deadline )
            self .getting_diff_for .update (entry for entry ,state in self .map .items ()if now >state .deadline )

            if __debug__ :
                self ._trace ('Deadlines met, now getting diff for %r',self .getting_diff_for )

            for entry in self .getting_diff_for :
                self .possible_gaps .pop (entry ,None )

        return deadline 

    def reset_deadline (self ,entry ,deadline ):
        if entry not in self .map :
            raise RuntimeError ('Called reset_deadline on an entry for which we do not have state')
        self .map [entry ].deadline =deadline 

        if self .next_deadline ==entry :

            self .next_deadline =min (self .map .items (),key =lambda entry_state :entry_state [1 ].deadline )[0 ]
        elif self .next_deadline in self .map and deadline <self .map [self .next_deadline ].deadline :

            self .next_deadline =entry 

    def reset_channel_deadline (self ,channel_id ,timeout ):
        self .reset_deadline (channel_id ,get_running_loop ().time ()+(timeout or NO_UPDATES_TIMEOUT ))

    def apply_deadlines_reset (self ):
        next_deadline =next_updates_deadline ()

        reset_deadlines_for =self .reset_deadlines_for 
        self .reset_deadlines_for =set ()

        for entry in reset_deadlines_for :
            self .reset_deadline (entry ,next_deadline )

        reset_deadlines_for .clear ()
        self .reset_deadlines_for =reset_deadlines_for 

    def set_state (self ,state ,reset =True ):
        if __debug__ :
            self ._trace ('Setting state %s',state )

        deadline =next_updates_deadline ()

        if state .pts !=NO_SEQ or not reset :
            self .map [ENTRY_ACCOUNT ]=State (pts =state .pts ,deadline =deadline )
        else :
            self .map .pop (ENTRY_ACCOUNT ,None )

        if state .qts !=NO_SEQ or not reset :
            self .map [ENTRY_SECRET ]=State (pts =state .qts ,deadline =deadline )
        else :
            self .map .pop (ENTRY_SECRET ,None )

        self .date =state .date 
        self .seq =state .seq 

    def try_set_channel_state (self ,id ,pts ):
        if __debug__ :
            self ._trace ('Trying to set channel state for %r: %r',id ,pts )

        if id not in self .map :
            self .map [id ]=State (pts =pts ,deadline =next_updates_deadline ())

    def try_begin_get_diff (self ,entry ):
        if entry not in self .map :

            if entry in self .possible_gaps :
                raise RuntimeError ('Should not have a possible_gap for an entry not in the state map')

            return 

        self .getting_diff_for .add (entry )
        self .possible_gaps .pop (entry ,None )

    def end_get_diff (self ,entry ):
        try :
            self .getting_diff_for .remove (entry )
        except KeyError :
            raise RuntimeError ('Called end_get_diff on an entry which was not getting diff for')

        self .reset_deadline (entry ,next_updates_deadline ())
        assert entry not in self .possible_gaps ,"gaps shouldn't be created while getting difference"

    def process_updates (
    self ,
    updates ,
    chat_hashes ,
    result ,
    ):
        if __debug__ :
            self ._trace ('Processing updates %s',updates )

        date =getattr (updates ,'date',None )
        if date is None :

            self .try_begin_get_diff (ENTRY_ACCOUNT )
            raise GapError 

        self_outgoing =getattr (updates ,'_self_outgoing',False )
        real_result =result 
        result =[]

        seq =getattr (updates ,'seq',None )or NO_SEQ 
        seq_start =getattr (updates ,'seq_start',None )or seq 
        users =getattr (updates ,'users',None )or []
        chats =getattr (updates ,'chats',None )or []

        updates =getattr (updates ,'updates',None )or [updates .update if isinstance (updates ,tl .UpdateShort )else updates ]

        for u in updates :
            u ._self_outgoing =self_outgoing 

        if seq_start !=NO_SEQ :
            if self .seq +1 >seq_start :

                return (users ,chats )
            elif self .seq +1 <seq_start :

                self .try_begin_get_diff (ENTRY_ACCOUNT )
                raise GapError 

            self .date =date 
            if seq !=NO_SEQ :
                self .seq =seq 

        def _sort_gaps (update ):
            pts =PtsInfo .from_update (update )
            return pts .pts -pts .pts_count if pts else 0 

        result .extend (filter (None ,(
        self .apply_pts_info (u ,reset_deadline =True )for u in sorted (updates ,key =_sort_gaps ))))

        self .apply_deadlines_reset ()

        if self .possible_gaps :

            for key in list (self .possible_gaps .keys ()):
                self .possible_gaps [key ].updates .sort (key =_sort_gaps )

                for _ in range (len (self .possible_gaps [key ].updates )):
                    update =self .possible_gaps [key ].updates .pop (0 )

                    update =self .apply_pts_info (update ,reset_deadline =False )
                    if update :
                        result .append (update )

            self .possible_gaps ={entry :gap for entry ,gap in self .possible_gaps .items ()if gap .updates }

        real_result .extend (u for u in result if not u ._self_outgoing )

        return (users ,chats )

    def apply_pts_info (
    self ,
    update ,
    *,
    reset_deadline ,
    ):

        if isinstance (update ,tl .UpdateChannelTooLong ):
            self .try_begin_get_diff (update .channel_id )
            return None 

        pts =PtsInfo .from_update (update )
        if not pts :

            return update 

        if reset_deadline :
            self .reset_deadlines_for .add (pts .entry )

        if pts .entry in self .getting_diff_for :

            return None 

        if pts .entry in self .map :
            local_pts =self .map [pts .entry ].pts 
            if local_pts +pts .pts_count >pts .pts :

                return None 
            elif local_pts +pts .pts_count <pts .pts :

                if pts .entry not in self .possible_gaps :
                    self .possible_gaps [pts .entry ]=PossibleGap (
                    deadline =get_running_loop ().time ()+POSSIBLE_GAP_TIMEOUT ,
                    updates =[]
                    )

                self .possible_gaps [pts .entry ].updates .append (update )
                return None 
            else :

                pass 

        if pts .entry in self .map :
            self .map [pts .entry ].pts =pts .pts 
        else :

            self .map [pts .entry ]=State (
            pts =(pts .pts -(0 if pts .pts_count else 1 ))or 1 ,
            deadline =next_updates_deadline ()
            )

        return update 

    def get_difference (self ):
        for entry in (ENTRY_ACCOUNT ,ENTRY_SECRET ):
            if entry in self .getting_diff_for :
                if entry not in self .map :
                    raise RuntimeError ('Should not try to get difference for an entry without known state')

                gd =fn .updates .GetDifferenceRequest (
                pts =self .map [ENTRY_ACCOUNT ].pts ,
                pts_total_limit =None ,
                date =self .date ,
                qts =self .map [ENTRY_SECRET ].pts if ENTRY_SECRET in self .map else NO_SEQ ,
                )
                if __debug__ :
                    self ._trace ('Requesting account difference %s',gd )
                return gd 

        return None 

    def apply_difference (
    self ,
    diff ,
    chat_hashes ,
    ):
        if __debug__ :
            self ._trace ('Applying account difference %s',diff )

        finish =None 
        result =None 

        if isinstance (diff ,tl .updates .DifferenceEmpty ):
            finish =True 
            self .date =diff .date 
            self .seq =diff .seq 
            result =[],[],[]
        elif isinstance (diff ,tl .updates .Difference ):
            finish =True 
            chat_hashes .extend (diff .users ,diff .chats )
            result =self .apply_difference_type (diff ,chat_hashes )
        elif isinstance (diff ,tl .updates .DifferenceSlice ):
            finish =False 
            chat_hashes .extend (diff .users ,diff .chats )
            result =self .apply_difference_type (diff ,chat_hashes )
        elif isinstance (diff ,tl .updates .DifferenceTooLong ):
            finish =True 
            self .map [ENTRY_ACCOUNT ].pts =diff .pts 
            result =[],[],[]

        if finish :
            account =ENTRY_ACCOUNT in self .getting_diff_for 
            secret =ENTRY_SECRET in self .getting_diff_for 

            if not account and not secret :
                raise RuntimeError ('Should not be applying the difference when neither account or secret was diff was active')

            if account :
                self .end_get_diff (ENTRY_ACCOUNT )
            if secret :
                self .end_get_diff (ENTRY_SECRET )

        return result 

    def apply_difference_type (
    self ,
    diff ,
    chat_hashes ,
    ):
        state =getattr (diff ,'intermediate_state',None )or diff .state 
        self .set_state (state ,reset =False )

        updates =[]
        self .process_updates (tl .Updates (
        updates =diff .other_updates ,
        users =diff .users ,
        chats =diff .chats ,
        date =1 ,
        seq =NO_SEQ ,
        ),chat_hashes ,updates )

        updates .extend (tl .UpdateNewMessage (
        message =m ,
        pts =NO_SEQ ,
        pts_count =NO_SEQ ,
        )for m in diff .new_messages )
        updates .extend (tl .UpdateNewEncryptedMessage (
        message =m ,
        qts =NO_SEQ ,
        )for m in diff .new_encrypted_messages )

        return updates ,diff .users ,diff .chats 

    def end_difference (self ):
        if __debug__ :
            self ._trace ('Ending account difference')

        account =ENTRY_ACCOUNT in self .getting_diff_for 
        secret =ENTRY_SECRET in self .getting_diff_for 

        if not account and not secret :
            raise RuntimeError ('Should not be ending get difference when neither account or secret was diff was active')

        if account :
            self .end_get_diff (ENTRY_ACCOUNT )
        if secret :
            self .end_get_diff (ENTRY_SECRET )

    def get_channel_difference (
    self ,
    chat_hashes ,
    ):
        entry =next ((id for id in self .getting_diff_for if isinstance (id ,int )),None )
        if not entry :
            return None 

        packed =chat_hashes .get (entry )
        if not packed :

            self .end_get_diff (entry )

            self .map .pop (entry ,None )
            return None 

        state =self .map .get (entry )
        if not state :
            raise RuntimeError ('Should not try to get difference for an entry without known state')

        gd =fn .updates .GetChannelDifferenceRequest (
        force =False ,
        channel =tl .InputChannel (packed .id ,packed .hash ),
        filter =tl .ChannelMessagesFilterEmpty (),
        pts =state .pts ,
        limit =BOT_CHANNEL_DIFF_LIMIT if chat_hashes .self_bot else USER_CHANNEL_DIFF_LIMIT 
        )
        if __debug__ :
            self ._trace ('Requesting channel difference %s',gd )
        return gd 

    def apply_channel_difference (
    self ,
    request ,
    diff ,
    chat_hashes ,
    ):
        entry =request .channel .channel_id 
        if __debug__ :
            self ._trace ('Applying channel difference for %r: %s',entry ,diff )

        self .possible_gaps .pop (entry ,None )

        if isinstance (diff ,tl .updates .ChannelDifferenceEmpty ):
            assert diff .final 
            self .end_get_diff (entry )
            self .map [entry ].pts =diff .pts 
            return [],[],[]
        elif isinstance (diff ,tl .updates .ChannelDifferenceTooLong ):
            assert diff .final 
            self .map [entry ].pts =diff .dialog .pts 
            chat_hashes .extend (diff .users ,diff .chats )
            self .reset_channel_deadline (entry ,diff .timeout )

            return [],[],[]
        elif isinstance (diff ,tl .updates .ChannelDifference ):
            if diff .final :
                self .end_get_diff (entry )

            self .map [entry ].pts =diff .pts 
            chat_hashes .extend (diff .users ,diff .chats )

            updates =[]
            self .process_updates (tl .Updates (
            updates =diff .other_updates ,
            users =diff .users ,
            chats =diff .chats ,
            date =1 ,
            seq =NO_SEQ ,
            ),chat_hashes ,updates )

            updates .extend (tl .UpdateNewChannelMessage (
            message =m ,
            pts =NO_SEQ ,
            pts_count =NO_SEQ ,
            )for m in diff .new_messages )
            self .reset_channel_deadline (entry ,None )

            return updates ,diff .users ,diff .chats 

    def end_channel_difference (self ,request ,reason :PrematureEndReason ,chat_hashes ):
        entry =request .channel .channel_id 
        if __debug__ :
            self ._trace ('Ending channel difference for %r because %s',entry ,reason )

        if reason ==PrematureEndReason .TEMPORARY_SERVER_ISSUES :

            self .possible_gaps .pop (entry ,None )
            self .end_get_diff (entry )
        elif reason ==PrematureEndReason .BANNED :

            self .possible_gaps .pop (entry ,None )
            self .end_get_diff (entry )
            del self .map [entry ]
        else :
            raise RuntimeError ('Unknown reason to end channel difference')

