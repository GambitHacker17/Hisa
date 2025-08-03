import asyncio 
import inspect 
import itertools 
import random 
import sys 
import time 
import traceback 
import typing 
import logging 
from collections import deque 

from ..import events ,utils ,errors 
from ..events .common import EventBuilder ,EventCommon 
from ..tl import types ,functions 
from .._updates import GapError ,PrematureEndReason 
from ..helpers import get_running_loop 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

Callback =typing .Callable [[typing .Any ],typing .Any ]

class UpdateMethods :

    async def _run_until_disconnected (self :'TelegramClient'):
        try :

            await self (functions .updates .GetStateRequest ())
            result =await self .disconnected 
            if self ._updates_error is not None :
                raise self ._updates_error 
            return result 
        except KeyboardInterrupt :
            pass 
        finally :
            await self .disconnect ()

    async def set_receive_updates (self :'TelegramClient',receive_updates ):
        """"""
        self ._no_updates =not receive_updates 
        if receive_updates :
            await self (functions .updates .GetStateRequest ())

    def run_until_disconnected (self :'TelegramClient'):
        """"""
        if self .loop .is_running ():
            return self ._run_until_disconnected ()
        try :
            return self .loop .run_until_complete (self ._run_until_disconnected ())
        except KeyboardInterrupt :
            pass 
        finally :

            self .disconnect ()

    def on (self :'TelegramClient',event :EventBuilder ):
        """"""
        def decorator (f ):
            self .add_event_handler (f ,event )
            return f 

        return decorator 

    def add_event_handler (
    self :'TelegramClient',
    callback :Callback ,
    event :EventBuilder =None ):
        """"""
        builders =events ._get_handlers (callback )
        if builders is not None :
            for event in builders :
                self ._event_builders .append ((event ,callback ))
            return 

        if isinstance (event ,type ):
            event =event ()
        elif not event :
            event =events .Raw ()

        self ._event_builders .append ((event ,callback ))

    def remove_event_handler (
    self :'TelegramClient',
    callback :Callback ,
    event :EventBuilder =None )->int :
        """"""
        found =0 
        if event and not isinstance (event ,type ):
            event =type (event )

        i =len (self ._event_builders )
        while i :
            i -=1 
            ev ,cb =self ._event_builders [i ]
            if cb ==callback and (not event or isinstance (ev ,event )):
                del self ._event_builders [i ]
                found +=1 

        return found 

    def list_event_handlers (self :'TelegramClient')->'typing.Sequence[typing.Tuple[Callback, EventBuilder]]':
        """"""
        return [(callback ,event )for event ,callback in self ._event_builders ]

    async def catch_up (self :'TelegramClient'):
        """"""
        await self ._updates_queue .put (types .UpdatesTooLong ())

    async def _update_loop (self :'TelegramClient'):

        was_once_logged_in =self ._authorized is True or not self ._message_box .is_empty ()

        self ._updates_error =None 
        try :
            if self ._catch_up :

                await self .catch_up ()

            updates_to_dispatch =deque ()

            while self .is_connected ():
                if updates_to_dispatch :
                    if self ._sequential_updates :
                        await self ._dispatch_update (updates_to_dispatch .popleft ())
                    else :
                        while updates_to_dispatch :

                            task =self .loop .create_task (self ._dispatch_update (updates_to_dispatch .popleft ()))
                            self ._event_handler_tasks .add (task )
                            task .add_done_callback (self ._event_handler_tasks .discard )

                    continue 

                get_diff =self ._message_box .get_difference ()
                if get_diff :
                    self ._log [__name__ ].debug ('Getting difference for account updates')
                    try :
                        diff =await self (get_diff )
                    except (errors .ServerError ,errors .TimeoutError ,ValueError )as e :

                        self ._log [__name__ ].info ('Cannot get difference since Telegram is having issues: %s',type (e ).__name__ )
                        self ._message_box .end_difference ()
                        continue 
                    except (errors .UnauthorizedError ,errors .AuthKeyError )as e :

                        self ._log [__name__ ].info ('Cannot get difference since the account is not logged in: %s',type (e ).__name__ )
                        self ._message_box .end_difference ()
                        if was_once_logged_in :
                            self ._updates_error =e 
                            await self .disconnect ()
                            break 
                        continue 
                    except errors .TypeNotFoundError as e :

                        self ._log [__name__ ].warning ('Cannot get difference since the account is likely misusing the session: %s',e )
                        self ._message_box .end_difference ()
                        self ._updates_error =e 
                        await self .disconnect ()
                        break 
                    except OSError as e :

                        self ._log [__name__ ].info ('Cannot get difference since the network is down: %s: %s',type (e ).__name__ ,e )
                        await asyncio .sleep (5 )
                        continue 
                    updates ,users ,chats =self ._message_box .apply_difference (diff ,self ._mb_entity_cache )
                    if updates :
                        self ._log [__name__ ].info ('Got difference for account updates')

                    updates_to_dispatch .extend (self ._preprocess_updates (updates ,users ,chats ))
                    continue 

                get_diff =self ._message_box .get_channel_difference (self ._mb_entity_cache )
                if get_diff :
                    self ._log [__name__ ].debug ('Getting difference for channel %s updates',get_diff .channel .channel_id )
                    try :
                        diff =await self (get_diff )
                    except (errors .UnauthorizedError ,errors .AuthKeyError )as e :

                        self ._log [__name__ ].warning (
                        'Cannot get difference for channel %s since the account is not logged in: %s',
                        get_diff .channel .channel_id ,type (e ).__name__ 
                        )
                        self ._message_box .end_channel_difference (
                        get_diff ,
                        PrematureEndReason .TEMPORARY_SERVER_ISSUES ,
                        self ._mb_entity_cache 
                        )
                        if was_once_logged_in :
                            self ._updates_error =e 
                            await self .disconnect ()
                            break 
                        continue 
                    except errors .TypeNotFoundError as e :
                        self ._log [__name__ ].warning (
                        'Cannot get difference for channel %s since the account is likely misusing the session: %s',
                        get_diff .channel .channel_id ,e 
                        )
                        self ._message_box .end_channel_difference (
                        get_diff ,
                        PrematureEndReason .TEMPORARY_SERVER_ISSUES ,
                        self ._mb_entity_cache 
                        )
                        self ._updates_error =e 
                        await self .disconnect ()
                        break 
                    except (
                    errors .PersistentTimestampOutdatedError ,
                    errors .PersistentTimestampInvalidError ,
                    errors .ServerError ,
                    errors .TimeoutError ,
                    ValueError 
                    )as e :

                        self ._log [__name__ ].warning (
                        'Getting difference for channel updates %s caused %s;'
                        ' ending getting difference prematurely until server issues are resolved',
                        get_diff .channel .channel_id ,type (e ).__name__ 
                        )
                        self ._message_box .end_channel_difference (
                        get_diff ,
                        PrematureEndReason .TEMPORARY_SERVER_ISSUES ,
                        self ._mb_entity_cache 
                        )
                        continue 
                    except (errors .ChannelPrivateError ,errors .ChannelInvalidError ):

                        self ._log [__name__ ].info (
                        'Account is now banned in %d so we can no longer fetch updates from it',
                        get_diff .channel .channel_id 
                        )
                        self ._message_box .end_channel_difference (
                        get_diff ,
                        PrematureEndReason .BANNED ,
                        self ._mb_entity_cache 
                        )
                        continue 
                    except OSError as e :
                        self ._log [__name__ ].info (
                        'Cannot get difference for channel %d since the network is down: %s: %s',
                        get_diff .channel .channel_id ,type (e ).__name__ ,e 
                        )
                        await asyncio .sleep (5 )
                        continue 

                    updates ,users ,chats =self ._message_box .apply_channel_difference (get_diff ,diff ,self ._mb_entity_cache )
                    if updates :
                        self ._log [__name__ ].info ('Got difference for channel %d updates',get_diff .channel .channel_id )

                    updates_to_dispatch .extend (self ._preprocess_updates (updates ,users ,chats ))
                    continue 

                deadline =self ._message_box .check_deadlines ()
                deadline_delay =deadline -get_running_loop ().time ()
                if deadline_delay >0 :

                    try :
                        updates =await asyncio .wait_for (self ._updates_queue .get (),deadline_delay )
                    except asyncio .TimeoutError :
                        self ._log [__name__ ].debug ('Timeout waiting for updates expired')
                        continue 
                else :
                    continue 

                processed =[]
                try :
                    users ,chats =self ._message_box .process_updates (updates ,self ._mb_entity_cache ,processed )
                except GapError :
                    continue 

                updates_to_dispatch .extend (self ._preprocess_updates (processed ,users ,chats ))
        except asyncio .CancelledError :
            pass 
        except Exception as e :
            self ._log [__name__ ].exception ('Fatal error handling updates (this is a bug in Telethon, please report it)')
            self ._updates_error =e 
            await self .disconnect ()

    def _preprocess_updates (self ,updates ,users ,chats ):
        self ._mb_entity_cache .extend (users ,chats )
        entities ={utils .get_peer_id (x ):x 
        for x in itertools .chain (users ,chats )}
        for u in updates :
            u ._entities =entities 
        return updates 

    async def _keepalive_loop (self :'TelegramClient'):

        rnd =lambda :random .randrange (-2 **63 ,2 **63 )
        while self .is_connected ():
            try :
                await asyncio .wait_for (
                self .disconnected ,timeout =60 
                )
                continue 
            except asyncio .TimeoutError :
                pass 
            except asyncio .CancelledError :
                return 
            except Exception :
                continue 

            await self ._clean_exported_senders ()

            if not self ._sender ._transport_connected ():
                continue 

            try :
                self ._sender ._keepalive_ping (rnd ())
            except (ConnectionError ,asyncio .CancelledError ):
                return 

            self .session .save ()

    async def _dispatch_update (self :'TelegramClient',update ):

        others =None 

        if not self ._self_input_peer :

            try :
                await self .get_me (input_peer =True )
            except OSError :
                pass 

        built =EventBuilderDict (self ,update ,others )
        for conv_set in self ._conversations .values ():
            for conv in conv_set :
                ev =built [events .NewMessage ]
                if ev :
                    conv ._on_new_message (ev )

                ev =built [events .MessageEdited ]
                if ev :
                    conv ._on_edit (ev )

                ev =built [events .MessageRead ]
                if ev :
                    conv ._on_read (ev )

                if conv ._custom :
                    await conv ._check_custom (built )

        for builder ,callback in self ._event_builders :
            event =built [type (builder )]
            if not event :
                continue 

            if not builder .resolved :
                await builder .resolve (self )

            filter =builder .filter (event )
            if inspect .isawaitable (filter ):
                filter =await filter 
            if not filter :
                continue 

            try :
                await callback (event )
            except errors .AlreadyInConversationError :
                name =getattr (callback ,'__name__',repr (callback ))
                self ._log [__name__ ].debug (
                'Event handler "%s" already has an open conversation, '
                'ignoring new one',name )
            except events .StopPropagation :
                name =getattr (callback ,'__name__',repr (callback ))
                self ._log [__name__ ].debug (
                'Event handler "%s" stopped chain of propagation '
                'for event %s.',name ,type (event ).__name__ 
                )
                break 
            except Exception as e :
                if not isinstance (e ,asyncio .CancelledError )or self .is_connected ():
                    name =getattr (callback ,'__name__',repr (callback ))
                    self ._log [__name__ ].exception ('Unhandled exception on %s',name )

    async def _dispatch_event (self :'TelegramClient',event ):
        """"""

        for builder ,callback in self ._event_builders :
            if isinstance (builder ,events .Raw ):
                continue 
            if not isinstance (event ,builder .Event ):
                continue 

            if not builder .resolved :
                await builder .resolve (self )

            filter =builder .filter (event )
            if inspect .isawaitable (filter ):
                filter =await filter 
            if not filter :
                continue 

            try :
                await callback (event )
            except errors .AlreadyInConversationError :
                name =getattr (callback ,'__name__',repr (callback ))
                self ._log [__name__ ].debug (
                'Event handler "%s" already has an open conversation, '
                'ignoring new one',name )
            except events .StopPropagation :
                name =getattr (callback ,'__name__',repr (callback ))
                self ._log [__name__ ].debug (
                'Event handler "%s" stopped chain of propagation '
                'for event %s.',name ,type (event ).__name__ 
                )
                break 
            except Exception as e :
                if not isinstance (e ,asyncio .CancelledError )or self .is_connected ():
                    name =getattr (callback ,'__name__',repr (callback ))
                    self ._log [__name__ ].exception ('Unhandled exception on %s',name )

    async def _handle_auto_reconnect (self :'TelegramClient'):

        try :
            await self .get_me ()
        except Exception as e :
            self ._log [__name__ ].warning ('Error executing high-level request '
            'after reconnect: %s: %s',type (e ),e )

        return 
        try :
            self ._log [__name__ ].info (
            'Asking for the current state after reconnect...')

            await self .catch_up ()

            self ._log [__name__ ].info ('Successfully fetched missed updates')
        except errors .RPCError as e :
            self ._log [__name__ ].warning ('Failed to get missed updates after '
            'reconnect: %r',e )
        except Exception :
            self ._log [__name__ ].exception (
            'Unhandled exception while getting update difference after reconnect')

class EventBuilderDict :
    """"""
    def __init__ (self ,client :'TelegramClient',update ,others ):
        self .client =client 
        self .update =update 
        self .others =others 

    def __getitem__ (self ,builder ):
        try :
            return self .__dict__ [builder ]
        except KeyError :
            event =self .__dict__ [builder ]=builder .build (
            self .update ,self .others ,self .client ._self_id )

            if isinstance (event ,EventCommon ):
                event .original_update =self .update 
                event ._entities =self .update ._entities 
                event ._set_client (self .client )
            elif event :
                event ._client =self .client 

            return event 
