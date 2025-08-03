import asyncio 
import hashlib 
import os 

from .connection import ObfuscatedConnection 
from .tcpabridged import AbridgedPacketCodec 
from .tcpintermediate import (
IntermediatePacketCodec ,
RandomizedIntermediatePacketCodec 
)

from ...crypto import AESModeCTR 

class MTProxyIO :
    """"""
    header =None 

    def __init__ (self ,connection ):
        self ._reader =connection ._reader 
        self ._writer =connection ._writer 

        (self .header ,
        self ._encrypt ,
        self ._decrypt )=self .init_header (
        connection ._secret ,connection ._dc_id ,connection .packet_codec )

    @staticmethod 
    def init_header (secret ,dc_id ,packet_codec ):

        is_dd =(len (secret )==17 )and (secret [0 ]==0xDD )
        is_rand_codec =issubclass (
        packet_codec ,RandomizedIntermediatePacketCodec )
        if is_dd and not is_rand_codec :
            raise ValueError (
            "Only RandomizedIntermediate can be used with dd-secrets")
        secret =secret [1 :]if is_dd else secret 
        if len (secret )!=16 :
            raise ValueError (
            "MTProxy secret must be a hex-string representing 16 bytes")

        keywords =(b'PVrG',b'GET ',b'POST',b'\xee\xee\xee\xee')
        while True :
            random =os .urandom (64 )
            if (random [0 ]!=0xef and 
            random [:4 ]not in keywords and 
            random [4 :4 ]!=b'\0\0\0\0'):
                break 

        random =bytearray (random )
        random_reversed =random [55 :7 :-1 ]

        encrypt_key =hashlib .sha256 (
        bytes (random [8 :40 ])+secret ).digest ()
        encrypt_iv =bytes (random [40 :56 ])
        decrypt_key =hashlib .sha256 (
        bytes (random_reversed [:32 ])+secret ).digest ()
        decrypt_iv =bytes (random_reversed [32 :48 ])

        encryptor =AESModeCTR (encrypt_key ,encrypt_iv )
        decryptor =AESModeCTR (decrypt_key ,decrypt_iv )

        random [56 :60 ]=packet_codec .obfuscate_tag 

        dc_id_bytes =dc_id .to_bytes (2 ,"little",signed =True )
        random =random [:60 ]+dc_id_bytes +random [62 :]
        random [56 :64 ]=encryptor .encrypt (bytes (random ))[56 :64 ]
        return (random ,encryptor ,decryptor )

    async def readexactly (self ,n ):
        return self ._decrypt .encrypt (await self ._reader .readexactly (n ))

    def write (self ,data ):
        self ._writer .write (self ._encrypt .encrypt (data ))

class TcpMTProxy (ObfuscatedConnection ):
    """"""
    packet_codec =None 
    obfuscated_io =MTProxyIO 

    def __init__ (self ,ip ,port ,dc_id ,*,loggers ,proxy =None ,local_addr =None ):

        proxy_host ,proxy_port =self .address_info (proxy )
        self ._secret =bytes .fromhex (proxy [2 ])
        super ().__init__ (
        proxy_host ,proxy_port ,dc_id ,loggers =loggers )

    async def _connect (self ,timeout =None ,ssl =None ):
        await super ()._connect (timeout =timeout ,ssl =ssl )

        try :
            await asyncio .wait_for (self ._reader ._wait_for_data ('proxy'),2 )
        except asyncio .TimeoutError :
            pass 
        except Exception :
            await asyncio .sleep (2 )

        if self ._reader .at_eof ():
            await self .disconnect ()
            raise ConnectionError (
            'Proxy closed the connection after sending initial payload')

    @staticmethod 
    def address_info (proxy_info ):
        if proxy_info is None :
            raise ValueError ("No proxy info specified for MTProxy connection")
        return proxy_info [:2 ]

class ConnectionTcpMTProxyAbridged (TcpMTProxy ):
    """"""
    packet_codec =AbridgedPacketCodec 

class ConnectionTcpMTProxyIntermediate (TcpMTProxy ):
    """"""
    packet_codec =IntermediatePacketCodec 

class ConnectionTcpMTProxyRandomizedIntermediate (TcpMTProxy ):
    """"""
    packet_codec =RandomizedIntermediatePacketCodec 
