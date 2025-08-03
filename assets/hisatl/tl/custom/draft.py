import datetime 

from ..import TLObject 
from ..functions .messages import SaveDraftRequest 
from ..types import DraftMessage 
from ...errors import RPCError 
from ...extensions import markdown 
from ...utils import get_input_peer ,get_peer 

class Draft :
    """"""
    def __init__ (self ,client ,entity ,draft ):
        self ._client =client 
        self ._peer =get_peer (entity )
        self ._entity =entity 
        self ._input_entity =get_input_peer (entity )if entity else None 

        if not draft or not isinstance (draft ,DraftMessage ):
            draft =DraftMessage ('',None ,None ,None ,None )

        self ._text =markdown .unparse (draft .message ,draft .entities )
        self ._raw_text =draft .message 
        self .date =draft .date 
        self .link_preview =not draft .no_webpage 
        self .reply_to =draft .reply_to 

    @property 
    def entity (self ):
        """"""
        return self ._entity 

    @property 
    def input_entity (self ):
        """"""
        if not self ._input_entity :
            try :
                self ._input_entity =self ._client ._entity_cache [self ._peer ]
            except KeyError :
                pass 

        return self ._input_entity 

    async def get_entity (self ):
        """"""
        if not self .entity and await self .get_input_entity ():
            try :
                self ._entity =await self ._client .get_entity (self ._input_entity )
            except ValueError :
                pass 

        return self ._entity 

    async def get_input_entity (self ):
        """"""

        return self .input_entity 

    @property 
    def text (self ):
        """"""
        return self ._text 

    @property 
    def raw_text (self ):
        """"""
        return self ._raw_text 

    @property 
    def is_empty (self ):
        """"""
        return not self ._text 

    async def set_message (
    self ,text =None ,reply_to =0 ,parse_mode =(),
    link_preview =None ):
        """"""
        if text is None :
            text =self ._text 

        if not reply_to :
            reply_to =self .reply_to 

        if link_preview is None :
            link_preview =self .link_preview 

        raw_text ,entities =await self ._client ._parse_message_text (text ,parse_mode )

        result =await self ._client (SaveDraftRequest (
        peer =self ._peer ,
        message =raw_text ,
        no_webpage =not link_preview ,
        reply_to =reply_to ,
        entities =entities 
        ))

        if result :
            self ._text =text 
            self ._raw_text =raw_text 
            self .link_preview =link_preview 
            self .reply_to =reply_to 
            self .date =datetime .datetime .now (tz =datetime .timezone .utc )

        return result 

    async def send (self ,clear =True ,parse_mode =()):
        """"""
        await self ._client .send_message (
        self ._peer ,self .text ,reply_to =self .reply_to ,
        link_preview =self .link_preview ,parse_mode =parse_mode ,
        clear_draft =clear 
        )

    async def delete (self ):
        """"""
        return await self .set_message (text ='')

    def to_dict (self ):
        try :
            entity =self .entity 
        except RPCError as e :
            entity =e 

        return {
        '_':'Draft',
        'text':self .text ,
        'entity':entity ,
        'date':self .date ,
        'link_preview':self .link_preview ,
        'reply_to':self .reply_to 
        }

    def __str__ (self ):
        return TLObject .pretty_format (self .to_dict ())

    def stringify (self ):
        return TLObject .pretty_format (self .to_dict (),indent =0 )
