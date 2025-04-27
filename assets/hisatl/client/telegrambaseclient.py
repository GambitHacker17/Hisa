import abc 
import re 
import asyncio 
import collections 
import logging 
import platform 
import time 
import typing 
import datetime 

from ..import version ,helpers ,__name__ as __base_name__ 
from ..crypto import rsa 
from ..entitycache import EntityCache 
from ..extensions import markdown 
from ..network import MTProtoSender ,Connection ,ConnectionTcpFull ,TcpMTProxy 
from ..sessions import Session ,SQLiteSession ,MemorySession 
from ..tl import functions ,types 
from ..tl .alltlobjects import LAYER 
from .._updates import MessageBox ,EntityCache as MbEntityCache ,SessionState ,ChannelState ,Entity ,EntityType 

DEFAULT_DC_ID =2 
DEFAULT_IPV4_IP ='149.154.167.51'
DEFAULT_IPV6_IP ='2001:67c:4e8:f002::a'
DEFAULT_PORT =443 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

_base_log =logging .getLogger (__base_name__ )

_DISCONNECT_EXPORTED_AFTER =60 

class _ExportState :
    def __init__ (self ):

        self ._n =0 
        self ._zero_ts =0 
        self ._connected =False 

    def add_borrow (self ):
        self ._n +=1 
        self ._connected =True 

    def add_return (self ):
        self ._n -=1 
        assert self ._n >=0 ,'returned sender more than it was borrowed'
        if self ._n ==0 :
            self ._zero_ts =time .time ()

    def should_disconnect (self ):
        return (self ._n ==0 
        and self ._connected 
        and (time .time ()-self ._zero_ts )>_DISCONNECT_EXPORTED_AFTER )

    def need_connect (self ):
        return not self ._connected 

    def mark_disconnected (self ):
        assert self .should_disconnect (),'marked as disconnected when it was borrowed'
        self ._connected =False 

class TelegramBaseClient (abc .ABC ):
    """"""

    __version__ =version .__version__ 

    _config =None 
    _cdn_config =None 

    def __init__ (
    self :'TelegramClient',
    session :'typing.Union[str, Session]',
    api_id :int ,
    api_hash :str ,
    *,
    connection :'typing.Type[Connection]'=ConnectionTcpFull ,
    use_ipv6 :bool =False ,
    proxy :typing .Union [tuple ,dict ]=None ,
    local_addr :typing .Union [str ,tuple ]=None ,
    timeout :int =10 ,
    request_retries :int =5 ,
    connection_retries :int =5 ,
    retry_delay :int =1 ,
    auto_reconnect :bool =True ,
    sequential_updates :bool =False ,
    flood_sleep_threshold :int =60 ,
    raise_last_call_error :bool =False ,
    device_model :str =None ,
    system_version :str =None ,
    app_version :str =None ,
    lang_code :str ='en',
    system_lang_code :str ='en',
    loop :asyncio .AbstractEventLoop =None ,
    base_logger :typing .Union [str ,logging .Logger ]=None ,
    receive_updates :bool =True ,
    catch_up :bool =False 
    ):
        if not api_id or not api_hash :
            raise ValueError (
            "Your API ID or Hash cannot be empty or None. "
            "Refer to telethon.rtfd.io for more information.")

        self ._use_ipv6 =use_ipv6 

        if isinstance (base_logger ,str ):
            base_logger =logging .getLogger (base_logger )
        elif not isinstance (base_logger ,logging .Logger ):
            base_logger =_base_log 

        class _Loggers (dict ):
            def __missing__ (self ,key ):
                if key .startswith ("telethon."):
                    key =key .split ('.',maxsplit =1 )[1 ]

                return base_logger .getChild (key )

        self ._log =_Loggers ()

        if isinstance (session ,str )or session is None :
            try :
                session =SQLiteSession (session )
            except ImportError :
                import warnings 
                warnings .warn (
                'The sqlite3 module is not available under this '
                'Python installation and no custom session '
                'instance was given; using MemorySession.\n'
                'You will need to re-login every time unless '
                'you use another session storage'
                )
                session =MemorySession ()
        elif not isinstance (session ,Session ):
            raise TypeError (
            'The given session must be a str or a Session instance.'
            )

        if (not session .server_address or 
        (':'in session .server_address )!=use_ipv6 ):
            session .set_dc (
            DEFAULT_DC_ID ,
            DEFAULT_IPV6_IP if self ._use_ipv6 else DEFAULT_IPV4_IP ,
            DEFAULT_PORT 
            )

        self .flood_sleep_threshold =flood_sleep_threshold 

        self .session =session 
        self ._entity_cache =EntityCache ()
        self .api_id =int (api_id )
        self .api_hash =api_hash 

        if not callable (getattr (self .loop ,'sock_connect',None )):
            raise TypeError (
            'Event loop of type {} lacks `sock_connect`, which is needed to use proxies.\n\n'
            'Change the event loop in use to use proxies:\n'
            '#\n'
            'import asyncio\n'
            'asyncio.set_event_loop(asyncio.SelectorEventLoop())'.format (
            self .loop .__class__ .__name__ 
            )
            )

        if local_addr is not None :
            if use_ipv6 is False and ':'in local_addr :
                raise TypeError (
                'A local IPv6 address must only be used with `use_ipv6=True`.'
                )
            elif use_ipv6 is True and ':'not in local_addr :
                raise TypeError (
                '`use_ipv6=True` must only be used with a local IPv6 address.'
                )

        self ._raise_last_call_error =raise_last_call_error 

        self ._request_retries =request_retries 
        self ._connection_retries =connection_retries 
        self ._retry_delay =retry_delay or 0 
        self ._proxy =proxy 
        self ._local_addr =local_addr 
        self ._timeout =timeout 
        self ._auto_reconnect =auto_reconnect 

        assert isinstance (connection ,type )
        self ._connection =connection 
        init_proxy =None if not issubclass (connection ,TcpMTProxy )else types .InputClientProxy (*connection .address_info (proxy ))

        system =platform .uname ()

        if system .machine in ('x86_64','AMD64'):
            default_device_model ='PC 64bit'
        elif system .machine in ('i386','i686','x86'):
            default_device_model ='PC 32bit'
        else :
            default_device_model =system .machine 
        default_system_version =re .sub (r'-.+','',system .release )

        self ._init_request =functions .InitConnectionRequest (
        api_id =self .api_id ,
        device_model =device_model or default_device_model or 'Unknown',
        system_version =system_version or default_system_version or '1.0',
        app_version =app_version or self .__version__ ,
        lang_code =lang_code ,
        system_lang_code =system_lang_code ,
        lang_pack ='',
        query =None ,
        proxy =init_proxy 
        )

        self ._flood_waited_requests ={}

        self ._borrowed_senders ={}
        self ._borrow_sender_lock =asyncio .Lock ()

        self ._loop =None 
        self ._updates_error =None 
        self ._updates_handle =None 
        self ._keepalive_handle =None 
        self ._last_request =time .time ()
        self ._no_updates =not receive_updates 

        self ._sequential_updates =sequential_updates 
        self ._event_handler_tasks =set ()

        self ._authorized =None 

        self ._event_builders =[]

        self ._conversations =collections .defaultdict (set )

        self ._albums ={}

        self ._parse_mode =markdown 

        self ._phone_code_hash ={}
        self ._phone =None 
        self ._tos =None 

        self ._self_input_peer =None 
        self ._bot =None 

        self ._megagroup_cache ={}

        self ._catch_up =catch_up 
        self ._updates_queue =asyncio .Queue ()
        self ._message_box =MessageBox (self ._log ['messagebox'])

        self ._mb_entity_cache =MbEntityCache ()

        self ._sender =MTProtoSender (
        self .session .auth_key ,
        loggers =self ._log ,
        retries =self ._connection_retries ,
        delay =self ._retry_delay ,
        auto_reconnect =self ._auto_reconnect ,
        connect_timeout =self ._timeout ,
        auth_key_callback =self ._auth_key_callback ,
        updates_queue =self ._updates_queue ,
        auto_reconnect_callback =self ._handle_auto_reconnect 
        )

    @property 
    def loop (self :'TelegramClient')->asyncio .AbstractEventLoop :
        """"""
        return helpers .get_running_loop ()

    @property 
    def disconnected (self :'TelegramClient')->asyncio .Future :
        """"""
        return self ._sender .disconnected 

    @property 
    def flood_sleep_threshold (self ):
        return self ._flood_sleep_threshold 

    @flood_sleep_threshold .setter 
    def flood_sleep_threshold (self ,value ):

        self ._flood_sleep_threshold =min (value or 0 ,24 *60 *60 )

    async def connect (self :'TelegramClient')->None :
        """"""
        if self .session is None :
            raise ValueError ('TelegramClient instance cannot be reused after logging out')

        if self ._loop is None :
            self ._loop =helpers .get_running_loop ()
        elif self ._loop !=helpers .get_running_loop ():
            raise RuntimeError ('The asyncio event loop must not change after connection (see the FAQ for details)')

        if not await self ._sender .connect (self ._connection (
        self .session .server_address ,
        self .session .port ,
        self .session .dc_id ,
        loggers =self ._log ,
        proxy =self ._proxy ,
        local_addr =self ._local_addr 
        )):

            return 

        self .session .auth_key =self ._sender .auth_key 
        self .session .save ()

        if self ._catch_up :
            ss =SessionState (0 ,0 ,False ,0 ,0 ,0 ,0 ,None )
            cs =[]

            for entity_id ,state in self .session .get_update_states ():
                if entity_id ==0 :

                    ss =SessionState (0 ,0 ,False ,state .pts ,state .qts ,int (state .date .timestamp ()),state .seq ,None )
                else :
                    cs .append (ChannelState (entity_id ,state .pts ))

            self ._message_box .load (ss ,cs )
            for state in cs :
                try :
                    entity =self .session .get_input_entity (state .channel_id )
                except ValueError :
                    self ._log [__name__ ].warning (
                    'No access_hash in cache for channel %s, will not catch up',state .channel_id )
                else :
                    self ._mb_entity_cache .put (Entity (EntityType .CHANNEL ,entity .channel_id ,entity .access_hash ))

        self ._init_request .query =functions .help .GetConfigRequest ()

        req =self ._init_request 
        if self ._no_updates :
            req =functions .InvokeWithoutUpdatesRequest (req )

        await self ._sender .send (functions .InvokeWithLayerRequest (LAYER ,req ))

        if self ._message_box .is_empty ():
            me =await self .get_me ()
            if me :
                await self ._on_login (me )

        self ._updates_handle =self .loop .create_task (self ._update_loop ())
        self ._keepalive_handle =self .loop .create_task (self ._keepalive_loop ())

    def is_connected (self :'TelegramClient')->bool :
        """"""
        sender =getattr (self ,'_sender',None )
        return sender and sender .is_connected ()

    def disconnect (self :'TelegramClient'):
        """"""
        if self .loop .is_running ():

            return asyncio .shield (self .loop .create_task (self ._disconnect_coro ()))
        else :
            try :
                self .loop .run_until_complete (self ._disconnect_coro ())
            except RuntimeError :

                pass 

    def set_proxy (self :'TelegramClient',proxy :typing .Union [tuple ,dict ]):
        """"""
        init_proxy =None if not issubclass (self ._connection ,TcpMTProxy )else types .InputClientProxy (*self ._connection .address_info (proxy ))

        self ._init_request .proxy =init_proxy 
        self ._proxy =proxy 

        connection =getattr (self ._sender ,"_connection",None )
        if connection :
            if isinstance (connection ,TcpMTProxy ):
                connection ._ip =proxy [0 ]
                connection ._port =proxy [1 ]
            else :
                connection ._proxy =proxy 

    async def _disconnect_coro (self :'TelegramClient'):
        if self .session is None :
            return 

        await self ._disconnect ()

        async with self ._borrow_sender_lock :
            for state ,sender in self ._borrowed_senders .values ():

                await sender .disconnect ()

                state ._connected =False 

            self ._borrowed_senders .clear ()

        if self ._event_handler_tasks :
            for task in self ._event_handler_tasks :
                task .cancel ()

            await asyncio .wait (self ._event_handler_tasks )
            self ._event_handler_tasks .clear ()

        entities =self ._mb_entity_cache .get_all_entities ()

        self .session .process_entities (types .contacts .ResolvedPeer (None ,[e ._as_input_peer ()for e in entities ],[]))

        ss ,cs =self ._message_box .session_state ()
        self .session .set_update_state (0 ,types .updates .State (**ss ,unread_count =0 ))
        now =datetime .datetime .now ()
        for channel_id ,pts in cs .items ():
            self .session .set_update_state (channel_id ,types .updates .State (pts ,0 ,now ,0 ,unread_count =0 ))

        self .session .close ()

    async def _disconnect (self :'TelegramClient'):
        """"""
        await self ._sender .disconnect ()
        await helpers ._cancel (self ._log [__name__ ],
        updates_handle =self ._updates_handle ,
        keepalive_handle =self ._keepalive_handle )

    async def _switch_dc (self :'TelegramClient',new_dc ):
        """"""
        self ._log [__name__ ].info ('Reconnecting to new data center %s',new_dc )
        dc =await self ._get_dc (new_dc )

        self .session .set_dc (dc .id ,dc .ip_address ,dc .port )

        self ._sender .auth_key .key =None 
        self .session .auth_key =None 
        self .session .save ()
        await self ._disconnect ()
        return await self .connect ()

    def _auth_key_callback (self :'TelegramClient',auth_key ):
        """"""
        self .session .auth_key =auth_key 
        self .session .save ()

    async def _get_dc (self :'TelegramClient',dc_id ,cdn =False ):
        """"""
        cls =self .__class__ 
        if not cls ._config :
            cls ._config =await self (functions .help .GetConfigRequest ())

        if cdn and not self ._cdn_config :
            cls ._cdn_config =await self (functions .help .GetCdnConfigRequest ())
            for pk in cls ._cdn_config .public_keys :
                rsa .add_key (pk .public_key )

        try :
            return next (
            dc for dc in cls ._config .dc_options 
            if dc .id ==dc_id 
            and bool (dc .ipv6 )==self ._use_ipv6 and bool (dc .cdn )==cdn 
            )
        except StopIteration :
            self ._log [__name__ ].warning (
            'Failed to get DC %s (cdn = %s) with use_ipv6 = %s; retrying ignoring IPv6 check',
            dc_id ,cdn ,self ._use_ipv6 
            )
            return next (
            dc for dc in cls ._config .dc_options 
            if dc .id ==dc_id and bool (dc .cdn )==cdn 
            )

    async def _create_exported_sender (self :'TelegramClient',dc_id ):
        """"""

        dc =await self ._get_dc (dc_id )

        sender =MTProtoSender (None ,loggers =self ._log )
        await sender .connect (self ._connection (
        dc .ip_address ,
        dc .port ,
        dc .id ,
        loggers =self ._log ,
        proxy =self ._proxy ,
        local_addr =self ._local_addr 
        ))
        self ._log [__name__ ].info ('Exporting auth for new borrowed sender in %s',dc )
        auth =await self (functions .auth .ExportAuthorizationRequest (dc_id ))
        self ._init_request .query =functions .auth .ImportAuthorizationRequest (id =auth .id ,bytes =auth .bytes )
        req =functions .InvokeWithLayerRequest (LAYER ,self ._init_request )
        await sender .send (req )
        return sender 

    async def _borrow_exported_sender (self :'TelegramClient',dc_id ):
        """"""
        async with self ._borrow_sender_lock :
            self ._log [__name__ ].debug ('Borrowing sender for dc_id %d',dc_id )
            state ,sender =self ._borrowed_senders .get (dc_id ,(None ,None ))

            if state is None :
                state =_ExportState ()
                sender =await self ._create_exported_sender (dc_id )
                sender .dc_id =dc_id 
                self ._borrowed_senders [dc_id ]=(state ,sender )

            elif state .need_connect ():
                dc =await self ._get_dc (dc_id )
                await sender .connect (self ._connection (
                dc .ip_address ,
                dc .port ,
                dc .id ,
                loggers =self ._log ,
                proxy =self ._proxy ,
                local_addr =self ._local_addr 
                ))

            state .add_borrow ()
            return sender 

    async def _return_exported_sender (self :'TelegramClient',sender ):
        """"""
        async with self ._borrow_sender_lock :
            self ._log [__name__ ].debug ('Returning borrowed sender for dc_id %d',sender .dc_id )
            state ,_ =self ._borrowed_senders [sender .dc_id ]
            state .add_return ()

    async def _clean_exported_senders (self :'TelegramClient'):
        """"""
        async with self ._borrow_sender_lock :
            for dc_id ,(state ,sender )in self ._borrowed_senders .items ():
                if state .should_disconnect ():
                    self ._log [__name__ ].info (
                    'Disconnecting borrowed sender for DC %d',dc_id )

                    await sender .disconnect ()
                    state .mark_disconnected ()

    async def _get_cdn_client (self :'TelegramClient',cdn_redirect ):
        """"""

        raise NotImplementedError 
        session =self ._exported_sessions .get (cdn_redirect .dc_id )
        if not session :
            dc =await self ._get_dc (cdn_redirect .dc_id ,cdn =True )
            session =self .session .clone ()
            session .set_dc (dc .id ,dc .ip_address ,dc .port )
            self ._exported_sessions [cdn_redirect .dc_id ]=session 

        self ._log [__name__ ].info ('Creating new CDN client')
        client =TelegramBaseClient (
        session ,self .api_id ,self .api_hash ,
        proxy =self ._sender .connection .conn .proxy ,
        timeout =self ._sender .connection .get_timeout ()
        )

        client .connect (_sync_updates =False )
        return client 

    @abc .abstractmethod 
    def __call__ (self :'TelegramClient',request ,ordered =False ):
        """"""
        raise NotImplementedError 

    @abc .abstractmethod 
    def _update_loop (self :'TelegramClient'):
        raise NotImplementedError 

    @abc .abstractmethod 
    async def _handle_auto_reconnect (self :'TelegramClient'):
        raise NotImplementedError 

