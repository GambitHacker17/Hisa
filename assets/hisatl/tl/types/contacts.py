from ...tl.tlobject import TLObject
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeChat, TypeContact, TypeImportedContact, TypePeer, TypePeerBlocked, TypePopularContact, TypeTopPeerCategoryPeers, TypeUser
class Blocked(TLObject):
    CONSTRUCTOR_ID = 0xade1591
    SUBCLASS_OF_ID = 0xffba4f4f
    def __init__(self, blocked: List['TypePeerBlocked'], chats: List['TypeChat'], users: List['TypeUser']):
        self.blocked = blocked
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {
            '_': 'Blocked',
            'blocked': [] if self.blocked is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.blocked],
            'chats': [] if self.chats is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.chats],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'\x91\x15\xde\n',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.blocked)),b''.join(x._bytes() for x in self.blocked),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _blocked = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _blocked.append(_x)
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(blocked=_blocked, chats=_chats, users=_users)
class BlockedSlice(TLObject):
    CONSTRUCTOR_ID = 0xe1664194
    SUBCLASS_OF_ID = 0xffba4f4f
    def __init__(self, count: int, blocked: List['TypePeerBlocked'], chats: List['TypeChat'], users: List['TypeUser']):
        self.count = count
        self.blocked = blocked
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {
            '_': 'BlockedSlice',
            'count': self.count,
            'blocked': [] if self.blocked is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.blocked],
            'chats': [] if self.chats is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.chats],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'\x94Af\xe1',
            struct.pack('<i', self.count),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.blocked)),b''.join(x._bytes() for x in self.blocked),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        _count = reader.read_int()
        reader.read_int()
        _blocked = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _blocked.append(_x)
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(count=_count, blocked=_blocked, chats=_chats, users=_users)
class Contacts(TLObject):
    CONSTRUCTOR_ID = 0xeae87e42
    SUBCLASS_OF_ID = 0x38be25f6
    def __init__(self, contacts: List['TypeContact'], saved_count: int, users: List['TypeUser']):
        self.contacts = contacts
        self.saved_count = saved_count
        self.users = users
    def to_dict(self):
        return {
            '_': 'Contacts',
            'contacts': [] if self.contacts is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.contacts],
            'saved_count': self.saved_count,
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'B~\xe8\xea',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.contacts)),b''.join(x._bytes() for x in self.contacts),
            struct.pack('<i', self.saved_count),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _contacts = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _contacts.append(_x)
        _saved_count = reader.read_int()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(contacts=_contacts, saved_count=_saved_count, users=_users)
class ContactsNotModified(TLObject):
    CONSTRUCTOR_ID = 0xb74ba9d2
    SUBCLASS_OF_ID = 0x38be25f6
    def to_dict(self):
        return {
            '_': 'ContactsNotModified'
        }
    def _bytes(self):
        return b''.join((
            b'\xd2\xa9K\xb7',
        ))
    @classmethod
    def from_reader(cls, reader):
        return cls()
class Found(TLObject):
    CONSTRUCTOR_ID = 0xb3134d9d
    SUBCLASS_OF_ID = 0x4386a2e3
    def __init__(self, my_results: List['TypePeer'], results: List['TypePeer'], chats: List['TypeChat'], users: List['TypeUser']):
        self.my_results = my_results
        self.results = results
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {
            '_': 'Found',
            'my_results': [] if self.my_results is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.my_results],
            'results': [] if self.results is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.results],
            'chats': [] if self.chats is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.chats],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'\x9dM\x13\xb3',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.my_results)),b''.join(x._bytes() for x in self.my_results),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.results)),b''.join(x._bytes() for x in self.results),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _my_results = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _my_results.append(_x)
        reader.read_int()
        _results = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _results.append(_x)
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(my_results=_my_results, results=_results, chats=_chats, users=_users)
class ImportedContacts(TLObject):
    CONSTRUCTOR_ID = 0x77d01c3b
    SUBCLASS_OF_ID = 0x8172ad93
    def __init__(self, imported: List['TypeImportedContact'], popular_invites: List['TypePopularContact'], retry_contacts: List[int], users: List['TypeUser']):
        self.imported = imported
        self.popular_invites = popular_invites
        self.retry_contacts = retry_contacts
        self.users = users
    def to_dict(self):
        return {
            '_': 'ImportedContacts',
            'imported': [] if self.imported is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.imported],
            'popular_invites': [] if self.popular_invites is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.popular_invites],
            'retry_contacts': [] if self.retry_contacts is None else self.retry_contacts[:],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b';\x1c\xd0w',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.imported)),b''.join(x._bytes() for x in self.imported),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.popular_invites)),b''.join(x._bytes() for x in self.popular_invites),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.retry_contacts)),b''.join(struct.pack('<q', x) for x in self.retry_contacts),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _imported = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _imported.append(_x)
        reader.read_int()
        _popular_invites = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _popular_invites.append(_x)
        reader.read_int()
        _retry_contacts = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _retry_contacts.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(imported=_imported, popular_invites=_popular_invites, retry_contacts=_retry_contacts, users=_users)
class ResolvedPeer(TLObject):
    CONSTRUCTOR_ID = 0x7f077ad9
    SUBCLASS_OF_ID = 0xf065b3a8
    def __init__(self, peer: 'TypePeer', chats: List['TypeChat'], users: List['TypeUser']):
        self.peer = peer
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {
            '_': 'ResolvedPeer',
            'peer': self.peer.to_dict() if isinstance(self.peer, TLObject) else self.peer,
            'chats': [] if self.chats is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.chats],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'\xd9z\x07\x7f',
            self.peer._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        _peer = reader.tgread_object()
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(peer=_peer, chats=_chats, users=_users)
class TopPeers(TLObject):
    CONSTRUCTOR_ID = 0x70b772a8
    SUBCLASS_OF_ID = 0x9ee8bb88
    def __init__(self, categories: List['TypeTopPeerCategoryPeers'], chats: List['TypeChat'], users: List['TypeUser']):
        self.categories = categories
        self.chats = chats
        self.users = users
    def to_dict(self):
        return {
            '_': 'TopPeers',
            'categories': [] if self.categories is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.categories],
            'chats': [] if self.chats is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.chats],
            'users': [] if self.users is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.users]
        }
    def _bytes(self):
        return b''.join((
            b'\xa8r\xb7p',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.categories)),b''.join(x._bytes() for x in self.categories),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.chats)),b''.join(x._bytes() for x in self.chats),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(x._bytes() for x in self.users),
        ))
    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _categories = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _categories.append(_x)
        reader.read_int()
        _chats = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _chats.append(_x)
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)
        return cls(categories=_categories, chats=_chats, users=_users)
class TopPeersDisabled(TLObject):
    CONSTRUCTOR_ID = 0xb52c939d
    SUBCLASS_OF_ID = 0x9ee8bb88
    def to_dict(self):
        return {
            '_': 'TopPeersDisabled'
        }
    def _bytes(self):
        return b''.join((
            b'\x9d\x93,\xb5',
        ))
    @classmethod
    def from_reader(cls, reader):
        return cls()
class TopPeersNotModified(TLObject):
    CONSTRUCTOR_ID = 0xde266ef5
    SUBCLASS_OF_ID = 0x9ee8bb88
    def to_dict(self):
        return {
            '_': 'TopPeersNotModified'
        }
    def _bytes(self):
        return b''.join((
            b'\xf5n&\xde',
        ))
    @classmethod
    def from_reader(cls, reader):
        return cls()