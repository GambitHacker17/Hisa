from ..import types ,functions 
from ...import password as pwd_mod 
from ...errors import BotResponseTimeoutError 
import webbrowser 
import os 

class MessageButton :
    """"""
    def __init__ (self ,client ,original ,chat ,bot ,msg_id ):
        self .button =original 
        self ._bot =bot 
        self ._chat =chat 
        self ._msg_id =msg_id 
        self ._client =client 

    @property 
    def client (self ):
        """"""
        return self ._client 

    @property 
    def text (self ):
        """"""
        return self .button .text 

    @property 
    def data (self ):
        """"""
        if isinstance (self .button ,types .KeyboardButtonCallback ):
            return self .button .data 

    @property 
    def inline_query (self ):
        """"""
        if isinstance (self .button ,types .KeyboardButtonSwitchInline ):
            return self .button .query 

    @property 
    def url (self ):
        """"""
        if isinstance (self .button ,types .KeyboardButtonUrl ):
            return self .button .url 

    async def click (self ,share_phone =None ,share_geo =None ,*,password =None ):
        """"""
        if isinstance (self .button ,types .KeyboardButton ):
            return await self ._client .send_message (
            self ._chat ,self .button .text ,parse_mode =None )
        elif isinstance (self .button ,types .KeyboardButtonCallback ):
            if password is not None :
                pwd =await self ._client (functions .account .GetPasswordRequest ())
                password =pwd_mod .compute_check (pwd ,password )

            req =functions .messages .GetBotCallbackAnswerRequest (
            peer =self ._chat ,msg_id =self ._msg_id ,data =self .button .data ,
            password =password 
            )
            try :
                return await self ._client (req )
            except BotResponseTimeoutError :
                return None 
        elif isinstance (self .button ,types .KeyboardButtonSwitchInline ):
            return await self ._client (functions .messages .StartBotRequest (
            bot =self ._bot ,peer =self ._chat ,start_param =self .button .query 
            ))
        elif isinstance (self .button ,types .KeyboardButtonUrl ):
            return webbrowser .open (self .button .url )
        elif isinstance (self .button ,types .KeyboardButtonGame ):
            req =functions .messages .GetBotCallbackAnswerRequest (
            peer =self ._chat ,msg_id =self ._msg_id ,game =True 
            )
            try :
                return await self ._client (req )
            except BotResponseTimeoutError :
                return None 
        elif isinstance (self .button ,types .KeyboardButtonRequestPhone ):
            if not share_phone :
                raise ValueError ('cannot click on phone buttons unless share_phone=True')

            if share_phone ==True or isinstance (share_phone ,str ):
                me =await self ._client .get_me ()
                share_phone =types .InputMediaContact (
                phone_number =me .phone if share_phone ==True else share_phone ,
                first_name =me .first_name or '',
                last_name =me .last_name or '',
                vcard =''
                )

            return await self ._client .send_file (self ._chat ,share_phone )
        elif isinstance (self .button ,types .KeyboardButtonRequestGeoLocation ):
            if not share_geo :
                raise ValueError ('cannot click on geo buttons unless share_geo=(longitude, latitude)')

            if isinstance (share_geo ,(tuple ,list )):
                long ,lat =share_geo 
                share_geo =types .InputMediaGeoPoint (types .InputGeoPoint (lat =lat ,long =long ))

            return await self ._client .send_file (self ._chat ,share_geo )
