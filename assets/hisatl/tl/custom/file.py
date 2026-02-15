import mimetypes 
import os 

from ...import utils 
from ...tl import types 

class File :
    """"""
    def __init__ (self ,media ):
        self .media =media 

    @property 
    def id (self ):
        """"""
        return utils .pack_bot_file_id (self .media )

    @property 
    def name (self ):
        """"""
        return self ._from_attr (types .DocumentAttributeFilename ,'file_name')

    @property 
    def ext (self ):
        """"""
        return (
        mimetypes .guess_extension (self .mime_type )
        or os .path .splitext (self .name or '')[-1 ]
        or None 
        )

    @property 
    def mime_type (self ):
        """"""
        if isinstance (self .media ,types .Photo ):
            return 'image/jpeg'
        elif isinstance (self .media ,types .Document ):
            return self .media .mime_type 

    @property 
    def width (self ):
        """"""
        if isinstance (self .media ,types .Photo ):
            return max (getattr (s ,'w',0 )for s in self .media .sizes )

        return self ._from_attr ((
        types .DocumentAttributeImageSize ,types .DocumentAttributeVideo ),'w')

    @property 
    def height (self ):
        """"""
        if isinstance (self .media ,types .Photo ):
            return max (getattr (s ,'h',0 )for s in self .media .sizes )

        return self ._from_attr ((
        types .DocumentAttributeImageSize ,types .DocumentAttributeVideo ),'h')

    @property 
    def duration (self ):
        """"""
        return self ._from_attr ((
        types .DocumentAttributeAudio ,types .DocumentAttributeVideo ),'duration')

    @property 
    def title (self ):
        """"""
        return self ._from_attr (types .DocumentAttributeAudio ,'title')

    @property 
    def performer (self ):
        """"""
        return self ._from_attr (types .DocumentAttributeAudio ,'performer')

    @property 
    def emoji (self ):
        """"""
        return self ._from_attr (types .DocumentAttributeSticker ,'alt')

    @property 
    def sticker_set (self ):
        """"""
        return self ._from_attr (types .DocumentAttributeSticker ,'stickerset')

    @property 
    def size (self ):
        """"""
        if isinstance (self .media ,types .Photo ):
            return max (filter (None ,map (utils ._photo_size_byte_count ,self .media .sizes )),default =None )
        elif isinstance (self .media ,types .Document ):
            return self .media .size 

    def _from_attr (self ,cls ,field ):
        if isinstance (self .media ,types .Document ):
            for attr in self .media .attributes :
                if isinstance (attr ,cls ):
                    return getattr (attr ,field ,None )
