
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

PrivacyRule =Union [raw .types .PrivacyValueAllowAll ,raw .types .PrivacyValueAllowChatParticipants ,raw .types .PrivacyValueAllowContacts ,raw .types .PrivacyValueAllowUsers ,raw .types .PrivacyValueDisallowAll ,raw .types .PrivacyValueDisallowChatParticipants ,raw .types .PrivacyValueDisallowContacts ,raw .types .PrivacyValueDisallowUsers ]

class PrivacyRule :
    """"""

    QUALNAME ="hisapyro.raw.base.PrivacyRule"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/privacy-rule")
