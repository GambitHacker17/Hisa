import time 

from .inlineresult import InlineResult 

class InlineResults (list ):
    """"""
    def __init__ (self ,client ,original ,*,entity =None ):
        super ().__init__ (InlineResult (client ,x ,original .query_id ,entity =entity )
        for x in original .results )

        self .result =original 
        self .query_id =original .query_id 
        self .cache_time =original .cache_time 
        self ._valid_until =time .time ()+self .cache_time 
        self .users =original .users 
        self .gallery =bool (original .gallery )
        self .next_offset =original .next_offset 
        self .switch_pm =original .switch_pm 

    def results_valid (self ):
        """"""
        return time .time ()<self ._valid_until 

    def _to_str (self ,item_function ):
        return ('[{}, query_id={}, cache_time={}, users={}, gallery={}, '
        'next_offset={}, switch_pm={}]'.format (
        ', '.join (item_function (x )for x in self ),
        self .query_id ,
        self .cache_time ,
        self .users ,
        self .gallery ,
        self .next_offset ,
        self .switch_pm 
        ))

    def __str__ (self ):
        return self ._to_str (str )

    def __repr__ (self ):
        return self ._to_str (repr )
