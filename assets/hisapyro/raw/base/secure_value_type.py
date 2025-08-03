
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

SecureValueType =Union [raw .types .SecureValueTypeAddress ,raw .types .SecureValueTypeBankStatement ,raw .types .SecureValueTypeDriverLicense ,raw .types .SecureValueTypeEmail ,raw .types .SecureValueTypeIdentityCard ,raw .types .SecureValueTypeInternalPassport ,raw .types .SecureValueTypePassport ,raw .types .SecureValueTypePassportRegistration ,raw .types .SecureValueTypePersonalDetails ,raw .types .SecureValueTypePhone ,raw .types .SecureValueTypeRentalAgreement ,raw .types .SecureValueTypeTemporaryRegistration ,raw .types .SecureValueTypeUtilityBill ]

class SecureValueType :
    """"""

    QUALNAME ="hisapyro.raw.base.SecureValueType"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/secure-value-type")
