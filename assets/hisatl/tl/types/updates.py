""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeChat ,TypeDialog ,TypeEncryptedMessage ,TypeMessage ,TypeUpdate ,TypeUser 
    from ...tl .types .updates import TypeState 

class ChannelDifference (TLObject ):
    CONSTRUCTOR_ID =0x2064674e 
    SUBCLASS_OF_ID =0x29896f5d 

    def __init__ (self ,pts :int ,new_messages :List ['TypeMessage'],other_updates :List ['TypeUpdate'],chats :List ['TypeChat'],users :List ['TypeUser'],final :Optional [bool ]=None ,timeout :Optional [int ]=None ):
        """"""
        self .pts =pts 
        self .new_messages =new_messages 
        self .other_updates =other_updates 
        self .chats =chats 
        self .users =users 
        self .final =final 
        self .timeout =timeout 

    def to_dict (self ):
        return {
        '_':'ChannelDifference',
        'pts':self .pts ,
        'new_messages':[]if self .new_messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .new_messages ],
        'other_updates':[]if self .other_updates is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .other_updates ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'final':self .final ,
        'timeout':self .timeout 
        }

    def _bytes (self ):
        return b''.join ((
        b'Ngd ',
        struct .pack ('<I',(0 if self .final is None or self .final is False else 1 )|(0 if self .timeout is None or self .timeout is False else 2 )),
        struct .pack ('<i',self .pts ),
        b''if self .timeout is None or self .timeout is False else (struct .pack ('<i',self .timeout )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .new_messages )),b''.join (x ._bytes ()for x in self .new_messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .other_updates )),b''.join (x ._bytes ()for x in self .other_updates ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _final =bool (flags &1 )
        _pts =reader .read_int ()
        if flags &2 :
            _timeout =reader .read_int ()
        else :
            _timeout =None 
        reader .read_int ()
        _new_messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _new_messages .append (_x )

        reader .read_int ()
        _other_updates =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _other_updates .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (pts =_pts ,new_messages =_new_messages ,other_updates =_other_updates ,chats =_chats ,users =_users ,final =_final ,timeout =_timeout )

class ChannelDifferenceEmpty (TLObject ):
    CONSTRUCTOR_ID =0x3e11affb 
    SUBCLASS_OF_ID =0x29896f5d 

    def __init__ (self ,pts :int ,final :Optional [bool ]=None ,timeout :Optional [int ]=None ):
        """"""
        self .pts =pts 
        self .final =final 
        self .timeout =timeout 

    def to_dict (self ):
        return {
        '_':'ChannelDifferenceEmpty',
        'pts':self .pts ,
        'final':self .final ,
        'timeout':self .timeout 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfb\xaf\x11>',
        struct .pack ('<I',(0 if self .final is None or self .final is False else 1 )|(0 if self .timeout is None or self .timeout is False else 2 )),
        struct .pack ('<i',self .pts ),
        b''if self .timeout is None or self .timeout is False else (struct .pack ('<i',self .timeout )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _final =bool (flags &1 )
        _pts =reader .read_int ()
        if flags &2 :
            _timeout =reader .read_int ()
        else :
            _timeout =None 
        return cls (pts =_pts ,final =_final ,timeout =_timeout )

class ChannelDifferenceTooLong (TLObject ):
    CONSTRUCTOR_ID =0xa4bcc6fe 
    SUBCLASS_OF_ID =0x29896f5d 

    def __init__ (self ,dialog :'TypeDialog',messages :List ['TypeMessage'],chats :List ['TypeChat'],users :List ['TypeUser'],final :Optional [bool ]=None ,timeout :Optional [int ]=None ):
        """"""
        self .dialog =dialog 
        self .messages =messages 
        self .chats =chats 
        self .users =users 
        self .final =final 
        self .timeout =timeout 

    def to_dict (self ):
        return {
        '_':'ChannelDifferenceTooLong',
        'dialog':self .dialog .to_dict ()if isinstance (self .dialog ,TLObject )else self .dialog ,
        'messages':[]if self .messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .messages ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'final':self .final ,
        'timeout':self .timeout 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xfe\xc6\xbc\xa4',
        struct .pack ('<I',(0 if self .final is None or self .final is False else 1 )|(0 if self .timeout is None or self .timeout is False else 2 )),
        b''if self .timeout is None or self .timeout is False else (struct .pack ('<i',self .timeout )),
        self .dialog ._bytes (),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .messages )),b''.join (x ._bytes ()for x in self .messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _final =bool (flags &1 )
        if flags &2 :
            _timeout =reader .read_int ()
        else :
            _timeout =None 
        _dialog =reader .tgread_object ()
        reader .read_int ()
        _messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _messages .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (dialog =_dialog ,messages =_messages ,chats =_chats ,users =_users ,final =_final ,timeout =_timeout )

class Difference (TLObject ):
    CONSTRUCTOR_ID =0xf49ca0 
    SUBCLASS_OF_ID =0x20482874 

    def __init__ (self ,new_messages :List ['TypeMessage'],new_encrypted_messages :List ['TypeEncryptedMessage'],other_updates :List ['TypeUpdate'],chats :List ['TypeChat'],users :List ['TypeUser'],state :'TypeState'):
        """"""
        self .new_messages =new_messages 
        self .new_encrypted_messages =new_encrypted_messages 
        self .other_updates =other_updates 
        self .chats =chats 
        self .users =users 
        self .state =state 

    def to_dict (self ):
        return {
        '_':'Difference',
        'new_messages':[]if self .new_messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .new_messages ],
        'new_encrypted_messages':[]if self .new_encrypted_messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .new_encrypted_messages ],
        'other_updates':[]if self .other_updates is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .other_updates ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'state':self .state .to_dict ()if isinstance (self .state ,TLObject )else self .state 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0\x9c\xf4\x00',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .new_messages )),b''.join (x ._bytes ()for x in self .new_messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .new_encrypted_messages )),b''.join (x ._bytes ()for x in self .new_encrypted_messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .other_updates )),b''.join (x ._bytes ()for x in self .other_updates ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        self .state ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _new_messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _new_messages .append (_x )

        reader .read_int ()
        _new_encrypted_messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _new_encrypted_messages .append (_x )

        reader .read_int ()
        _other_updates =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _other_updates .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        _state =reader .tgread_object ()
        return cls (new_messages =_new_messages ,new_encrypted_messages =_new_encrypted_messages ,other_updates =_other_updates ,chats =_chats ,users =_users ,state =_state )

class DifferenceEmpty (TLObject ):
    CONSTRUCTOR_ID =0x5d75a138 
    SUBCLASS_OF_ID =0x20482874 

    def __init__ (self ,date :Optional [datetime ],seq :int ):
        """"""
        self .date =date 
        self .seq =seq 

    def to_dict (self ):
        return {
        '_':'DifferenceEmpty',
        'date':self .date ,
        'seq':self .seq 
        }

    def _bytes (self ):
        return b''.join ((
        b'8\xa1u]',
        self .serialize_datetime (self .date ),
        struct .pack ('<i',self .seq ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _date =reader .tgread_date ()
        _seq =reader .read_int ()
        return cls (date =_date ,seq =_seq )

class DifferenceSlice (TLObject ):
    CONSTRUCTOR_ID =0xa8fb1981 
    SUBCLASS_OF_ID =0x20482874 

    def __init__ (self ,new_messages :List ['TypeMessage'],new_encrypted_messages :List ['TypeEncryptedMessage'],other_updates :List ['TypeUpdate'],chats :List ['TypeChat'],users :List ['TypeUser'],intermediate_state :'TypeState'):
        """"""
        self .new_messages =new_messages 
        self .new_encrypted_messages =new_encrypted_messages 
        self .other_updates =other_updates 
        self .chats =chats 
        self .users =users 
        self .intermediate_state =intermediate_state 

    def to_dict (self ):
        return {
        '_':'DifferenceSlice',
        'new_messages':[]if self .new_messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .new_messages ],
        'new_encrypted_messages':[]if self .new_encrypted_messages is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .new_encrypted_messages ],
        'other_updates':[]if self .other_updates is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .other_updates ],
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'intermediate_state':self .intermediate_state .to_dict ()if isinstance (self .intermediate_state ,TLObject )else self .intermediate_state 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x81\x19\xfb\xa8',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .new_messages )),b''.join (x ._bytes ()for x in self .new_messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .new_encrypted_messages )),b''.join (x ._bytes ()for x in self .new_encrypted_messages ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .other_updates )),b''.join (x ._bytes ()for x in self .other_updates ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        self .intermediate_state ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _new_messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _new_messages .append (_x )

        reader .read_int ()
        _new_encrypted_messages =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _new_encrypted_messages .append (_x )

        reader .read_int ()
        _other_updates =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _other_updates .append (_x )

        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        _intermediate_state =reader .tgread_object ()
        return cls (new_messages =_new_messages ,new_encrypted_messages =_new_encrypted_messages ,other_updates =_other_updates ,chats =_chats ,users =_users ,intermediate_state =_intermediate_state )

class DifferenceTooLong (TLObject ):
    CONSTRUCTOR_ID =0x4afe8f6d 
    SUBCLASS_OF_ID =0x20482874 

    def __init__ (self ,pts :int ):
        """"""
        self .pts =pts 

    def to_dict (self ):
        return {
        '_':'DifferenceTooLong',
        'pts':self .pts 
        }

    def _bytes (self ):
        return b''.join ((
        b'm\x8f\xfeJ',
        struct .pack ('<i',self .pts ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pts =reader .read_int ()
        return cls (pts =_pts )

class State (TLObject ):
    CONSTRUCTOR_ID =0xa56c2a3e 
    SUBCLASS_OF_ID =0x23df1a01 

    def __init__ (self ,pts :int ,qts :int ,date :Optional [datetime ],seq :int ,unread_count :int ):
        """"""
        self .pts =pts 
        self .qts =qts 
        self .date =date 
        self .seq =seq 
        self .unread_count =unread_count 

    def to_dict (self ):
        return {
        '_':'State',
        'pts':self .pts ,
        'qts':self .qts ,
        'date':self .date ,
        'seq':self .seq ,
        'unread_count':self .unread_count 
        }

    def _bytes (self ):
        return b''.join ((
        b'>*l\xa5',
        struct .pack ('<i',self .pts ),
        struct .pack ('<i',self .qts ),
        self .serialize_datetime (self .date ),
        struct .pack ('<i',self .seq ),
        struct .pack ('<i',self .unread_count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _pts =reader .read_int ()
        _qts =reader .read_int ()
        _date =reader .tgread_date ()
        _seq =reader .read_int ()
        _unread_count =reader .read_int ()
        return cls (pts =_pts ,qts =_qts ,date =_date ,seq =_seq ,unread_count =_unread_count )

