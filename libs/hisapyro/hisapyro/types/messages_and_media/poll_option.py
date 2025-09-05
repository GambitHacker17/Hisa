
import hisapyro 
from ..object import Object 

class PollOption (Object ):
    """"""

    def __init__ (
    self ,
    *,
    client :"hisapyro.Client"=None ,
    text :str ,
    voter_count :int ,
    data :bytes 
    ):
        super ().__init__ (client )

        self .text =text 
        self .voter_count =voter_count 
        self .data =data 
