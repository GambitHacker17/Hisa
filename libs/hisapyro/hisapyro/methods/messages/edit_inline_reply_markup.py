
import hisapyro 
from hisapyro import raw 
from hisapyro import types 
from hisapyro import utils 
from .inline_session import get_session 

class EditInlineReplyMarkup :
    async def edit_inline_reply_markup (
    self :"hisapyro.Client",
    inline_message_id :str ,
    reply_markup :"types.InlineKeyboardMarkup"=None 
    )->bool :
        """"""

        unpacked =utils .unpack_inline_message_id (inline_message_id )
        dc_id =unpacked .dc_id 

        session =await get_session (self ,dc_id )

        return await session .invoke (
        raw .functions .messages .EditInlineBotMessage (
        id =unpacked ,
        reply_markup =await reply_markup .write (self )if reply_markup else None ,
        ),
        sleep_threshold =self .sleep_threshold 
        )
