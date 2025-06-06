""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputFile ,TypeInputPhoto ,TypeInputUser ,TypeVideoSize 

class DeletePhotosRequest (TLRequest ):
    CONSTRUCTOR_ID =0x87cf7f2f 
    SUBCLASS_OF_ID =0x8918e168 

    def __init__ (self ,id :List ['TypeInputPhoto']):
        """"""
        self .id =id 

    async def resolve (self ,client ,utils ):
        _tmp =[]
        for _x in self .id :
            _tmp .append (utils .get_input_photo (_x ))

        self .id =_tmp 

    def to_dict (self ):
        return {
        '_':'DeletePhotosRequest',
        'id':[]if self .id is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .id ]
        }

    def _bytes (self ):
        return b''.join ((
        b'/\x7f\xcf\x87',
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .id )),b''.join (x ._bytes ()for x in self .id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        reader .read_int ()
        _id =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _id .append (_x )

        return cls (id =_id )

    @staticmethod 
    def read_result (reader ):
        reader .read_int ()
        return [reader .read_long ()for _ in range (reader .read_int ())]

class GetUserPhotosRequest (TLRequest ):
    CONSTRUCTOR_ID =0x91cd32a8 
    SUBCLASS_OF_ID =0x27cfb967 

    def __init__ (self ,user_id :'TypeInputUser',offset :int ,max_id :int ,limit :int ):
        """"""
        self .user_id =user_id 
        self .offset =offset 
        self .max_id =max_id 
        self .limit =limit 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'GetUserPhotosRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'offset':self .offset ,
        'max_id':self .max_id ,
        'limit':self .limit 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa82\xcd\x91',
        self .user_id ._bytes (),
        struct .pack ('<i',self .offset ),
        struct .pack ('<q',self .max_id ),
        struct .pack ('<i',self .limit ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _user_id =reader .tgread_object ()
        _offset =reader .read_int ()
        _max_id =reader .read_long ()
        _limit =reader .read_int ()
        return cls (user_id =_user_id ,offset =_offset ,max_id =_max_id ,limit =_limit )

class UpdateProfilePhotoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9e82039 
    SUBCLASS_OF_ID =0xc292bd24 

    def __init__ (self ,id :'TypeInputPhoto',fallback :Optional [bool ]=None ,bot :Optional ['TypeInputUser']=None ):
        """"""
        self .id =id 
        self .fallback =fallback 
        self .bot =bot 

    async def resolve (self ,client ,utils ):
        self .id =utils .get_input_photo (self .id )
        if self .bot :
            self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'UpdateProfilePhotoRequest',
        'id':self .id .to_dict ()if isinstance (self .id ,TLObject )else self .id ,
        'fallback':self .fallback ,
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot 
        }

    def _bytes (self ):
        return b''.join ((
        b'9 \xe8\t',
        struct .pack ('<I',(0 if self .fallback is None or self .fallback is False else 1 )|(0 if self .bot is None or self .bot is False else 2 )),
        b''if self .bot is None or self .bot is False else (self .bot ._bytes ()),
        self .id ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _fallback =bool (flags &1 )
        if flags &2 :
            _bot =reader .tgread_object ()
        else :
            _bot =None 
        _id =reader .tgread_object ()
        return cls (id =_id ,fallback =_fallback ,bot =_bot )

class UploadContactProfilePhotoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xe14c4a71 
    SUBCLASS_OF_ID =0xc292bd24 

    def __init__ (self ,user_id :'TypeInputUser',suggest :Optional [bool ]=None ,save :Optional [bool ]=None ,file :Optional ['TypeInputFile']=None ,video :Optional ['TypeInputFile']=None ,video_start_ts :Optional [float ]=None ,video_emoji_markup :Optional ['TypeVideoSize']=None ):
        """"""
        self .user_id =user_id 
        self .suggest =suggest 
        self .save =save 
        self .file =file 
        self .video =video 
        self .video_start_ts =video_start_ts 
        self .video_emoji_markup =video_emoji_markup 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))

    def to_dict (self ):
        return {
        '_':'UploadContactProfilePhotoRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'suggest':self .suggest ,
        'save':self .save ,
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file ,
        'video':self .video .to_dict ()if isinstance (self .video ,TLObject )else self .video ,
        'video_start_ts':self .video_start_ts ,
        'video_emoji_markup':self .video_emoji_markup .to_dict ()if isinstance (self .video_emoji_markup ,TLObject )else self .video_emoji_markup 
        }

    def _bytes (self ):
        return b''.join ((
        b'qJL\xe1',
        struct .pack ('<I',(0 if self .suggest is None or self .suggest is False else 8 )|(0 if self .save is None or self .save is False else 16 )|(0 if self .file is None or self .file is False else 1 )|(0 if self .video is None or self .video is False else 2 )|(0 if self .video_start_ts is None or self .video_start_ts is False else 4 )|(0 if self .video_emoji_markup is None or self .video_emoji_markup is False else 32 )),
        self .user_id ._bytes (),
        b''if self .file is None or self .file is False else (self .file ._bytes ()),
        b''if self .video is None or self .video is False else (self .video ._bytes ()),
        b''if self .video_start_ts is None or self .video_start_ts is False else (struct .pack ('<d',self .video_start_ts )),
        b''if self .video_emoji_markup is None or self .video_emoji_markup is False else (self .video_emoji_markup ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _suggest =bool (flags &8 )
        _save =bool (flags &16 )
        _user_id =reader .tgread_object ()
        if flags &1 :
            _file =reader .tgread_object ()
        else :
            _file =None 
        if flags &2 :
            _video =reader .tgread_object ()
        else :
            _video =None 
        if flags &4 :
            _video_start_ts =reader .read_double ()
        else :
            _video_start_ts =None 
        if flags &32 :
            _video_emoji_markup =reader .tgread_object ()
        else :
            _video_emoji_markup =None 
        return cls (user_id =_user_id ,suggest =_suggest ,save =_save ,file =_file ,video =_video ,video_start_ts =_video_start_ts ,video_emoji_markup =_video_emoji_markup )

class UploadProfilePhotoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x388a3b5 
    SUBCLASS_OF_ID =0xc292bd24 

    def __init__ (self ,fallback :Optional [bool ]=None ,bot :Optional ['TypeInputUser']=None ,file :Optional ['TypeInputFile']=None ,video :Optional ['TypeInputFile']=None ,video_start_ts :Optional [float ]=None ,video_emoji_markup :Optional ['TypeVideoSize']=None ):
        """"""
        self .fallback =fallback 
        self .bot =bot 
        self .file =file 
        self .video =video 
        self .video_start_ts =video_start_ts 
        self .video_emoji_markup =video_emoji_markup 

    async def resolve (self ,client ,utils ):
        if self .bot :
            self .bot =utils .get_input_user (await client .get_input_entity (self .bot ))

    def to_dict (self ):
        return {
        '_':'UploadProfilePhotoRequest',
        'fallback':self .fallback ,
        'bot':self .bot .to_dict ()if isinstance (self .bot ,TLObject )else self .bot ,
        'file':self .file .to_dict ()if isinstance (self .file ,TLObject )else self .file ,
        'video':self .video .to_dict ()if isinstance (self .video ,TLObject )else self .video ,
        'video_start_ts':self .video_start_ts ,
        'video_emoji_markup':self .video_emoji_markup .to_dict ()if isinstance (self .video_emoji_markup ,TLObject )else self .video_emoji_markup 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb5\xa3\x88\x03',
        struct .pack ('<I',(0 if self .fallback is None or self .fallback is False else 8 )|(0 if self .bot is None or self .bot is False else 32 )|(0 if self .file is None or self .file is False else 1 )|(0 if self .video is None or self .video is False else 2 )|(0 if self .video_start_ts is None or self .video_start_ts is False else 4 )|(0 if self .video_emoji_markup is None or self .video_emoji_markup is False else 16 )),
        b''if self .bot is None or self .bot is False else (self .bot ._bytes ()),
        b''if self .file is None or self .file is False else (self .file ._bytes ()),
        b''if self .video is None or self .video is False else (self .video ._bytes ()),
        b''if self .video_start_ts is None or self .video_start_ts is False else (struct .pack ('<d',self .video_start_ts )),
        b''if self .video_emoji_markup is None or self .video_emoji_markup is False else (self .video_emoji_markup ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _fallback =bool (flags &8 )
        if flags &32 :
            _bot =reader .tgread_object ()
        else :
            _bot =None 
        if flags &1 :
            _file =reader .tgread_object ()
        else :
            _file =None 
        if flags &2 :
            _video =reader .tgread_object ()
        else :
            _video =None 
        if flags &4 :
            _video_start_ts =reader .read_double ()
        else :
            _video_start_ts =None 
        if flags &16 :
            _video_emoji_markup =reader .tgread_object ()
        else :
            _video_emoji_markup =None 
        return cls (fallback =_fallback ,bot =_bot ,file =_file ,video =_video ,video_start_ts =_video_start_ts ,video_emoji_markup =_video_emoji_markup )

