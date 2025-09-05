""""""
import asyncio 
import io 
import enum 
import os 
import struct 
import inspect 
import logging 
import functools 
import sys 
from pathlib import Path 
from hashlib import sha1 

class _EntityType (enum .Enum ):
    USER =0 
    CHAT =1 
    CHANNEL =2 

_log =logging .getLogger (__name__ )

def generate_random_long (signed =True ):
    """"""
    return int .from_bytes (os .urandom (8 ),signed =signed ,byteorder ='little')

def ensure_parent_dir_exists (file_path ):
    """"""
    parent =os .path .dirname (file_path )
    if parent :
        os .makedirs (parent ,exist_ok =True )

def add_surrogate (text ):
    return ''.join (

    ''.join (chr (y )for y in struct .unpack ('<HH',x .encode ('utf-16le')))
    if (0x10000 <=ord (x )<=0x10FFFF )else x for x in text 
    )

def del_surrogate (text ):
    return text .encode ('utf-16','surrogatepass').decode ('utf-16')

def within_surrogate (text ,index ,*,length =None ):
    """"""
    if length is None :
        length =len (text )

    return (
    1 <index <len (text )and 
    '\ud800'<=text [index -1 ]<='\udfff'and 
    '\ud800'<=text [index ]<='\udfff'
    )

def strip_text (text ,entities ):
    """"""
    if not entities :
        return text .strip ()

    len_ori =len (text )
    text =text .lstrip ()
    left_offset =len_ori -len (text )
    text =text .rstrip ()
    len_final =len (text )

    for i in reversed (range (len (entities ))):
        e =entities [i ]
        if e .length ==0 :
            del entities [i ]
            continue 

        if e .offset +e .length >left_offset :
            if e .offset >=left_offset :

                e .offset -=left_offset 

            else :

                e .length =e .offset +e .length -left_offset 
                e .offset =0 

        else :

            del entities [i ]
            continue 

        if e .offset +e .length <=len_final :

            continue 
        if e .offset >=len_final :

            del entities [i ]
        else :

            e .length =len_final -e .offset 

    return text 

def retry_range (retries ,force_retry =True ):
    """"""

    if force_retry and not (retries is None or retries <0 ):
        retries +=1 

    attempt =0 
    while attempt !=retries :
        attempt +=1 
        yield attempt 

async def _maybe_await (value ):
    if inspect .isawaitable (value ):
        return await value 
    else :
        return value 

async def _cancel (log ,**tasks ):
    """"""
    for name ,task in tasks .items ():
        if not task :
            continue 

        task .cancel ()
        try :
            await task 
        except asyncio .CancelledError :
            pass 
        except RuntimeError :

            pass 
        except AssertionError as e :

            if e .args !=("yield from wasn't used with future",):
                log .exception ('Unhandled exception from %s after cancelling '
                '%s (%s)',name ,type (task ),task )
        except Exception :
            log .exception ('Unhandled exception from %s after cancelling '
            '%s (%s)',name ,type (task ),task )

def _sync_enter (self ):
    """"""
    if hasattr (self ,'loop'):
        loop =self .loop 
    else :
        loop =self ._client .loop 

    if loop .is_running ():
        raise RuntimeError (
        'You must use "async with" if the event loop '
        'is running (i.e. you are inside an "async def")'
        )

    return loop .run_until_complete (self .__aenter__ ())

def _sync_exit (self ,*args ):
    if hasattr (self ,'loop'):
        loop =self .loop 
    else :
        loop =self ._client .loop 

    return loop .run_until_complete (self .__aexit__ (*args ))

def _entity_type (entity ):

    try :
        if entity .SUBCLASS_OF_ID not in (
        0x2d45687 ,
        0xc91c90b6 ,
        0xe669bf46 ,
        0x40f202fd ,
        0x2da17977 ,
        0xc5af5d94 ,
        0x1f4661b9 ,
        0xd49a2697 ,
        ):
            raise TypeError ('{} does not have any entity type'.format (entity ))
    except AttributeError :
        raise TypeError ('{} is not a TLObject, cannot determine entity type'.format (entity ))

    name =entity .__class__ .__name__ 
    if 'User'in name :
        return _EntityType .USER 
    elif 'Chat'in name :
        return _EntityType .CHAT 
    elif 'Channel'in name :
        return _EntityType .CHANNEL 
    elif 'Self'in name :
        return _EntityType .USER 

    raise TypeError ('{} does not have any entity type'.format (entity ))

def generate_key_data_from_nonce (server_nonce ,new_nonce ):
    """"""
    server_nonce =server_nonce .to_bytes (16 ,'little',signed =True )
    new_nonce =new_nonce .to_bytes (32 ,'little',signed =True )
    hash1 =sha1 (new_nonce +server_nonce ).digest ()
    hash2 =sha1 (server_nonce +new_nonce ).digest ()
    hash3 =sha1 (new_nonce +new_nonce ).digest ()

    key =hash1 +hash2 [:12 ]
    iv =hash2 [12 :20 ]+hash3 +new_nonce [:4 ]
    return key ,iv 

class TotalList (list ):
    """"""
    def __init__ (self ,*args ,**kwargs ):
        super ().__init__ (*args ,**kwargs )
        self .total =0 

    def __str__ (self ):
        return '[{}, total={}]'.format (
        ', '.join (str (x )for x in self ),self .total )

    def __repr__ (self ):
        return '[{}, total={}]'.format (
        ', '.join (repr (x )for x in self ),self .total )

class _FileStream (io .IOBase ):
    """"""
    def __init__ (self ,file ,*,file_size =None ):
        if isinstance (file ,Path ):
            file =str (file .absolute ())

        self ._file =file 
        self ._name =None 
        self ._size =file_size 
        self ._stream =None 
        self ._close_stream =None 

    async def __aenter__ (self ):
        if isinstance (self ._file ,str ):
            self ._name =os .path .basename (self ._file )
            self ._size =os .path .getsize (self ._file )
            self ._stream =open (self ._file ,'rb')
            self ._close_stream =True 

        elif isinstance (self ._file ,bytes ):
            self ._size =len (self ._file )
            self ._stream =io .BytesIO (self ._file )
            self ._close_stream =True 

        elif not callable (getattr (self ._file ,'read',None )):
            raise TypeError ('file description should have a `read` method')

        elif self ._size is not None :
            self ._name =getattr (self ._file ,'name',None )
            self ._stream =self ._file 
            self ._close_stream =False 

        else :
            if callable (getattr (self ._file ,'seekable',None )):
                seekable =await _maybe_await (self ._file .seekable ())
            else :
                seekable =False 

            if seekable :
                pos =await _maybe_await (self ._file .tell ())
                await _maybe_await (self ._file .seek (0 ,os .SEEK_END ))
                self ._size =await _maybe_await (self ._file .tell ())
                await _maybe_await (self ._file .seek (pos ,os .SEEK_SET ))
                self ._stream =self ._file 
                self ._close_stream =False 
            else :
                _log .warning (
                'Could not determine file size beforehand so the entire '
                'file will be read in-memory')

                data =await _maybe_await (self ._file .read ())
                self ._size =len (data )
                self ._stream =io .BytesIO (data )
                self ._close_stream =True 

        return self 

    async def __aexit__ (self ,exc_type ,exc_val ,exc_tb ):
        if self ._close_stream and self ._stream :
            await _maybe_await (self ._stream .close ())

    @property 
    def file_size (self ):
        return self ._size 

    @property 
    def name (self ):
        return self ._name 

    def read (self ,*args ,**kwargs ):return self ._stream .read (*args ,**kwargs )
    def readinto (self ,*args ,**kwargs ):return self ._stream .readinto (*args ,**kwargs )
    def write (self ,*args ,**kwargs ):return self ._stream .write (*args ,**kwargs )
    def fileno (self ,*args ,**kwargs ):return self ._stream .fileno (*args ,**kwargs )
    def flush (self ,*args ,**kwargs ):return self ._stream .flush (*args ,**kwargs )
    def isatty (self ,*args ,**kwargs ):return self ._stream .isatty (*args ,**kwargs )
    def readable (self ,*args ,**kwargs ):return self ._stream .readable (*args ,**kwargs )
    def readline (self ,*args ,**kwargs ):return self ._stream .readline (*args ,**kwargs )
    def readlines (self ,*args ,**kwargs ):return self ._stream .readlines (*args ,**kwargs )
    def seek (self ,*args ,**kwargs ):return self ._stream .seek (*args ,**kwargs )
    def seekable (self ,*args ,**kwargs ):return self ._stream .seekable (*args ,**kwargs )
    def tell (self ,*args ,**kwargs ):return self ._stream .tell (*args ,**kwargs )
    def truncate (self ,*args ,**kwargs ):return self ._stream .truncate (*args ,**kwargs )
    def writable (self ,*args ,**kwargs ):return self ._stream .writable (*args ,**kwargs )
    def writelines (self ,*args ,**kwargs ):return self ._stream .writelines (*args ,**kwargs )

    def close (self ,*args ,**kwargs ):
        pass 

def get_running_loop ():
    if sys .version_info >=(3 ,7 ):
        try :
            return asyncio .get_running_loop ()
        except RuntimeError :
            return asyncio .get_event_loop_policy ().get_event_loop ()
    else :
        return asyncio .get_event_loop ()
