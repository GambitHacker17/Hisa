import abc 

from ...import errors ,utils 
from ...tl import types 

class ChatGetter (abc .ABC ):
    """"""
    def __init__ (self ,chat_peer =None ,*,input_chat =None ,chat =None ,broadcast =None ):
        self ._chat_peer =chat_peer 
        self ._input_chat =input_chat 
        self ._chat =chat 
        self ._broadcast =broadcast 
        self ._client =None 

    @property 
    def chat (self ):
        """"""
        return self ._chat 

    async def get_chat (self ):
        """"""

        if (self ._chat is None or getattr (self ._chat ,'min',None ))and await self .get_input_chat ():
            try :
                self ._chat =await self ._client .get_entity (self ._input_chat )
            except ValueError :
                await self ._refetch_chat ()
        return self ._chat 

    @property 
    def input_chat (self ):
        """"""
        if self ._input_chat is None and self ._chat_peer and self ._client :
            try :
                self ._input_chat =self ._client ._entity_cache [self ._chat_peer ]
            except KeyError :
                pass 

        return self ._input_chat 

    async def get_input_chat (self ):
        """"""
        if self .input_chat is None and self .chat_id and self ._client :
            try :

                target =self .chat_id 
                async for d in self ._client .iter_dialogs (100 ):
                    if d .id ==target :
                        self ._chat =d .entity 
                        self ._input_chat =d .input_entity 
                        break 
            except errors .RPCError :
                pass 

        return self ._input_chat 

    @property 
    def chat_id (self ):
        """"""
        return utils .get_peer_id (self ._chat_peer )if self ._chat_peer else None 

    @property 
    def is_private (self ):
        """"""
        return isinstance (self ._chat_peer ,types .PeerUser )if self ._chat_peer else None 

    @property 
    def is_group (self ):
        """"""

        if self ._broadcast is None and hasattr (self .chat ,'broadcast'):
            self ._broadcast =bool (self .chat .broadcast )

        if isinstance (self ._chat_peer ,types .PeerChannel ):
            if self ._broadcast is None :
                return None 
            else :
                return not self ._broadcast 

        return isinstance (self ._chat_peer ,types .PeerChat )

    @property 
    def is_channel (self ):
        """"""

        return isinstance (self ._chat_peer ,types .PeerChannel )

    async def _refetch_chat (self ):
        """"""
