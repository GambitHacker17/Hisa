""""""
import ctypes 
import ctypes .util 
import platform 
import sys 
try :
    import ctypes .macholib .dyld 
except ImportError :
    pass 
import logging 
import os 

__log__ =logging .getLogger (__name__ )

def _find_ssl_lib ():
    lib =ctypes .util .find_library ('ssl')

    if sys .platform =='darwin':
        release ,_version_info ,_machine =platform .mac_ver ()
        ver ,major ,*_ =release .split ('.')

        if int (ver )>10 or int (ver )==10 and int (major )>14 :
            lib =(
            ctypes .util .find_library ('libssl.46')or 
            ctypes .util .find_library ('libssl.44')or 
            ctypes .util .find_library ('libssl.42')
            )
    if not lib :
        raise OSError ('no library called "ssl" found')

    try :
        libssl =ctypes .cdll .LoadLibrary (lib )
    except OSError :
        pass 
    else :
        return libssl 

    try :

        paths =ctypes .macholib .dyld .DEFAULT_LIBRARY_FALLBACK 
    except AttributeError :
        paths =[
        os .path .expanduser ("~/lib"),
        "/usr/local/lib",
        "/lib",
        "/usr/lib",
        ]

    for path in paths :
        if os .path .isdir (path ):
            for root ,_ ,files in os .walk (path ):
                if lib in files :

                    lib =os .path .realpath (os .path .join (root ,lib ))
                    return ctypes .cdll .LoadLibrary (lib )
    else :
        raise OSError ('no absolute path for "%s" and cannot load by name'%lib )

try :
    _libssl =_find_ssl_lib ()
except OSError as e :

    __log__ .info ('Failed to load SSL library: %s (%s)',type (e ),e )
    _libssl =None 

if not _libssl :
    decrypt_ige =None 
    encrypt_ige =None 
else :

    AES_ENCRYPT =ctypes .c_int (1 )
    AES_DECRYPT =ctypes .c_int (0 )
    AES_MAXNR =14 

    class AES_KEY (ctypes .Structure ):
        """"""
        _fields_ =[
        ('rd_key',ctypes .c_uint32 *(4 *(AES_MAXNR +1 ))),
        ('rounds',ctypes .c_uint ),
        ]

    def decrypt_ige (cipher_text ,key ,iv ):
        aes_key =AES_KEY ()
        key_len =ctypes .c_int (8 *len (key ))
        key =(ctypes .c_ubyte *len (key ))(*key )
        iv =(ctypes .c_ubyte *len (iv ))(*iv )

        in_len =ctypes .c_size_t (len (cipher_text ))
        in_ptr =(ctypes .c_ubyte *len (cipher_text ))(*cipher_text )
        out_ptr =(ctypes .c_ubyte *len (cipher_text ))()

        _libssl .AES_set_decrypt_key (key ,key_len ,ctypes .byref (aes_key ))
        _libssl .AES_ige_encrypt (
        ctypes .byref (in_ptr ),
        ctypes .byref (out_ptr ),
        in_len ,
        ctypes .byref (aes_key ),
        ctypes .byref (iv ),
        AES_DECRYPT 
        )

        return bytes (out_ptr )

    def encrypt_ige (plain_text ,key ,iv ):
        aes_key =AES_KEY ()
        key_len =ctypes .c_int (8 *len (key ))
        key =(ctypes .c_ubyte *len (key ))(*key )
        iv =(ctypes .c_ubyte *len (iv ))(*iv )

        in_len =ctypes .c_size_t (len (plain_text ))
        in_ptr =(ctypes .c_ubyte *len (plain_text ))(*plain_text )
        out_ptr =(ctypes .c_ubyte *len (plain_text ))()

        _libssl .AES_set_encrypt_key (key ,key_len ,ctypes .byref (aes_key ))
        _libssl .AES_ige_encrypt (
        ctypes .byref (in_ptr ),
        ctypes .byref (out_ptr ),
        in_len ,
        ctypes .byref (aes_key ),
        ctypes .byref (iv ),
        AES_ENCRYPT 
        )

        return bytes (out_ptr )
