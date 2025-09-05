
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputMedia =Union [raw .types .InputMediaContact ,raw .types .InputMediaDice ,raw .types .InputMediaDocument ,raw .types .InputMediaDocumentExternal ,raw .types .InputMediaEmpty ,raw .types .InputMediaGame ,raw .types .InputMediaGeoLive ,raw .types .InputMediaGeoPoint ,raw .types .InputMediaInvoice ,raw .types .InputMediaPhoto ,raw .types .InputMediaPhotoExternal ,raw .types .InputMediaPoll ,raw .types .InputMediaUploadedDocument ,raw .types .InputMediaUploadedPhoto ,raw .types .InputMediaVenue ]

class InputMedia :
    """"""

    QUALNAME ="hisapyro.raw.base.InputMedia"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-media")
