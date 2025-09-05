
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputPrivacyKey =Union [raw .types .InputPrivacyKeyAddedByPhone ,raw .types .InputPrivacyKeyChatInvite ,raw .types .InputPrivacyKeyForwards ,raw .types .InputPrivacyKeyPhoneCall ,raw .types .InputPrivacyKeyPhoneNumber ,raw .types .InputPrivacyKeyPhoneP2P ,raw .types .InputPrivacyKeyProfilePhoto ,raw .types .InputPrivacyKeyStatusTimestamp ,raw .types .InputPrivacyKeyVoiceMessages ]

class InputPrivacyKey :
    """"""

    QUALNAME ="hisapyro.raw.base.InputPrivacyKey"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-privacy-key")
