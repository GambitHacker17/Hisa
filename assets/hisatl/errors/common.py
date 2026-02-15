""""""
import struct 
import textwrap 

from ..tl import TLRequest 

class ReadCancelledError (Exception ):
    """"""
    def __init__ (self ):
        super ().__init__ ('The read operation was cancelled.')

class TypeNotFoundError (Exception ):
    """"""
    def __init__ (self ,invalid_constructor_id ,remaining ):
        super ().__init__ (
        'Could not find a matching Constructor ID for the TLObject '
        'that was supposed to be read with ID {:08x}. Most likely, '
        'a TLObject was trying to be read when it should not be read. '
        'Remaining bytes: {!r}'.format (invalid_constructor_id ,remaining ))

        self .invalid_constructor_id =invalid_constructor_id 
        self .remaining =remaining 

class InvalidChecksumError (Exception ):
    """"""
    def __init__ (self ,checksum ,valid_checksum ):
        super ().__init__ (
        'Invalid checksum ({} when {} was expected). '
        'This packet should be skipped.'
        .format (checksum ,valid_checksum ))

        self .checksum =checksum 
        self .valid_checksum =valid_checksum 

class InvalidBufferError (BufferError ):
    """"""
    def __init__ (self ,payload ):
        self .payload =payload 
        if len (payload )==4 :
            self .code =-struct .unpack ('<i',payload )[0 ]
            super ().__init__ (
            'Invalid response buffer (HTTP code {})'.format (self .code ))
        else :
            self .code =None 
            super ().__init__ (
            'Invalid response buffer (too short {})'.format (self .payload ))

class AuthKeyNotFound (Exception ):
    """"""
    def __init__ (self ):
        super ().__init__ (textwrap .dedent (self .__class__ .__doc__ ))

class SecurityError (Exception ):
    """"""
    def __init__ (self ,*args ):
        if not args :
            args =['A security check failed.']
        super ().__init__ (*args )

class CdnFileTamperedError (SecurityError ):
    """"""
    def __init__ (self ):
        super ().__init__ (
        'The CDN file has been altered and its download cancelled.'
        )

class AlreadyInConversationError (Exception ):
    """"""
    def __init__ (self ):
        super ().__init__ (
        'Cannot open exclusive conversation in a '
        'chat that already has one open conversation'
        )

class BadMessageError (Exception ):
    """"""
    ErrorMessages ={
    16 :
    'msg_id too low (most likely, client time is wrong it would be '
    'worthwhile to synchronize it using msg_id notifications and re-send '
    'the original message with the "correct" msg_id or wrap it in a '
    'container with a new msg_id if the original message had waited too '
    'long on the client to be transmitted).',
    17 :
    'msg_id too high (similar to the previous case, the client time has '
    'to be synchronized, and the message re-sent with the correct msg_id).',
    18 :
    'Incorrect two lower order msg_id bits (the server expects client '
    'message msg_id to be divisible by 4).',
    19 :
    'Container msg_id is the same as msg_id of a previously received '
    'message (this must never happen).',
    20 :
    'Message too old, and it cannot be verified whether the server has '
    'received a message with this msg_id or not.',
    32 :
    'msg_seqno too low (the server has already received a message with a '
    'lower msg_id but with either a higher or an equal and odd seqno).',
    33 :
    'msg_seqno too high (similarly, there is a message with a higher '
    'msg_id but with either a lower or an equal and odd seqno).',
    34 :
    'An even msg_seqno expected (irrelevant message), but odd received.',
    35 :
    'Odd msg_seqno expected (relevant message), but even received.',
    48 :
    'Incorrect server salt (in this case, the bad_server_salt response '
    'is received with the correct salt, and the message is to be re-sent '
    'with it).',
    64 :
    'Invalid container.'
    }

    def __init__ (self ,request ,code ):
        super ().__init__ (request ,self .ErrorMessages .get (
        code ,
        'Unknown error code (this should not happen): {}.'.format (code )))

        self .code =code 

class MultiError (Exception ):
    """"""

    def __new__ (cls ,exceptions ,result ,requests ):
        if len (result )!=len (exceptions )!=len (requests ):
            raise ValueError (
            'Need result, exception and request for each error')
        for e ,req in zip (exceptions ,requests ):
            if not isinstance (e ,BaseException )and e is not None :
                raise TypeError (
                "Expected an exception object, not '%r'"%e 
                )
            if not isinstance (req ,TLRequest ):
                raise TypeError (
                "Expected TLRequest object, not '%r'"%req 
                )

        if len (exceptions )==1 :
            return exceptions [0 ]
        self =BaseException .__new__ (cls )
        self .exceptions =list (exceptions )
        self .results =list (result )
        self .requests =list (requests )
        return self 
