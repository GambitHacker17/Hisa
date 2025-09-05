
from hisapyro import raw ,types 
from ..object import Object 

class KeyboardButton (Object ):
    """"""

    def __init__ (
    self ,
    text :str ,
    request_contact :bool =None ,
    request_location :bool =None ,
    web_app :"types.WebAppInfo"=None 
    ):
        super ().__init__ ()

        self .text =str (text )
        self .request_contact =request_contact 
        self .request_location =request_location 
        self .web_app =web_app 

    @staticmethod 
    def read (b ):
        if isinstance (b ,raw .types .KeyboardButton ):
            return b .text 

        if isinstance (b ,raw .types .KeyboardButtonRequestPhone ):
            return KeyboardButton (
            text =b .text ,
            request_contact =True 
            )

        if isinstance (b ,raw .types .KeyboardButtonRequestGeoLocation ):
            return KeyboardButton (
            text =b .text ,
            request_location =True 
            )

        if isinstance (b ,raw .types .KeyboardButtonSimpleWebView ):
            return KeyboardButton (
            text =b .text ,
            web_app =types .WebAppInfo (
            url =b .url 
            )
            )

    def write (self ):
        if self .request_contact :
            return raw .types .KeyboardButtonRequestPhone (text =self .text )
        elif self .request_location :
            return raw .types .KeyboardButtonRequestGeoLocation (text =self .text )
        elif self .web_app :
            return raw .types .KeyboardButtonSimpleWebView (text =self .text ,url =self .web_app .url )
        else :
            return raw .types .KeyboardButton (text =self .text )
