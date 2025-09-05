import abc 

class SenderGetter (abc .ABC ):
    """"""
    def __init__ (self ,sender_id =None ,*,sender =None ,input_sender =None ):
        self ._sender_id =sender_id 
        self ._sender =sender 
        self ._input_sender =input_sender 
        self ._client =None 

    @property 
    def sender (self ):
        """"""
        return self ._sender 

    async def get_sender (self ):
        """"""

        if (self ._sender is None or getattr (self ._sender ,'min',None ))and await self .get_input_sender ():

            if self ._sender is None or getattr (self ._sender ,'min',None ):
                try :
                    self ._sender =await self ._client .get_entity (self ._input_sender )
                except ValueError :
                    await self ._refetch_sender ()
        return self ._sender 

    @property 
    def input_sender (self ):
        """"""
        if self ._input_sender is None and self ._sender_id and self ._client :
            try :
                self ._input_sender =self ._client ._entity_cache [self ._sender_id ]
            except KeyError :
                pass 
        return self ._input_sender 

    async def get_input_sender (self ):
        """"""
        if self .input_sender is None and self ._sender_id and self ._client :
            await self ._refetch_sender ()
        return self ._input_sender 

    @property 
    def sender_id (self ):
        """"""
        return self ._sender_id 

    async def _refetch_sender (self ):
        """"""
