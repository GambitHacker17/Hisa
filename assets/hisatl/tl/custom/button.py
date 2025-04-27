from ..import types 
from ...import utils 

class Button :
    """"""
    def __init__ (self ,button ,*,resize ,single_use ,selective ):
        self .button =button 
        self .resize =resize 
        self .single_use =single_use 
        self .selective =selective 

    @staticmethod 
    def _is_inline (button ):
        """"""
        return isinstance (button ,(
        types .KeyboardButtonBuy ,
        types .KeyboardButtonCallback ,
        types .KeyboardButtonGame ,
        types .KeyboardButtonSwitchInline ,
        types .KeyboardButtonUrl ,
        types .InputKeyboardButtonUrlAuth 
        ))

    @staticmethod 
    def inline (text ,data =None ):
        """"""
        if not data :
            data =text .encode ('utf-8')
        elif not isinstance (data ,(bytes ,bytearray ,memoryview )):
            data =str (data ).encode ('utf-8')

        if len (data )>64 :
            raise ValueError ('Too many bytes for the data')

        return types .KeyboardButtonCallback (text ,data )

    @staticmethod 
    def switch_inline (text ,query ='',same_peer =False ):
        """"""
        return types .KeyboardButtonSwitchInline (text ,query ,same_peer )

    @staticmethod 
    def url (text ,url =None ):
        """"""
        return types .KeyboardButtonUrl (text ,url or text )

    @staticmethod 
    def auth (text ,url =None ,*,bot =None ,write_access =False ,fwd_text =None ):
        """"""
        return types .InputKeyboardButtonUrlAuth (
        text =text ,
        url =url or text ,
        bot =utils .get_input_user (bot or types .InputUserSelf ()),
        request_write_access =write_access ,
        fwd_text =fwd_text 
        )

    @classmethod 
    def text (cls ,text ,*,resize =None ,single_use =None ,selective =None ):
        """"""
        return cls (types .KeyboardButton (text ),
        resize =resize ,single_use =single_use ,selective =selective )

    @classmethod 
    def request_location (cls ,text ,*,
    resize =None ,single_use =None ,selective =None ):
        """"""
        return cls (types .KeyboardButtonRequestGeoLocation (text ),
        resize =resize ,single_use =single_use ,selective =selective )

    @classmethod 
    def request_phone (cls ,text ,*,
    resize =None ,single_use =None ,selective =None ):
        """"""
        return cls (types .KeyboardButtonRequestPhone (text ),
        resize =resize ,single_use =single_use ,selective =selective )

    @classmethod 
    def request_poll (cls ,text ,*,force_quiz =False ,
    resize =None ,single_use =None ,selective =None ):
        """"""
        return cls (types .KeyboardButtonRequestPoll (text ,quiz =force_quiz ),
        resize =resize ,single_use =single_use ,selective =selective )

    @staticmethod 
    def clear (selective =None ):
        """"""
        return types .ReplyKeyboardHide (selective =selective )

    @staticmethod 
    def force_reply (single_use =None ,selective =None ,placeholder =None ):
        """"""
        return types .ReplyKeyboardForceReply (
        single_use =single_use ,
        selective =selective ,
        placeholder =placeholder )

    @staticmethod 
    def buy (text ):
        """"""
        return types .KeyboardButtonBuy (text )

    @staticmethod 
    def game (text ):
        """"""
        return types .KeyboardButtonGame (text )
