
import asyncio 
import logging 
import time 
from hashlib import sha1 
from io import BytesIO 
from os import urandom 

import hisapyro 
from hisapyro import raw 
from hisapyro .connection import Connection 
from hisapyro .crypto import aes ,rsa ,prime 
from hisapyro .errors import SecurityCheckMismatch 
from hisapyro .raw .core import TLObject ,Long ,Int 
from .internals import MsgId 

log =logging .getLogger (__name__ )

class Auth :
    MAX_RETRIES =5 

    def __init__ (self ,client :"hisapyro.Client",dc_id :int ,test_mode :bool ):
        self .dc_id =dc_id 
        self .test_mode =test_mode 
        self .ipv6 =client .ipv6 
        self .proxy =client .proxy 

        self .connection =None 

    @staticmethod 
    def pack (data :TLObject )->bytes :
        return (
        bytes (8 )
        +Long (MsgId ())
        +Int (len (data .write ()))
        +data .write ()
        )

    @staticmethod 
    def unpack (b :BytesIO ):
        b .seek (20 )
        return TLObject .read (b )

    async def invoke (self ,data :TLObject ):
        data =self .pack (data )
        await self .connection .send (data )
        response =BytesIO (await self .connection .recv ())

        return self .unpack (response )

    async def create (self ):
        """"""
        retries_left =self .MAX_RETRIES 

        while True :
            self .connection =Connection (self .dc_id ,self .test_mode ,self .ipv6 ,self .proxy )

            try :
                log .info ("Start creating a new auth key on DC%s",self .dc_id )

                await self .connection .connect ()

                nonce =int .from_bytes (urandom (16 ),"little",signed =True )
                log .debug ("Send req_pq: %s",nonce )
                res_pq =await self .invoke (raw .functions .ReqPqMulti (nonce =nonce ))
                log .debug ("Got ResPq: %s",res_pq .server_nonce )
                log .debug ("Server public key fingerprints: %s",res_pq .server_public_key_fingerprints )

                for i in res_pq .server_public_key_fingerprints :
                    if i in rsa .server_public_keys :
                        log .debug ("Using fingerprint: %s",i )
                        public_key_fingerprint =i 
                        break 
                    else :
                        log .debug ("Fingerprint unknown: %s",i )
                else :
                    raise Exception ("Public key not found")

                pq =int .from_bytes (res_pq .pq ,"big")
                log .debug ("Start PQ factorization: %s",pq )
                start =time .time ()
                g =prime .decompose (pq )
                p ,q =sorted ((g ,pq //g ))
                log .debug ("Done PQ factorization (%ss): %s %s",round (time .time ()-start ,3 ),p ,q )

                server_nonce =res_pq .server_nonce 
                new_nonce =int .from_bytes (urandom (32 ),"little",signed =True )

                data =raw .types .PQInnerData (
                pq =res_pq .pq ,
                p =p .to_bytes (4 ,"big"),
                q =q .to_bytes (4 ,"big"),
                nonce =nonce ,
                server_nonce =server_nonce ,
                new_nonce =new_nonce ,
                ).write ()

                sha =sha1 (data ).digest ()
                padding =urandom (-(len (data )+len (sha ))%255 )
                data_with_hash =sha +data +padding 
                encrypted_data =rsa .encrypt (data_with_hash ,public_key_fingerprint )

                log .debug ("Done encrypt data with RSA")

                log .debug ("Send req_DH_params")
                server_dh_params =await self .invoke (
                raw .functions .ReqDHParams (
                nonce =nonce ,
                server_nonce =server_nonce ,
                p =p .to_bytes (4 ,"big"),
                q =q .to_bytes (4 ,"big"),
                public_key_fingerprint =public_key_fingerprint ,
                encrypted_data =encrypted_data 
                )
                )

                encrypted_answer =server_dh_params .encrypted_answer 

                server_nonce =server_nonce .to_bytes (16 ,"little",signed =True )
                new_nonce =new_nonce .to_bytes (32 ,"little",signed =True )

                tmp_aes_key =(
                sha1 (new_nonce +server_nonce ).digest ()
                +sha1 (server_nonce +new_nonce ).digest ()[:12 ]
                )

                tmp_aes_iv =(
                sha1 (server_nonce +new_nonce ).digest ()[12 :]
                +sha1 (new_nonce +new_nonce ).digest ()+new_nonce [:4 ]
                )

                server_nonce =int .from_bytes (server_nonce ,"little",signed =True )

                answer_with_hash =aes .ige256_decrypt (encrypted_answer ,tmp_aes_key ,tmp_aes_iv )
                answer =answer_with_hash [20 :]

                server_dh_inner_data =TLObject .read (BytesIO (answer ))

                log .debug ("Done decrypting answer")

                dh_prime =int .from_bytes (server_dh_inner_data .dh_prime ,"big")
                delta_time =server_dh_inner_data .server_time -time .time ()

                log .debug ("Delta time: %s",round (delta_time ,3 ))

                g =server_dh_inner_data .g 
                b =int .from_bytes (urandom (256 ),"big")
                g_b =pow (g ,b ,dh_prime ).to_bytes (256 ,"big")

                retry_id =0 

                data =raw .types .ClientDHInnerData (
                nonce =nonce ,
                server_nonce =server_nonce ,
                retry_id =retry_id ,
                g_b =g_b 
                ).write ()

                sha =sha1 (data ).digest ()
                padding =urandom (-(len (data )+len (sha ))%16 )
                data_with_hash =sha +data +padding 
                encrypted_data =aes .ige256_encrypt (data_with_hash ,tmp_aes_key ,tmp_aes_iv )

                log .debug ("Send set_client_DH_params")
                set_client_dh_params_answer =await self .invoke (
                raw .functions .SetClientDHParams (
                nonce =nonce ,
                server_nonce =server_nonce ,
                encrypted_data =encrypted_data 
                )
                )

                g_a =int .from_bytes (server_dh_inner_data .g_a ,"big")
                auth_key =pow (g_a ,b ,dh_prime ).to_bytes (256 ,"big")
                server_nonce =server_nonce .to_bytes (16 ,"little",signed =True )

                SecurityCheckMismatch .check (dh_prime ==prime .CURRENT_DH_PRIME ,"dh_prime == prime.CURRENT_DH_PRIME")
                log .debug ("DH parameters check: OK")

                g_b =int .from_bytes (g_b ,"big")
                SecurityCheckMismatch .check (1 <g <dh_prime -1 ,"1 < g < dh_prime - 1")
                SecurityCheckMismatch .check (1 <g_a <dh_prime -1 ,"1 < g_a < dh_prime - 1")
                SecurityCheckMismatch .check (1 <g_b <dh_prime -1 ,"1 < g_b < dh_prime - 1")
                SecurityCheckMismatch .check (
                2 **(2048 -64 )<g_a <dh_prime -2 **(2048 -64 ),
                "2 ** (2048 - 64) < g_a < dh_prime - 2 ** (2048 - 64)"
                )
                SecurityCheckMismatch .check (
                2 **(2048 -64 )<g_b <dh_prime -2 **(2048 -64 ),
                "2 ** (2048 - 64) < g_b < dh_prime - 2 ** (2048 - 64)"
                )
                log .debug ("g_a and g_b validation: OK")

                answer =server_dh_inner_data .write ()
                SecurityCheckMismatch .check (
                answer_with_hash [:20 ]==sha1 (answer ).digest (),
                "answer_with_hash[:20] == sha1(answer).digest()"
                )
                log .debug ("SHA1 hash values check: OK")

                SecurityCheckMismatch .check (nonce ==res_pq .nonce ,"nonce == res_pq.nonce")

                server_nonce =int .from_bytes (server_nonce ,"little",signed =True )
                SecurityCheckMismatch .check (nonce ==server_dh_params .nonce ,"nonce == server_dh_params.nonce")
                SecurityCheckMismatch .check (
                server_nonce ==server_dh_params .server_nonce ,
                "server_nonce == server_dh_params.server_nonce"
                )

                SecurityCheckMismatch .check (
                nonce ==set_client_dh_params_answer .nonce ,
                "nonce == set_client_dh_params_answer.nonce"
                )
                SecurityCheckMismatch .check (
                server_nonce ==set_client_dh_params_answer .server_nonce ,
                "server_nonce == set_client_dh_params_answer.server_nonce"
                )
                server_nonce =server_nonce .to_bytes (16 ,"little",signed =True )
                log .debug ("Nonce fields check: OK")

                server_salt =aes .xor (new_nonce [:8 ],server_nonce [:8 ])

                log .debug ("Server salt: %s",int .from_bytes (server_salt ,"little"))

                log .info ("Done auth key exchange: %s",set_client_dh_params_answer .__class__ .__name__ )
            except Exception as e :
                log .info ("Retrying due to %s: %s",type (e ).__name__ ,e )

                if retries_left :
                    retries_left -=1 
                else :
                    raise e 

                await asyncio .sleep (1 )
                continue 
            else :
                return auth_key 
            finally :
                await self .connection .close ()
