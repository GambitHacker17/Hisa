from .import Draft 
from ..import TLObject ,types ,functions 
from ...import utils 

class Dialog :
    """"""
    def __init__ (self ,client ,dialog ,entities ,message ):

        self ._client =client 
        self .dialog =dialog 
        self .pinned =bool (dialog .pinned )
        self .folder_id =dialog .folder_id 
        self .archived =dialog .folder_id is not None 
        self .message =message 
        self .date =getattr (self .message ,'date',None )

        self .entity =entities [utils .get_peer_id (dialog .peer )]
        self .input_entity =utils .get_input_peer (self .entity )
        self .id =utils .get_peer_id (self .entity )
        self .name =self .title =utils .get_display_name (self .entity )

        self .unread_count =dialog .unread_count 
        self .unread_mentions_count =dialog .unread_mentions_count 

        self .draft =Draft (client ,self .entity ,self .dialog .draft )

        self .is_user =isinstance (self .entity ,types .User )
        self .is_group =(
        isinstance (self .entity ,(types .Chat ,types .ChatForbidden ))or 
        (isinstance (self .entity ,types .Channel )and self .entity .megagroup )
        )
        self .is_channel =isinstance (self .entity ,types .Channel )

    async def send_message (self ,*args ,**kwargs ):
        """"""
        return await self ._client .send_message (
        self .input_entity ,*args ,**kwargs )

    async def delete (self ,revoke =False ):
        """"""

        await self ._client .delete_dialog (self .entity ,revoke =revoke )

    async def archive (self ,folder =1 ):
        """"""
        return await self ._client (functions .folders .EditPeerFoldersRequest ([
        types .InputFolderPeer (self .input_entity ,folder_id =folder )
        ]))

    def to_dict (self ):
        return {
        '_':'Dialog',
        'name':self .name ,
        'date':self .date ,
        'draft':self .draft ,
        'message':self .message ,
        'entity':self .entity ,
        }

    def __str__ (self ):
        return TLObject .pretty_format (self .to_dict ())

    def stringify (self ):
        return TLObject .pretty_format (self .to_dict (),indent =0 )
