
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

TopPeerCategory =Union [raw .types .TopPeerCategoryBotsInline ,raw .types .TopPeerCategoryBotsPM ,raw .types .TopPeerCategoryChannels ,raw .types .TopPeerCategoryCorrespondents ,raw .types .TopPeerCategoryForwardChats ,raw .types .TopPeerCategoryForwardUsers ,raw .types .TopPeerCategoryGroups ,raw .types .TopPeerCategoryPhoneCalls ]

class TopPeerCategory :
    """"""

    QUALNAME ="hisapyro.raw.base.TopPeerCategory"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/top-peer-category")
