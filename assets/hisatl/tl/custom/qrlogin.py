import asyncio 
import base64 
import datetime 

from ..import types ,functions 
from ...import events 

class QRLogin :
    """"""
    def __init__ (self ,client ,ignored_ids ):
        self ._client =client 
        self ._request =functions .auth .ExportLoginTokenRequest (
        self ._client .api_id ,self ._client .api_hash ,ignored_ids )
        self ._resp =None 

    async def recreate (self ):
        """"""
        self ._resp =await self ._client (self ._request )

    @property 
    def token (self )->bytes :
        """"""
        return self ._resp .token 

    @property 
    def url (self )->str :
        """"""
        return 'tg://login?token={}'.format (base64 .urlsafe_b64encode (self ._resp .token ).decode ('utf-8').rstrip ('='))

    @property 
    def expires (self )->datetime .datetime :
        """"""
        return self ._resp .expires 

    async def wait (self ,timeout :float =None ):
        """"""
        if timeout is None :
            timeout =(self ._resp .expires -datetime .datetime .now (tz =datetime .timezone .utc )).total_seconds ()

        event =asyncio .Event ()

        async def handler (_update ):
            event .set ()

        self ._client .add_event_handler (handler ,events .Raw (types .UpdateLoginToken ))

        try :

            await asyncio .wait_for (event .wait (),timeout =timeout )
        finally :
            self ._client .remove_event_handler (handler )

        resp =await self ._client (self ._request )
        if isinstance (resp ,types .auth .LoginTokenMigrateTo ):
            await self ._client ._switch_dc (resp .dc_id )
            resp =await self ._client (functions .auth .ImportLoginTokenRequest (resp .token ))

        if isinstance (resp ,types .auth .LoginTokenSuccess ):
            user =resp .authorization .user 
            await self ._client ._on_login (user )
            return user 

        raise TypeError ('Login token response was unexpected: {}'.format (resp ))
