""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeInputDocument ,TypeInputStickerSet ,TypeInputStickerSetItem ,TypeInputUser ,TypeMaskCoords 

class AddStickerToSetRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8653febe 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,stickerset :'TypeInputStickerSet',sticker :'TypeInputStickerSetItem'):
        """"""
        self .stickerset =stickerset 
        self .sticker =sticker 

    def to_dict (self ):
        return {
        '_':'AddStickerToSetRequest',
        'stickerset':self .stickerset .to_dict ()if isinstance (self .stickerset ,TLObject )else self .stickerset ,
        'sticker':self .sticker .to_dict ()if isinstance (self .sticker ,TLObject )else self .sticker 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbe\xfeS\x86',
        self .stickerset ._bytes (),
        self .sticker ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _stickerset =reader .tgread_object ()
        _sticker =reader .tgread_object ()
        return cls (stickerset =_stickerset ,sticker =_sticker )

class ChangeStickerRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf5537ebc 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,sticker :'TypeInputDocument',emoji :Optional [str ]=None ,mask_coords :Optional ['TypeMaskCoords']=None ,keywords :Optional [str ]=None ):
        """"""
        self .sticker =sticker 
        self .emoji =emoji 
        self .mask_coords =mask_coords 
        self .keywords =keywords 

    async def resolve (self ,client ,utils ):
        self .sticker =utils .get_input_document (self .sticker )

    def to_dict (self ):
        return {
        '_':'ChangeStickerRequest',
        'sticker':self .sticker .to_dict ()if isinstance (self .sticker ,TLObject )else self .sticker ,
        'emoji':self .emoji ,
        'mask_coords':self .mask_coords .to_dict ()if isinstance (self .mask_coords ,TLObject )else self .mask_coords ,
        'keywords':self .keywords 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbc~S\xf5',
        struct .pack ('<I',(0 if self .emoji is None or self .emoji is False else 1 )|(0 if self .mask_coords is None or self .mask_coords is False else 2 )|(0 if self .keywords is None or self .keywords is False else 4 )),
        self .sticker ._bytes (),
        b''if self .emoji is None or self .emoji is False else (self .serialize_bytes (self .emoji )),
        b''if self .mask_coords is None or self .mask_coords is False else (self .mask_coords ._bytes ()),
        b''if self .keywords is None or self .keywords is False else (self .serialize_bytes (self .keywords )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _sticker =reader .tgread_object ()
        if flags &1 :
            _emoji =reader .tgread_string ()
        else :
            _emoji =None 
        if flags &2 :
            _mask_coords =reader .tgread_object ()
        else :
            _mask_coords =None 
        if flags &4 :
            _keywords =reader .tgread_string ()
        else :
            _keywords =None 
        return cls (sticker =_sticker ,emoji =_emoji ,mask_coords =_mask_coords ,keywords =_keywords )

class ChangeStickerPositionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xffb6d4ca 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,sticker :'TypeInputDocument',position :int ):
        """"""
        self .sticker =sticker 
        self .position =position 

    async def resolve (self ,client ,utils ):
        self .sticker =utils .get_input_document (self .sticker )

    def to_dict (self ):
        return {
        '_':'ChangeStickerPositionRequest',
        'sticker':self .sticker .to_dict ()if isinstance (self .sticker ,TLObject )else self .sticker ,
        'position':self .position 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xca\xd4\xb6\xff',
        self .sticker ._bytes (),
        struct .pack ('<i',self .position ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _sticker =reader .tgread_object ()
        _position =reader .read_int ()
        return cls (sticker =_sticker ,position =_position )

class CheckShortNameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x284b3639 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,short_name :str ):
        """"""
        self .short_name =short_name 

    def to_dict (self ):
        return {
        '_':'CheckShortNameRequest',
        'short_name':self .short_name 
        }

    def _bytes (self ):
        return b''.join ((
        b'96K(',
        self .serialize_bytes (self .short_name ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _short_name =reader .tgread_string ()
        return cls (short_name =_short_name )

class CreateStickerSetRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9021ab67 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,user_id :'TypeInputUser',title :str ,short_name :str ,stickers :List ['TypeInputStickerSetItem'],masks :Optional [bool ]=None ,animated :Optional [bool ]=None ,videos :Optional [bool ]=None ,emojis :Optional [bool ]=None ,text_color :Optional [bool ]=None ,thumb :Optional ['TypeInputDocument']=None ,software :Optional [str ]=None ):
        """"""
        self .user_id =user_id 
        self .title =title 
        self .short_name =short_name 
        self .stickers =stickers 
        self .masks =masks 
        self .animated =animated 
        self .videos =videos 
        self .emojis =emojis 
        self .text_color =text_color 
        self .thumb =thumb 
        self .software =software 

    async def resolve (self ,client ,utils ):
        self .user_id =utils .get_input_user (await client .get_input_entity (self .user_id ))
        if self .thumb :
            self .thumb =utils .get_input_document (self .thumb )

    def to_dict (self ):
        return {
        '_':'CreateStickerSetRequest',
        'user_id':self .user_id .to_dict ()if isinstance (self .user_id ,TLObject )else self .user_id ,
        'title':self .title ,
        'short_name':self .short_name ,
        'stickers':[]if self .stickers is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .stickers ],
        'masks':self .masks ,
        'animated':self .animated ,
        'videos':self .videos ,
        'emojis':self .emojis ,
        'text_color':self .text_color ,
        'thumb':self .thumb .to_dict ()if isinstance (self .thumb ,TLObject )else self .thumb ,
        'software':self .software 
        }

    def _bytes (self ):
        return b''.join ((
        b'g\xab!\x90',
        struct .pack ('<I',(0 if self .masks is None or self .masks is False else 1 )|(0 if self .animated is None or self .animated is False else 2 )|(0 if self .videos is None or self .videos is False else 16 )|(0 if self .emojis is None or self .emojis is False else 32 )|(0 if self .text_color is None or self .text_color is False else 64 )|(0 if self .thumb is None or self .thumb is False else 4 )|(0 if self .software is None or self .software is False else 8 )),
        self .user_id ._bytes (),
        self .serialize_bytes (self .title ),
        self .serialize_bytes (self .short_name ),
        b''if self .thumb is None or self .thumb is False else (self .thumb ._bytes ()),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .stickers )),b''.join (x ._bytes ()for x in self .stickers ),
        b''if self .software is None or self .software is False else (self .serialize_bytes (self .software )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _masks =bool (flags &1 )
        _animated =bool (flags &2 )
        _videos =bool (flags &16 )
        _emojis =bool (flags &32 )
        _text_color =bool (flags &64 )
        _user_id =reader .tgread_object ()
        _title =reader .tgread_string ()
        _short_name =reader .tgread_string ()
        if flags &4 :
            _thumb =reader .tgread_object ()
        else :
            _thumb =None 
        reader .read_int ()
        _stickers =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _stickers .append (_x )

        if flags &8 :
            _software =reader .tgread_string ()
        else :
            _software =None 
        return cls (user_id =_user_id ,title =_title ,short_name =_short_name ,stickers =_stickers ,masks =_masks ,animated =_animated ,videos =_videos ,emojis =_emojis ,text_color =_text_color ,thumb =_thumb ,software =_software )

class DeleteStickerSetRequest (TLRequest ):
    CONSTRUCTOR_ID =0x87704394 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,stickerset :'TypeInputStickerSet'):
        """"""
        self .stickerset =stickerset 

    def to_dict (self ):
        return {
        '_':'DeleteStickerSetRequest',
        'stickerset':self .stickerset .to_dict ()if isinstance (self .stickerset ,TLObject )else self .stickerset 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x94Cp\x87',
        self .stickerset ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _stickerset =reader .tgread_object ()
        return cls (stickerset =_stickerset )

class RemoveStickerFromSetRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf7760f51 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,sticker :'TypeInputDocument'):
        """"""
        self .sticker =sticker 

    async def resolve (self ,client ,utils ):
        self .sticker =utils .get_input_document (self .sticker )

    def to_dict (self ):
        return {
        '_':'RemoveStickerFromSetRequest',
        'sticker':self .sticker .to_dict ()if isinstance (self .sticker ,TLObject )else self .sticker 
        }

    def _bytes (self ):
        return b''.join ((
        b'Q\x0fv\xf7',
        self .sticker ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _sticker =reader .tgread_object ()
        return cls (sticker =_sticker )

class RenameStickerSetRequest (TLRequest ):
    CONSTRUCTOR_ID =0x124b1c00 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,stickerset :'TypeInputStickerSet',title :str ):
        """"""
        self .stickerset =stickerset 
        self .title =title 

    def to_dict (self ):
        return {
        '_':'RenameStickerSetRequest',
        'stickerset':self .stickerset .to_dict ()if isinstance (self .stickerset ,TLObject )else self .stickerset ,
        'title':self .title 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x00\x1cK\x12',
        self .stickerset ._bytes (),
        self .serialize_bytes (self .title ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _stickerset =reader .tgread_object ()
        _title =reader .tgread_string ()
        return cls (stickerset =_stickerset ,title =_title )

class SetStickerSetThumbRequest (TLRequest ):
    CONSTRUCTOR_ID =0xa76a5392 
    SUBCLASS_OF_ID =0x9b704a5a 

    def __init__ (self ,stickerset :'TypeInputStickerSet',thumb :Optional ['TypeInputDocument']=None ,thumb_document_id :Optional [int ]=None ):
        """"""
        self .stickerset =stickerset 
        self .thumb =thumb 
        self .thumb_document_id =thumb_document_id 

    async def resolve (self ,client ,utils ):
        if self .thumb :
            self .thumb =utils .get_input_document (self .thumb )

    def to_dict (self ):
        return {
        '_':'SetStickerSetThumbRequest',
        'stickerset':self .stickerset .to_dict ()if isinstance (self .stickerset ,TLObject )else self .stickerset ,
        'thumb':self .thumb .to_dict ()if isinstance (self .thumb ,TLObject )else self .thumb ,
        'thumb_document_id':self .thumb_document_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x92Sj\xa7',
        struct .pack ('<I',(0 if self .thumb is None or self .thumb is False else 1 )|(0 if self .thumb_document_id is None or self .thumb_document_id is False else 2 )),
        self .stickerset ._bytes (),
        b''if self .thumb is None or self .thumb is False else (self .thumb ._bytes ()),
        b''if self .thumb_document_id is None or self .thumb_document_id is False else (struct .pack ('<q',self .thumb_document_id )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _stickerset =reader .tgread_object ()
        if flags &1 :
            _thumb =reader .tgread_object ()
        else :
            _thumb =None 
        if flags &2 :
            _thumb_document_id =reader .read_long ()
        else :
            _thumb_document_id =None 
        return cls (stickerset =_stickerset ,thumb =_thumb ,thumb_document_id =_thumb_document_id )

class SuggestShortNameRequest (TLRequest ):
    CONSTRUCTOR_ID =0x4dafc503 
    SUBCLASS_OF_ID =0xc44a4b21 

    def __init__ (self ,title :str ):
        """"""
        self .title =title 

    def to_dict (self ):
        return {
        '_':'SuggestShortNameRequest',
        'title':self .title 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x03\xc5\xafM',
        self .serialize_bytes (self .title ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _title =reader .tgread_string ()
        return cls (title =_title )

