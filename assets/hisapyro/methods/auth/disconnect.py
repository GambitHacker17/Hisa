
import hisapyro 

class Disconnect :
    async def disconnect (
    self :"hisapyro.Client",
    ):
        """"""
        if not self .is_connected :
            raise ConnectionError ("Client is already disconnected")

        if self .is_initialized :
            raise ConnectionError ("Can't disconnect an initialized client")

        await self .session .stop ()
        await self .storage .close ()
        self .is_connected =False 
