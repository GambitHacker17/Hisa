
from typing import Union 
from hisapyro import raw 
from hisapyro .raw .core import TLObject 

MessageAction =Union [raw .types .MessageActionBotAllowed ,raw .types .MessageActionChannelCreate ,raw .types .MessageActionChannelMigrateFrom ,raw .types .MessageActionChatAddUser ,raw .types .MessageActionChatCreate ,raw .types .MessageActionChatDeletePhoto ,raw .types .MessageActionChatDeleteUser ,raw .types .MessageActionChatEditPhoto ,raw .types .MessageActionChatEditTitle ,raw .types .MessageActionChatJoinedByLink ,raw .types .MessageActionChatJoinedByRequest ,raw .types .MessageActionChatMigrateTo ,raw .types .MessageActionContactSignUp ,raw .types .MessageActionCustomAction ,raw .types .MessageActionEmpty ,raw .types .MessageActionGameScore ,raw .types .MessageActionGeoProximityReached ,raw .types .MessageActionGiftPremium ,raw .types .MessageActionGroupCall ,raw .types .MessageActionGroupCallScheduled ,raw .types .MessageActionHistoryClear ,raw .types .MessageActionInviteToGroupCall ,raw .types .MessageActionPaymentSent ,raw .types .MessageActionPaymentSentMe ,raw .types .MessageActionPhoneCall ,raw .types .MessageActionPinMessage ,raw .types .MessageActionRequestedPeer ,raw .types .MessageActionScreenshotTaken ,raw .types .MessageActionSecureValuesSent ,raw .types .MessageActionSecureValuesSentMe ,raw .types .MessageActionSetChatTheme ,raw .types .MessageActionSetChatWallPaper ,raw .types .MessageActionSetMessagesTTL ,raw .types .MessageActionSetSameChatWallPaper ,raw .types .MessageActionSuggestProfilePhoto ,raw .types .MessageActionTopicCreate ,raw .types .MessageActionTopicEdit ,raw .types .MessageActionWebViewDataSent ,raw .types .MessageActionWebViewDataSentMe ]

class MessageAction :
    """"""

    QUALNAME ="hisapyro.raw.base.MessageAction"

    def __init__ (self ):
        raise TypeError ("Base types can only be used for type checking purposes: "
        "you tried to use a base type instance as argument, "
        "but you need to instantiate one of its constructors instead. "
        "More info: https://docs.pyrogram.org/telegram/base/message-action")
