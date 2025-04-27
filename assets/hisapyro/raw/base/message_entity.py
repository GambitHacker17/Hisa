
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

MessageEntity =Union [raw .types .InputMessageEntityMentionName ,raw .types .MessageEntityBankCard ,raw .types .MessageEntityBlockquote ,raw .types .MessageEntityBold ,raw .types .MessageEntityBotCommand ,raw .types .MessageEntityCashtag ,raw .types .MessageEntityCode ,raw .types .MessageEntityCustomEmoji ,raw .types .MessageEntityEmail ,raw .types .MessageEntityHashtag ,raw .types .MessageEntityItalic ,raw .types .MessageEntityMention ,raw .types .MessageEntityMentionName ,raw .types .MessageEntityPhone ,raw .types .MessageEntityPre ,raw .types .MessageEntitySpoiler ,raw .types .MessageEntityStrike ,raw .types .MessageEntityTextUrl ,raw .types .MessageEntityUnderline ,raw .types .MessageEntityUnknown ,raw .types .MessageEntityUrl ]

class MessageEntity :
    """"""

    QUALNAME ="hisapyro.raw.base.MessageEntity"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/message-entity")
