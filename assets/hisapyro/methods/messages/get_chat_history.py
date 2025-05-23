
from datetime import datetime 
from typing import Union ,Optional ,AsyncGenerator 

import hisapyro 
from hisapyro import types ,raw ,utils 

async def get_chunk (
*,
client :"hisapyro.Client",
chat_id :Union [int ,str ],
limit :int =0 ,
offset :int =0 ,
from_message_id :int =0 ,
from_date :datetime =utils .zero_datetime ()
):
    messages =await client .invoke (
    raw .functions .messages .GetHistory (
    peer =await client .resolve_peer (chat_id ),
    offset_id =from_message_id ,
    offset_date =utils .datetime_to_timestamp (from_date ),
    add_offset =offset ,
    limit =limit ,
    max_id =0 ,
    min_id =0 ,
    hash =0 
    ),
    sleep_threshold =60 
    )

    return await utils .parse_messages (client ,messages ,replies =0 )

class GetChatHistory :
    async def get_chat_history (
    self :"hisapyro.Client",
    chat_id :Union [int ,str ],
    limit :int =0 ,
    offset :int =0 ,
    offset_id :int =0 ,
    offset_date :datetime =utils .zero_datetime ()
    )->Optional [AsyncGenerator ["types.Message",None ]]:
        """"""
        current =0 
        total =limit or (1 <<31 )-1 
        limit =min (100 ,total )

        while True :
            messages =await get_chunk (
            client =self ,
            chat_id =chat_id ,
            limit =limit ,
            offset =offset ,
            from_message_id =offset_id ,
            from_date =offset_date 
            )

            if not messages :
                return 

            offset_id =messages [-1 ].id 

            for message in messages :
                yield message 

                current +=1 

                if current >=total :
                    return 
