import os
import struct
from hashlib import sha1
try:
    import rsa
    import rsa.core
except ImportError:
    rsa = None
    raise ImportError('Missing module "rsa", please install via pip.')
from ..tl import TLObject
_server_keys = {}
def get_byte_array(integer):
    return int.to_bytes(
        integer,
        (integer.bit_length() + 8 - 1) // 8,  
        byteorder='big',
        signed=False
    )
def _compute_fingerprint(key):
    n = TLObject.serialize_bytes(get_byte_array(key.n))
    e = TLObject.serialize_bytes(get_byte_array(key.e))
    return struct.unpack('<q', sha1(n + e).digest()[-8:])[0]
def add_key(pub, *, old):
    global _server_keys
    key = rsa.PublicKey.load_pkcs1(pub)
    _server_keys[_compute_fingerprint(key)] = (key, old)
def encrypt(fingerprint, data, *, use_old=False):
    global _server_keys
    key, old = _server_keys.get(fingerprint, [None, None])
    if (not key) or (old and not use_old):
        return None
    to_encrypt = sha1(data).digest() + data + os.urandom(235 - len(data))
    payload = int.from_bytes(to_encrypt, 'big')
    encrypted = rsa.core.encrypt_int(payload, key.e, key.n)
    block = encrypted.to_bytes(256, 'big')
    return block
for pub in (
        ,
        ,
        ,
        ,
):
    add_key(pub, old=False)
for pub in (
        ,
        ,
        ,
        ,
):
    add_key(pub, old=True)