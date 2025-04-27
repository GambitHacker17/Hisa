from ..import types ,functions 
from ...import utils 

class InlineResult :
    """"""

    ARTICLE ='article'
    PHOTO ='photo'
    GIF ='gif'
    VIDEO ='video'
    VIDEO_GIF ='mpeg4_gif'
    AUDIO ='audio'
    DOCUMENT ='document'
    LOCATION ='location'
    VENUE ='venue'
    CONTACT ='contact'
    GAME ='game'

    def __init__ (self ,client ,original ,query_id =None ,*,entity =None ):
        self ._client =client 
        self .result =original 
        self ._query_id =query_id 
        self ._entity =entity 

    @property 
    def type (self ):
        """"""
        return self .result .type 

    @property 
    def message (self ):
        """"""
        return self .result .send_message 

    @property 
    def title (self ):
        """"""
        return self .result .title 

    @property 
    def description (self ):
        """"""
        return self .result .description 

    @property 
    def url (self ):
        """"""
        if isinstance (self .result ,types .BotInlineResult ):
            return self .result .url 

    @property 
    def photo (self ):
        """"""
        if isinstance (self .result ,types .BotInlineResult ):
            return self .result .thumb 
        elif isinstance (self .result ,types .BotInlineMediaResult ):
            return self .result .photo 

    @property 
    def document (self ):
        """"""
        if isinstance (self .result ,types .BotInlineResult ):
            return self .result .content 
        elif isinstance (self .result ,types .BotInlineMediaResult ):
            return self .result .document 

    async def click (self ,entity =None ,reply_to =None ,comment_to =None ,
    silent =False ,clear_draft =False ,hide_via =False ,
    background =None ):
        """"""
        if entity :
            entity =await self ._client .get_input_entity (entity )
        elif self ._entity :
            entity =self ._entity 
        else :
            raise ValueError ('You must provide the entity where the result should be sent to')

        if comment_to :
            entity ,reply_to =await self ._client ._get_comment_data (entity ,comment_to )
        else :
            reply_to =(
            None 
            if reply_to is None 
            else utils .get_input_reply_to (
            entity ,
            reply_to ,
            (
            reply_to .id 
            if isinstance (reply_to ,types .Message )
            else reply_to 
            if isinstance (reply_to ,int )
            else None 
            ),
            )
            )

        req =functions .messages .SendInlineBotResultRequest (
        peer =entity ,
        query_id =self ._query_id ,
        id =self .result .id ,
        silent =silent ,
        background =background ,
        clear_draft =clear_draft ,
        hide_via =hide_via ,
        reply_to =reply_to 
        )
        return self ._client ._get_response_message (
        req ,await self ._client (req ),entity )

    async def download_media (self ,*args ,**kwargs ):
        """"""
        if self .document or self .photo :
            return await self ._client .download_media (
            self .document or self .photo ,*args ,**kwargs )
