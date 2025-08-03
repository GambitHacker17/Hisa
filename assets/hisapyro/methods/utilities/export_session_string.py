
import hisapyro 

class ExportSessionString :
    async def export_session_string (
    self :"hisapyro.Client"
    ):
        """"""
        return await self .storage .export_session_string ()
