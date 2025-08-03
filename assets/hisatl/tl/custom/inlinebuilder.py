import hashlib 

from ..import functions ,types 
from ...import utils 

_TYPE_TO_MIMES ={
'gif':['image/gif'],
'article':['text/html'],
'audio':['audio/mpeg'],
'contact':[],
'file':['application/pdf','application/zip'],
'geo':[],
'photo':['image/jpeg'],
'sticker':['image/webp','application/x-tgsticker'],
'venue':[],
'video':['video/mp4'],
'voice':['audio/ogg'],
}

class InlineBuilder :
    """"""
    def __init__ (self ,client ):
        self ._client =client 

    async def article (
    self ,title ,description =None ,
    *,url =None ,thumb =None ,content =None ,
    id =None ,text =None ,parse_mode =(),link_preview =True ,
    geo =None ,period =60 ,contact =None ,game =False ,buttons =None 
    ):
        """"""

        result =types .InputBotInlineResult (
        id =id or '',
        type ='article',
        send_message =await self ._message (
        text =text ,parse_mode =parse_mode ,link_preview =link_preview ,
        geo =geo ,period =period ,
        contact =contact ,
        game =game ,
        buttons =buttons 
        ),
        title =title ,
        description =description ,
        url =url ,
        thumb =thumb ,
        content =content 
        )
        if id is None :
            result .id =hashlib .sha256 (bytes (result )).hexdigest ()

        return result 

    async def photo (
    self ,file ,*,id =None ,include_media =True ,
    text =None ,parse_mode =(),link_preview =True ,
    geo =None ,period =60 ,contact =None ,game =False ,buttons =None 
    ):
        """"""
        try :
            fh =utils .get_input_photo (file )
        except TypeError :
            _ ,media ,_ =await self ._client ._file_to_media (
            file ,allow_cache =True ,as_image =True 
            )
            if isinstance (media ,types .InputPhoto ):
                fh =media 
            else :
                r =await self ._client (functions .messages .UploadMediaRequest (
                types .InputPeerSelf (),media =media 
                ))
                fh =utils .get_input_photo (r .photo )

        result =types .InputBotInlineResultPhoto (
        id =id or '',
        type ='photo',
        photo =fh ,
        send_message =await self ._message (
        text =text or '',
        parse_mode =parse_mode ,
        link_preview =link_preview ,
        media =include_media ,
        geo =geo ,
        period =period ,
        contact =contact ,
        game =game ,
        buttons =buttons 
        )
        )
        if id is None :
            result .id =hashlib .sha256 (bytes (result )).hexdigest ()

        return result 

    async def document (
    self ,file ,title =None ,*,description =None ,type =None ,
    mime_type =None ,attributes =None ,force_document =False ,
    voice_note =False ,video_note =False ,use_cache =True ,id =None ,
    text =None ,parse_mode =(),link_preview =True ,
    geo =None ,period =60 ,contact =None ,game =False ,buttons =None ,
    include_media =True 
    ):
        """"""
        if type is None :
            if voice_note :
                type ='voice'
            elif mime_type :
                for ty ,mimes in _TYPE_TO_MIMES .items ():
                    for mime in mimes :
                        if mime_type ==mime :
                            type =ty 
                            break 

            if type is None :
                type ='file'

        try :
            fh =utils .get_input_document (file )
        except TypeError :
            _ ,media ,_ =await self ._client ._file_to_media (
            file ,
            mime_type =mime_type ,
            attributes =attributes ,
            force_document =force_document ,
            voice_note =voice_note ,
            video_note =video_note ,
            allow_cache =use_cache 
            )
            if isinstance (media ,types .InputDocument ):
                fh =media 
            else :
                r =await self ._client (functions .messages .UploadMediaRequest (
                types .InputPeerSelf (),media =media 
                ))
                fh =utils .get_input_document (r .document )

        result =types .InputBotInlineResultDocument (
        id =id or '',
        type =type ,
        document =fh ,
        send_message =await self ._message (

        text =text or '',
        parse_mode =parse_mode ,
        link_preview =link_preview ,
        media =include_media ,
        geo =geo ,
        period =period ,
        contact =contact ,
        game =game ,
        buttons =buttons 
        ),
        title =title ,
        description =description 
        )
        if id is None :
            result .id =hashlib .sha256 (bytes (result )).hexdigest ()

        return result 

    async def game (
    self ,short_name ,*,id =None ,
    text =None ,parse_mode =(),link_preview =True ,
    geo =None ,period =60 ,contact =None ,game =False ,buttons =None 
    ):
        """"""
        result =types .InputBotInlineResultGame (
        id =id or '',
        short_name =short_name ,
        send_message =await self ._message (
        text =text ,parse_mode =parse_mode ,link_preview =link_preview ,
        geo =geo ,period =period ,
        contact =contact ,
        game =game ,
        buttons =buttons 
        )
        )
        if id is None :
            result .id =hashlib .sha256 (bytes (result )).hexdigest ()

        return result 

    async def _message (
    self ,*,
    text =None ,parse_mode =(),link_preview =True ,media =False ,
    geo =None ,period =60 ,contact =None ,game =False ,buttons =None 
    ):

        args =('\0'if text ==''else text ,geo ,contact ,game )
        if sum (1 for x in args if x is not None and x is not False )!=1 :
            raise ValueError (
            'Must set exactly one of text, geo, contact or game (set {})'
            .format (', '.join (x [0 ]for x in zip (
            'text geo contact game'.split (),args )if x [1 ])or 'none')
            )

        markup =self ._client .build_reply_markup (buttons ,inline_only =True )
        if text is not None :
            text ,msg_entities =await self ._client ._parse_message_text (
            text ,parse_mode 
            )
            if media :

                return types .InputBotInlineMessageMediaAuto (
                message =text ,
                entities =msg_entities ,
                reply_markup =markup 
                )
            else :
                return types .InputBotInlineMessageText (
                message =text ,
                no_webpage =not link_preview ,
                entities =msg_entities ,
                reply_markup =markup 
                )
        elif isinstance (geo ,(types .InputGeoPoint ,types .GeoPoint )):
            return types .InputBotInlineMessageMediaGeo (
            geo_point =utils .get_input_geo (geo ),
            period =period ,
            reply_markup =markup 
            )
        elif isinstance (geo ,(types .InputMediaVenue ,types .MessageMediaVenue )):
            if isinstance (geo ,types .InputMediaVenue ):
                geo_point =geo .geo_point 
            else :
                geo_point =geo .geo 

            return types .InputBotInlineMessageMediaVenue (
            geo_point =geo_point ,
            title =geo .title ,
            address =geo .address ,
            provider =geo .provider ,
            venue_id =geo .venue_id ,
            venue_type =geo .venue_type ,
            reply_markup =markup 
            )
        elif isinstance (contact ,(
        types .InputMediaContact ,types .MessageMediaContact )):
            return types .InputBotInlineMessageMediaContact (
            phone_number =contact .phone_number ,
            first_name =contact .first_name ,
            last_name =contact .last_name ,
            vcard =contact .vcard ,
            reply_markup =markup 
            )
        elif game :
            return types .InputBotInlineMessageGame (
            reply_markup =markup 
            )
        else :
            raise ValueError ('No text, game or valid geo or contact given')
