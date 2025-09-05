from .chatgetter import ChatGetter 
from .sendergetter import SenderGetter 
from ...import utils ,helpers 
from ...tl import types 

class Forward (ChatGetter ,SenderGetter ):
    """"""
    def __init__ (self ,client ,original ,entities ):

        self .__dict__ .update (original .__dict__ )
        self .original_fwd =original 

        sender_id =sender =input_sender =peer =chat =input_chat =None 
        if original .from_id :
            ty =helpers ._entity_type (original .from_id )
            if ty ==helpers ._EntityType .USER :
                sender_id =utils .get_peer_id (original .from_id )
                sender ,input_sender =utils ._get_entity_pair (
                sender_id ,entities ,client ._entity_cache )

            elif ty in (helpers ._EntityType .CHAT ,helpers ._EntityType .CHANNEL ):
                peer =original .from_id 
                chat ,input_chat =utils ._get_entity_pair (
                utils .get_peer_id (peer ),entities ,client ._entity_cache )

        ChatGetter .__init__ (self ,peer ,chat =chat ,input_chat =input_chat )
        SenderGetter .__init__ (self ,sender_id ,sender =sender ,input_sender =input_sender )
        self ._client =client 

