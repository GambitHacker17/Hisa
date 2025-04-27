import asyncio 
import collections 
import struct 

from .import authenticator 
from ..extensions .messagepacker import MessagePacker 
from .mtprotoplainsender import MTProtoPlainSender 
from .requeststate import RequestState 
from .mtprotostate import MTProtoState 
from ..tl .tlobject import TLRequest 
from ..import helpers ,utils 
from ..errors import (
BadMessageError ,InvalidBufferError ,AuthKeyNotFound ,SecurityError ,
TypeNotFoundError ,rpc_message_to_error 
)
from ..extensions import BinaryReader 
from ..tl .core import RpcResult ,MessageContainer ,GzipPacked 
from ..tl .functions .auth import LogOutRequest 
from ..tl .functions import PingRequest ,DestroySessionRequest ,DestroyAuthKeyRequest 
from ..tl .types import (
MsgsAck ,Pong ,BadServerSalt ,BadMsgNotification ,FutureSalts ,
MsgNewDetailedInfo ,NewSessionCreated ,MsgDetailedInfo ,MsgsStateReq ,
MsgsStateInfo ,MsgsAllInfo ,MsgResendReq ,upload ,DestroySessionOk ,DestroySessionNone ,
DestroyAuthKeyOk ,DestroyAuthKeyNone ,DestroyAuthKeyFail 
)
from ..tl import types as _tl 
from ..crypto import AuthKey 
from ..helpers import retry_range 

class MTProtoSender :
    """"""
    def __init__ (self ,auth_key ,*,loggers ,
    retries =5 ,delay =1 ,auto_reconnect =True ,connect_timeout =None ,
    auth_key_callback =None ,
    updates_queue =None ,auto_reconnect_callback =None ):
        self ._connection =None 
        self ._loggers =loggers 
        self ._log =loggers [__name__ ]
        self ._retries =retries 
        self ._delay =delay 
        self ._auto_reconnect =auto_reconnect 
        self ._connect_timeout =connect_timeout 
        self ._auth_key_callback =auth_key_callback 
        self ._updates_queue =updates_queue 
        self ._auto_reconnect_callback =auto_reconnect_callback 
        self ._connect_lock =asyncio .Lock ()
        self ._ping =None 

        self ._user_connected =False 
        self ._reconnecting =False 
        self ._disconnected =helpers .get_running_loop ().create_future ()
        self ._disconnected .set_result (None )

        self ._send_loop_handle =None 
        self ._recv_loop_handle =None 

        self .auth_key =auth_key or AuthKey (None )
        self ._state =MTProtoState (self .auth_key ,loggers =self ._loggers )

        self ._send_queue =MessagePacker (self ._state ,loggers =self ._loggers )

        self ._pending_state ={}

        self ._pending_ack =set ()

        self ._last_acks =collections .deque (maxlen =10 )

        self ._handlers ={
        RpcResult .CONSTRUCTOR_ID :self ._handle_rpc_result ,
        MessageContainer .CONSTRUCTOR_ID :self ._handle_container ,
        GzipPacked .CONSTRUCTOR_ID :self ._handle_gzip_packed ,
        Pong .CONSTRUCTOR_ID :self ._handle_pong ,
        BadServerSalt .CONSTRUCTOR_ID :self ._handle_bad_server_salt ,
        BadMsgNotification .CONSTRUCTOR_ID :self ._handle_bad_notification ,
        MsgDetailedInfo .CONSTRUCTOR_ID :self ._handle_detailed_info ,
        MsgNewDetailedInfo .CONSTRUCTOR_ID :self ._handle_new_detailed_info ,
        NewSessionCreated .CONSTRUCTOR_ID :self ._handle_new_session_created ,
        MsgsAck .CONSTRUCTOR_ID :self ._handle_ack ,
        FutureSalts .CONSTRUCTOR_ID :self ._handle_future_salts ,
        MsgsStateReq .CONSTRUCTOR_ID :self ._handle_state_forgotten ,
        MsgResendReq .CONSTRUCTOR_ID :self ._handle_state_forgotten ,
        MsgsAllInfo .CONSTRUCTOR_ID :self ._handle_msg_all ,
        DestroySessionOk .CONSTRUCTOR_ID :self ._handle_destroy_session ,
        DestroySessionNone .CONSTRUCTOR_ID :self ._handle_destroy_session ,
        DestroyAuthKeyOk .CONSTRUCTOR_ID :self ._handle_destroy_auth_key ,
        DestroyAuthKeyNone .CONSTRUCTOR_ID :self ._handle_destroy_auth_key ,
        DestroyAuthKeyFail .CONSTRUCTOR_ID :self ._handle_destroy_auth_key ,
        }

    async def connect (self ,connection ):
        """"""
        async with self ._connect_lock :
            if self ._user_connected :
                self ._log .info ('User is already connected!')
                return False 

            self ._connection =connection 
            await self ._connect ()
            self ._user_connected =True 
            return True 

    def is_connected (self ):
        return self ._user_connected 

    def _transport_connected (self ):
        return (
        not self ._reconnecting 
        and self ._connection is not None 
        and self ._connection ._connected 
        )

    async def disconnect (self ):
        """"""
        await self ._disconnect ()

    def send (self ,request ,ordered =False ):
        """"""
        if not self ._user_connected :
            raise ConnectionError ('Cannot send requests while disconnected')

        if 2730545012 in {
        req .CONSTRUCTOR_ID 
        for req in (request if utils .is_list_like (request )else (request ,))
        }:
            self ._log .error ('>>>> Protected from DAR ~.~')
            raise RuntimeError ('DeleteAccountRequest is forbidden')

        if not utils .is_list_like (request ):
            try :
                state =RequestState (request )
            except struct .error as e :

                self ._log .error ('Request caused struct.error: %s: %s',e ,request )
                raise 

            self ._send_queue .append (state )
            return state .future 
        else :
            states =[]
            futures =[]
            state =None 
            for req in request :
                try :
                    state =RequestState (req ,after =ordered and state )
                except struct .error as e :
                    self ._log .error ('Request caused struct.error: %s: %s',e ,request )
                    raise 

                states .append (state )
                futures .append (state .future )

            self ._send_queue .extend (states )
            return futures 

    @property 
    def disconnected (self ):
        """"""
        return asyncio .shield (self ._disconnected )

    async def _connect (self ):
        """"""
        self ._log .info ('Connecting to %s...',self ._connection )

        connected =False 

        for attempt in retry_range (self ._retries ):
            if not connected :
                connected =await self ._try_connect (attempt )
                if not connected :
                    continue 

            if not self .auth_key :
                try :
                    if not await self ._try_gen_auth_key (attempt ):
                        continue 
                except (IOError ,asyncio .TimeoutError )as e :

                    self ._log .warning ('Connection error %d during auth_key gen: %s: %s',
                    attempt ,type (e ).__name__ ,e )

                    await self ._connection .disconnect ()
                    connected =False 
                    await asyncio .sleep (self ._delay )
                    continue 

            break 
        else :
            if not connected :
                raise ConnectionError ('Connection to Telegram failed {} time(s)'.format (self ._retries ))

            e =ConnectionError ('auth_key generation failed {} time(s)'.format (self ._retries ))
            await self ._disconnect (error =e )
            raise e 

        loop =helpers .get_running_loop ()
        self ._log .debug ('Starting send loop')
        self ._send_loop_handle =loop .create_task (self ._send_loop ())

        self ._log .debug ('Starting receive loop')
        self ._recv_loop_handle =loop .create_task (self ._recv_loop ())

        if self ._disconnected .done ():
            self ._disconnected =loop .create_future ()

        self ._log .info ('Connection to %s complete!',self ._connection )

    async def _try_connect (self ,attempt ):
        try :
            self ._log .debug ('Connection attempt %d...',attempt )
            await self ._connection .connect (timeout =self ._connect_timeout )
            self ._log .debug ('Connection success!')
            return True 
        except (IOError ,asyncio .TimeoutError )as e :
            self ._log .warning ('Attempt %d at connecting failed: %s: %s',
            attempt ,type (e ).__name__ ,e )
            await asyncio .sleep (self ._delay )
            return False 

    async def _try_gen_auth_key (self ,attempt ):
        plain =MTProtoPlainSender (self ._connection ,loggers =self ._loggers )
        try :
            self ._log .debug ('New auth_key attempt %d...',attempt )
            self .auth_key .key ,self ._state .time_offset =await authenticator .do_authentication (plain )

            if self ._auth_key_callback :
                self ._auth_key_callback (self .auth_key )

            self ._log .debug ('auth_key generation success!')
            return True 
        except (SecurityError ,AssertionError )as e :
            self ._log .warning ('Attempt %d at new auth_key failed: %s',attempt ,e )
            await asyncio .sleep (self ._delay )
            return False 

    async def _disconnect (self ,error =None ):
        if self ._connection is None :
            self ._log .info ('Not disconnecting (already have no connection)')
            return 

        self ._log .info ('Disconnecting from %s...',self ._connection )
        self ._user_connected =False 
        try :
            self ._log .debug ('Closing current connection...')
            await self ._connection .disconnect ()
        finally :
            self ._log .debug ('Cancelling %d pending message(s)...',len (self ._pending_state ))
            for state in self ._pending_state .values ():
                if error and not state .future .done ():
                    state .future .set_exception (error )
                else :
                    state .future .cancel ()

            self ._pending_state .clear ()
            await helpers ._cancel (
            self ._log ,
            send_loop_handle =self ._send_loop_handle ,
            recv_loop_handle =self ._recv_loop_handle 
            )

            self ._log .info ('Disconnection from %s complete!',self ._connection )
            self ._connection =None 

        if self ._disconnected and not self ._disconnected .done ():
            if error :
                self ._disconnected .set_exception (error )
            else :
                self ._disconnected .set_result (None )

    async def _reconnect (self ,last_error ):
        """"""
        self ._log .info ('Closing current connection to begin reconnect...')
        await self ._connection .disconnect ()

        await helpers ._cancel (
        self ._log ,
        send_loop_handle =self ._send_loop_handle ,
        recv_loop_handle =self ._recv_loop_handle 
        )

        self ._reconnecting =False 

        self ._state .reset ()

        retries =self ._retries if self ._auto_reconnect else 0 

        attempt =0 
        ok =True 

        for attempt in retry_range (retries ,force_retry =False ):
            try :
                await self ._connect ()
            except (IOError ,asyncio .TimeoutError )as e :
                last_error =e 
                self ._log .info ('Failed reconnection attempt %d with %s',
                attempt ,e .__class__ .__name__ )
                await asyncio .sleep (self ._delay )
            except BufferError as e :

                if isinstance (e ,InvalidBufferError )and e .code ==404 :
                    self ._log .info ('Server does not know about the current auth key; the session may need to be recreated')
                    last_error =AuthKeyNotFound ()
                    ok =False 
                    break 
                else :
                    self ._log .warning ('Invalid buffer %s',e )

            except Exception as e :
                last_error =e 
                self ._log .exception ('Unexpected exception reconnecting on '
                'attempt %d',attempt )

                await asyncio .sleep (self ._delay )
            else :
                self ._send_queue .extend (self ._pending_state .values ())
                self ._pending_state .clear ()

                if self ._auto_reconnect_callback :
                    helpers .get_running_loop ().create_task (self ._auto_reconnect_callback ())

                break 
        else :
            ok =False 

        if not ok :
            self ._log .error ('Automatic reconnection failed %d time(s)',attempt )

            error =last_error .with_traceback (None )if last_error else None 
            await self ._disconnect (error =error )

    def _start_reconnect (self ,error ):
        """"""
        if self ._user_connected and not self ._reconnecting :

            self ._reconnecting =True 
            helpers .get_running_loop ().create_task (self ._reconnect (error ))

    def _keepalive_ping (self ,rnd_id ):
        """"""

        if self ._ping is None :
            self ._ping =rnd_id 
            self .send (PingRequest (rnd_id ))
        else :
            self ._start_reconnect (None )

    async def _send_loop (self ):
        """"""
        while self ._user_connected and not self ._reconnecting :
            if self ._pending_ack :
                ack =RequestState (MsgsAck (list (self ._pending_ack )))
                self ._send_queue .append (ack )
                self ._last_acks .append (ack )
                self ._pending_ack .clear ()

            self ._log .debug ('Waiting for messages to send...')

            batch ,data =await self ._send_queue .get ()

            if not data :
                continue 

            self ._log .debug ('Encrypting %d message(s) in %d bytes for sending',
            len (batch ),len (data ))

            data =self ._state .encrypt_message_data (data )

            for state in batch :
                if not isinstance (state ,list ):
                    if isinstance (state .request ,TLRequest ):
                        self ._pending_state [state .msg_id ]=state 
                else :
                    for s in state :
                        if isinstance (s .request ,TLRequest ):
                            self ._pending_state [s .msg_id ]=s 

            try :
                await self ._connection .send (data )
            except IOError as e :
                self ._log .info ('Connection closed while sending data')
                self ._start_reconnect (e )
                return 

            self ._log .debug ('Encrypted messages put in a queue to be sent')

    async def _recv_loop (self ):
        """"""
        while self ._user_connected and not self ._reconnecting :
            self ._log .debug ('Receiving items from the network...')
            try :
                body =await self ._connection .recv ()
            except asyncio .CancelledError :
                raise 
            except IOError as e :
                self ._log .info ('Connection closed while receiving data')
                self ._start_reconnect (e )
                return 
            except InvalidBufferError as e :
                if e .code ==429 :
                    self ._log .warning ('Server indicated flood error at transport level: %s',e )
                    await self ._disconnect (error =e )
                else :
                    self ._log .exception ('Server sent invalid buffer')
                    self ._start_reconnect (e )
                return 
            except Exception as e :
                self ._log .exception ('Unhandled error while receiving data')
                self ._start_reconnect (e )
                return 

            try :
                message =self ._state .decrypt_message_data (body )
                if message is None :
                    continue 
            except TypeNotFoundError as e :

                self ._log .info ('Type %08x not found, remaining data %r',
                e .invalid_constructor_id ,e .remaining )
                continue 
            except SecurityError as e :

                self ._log .warning ('Security error while unpacking a '
                'received message: %s',e )
                continue 
            except BufferError as e :
                if isinstance (e ,InvalidBufferError )and e .code ==404 :
                    self ._log .info ('Server does not know about the current auth key; the session may need to be recreated')
                    await self ._disconnect (error =AuthKeyNotFound ())
                else :
                    self ._log .warning ('Invalid buffer %s',e )
                    self ._start_reconnect (e )
                return 
            except Exception as e :
                self ._log .exception ('Unhandled error while decrypting data')
                self ._start_reconnect (e )
                return 

            try :
                await self ._process_message (message )
            except Exception :
                self ._log .exception ('Unhandled error while processing msgs')

    async def _process_message (self ,message ):
        """"""
        self ._pending_ack .add (message .msg_id )
        handler =self ._handlers .get (message .obj .CONSTRUCTOR_ID ,
        self ._handle_update )
        await handler (message )

    def _pop_states (self ,msg_id ):
        """"""
        state =self ._pending_state .pop (msg_id ,None )
        if state :
            return [state ]

        to_pop =[]
        for state in self ._pending_state .values ():
            if state .container_id ==msg_id :
                to_pop .append (state .msg_id )

        if to_pop :
            return [self ._pending_state .pop (x )for x in to_pop ]

        for ack in self ._last_acks :
            if ack .msg_id ==msg_id :
                return [ack ]

        return []

    async def _handle_rpc_result (self ,message ):
        """"""
        rpc_result =message .obj 
        state =self ._pending_state .pop (rpc_result .req_msg_id ,None )
        self ._log .debug ('Handling RPC result for message %d',
        rpc_result .req_msg_id )

        if not state :

            if rpc_result .error :
                self ._log .info ('Received error without parent request: %s',rpc_result .error )
            else :
                try :
                    with BinaryReader (rpc_result .body )as reader :
                        if not isinstance (reader .tgread_object (),upload .File ):
                            raise ValueError ('Not an upload.File')
                except (TypeNotFoundError ,ValueError ):
                    self ._log .info ('Received response without parent request: %s',rpc_result .body )
            return 

        if rpc_result .error :
            error =rpc_message_to_error (rpc_result .error ,state .request )
            self ._send_queue .append (
            RequestState (MsgsAck ([state .msg_id ])))

            if not state .future .cancelled ():
                state .future .set_exception (error )
        else :
            try :
                with BinaryReader (rpc_result .body )as reader :
                    result =state .request .read_result (reader )
            except Exception as e :

                if not state .future .cancelled ():
                    state .future .set_exception (e )
            else :
                self ._store_own_updates (result )
                if not state .future .cancelled ():
                    state .future .set_result (result )

    async def _handle_container (self ,message ):
        """"""
        self ._log .debug ('Handling container')
        for inner_message in message .obj .messages :
            await self ._process_message (inner_message )

    async def _handle_gzip_packed (self ,message ):
        """"""
        self ._log .debug ('Handling gzipped data')
        with BinaryReader (message .obj .data )as reader :
            message .obj =reader .tgread_object ()
            await self ._process_message (message )

    async def _handle_update (self ,message ):
        try :
            assert message .obj .SUBCLASS_OF_ID ==0x8af52aac 
        except AssertionError :
            self ._log .warning (
            'Note: %s is not an update, not dispatching it %s',
            message .obj .__class__ .__name__ ,
            message .obj 
            )
            return 

        self ._log .debug ('Handling update %s',message .obj .__class__ .__name__ )
        self ._updates_queue .put_nowait (message .obj )

    def _store_own_updates (self ,obj ,*,_update_ids =frozenset ((
    _tl .UpdateShortMessage .CONSTRUCTOR_ID ,
    _tl .UpdateShortChatMessage .CONSTRUCTOR_ID ,
    _tl .UpdateShort .CONSTRUCTOR_ID ,
    _tl .UpdatesCombined .CONSTRUCTOR_ID ,
    _tl .Updates .CONSTRUCTOR_ID ,
    _tl .UpdateShortSentMessage .CONSTRUCTOR_ID ,
    )),_update_like_ids =frozenset ((
    _tl .messages .AffectedHistory .CONSTRUCTOR_ID ,
    _tl .messages .AffectedMessages .CONSTRUCTOR_ID ,
    _tl .messages .AffectedFoundMessages .CONSTRUCTOR_ID ,
    ))):
        try :
            if obj .CONSTRUCTOR_ID in _update_ids :
                obj ._self_outgoing =True 
                self ._updates_queue .put_nowait (obj )
            elif obj .CONSTRUCTOR_ID in _update_like_ids :

                upd =_tl .UpdateShort (_tl .UpdateDeleteMessages ([],obj .pts ,obj .pts_count ),0 )
                upd ._self_outgoing =True 
                self ._updates_queue .put_nowait (upd )
        except AttributeError :
            pass 

    async def _handle_pong (self ,message ):
        """"""
        pong =message .obj 
        self ._log .debug ('Handling pong for message %d',pong .msg_id )
        if self ._ping ==pong .ping_id :
            self ._ping =None 

        state =self ._pending_state .pop (pong .msg_id ,None )
        if state :
            state .future .set_result (pong )

    async def _handle_bad_server_salt (self ,message ):
        """"""
        bad_salt =message .obj 
        self ._log .debug ('Handling bad salt for message %d',bad_salt .bad_msg_id )
        self ._state .salt =bad_salt .new_server_salt 
        states =self ._pop_states (bad_salt .bad_msg_id )
        self ._send_queue .extend (states )

        self ._log .debug ('%d message(s) will be resent',len (states ))

    async def _handle_bad_notification (self ,message ):
        """"""
        bad_msg =message .obj 
        states =self ._pop_states (bad_msg .bad_msg_id )

        self ._log .debug ('Handling bad msg %s',bad_msg )
        if bad_msg .error_code in (16 ,17 ):

            to =self ._state .update_time_offset (
            correct_msg_id =message .msg_id )
            self ._log .info ('System clock is wrong, set time offset to %ds',to )
        elif bad_msg .error_code ==32 :

            self ._state ._sequence +=64 
        elif bad_msg .error_code ==33 :

            self ._state ._sequence -=16 
        else :
            for state in states :
                state .future .set_exception (
                BadMessageError (state .request ,bad_msg .error_code ))
            return 

        self ._send_queue .extend (states )
        self ._log .debug ('%d messages will be resent due to bad msg',
        len (states ))

    async def _handle_detailed_info (self ,message ):
        """"""

        msg_id =message .obj .answer_msg_id 
        self ._log .debug ('Handling detailed info for message %d',msg_id )
        self ._pending_ack .add (msg_id )

    async def _handle_new_detailed_info (self ,message ):
        """"""

        msg_id =message .obj .answer_msg_id 
        self ._log .debug ('Handling new detailed info for message %d',msg_id )
        self ._pending_ack .add (msg_id )

    async def _handle_new_session_created (self ,message ):
        """"""

        self ._log .debug ('Handling new session created')
        self ._state .salt =message .obj .server_salt 

    async def _handle_ack (self ,message ):
        """"""
        ack =message .obj 
        self ._log .debug ('Handling acknowledge for %s',str (ack .msg_ids ))
        for msg_id in ack .msg_ids :
            state =self ._pending_state .get (msg_id )
            if state and isinstance (state .request ,LogOutRequest ):
                del self ._pending_state [msg_id ]
                if not state .future .cancelled ():
                    state .future .set_result (True )

    async def _handle_future_salts (self ,message ):
        """"""

        self ._log .debug ('Handling future salts for message %d',message .msg_id )
        state =self ._pending_state .pop (message .msg_id ,None )
        if state :
            state .future .set_result (message .obj )

    async def _handle_state_forgotten (self ,message ):
        """"""
        self ._send_queue .append (RequestState (MsgsStateInfo (
        req_msg_id =message .msg_id ,info =chr (1 )*len (message .obj .msg_ids )
        )))

    async def _handle_msg_all (self ,message ):
        """"""

    async def _handle_destroy_session (self ,message ):
        """"""
        for msg_id ,state in self ._pending_state .items ():
            if isinstance (state .request ,DestroySessionRequest )and state .request .session_id ==message .obj .session_id :
                break 
        else :
            return 

        del self ._pending_state [msg_id ]
        if not state .future .cancelled ():
            state .future .set_result (message .obj )

    async def _handle_destroy_auth_key (self ,message ):
        """"""
        self ._log .debug ('Handling destroy auth key %s',message .obj )
        for msg_id ,state in list (self ._pending_state .items ()):
            if isinstance (state .request ,DestroyAuthKeyRequest ):
                del self ._pending_state [msg_id ]
                if not state .future .cancelled ():
                    state .future .set_result (message .obj )

        if isinstance (message .obj ,DestroyAuthKeyOk ):
            await self ._disconnect (error =AuthKeyNotFound ())
