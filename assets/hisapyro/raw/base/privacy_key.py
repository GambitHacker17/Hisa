
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PrivacyKey =Union [raw .types .PrivacyKeyAddedByPhone ,raw .types .PrivacyKeyChatInvite ,raw .types .PrivacyKeyForwards ,raw .types .PrivacyKeyPhoneCall ,raw .types .PrivacyKeyPhoneNumber ,raw .types .PrivacyKeyPhoneP2P ,raw .types .PrivacyKeyProfilePhoto ,raw .types .PrivacyKeyStatusTimestamp ,raw .types .PrivacyKeyVoiceMessages ]

class PrivacyKey :
    """"""

    QUALNAME ="hisapyro.raw.base.PrivacyKey"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/privacy-key")
