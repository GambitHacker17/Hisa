
import inspect 
import sqlite3 
import time 
from typing import List ,Tuple ,Any 

from hisapyro import raw 
from .storage import Storage 
from ..import utils 

SCHEMA =""""""

def get_input_peer (peer_id :int ,access_hash :int ,peer_type :str ):
    if peer_type in ["user","bot"]:
        return raw .types .InputPeerUser (
        user_id =peer_id ,
        access_hash =access_hash 
        )

    if peer_type =="group":
        return raw .types .InputPeerChat (
        chat_id =-peer_id 
        )

    if peer_type in ["channel","supergroup"]:
        return raw .types .InputPeerChannel (
        channel_id =utils .get_channel_id (peer_id ),
        access_hash =access_hash 
        )

    raise ValueError (f"Invalid peer type: {peer_type }")

class SQLiteStorage (Storage ):
    VERSION =3 
    USERNAME_TTL =8 *60 *60 

    def __init__ (self ,name :str ):
        super ().__init__ (name )

        self .conn =None 

    def create (self ):
        with self .conn :
            self .conn .executescript (SCHEMA )

            self .conn .execute (
            "INSERT INTO version VALUES (?)",
            (self .VERSION ,)
            )

            self .conn .execute (
            "INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?, ?)",
            (2 ,None ,None ,None ,0 ,None ,None )
            )

    async def open (self ):
        raise NotImplementedError 

    async def save (self ):
        await self .date (int (time .time ()))
        self .conn .commit ()

    async def close (self ):
        self .conn .close ()

    async def delete (self ):
        raise NotImplementedError 

    async def update_peers (self ,peers :List [Tuple [int ,int ,str ,str ,str ]]):
        self .conn .executemany (
        "REPLACE INTO peers (id, access_hash, type, username, phone_number)"
        "VALUES (?, ?, ?, ?, ?)",
        peers 
        )

    async def get_peer_by_id (self ,peer_id :int ):
        r =self .conn .execute (
        "SELECT id, access_hash, type FROM peers WHERE id = ?",
        (peer_id ,)
        ).fetchone ()

        if r is None :
            raise KeyError (f"ID not found: {peer_id }")

        return get_input_peer (*r )

    async def get_peer_by_username (self ,username :str ):
        r =self .conn .execute (
        "SELECT id, access_hash, type, last_update_on FROM peers WHERE username = ?"
        "ORDER BY last_update_on DESC",
        (username ,)
        ).fetchone ()

        if r is None :
            raise KeyError (f"Username not found: {username }")

        if abs (time .time ()-r [3 ])>self .USERNAME_TTL :
            raise KeyError (f"Username expired: {username }")

        return get_input_peer (*r [:3 ])

    async def get_peer_by_phone_number (self ,phone_number :str ):
        r =self .conn .execute (
        "SELECT id, access_hash, type FROM peers WHERE phone_number = ?",
        (phone_number ,)
        ).fetchone ()

        if r is None :
            raise KeyError (f"Phone number not found: {phone_number }")

        return get_input_peer (*r )

    def _get (self ):
        attr =inspect .stack ()[2 ].function 

        return self .conn .execute (
        f"SELECT {attr } FROM sessions"
        ).fetchone ()[0 ]

    def _set (self ,value :Any ):
        attr =inspect .stack ()[2 ].function 

        with self .conn :
            self .conn .execute (
            f"UPDATE sessions SET {attr } = ?",
            (value ,)
            )

    def _accessor (self ,value :Any =object ):
        return self ._get ()if value ==object else self ._set (value )

    async def dc_id (self ,value :int =object ):
        return self ._accessor (value )

    async def api_id (self ,value :int =object ):
        return self ._accessor (value )

    async def test_mode (self ,value :bool =object ):
        return self ._accessor (value )

    async def auth_key (self ,value :bytes =object ):
        return self ._accessor (value )

    async def date (self ,value :int =object ):
        return self ._accessor (value )

    async def user_id (self ,value :int =object ):
        return self ._accessor (value )

    async def is_bot (self ,value :bool =object ):
        return self ._accessor (value )

    def version (self ,value :int =object ):
        if value ==object :
            return self .conn .execute (
            "SELECT number FROM version"
            ).fetchone ()[0 ]
        else :
            with self .conn :
                self .conn .execute (
                "UPDATE version SET number = ?",
                (value ,)
                )
