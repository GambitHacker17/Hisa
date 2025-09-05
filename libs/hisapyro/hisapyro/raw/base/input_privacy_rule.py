
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

InputPrivacyRule =Union [raw .types .InputPrivacyValueAllowAll ,raw .types .InputPrivacyValueAllowChatParticipants ,raw .types .InputPrivacyValueAllowContacts ,raw .types .InputPrivacyValueAllowUsers ,raw .types .InputPrivacyValueDisallowAll ,raw .types .InputPrivacyValueDisallowChatParticipants ,raw .types .InputPrivacyValueDisallowContacts ,raw .types .InputPrivacyValueDisallowUsers ]

class InputPrivacyRule :
    """"""

    QUALNAME ="hisapyro.raw.base.InputPrivacyRule"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/input-privacy-rule")
