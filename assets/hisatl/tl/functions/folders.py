""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputFolderPeer 

class EditPeerFoldersRequest (TLRequest ):
    CONSTRUCTOR_ID =0x6847d0ab 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,folder_peers :List ['TypeInputFolderPeer']):
        """"""
        self .folder_peers =folder_peers 

    def to_dict (self ):
        return {
        '_':'EditPeerFoldersRequest',
        'folder_peers':[]if self .folder_peers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .folder_peers ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\xab\xd0Gh',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .folder_peers )),b''.join (x ._bytes ()for x in self .folder_peers ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _folder_peers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _folder_peers .append (_x )

        return cls (folder_peers =_folder_peers )

