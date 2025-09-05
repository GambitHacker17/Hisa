
import logging 

import hisapyro 
from hisapyro import raw 

log =logging .getLogger (__name__ )

class Start :
    async def start (
    self :"hisapyro.Client"
    ):
        """"""
        is_authorized =await self .connect ()

        try :
            if not is_authorized :
                await self .authorize ()

            if not await self .storage .is_bot ()and self .takeout :
                self .takeout_id =(await self .invoke (raw .functions .account .InitTakeoutSession ())).id 
                log .info ("Takeout session %s initiated",self .takeout_id )

            await self .invoke (raw .functions .updates .GetState ())
        except (Exception ,KeyboardInterrupt ):
            await self .disconnect ()
            raise 
        else :
            self .me =await self .get_me ()
            await self .initialize ()

            return self 
