import asyncio 
import datetime 
import itertools 
import time 
import typing 

from ..import errors ,helpers ,utils ,hints 
from ..errors import MultiError ,RPCError 
from ..helpers import retry_range 
from ..tl import TLRequest ,types ,functions 

_NOT_A_REQUEST =lambda :TypeError ('You can only invoke requests, not types!')

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

def _fmt_flood (delay ,request ,*,early =False ,td =datetime .timedelta ):
    return (
    'Sleeping%s for %ds (%s) on %s flood wait',
    ' early'if early else '',
    delay ,
    td (seconds =delay ),
    request .__class__ .__name__ 
    )

class UserMethods :
    async def __call__ (self :'TelegramClient',request ,ordered =False ,flood_sleep_threshold =None ):
        return await self ._call (self ._sender ,request ,ordered =ordered )

    async def _call (self :'TelegramClient',sender ,request ,ordered =False ,flood_sleep_threshold =None ):
        if self ._loop is not None and self ._loop !=helpers .get_running_loop ():
            raise RuntimeError ('The asyncio event loop must not change after connection (see the FAQ for details)')

        if flood_sleep_threshold is None :
            flood_sleep_threshold =self .flood_sleep_threshold 
        requests =(request if utils .is_list_like (request )else (request ,))
        for r in requests :
            if not isinstance (r ,TLRequest ):
                raise _NOT_A_REQUEST ()
            await r .resolve (self ,utils )

            if r .CONSTRUCTOR_ID in self ._flood_waited_requests :
                due =self ._flood_waited_requests [r .CONSTRUCTOR_ID ]
                diff =round (due -time .time ())
                if diff <=3 :
                    self ._flood_waited_requests .pop (r .CONSTRUCTOR_ID ,None )
                elif diff <=flood_sleep_threshold :
                    self ._log [__name__ ].info (*_fmt_flood (diff ,r ,early =True ))
                    await asyncio .sleep (diff )
                    self ._flood_waited_requests .pop (r .CONSTRUCTOR_ID ,None )
                else :
                    raise errors .FloodWaitError (request =r ,capture =diff )

            if self ._no_updates :
                r =functions .InvokeWithoutUpdatesRequest (r )

        request_index =0 
        last_error =None 
        self ._last_request =time .time ()

        for attempt in retry_range (self ._request_retries ):
            try :
                future =sender .send (request ,ordered =ordered )
                if isinstance (future ,list ):
                    results =[]
                    exceptions =[]
                    for f in future :
                        try :
                            result =await f 
                        except RPCError as e :
                            exceptions .append (e )
                            results .append (None )
                            continue 
                        self .session .process_entities (result )
                        self ._entity_cache .add (result )
                        exceptions .append (None )
                        results .append (result )
                        request_index +=1 
                    if any (x is not None for x in exceptions ):
                        raise MultiError (exceptions ,results ,requests )
                    else :
                        return results 
                else :
                    result =await future 
                    self .session .process_entities (result )
                    self ._entity_cache .add (result )
                    return result 
            except (errors .ServerError ,errors .RpcCallFailError ,
            errors .RpcMcgetFailError ,errors .InterdcCallErrorError ,
            errors .InterdcCallRichErrorError )as e :
                last_error =e 
                self ._log [__name__ ].warning (
                'Telegram is having internal issues %s: %s',
                e .__class__ .__name__ ,e )

                await asyncio .sleep (2 )
            except (errors .FloodWaitError ,errors .SlowModeWaitError ,errors .FloodTestPhoneWaitError )as e :
                last_error =e 
                if utils .is_list_like (request ):
                    request =request [request_index ]

                if not isinstance (e ,errors .SlowModeWaitError ):
                    self ._flood_waited_requests [request .CONSTRUCTOR_ID ]=time .time ()+e .seconds 

                if e .seconds ==0 :
                    e .seconds =1 

                if e .seconds <=self .flood_sleep_threshold :
                    self ._log [__name__ ].info (*_fmt_flood (e .seconds ,request ))
                    await asyncio .sleep (e .seconds )
                else :
                    raise 
            except (errors .PhoneMigrateError ,errors .NetworkMigrateError ,
            errors .UserMigrateError )as e :
                last_error =e 
                self ._log [__name__ ].info ('Phone migrated to %d',e .new_dc )
                should_raise =isinstance (e ,(
                errors .PhoneMigrateError ,errors .NetworkMigrateError 
                ))
                if should_raise and await self .is_user_authorized ():
                    raise 
                await self ._switch_dc (e .new_dc )

        if self ._raise_last_call_error and last_error is not None :
            raise last_error 
        raise ValueError ('Request was unsuccessful {} time(s)'
        .format (attempt ))

    async def reorder_usernames (
    self :"TelegramClient",
    order :typing .List [str ],
    )->bool :
        """"""
        return await self (functions .account .ReorderUsernamesRequest (order =order ))

    async def toggle_username (
    self :"TelegramClient",
    username :str ,
    active :bool ,
    )->bool :
        """"""
        return await self (
        functions .account .ToggleUsernameRequest (username =username ,active =active )
        )

    async def set_status (
    self :"TelegramClient",
    document_id :int ,
    until :typing .Optional [int ]=None ,
    )->bool :
        return await self (
        functions .account .UpdateEmojiStatusRequest (
        types .EmojiStatusUntil (document_id ,until )
        if until 
        else types .EmojiStatus (document_id )
        )
        )

    async def get_me (self :'TelegramClient',input_peer :bool =False )->'typing.Union[types.User, types.InputPeerUser]':
        """"""
        if input_peer and self ._self_input_peer :
            return self ._self_input_peer 

        try :
            me =(await self (
            functions .users .GetUsersRequest ([types .InputUserSelf ()])))[0 ]

            self ._bot =me .bot 
            if not self ._self_input_peer :
                self ._self_input_peer =utils .get_input_peer (
                me ,allow_self =False 
                )

            return self ._self_input_peer if input_peer else me 
        except errors .UnauthorizedError :
            return None 

    @property 
    def _self_id (self :'TelegramClient')->typing .Optional [int ]:
        """"""
        return self ._self_input_peer .user_id if self ._self_input_peer else None 

    async def is_bot (self :'TelegramClient')->bool :
        """"""
        if self ._bot is None :
            self ._bot =(await self .get_me ()).bot 

        return self ._bot 

    async def is_user_authorized (self :'TelegramClient')->bool :
        """"""
        if self ._authorized is None :
            try :

                await self (functions .updates .GetStateRequest ())
                self ._authorized =True 
            except errors .RPCError :
                self ._authorized =False 

        return self ._authorized 

    async def get_entity (
    self :'TelegramClient',
    entity :'hints.EntitiesLike')->'hints.Entity':
        """"""
        single =not utils .is_list_like (entity )
        if single :
            entity =(entity ,)

        inputs =[]
        for x in entity :
            if isinstance (x ,str ):
                inputs .append (x )
            else :
                inputs .append (await self .get_input_entity (x ))

        lists ={
        helpers ._EntityType .USER :[],
        helpers ._EntityType .CHAT :[],
        helpers ._EntityType .CHANNEL :[],
        }
        for x in inputs :
            try :
                lists [helpers ._entity_type (x )].append (x )
            except TypeError :
                pass 

        users =lists [helpers ._EntityType .USER ]
        chats =lists [helpers ._EntityType .CHAT ]
        channels =lists [helpers ._EntityType .CHANNEL ]
        if users :

            tmp =[]
            while users :
                curr ,users =users [:200 ],users [200 :]
                tmp .extend (await self (functions .users .GetUsersRequest (curr )))
            users =tmp 
        if chats :
            chats =(await self (
            functions .messages .GetChatsRequest ([x .chat_id for x in chats ]))).chats 
        if channels :
            channels =(await self (
            functions .channels .GetChannelsRequest (channels ))).chats 

        id_entity ={

        utils .get_peer_id (x ,add_mark =False ):x 
        for x in itertools .chain (users ,chats ,channels )
        }

        result =[]
        for x in inputs :
            if isinstance (x ,str ):
                result .append (await self ._get_entity_from_string (x ))
            elif not isinstance (x ,types .InputPeerSelf ):
                result .append (id_entity [utils .get_peer_id (x ,add_mark =False )])
            else :
                result .append (next (
                u for u in id_entity .values ()
                if isinstance (u ,types .User )and u .is_self 
                ))

        return result [0 ]if single else result 

    async def get_input_entity (
    self :'TelegramClient',
    peer :'hints.EntityLike')->'types.TypeInputPeer':
        """"""

        try :
            return utils .get_input_peer (peer )
        except TypeError :
            pass 

        try :

            if isinstance (peer ,int )or peer .SUBCLASS_OF_ID ==0x2d45687 :
                return self ._entity_cache [peer ]
        except (AttributeError ,KeyError ):
            pass 

        if peer in ('me','self'):
            return types .InputPeerSelf ()

        try :
            return self .session .get_input_entity (peer )
        except ValueError :
            pass 

        if isinstance (peer ,str ):
            return utils .get_input_peer (
            await self ._get_entity_from_string (peer ))

        peer =utils .get_peer (peer )
        if isinstance (peer ,types .PeerUser ):
            users =await self (functions .users .GetUsersRequest ([
            types .InputUser (peer .user_id ,access_hash =0 )]))
            if users and not isinstance (users [0 ],types .UserEmpty ):

                return utils .get_input_peer (users [0 ])
        elif isinstance (peer ,types .PeerChat ):
            return types .InputPeerChat (peer .chat_id )
        elif isinstance (peer ,types .PeerChannel ):
            try :
                channels =await self (functions .channels .GetChannelsRequest ([
                types .InputChannel (peer .channel_id ,access_hash =0 )]))
                return utils .get_input_peer (channels .chats [0 ])
            except errors .ChannelInvalidError :
                pass 

        raise ValueError (
        'Could not find the input entity for {} ({}). Please read https://'
        'docs.telethon.dev/en/stable/concepts/entities.html to'
        ' find out more details.'
        .format (peer ,type (peer ).__name__ )
        )

    async def _get_peer (self :'TelegramClient',peer :'hints.EntityLike'):
        i ,cls =utils .resolve_id (await self .get_peer_id (peer ))
        return cls (i )

    async def get_peer_id (
    self :'TelegramClient',
    peer :'hints.EntityLike',
    add_mark :bool =True )->int :
        """"""
        if isinstance (peer ,int ):
            return utils .get_peer_id (peer ,add_mark =add_mark )

        try :
            if peer .SUBCLASS_OF_ID not in (0x2d45687 ,0xc91c90b6 ):

                peer =await self .get_input_entity (peer )
        except AttributeError :
            peer =await self .get_input_entity (peer )

        if isinstance (peer ,types .InputPeerSelf ):
            peer =await self .get_me (input_peer =True )

        return utils .get_peer_id (peer ,add_mark =add_mark )

    async def _get_entity_from_string (self :'TelegramClient',string ):
        """"""
        phone =utils .parse_phone (string )
        if phone :
            try :
                for user in (await self (
                functions .contacts .GetContactsRequest (0 ))).users :
                    if user .phone ==phone :
                        return user 
            except errors .BotMethodInvalidError :
                raise ValueError ('Cannot get entity by phone number as a '
                'bot (try using integer IDs, not strings)')
        elif string .lower ()in ('me','self'):
            return await self .get_me ()
        else :
            username ,is_join_chat =utils .parse_username (string )
            if is_join_chat :
                invite =await self (
                functions .messages .CheckChatInviteRequest (username ))

                if isinstance (invite ,types .ChatInvite ):
                    raise ValueError (
                    'Cannot get entity from a channel (or group) '
                    'that you are not part of. Join the group and retry'
                    )
                elif isinstance (invite ,types .ChatInviteAlready ):
                    return invite .chat 
            elif username :
                try :
                    result =await self (
                    functions .contacts .ResolveUsernameRequest (username ))
                except errors .UsernameNotOccupiedError as e :
                    raise ValueError ('No user has "{}" as username'
                    .format (username ))from e 

                try :
                    pid =utils .get_peer_id (result .peer ,add_mark =False )
                    if isinstance (result .peer ,types .PeerUser ):
                        return next (x for x in result .users if x .id ==pid )
                    else :
                        return next (x for x in result .chats if x .id ==pid )
                except StopIteration :
                    pass 
            try :

                return await self .get_entity (
                self .session .get_input_entity (string ))
            except ValueError :
                pass 

        raise ValueError (
        'Cannot find any entity corresponding to "{}"'.format (string )
        )

    async def _get_input_dialog (self :'TelegramClient',dialog ):
        """"""
        try :
            if dialog .SUBCLASS_OF_ID ==0xa21c9795 :
                dialog .peer =await self .get_input_entity (dialog .peer )
                return dialog 
            elif dialog .SUBCLASS_OF_ID ==0xc91c90b6 :
                return types .InputDialogPeer (dialog )
        except AttributeError :
            pass 

        return types .InputDialogPeer (await self .get_input_entity (dialog ))

    async def _get_input_notify (self :'TelegramClient',notify ):
        """"""
        try :
            if notify .SUBCLASS_OF_ID ==0x58981615 :
                if isinstance (notify ,types .InputNotifyPeer ):
                    notify .peer =await self .get_input_entity (notify .peer )
                return notify 
        except AttributeError :
            pass 

        return types .InputNotifyPeer (await self .get_input_entity (notify ))

