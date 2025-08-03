from .common import EventBuilder ,EventCommon ,name_inner_event 
from ..import utils 
from ..tl import types 

@name_inner_event 
class ChatAction (EventBuilder ):
    """"""

    @classmethod 
    def build (cls ,update ,others =None ,self_id =None ):

        if isinstance (update ,types .UpdatePinnedChannelMessages )and not update .pinned :
            return cls .Event (types .PeerChannel (update .channel_id ),
            pin_ids =update .messages ,
            pin =update .pinned )

        elif isinstance (update ,types .UpdatePinnedMessages )and not update .pinned :
            return cls .Event (update .peer ,
            pin_ids =update .messages ,
            pin =update .pinned )

        elif isinstance (update ,types .UpdateChatParticipantAdd ):
            return cls .Event (types .PeerChat (update .chat_id ),
            added_by =update .inviter_id or True ,
            users =update .user_id )

        elif isinstance (update ,types .UpdateChatParticipantDelete ):
            return cls .Event (types .PeerChat (update .chat_id ),
            kicked_by =True ,
            users =update .user_id )

        elif (isinstance (update ,(
        types .UpdateNewMessage ,types .UpdateNewChannelMessage ))
        and isinstance (update .message ,types .MessageService )):
            msg =update .message 
            action =update .message .action 
            if isinstance (action ,types .MessageActionChatJoinedByLink ):
                return cls .Event (msg ,
                added_by =True ,
                users =msg .from_id )
            elif isinstance (action ,types .MessageActionChatAddUser ):

                added_by =([msg .sender_id ]==action .users )or msg .from_id 
                return cls .Event (msg ,
                added_by =added_by ,
                users =action .users )
            elif isinstance (action ,types .MessageActionChatDeleteUser ):
                return cls .Event (msg ,
                kicked_by =utils .get_peer_id (msg .from_id )if msg .from_id else True ,
                users =action .user_id )
            elif isinstance (action ,types .MessageActionChatCreate ):
                return cls .Event (msg ,
                users =action .users ,
                created =True ,
                new_title =action .title )
            elif isinstance (action ,types .MessageActionChannelCreate ):
                return cls .Event (msg ,
                created =True ,
                users =msg .from_id ,
                new_title =action .title )
            elif isinstance (action ,types .MessageActionChatEditTitle ):
                return cls .Event (msg ,
                users =msg .from_id ,
                new_title =action .title )
            elif isinstance (action ,types .MessageActionChatEditPhoto ):
                return cls .Event (msg ,
                users =msg .from_id ,
                new_photo =action .photo )
            elif isinstance (action ,types .MessageActionChatDeletePhoto ):
                return cls .Event (msg ,
                users =msg .from_id ,
                new_photo =True )
            elif isinstance (action ,types .MessageActionPinMessage )and msg .reply_to :
                return cls .Event (msg ,
                pin_ids =[msg .reply_to_msg_id ])
            elif isinstance (action ,types .MessageActionGameScore ):
                return cls .Event (msg ,
                new_score =action .score )

        elif isinstance (update ,types .UpdateChannelParticipant )and bool (update .new_participant )!=bool (update .prev_participant ):

            return cls .Event (types .PeerChannel (update .channel_id ),
            users =update .user_id ,
            added_by =update .actor_id if update .new_participant else None ,
            kicked_by =update .actor_id if update .prev_participant else None )

    class Event (EventCommon ):
        """"""

        def __init__ (self ,where ,new_photo =None ,
        added_by =None ,kicked_by =None ,created =None ,
        users =None ,new_title =None ,pin_ids =None ,pin =None ,new_score =None ):
            if isinstance (where ,types .MessageService ):
                self .action_message =where 
                where =where .peer_id 
            else :
                self .action_message =None 

            super ().__init__ (chat_peer =where ,msg_id =pin_ids [0 ]if pin_ids else None )

            self .new_pin =pin_ids is not None 
            self ._pin_ids =pin_ids 
            self ._pinned_messages =None 

            self .new_photo =new_photo is not None 
            self .photo =new_photo if isinstance (new_photo ,types .Photo )else None 

            self ._added_by =None 
            self ._kicked_by =None 
            self .user_added =self .user_joined =self .user_left =self .user_kicked =self .unpin =False 

            if added_by is True :
                self .user_joined =True 
            elif added_by :
                self .user_added =True 
                self ._added_by =added_by 

            if kicked_by is True or (users is not None and kicked_by ==users ):
                self .user_left =True 
            elif kicked_by :
                self .user_kicked =True 
                self ._kicked_by =kicked_by 

            self .created =bool (created )

            if isinstance (users ,list ):
                self ._user_ids =[utils .get_peer_id (u )for u in users ]
            elif users :
                self ._user_ids =[utils .get_peer_id (users )]
            else :
                self ._user_ids =[]

            self ._users =None 
            self ._input_users =None 
            self .new_title =new_title 
            self .new_score =new_score 
            self .unpin =not pin 

        def _set_client (self ,client ):
            super ()._set_client (client )
            if self .action_message :
                self .action_message ._finish_init (client ,self ._entities ,None )

        async def respond (self ,*args ,**kwargs ):
            """"""
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

        async def reply (self ,*args ,**kwargs ):
            """"""
            if not self .action_message :
                return await self .respond (*args ,**kwargs )

            kwargs ['reply_to']=self .action_message .id 
            return await self ._client .send_message (
            await self .get_input_chat (),*args ,**kwargs )

        async def delete (self ,*args ,**kwargs ):
            """"""
            if not self .action_message :
                return 

            return await self ._client .delete_messages (
            await self .get_input_chat (),[self .action_message ],
            *args ,**kwargs 
            )

        async def get_pinned_message (self ):
            """"""
            if self ._pinned_messages is None :
                await self .get_pinned_messages ()

            if self ._pinned_messages :
                return self ._pinned_messages [0 ]

        async def get_pinned_messages (self ):
            """"""
            if not self ._pin_ids :
                return self ._pin_ids 

            chat =await self .get_input_chat ()
            if chat :
                self ._pinned_messages =await self ._client .get_messages (
                self ._input_chat ,ids =self ._pin_ids )

            return self ._pinned_messages 

        @property 
        def added_by (self ):
            """"""
            if self ._added_by and not isinstance (self ._added_by ,types .User ):
                aby =self ._entities .get (utils .get_peer_id (self ._added_by ))
                if aby :
                    self ._added_by =aby 

            return self ._added_by 

        async def get_added_by (self ):
            """"""
            if not self .added_by and self ._added_by :
                self ._added_by =await self ._client .get_entity (self ._added_by )

            return self ._added_by 

        @property 
        def kicked_by (self ):
            """"""
            if self ._kicked_by and not isinstance (self ._kicked_by ,types .User ):
                kby =self ._entities .get (utils .get_peer_id (self ._kicked_by ))
                if kby :
                    self ._kicked_by =kby 

            return self ._kicked_by 

        async def get_kicked_by (self ):
            """"""
            if not self .kicked_by and self ._kicked_by :
                self ._kicked_by =await self ._client .get_entity (self ._kicked_by )

            return self ._kicked_by 

        @property 
        def user (self ):
            """"""
            if self .users :
                return self ._users [0 ]

        async def get_user (self ):
            """"""
            if self .users or await self .get_users ():
                return self ._users [0 ]

        @property 
        def input_user (self ):
            """"""
            if self .input_users :
                return self ._input_users [0 ]

        async def get_input_user (self ):
            """"""
            if self .input_users or await self .get_input_users ():
                return self ._input_users [0 ]

        @property 
        def user_id (self ):
            """"""
            if self ._user_ids :
                return self ._user_ids [0 ]

        @property 
        def users (self ):
            """"""
            if not self ._user_ids :
                return []

            if self ._users is None :
                self ._users =[
                self ._entities [user_id ]
                for user_id in self ._user_ids 
                if user_id in self ._entities 
                ]

            return self ._users 

        async def get_users (self ):
            """"""
            if not self ._user_ids :
                return []

            if (self .users is None or len (self ._users )!=len (self ._user_ids ))and self .action_message :
                await self .action_message ._reload_message ()
                self ._users =[
                u for u in self .action_message .action_entities 
                if isinstance (u ,(types .User ,types .UserEmpty ))]

            return self ._users 

        @property 
        def input_users (self ):
            """"""
            if self ._input_users is None and self ._user_ids :
                self ._input_users =[]
                for user_id in self ._user_ids :

                    try :
                        self ._input_users .append (utils .get_input_peer (self ._entities [user_id ]))
                        continue 
                    except (KeyError ,TypeError ):
                        pass 

                    try :
                        self ._input_users .append (self ._client ._entity_cache [user_id ])
                        continue 
                    except KeyError :
                        pass 

            return self ._input_users or []

        async def get_input_users (self ):
            """"""
            if not self ._user_ids :
                return []

            if (self .input_users is None or len (self ._input_users )!=len (self ._user_ids ))and self .action_message :
                self ._input_users =[
                utils .get_input_peer (u )
                for u in self .action_message .action_entities 
                if isinstance (u ,(types .User ,types .UserEmpty ))]

            return self ._input_users or []

        @property 
        def user_ids (self ):
            """"""
            if self ._user_ids :
                return self ._user_ids [:]
