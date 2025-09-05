from .common import EventBuilder 
from ..import utils 

class Raw (EventBuilder ):
    """"""
    def __init__ (self ,types =None ,*,func =None ):
        super ().__init__ (func =func )
        if not types :
            self .types =None 
        elif not utils .is_list_like (types ):
            if not isinstance (types ,type ):
                raise TypeError ('Invalid input type given: {}'.format (types ))

            self .types =types 
        else :
            if not all (isinstance (x ,type )for x in types ):
                raise TypeError ('Invalid input types given: {}'.format (types ))

            self .types =tuple (types )

    async def resolve (self ,client ):
        self .resolved =True 

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):
        return update 

    def filter (self ,event ):
        if not self .types or isinstance (event ,self .types ):
            if self .func :

                return self .func (event )
            return event 
