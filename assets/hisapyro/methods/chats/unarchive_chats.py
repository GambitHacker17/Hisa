
from typing import Union ,List 

import hisapyro 
from hisapyro import raw 

class UnarchiveChats :
    async def unarchive_chats (
    self :"hisapyro.Client",
    chat_ids :Union [int ,str ,List [Union [int ,str ]]],
    )->bool :
        """"""

        if not isinstance (chat_ids ,list ):
            chat_ids =[chat_ids ]

        folder_peers =[]

        for chat in chat_ids :
            folder_peers .append (
            raw .types .InputFolderPeer (
            peer =await self .resolve_peer (chat ),
            folder_id =0 
            )
            )

        await self .invoke (
        raw .functions .folders .EditPeerFolders (
        folder_peers =folder_peers 
        )
        )

        return True 
