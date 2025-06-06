""""""
from ...tl .tlobject import TLObject 
from ...tl .tlobject import TLRequest 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeDataJSON ,TypeInputInvoice ,TypeInputMedia ,TypeInputPaymentCredentials ,TypeInputPeer ,TypeInputStorePaymentPurpose ,TypePaymentRequestedInfo 

class ApplyGiftCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf6e26854 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,slug :str ):
        """"""
        self .slug =slug 

    def to_dict (self ):
        return {
        '_':'ApplyGiftCodeRequest',
        'slug':self .slug 
        }

    def _bytes (self ):
        return b''.join ((
        b'Th\xe2\xf6',
        self .serialize_bytes (self .slug ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _slug =reader .tgread_string ()
        return cls (slug =_slug )

class AssignAppStoreTransactionRequest (TLRequest ):
    CONSTRUCTOR_ID =0x80ed747d 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,receipt :bytes ,purpose :'TypeInputStorePaymentPurpose'):
        """"""
        self .receipt =receipt 
        self .purpose =purpose 

    def to_dict (self ):
        return {
        '_':'AssignAppStoreTransactionRequest',
        'receipt':self .receipt ,
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose 
        }

    def _bytes (self ):
        return b''.join ((
        b'}t\xed\x80',
        self .serialize_bytes (self .receipt ),
        self .purpose ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _receipt =reader .tgread_bytes ()
        _purpose =reader .tgread_object ()
        return cls (receipt =_receipt ,purpose =_purpose )

class AssignPlayMarketTransactionRequest (TLRequest ):
    CONSTRUCTOR_ID =0xdffd50d3 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,receipt :'TypeDataJSON',purpose :'TypeInputStorePaymentPurpose'):
        """"""
        self .receipt =receipt 
        self .purpose =purpose 

    def to_dict (self ):
        return {
        '_':'AssignPlayMarketTransactionRequest',
        'receipt':self .receipt .to_dict ()if isinstance (self .receipt ,TLObject )else self .receipt ,
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd3P\xfd\xdf',
        self .receipt ._bytes (),
        self .purpose ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _receipt =reader .tgread_object ()
        _purpose =reader .tgread_object ()
        return cls (receipt =_receipt ,purpose =_purpose )

class CanPurchasePremiumRequest (TLRequest ):
    CONSTRUCTOR_ID =0x9fc19eb6 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,purpose :'TypeInputStorePaymentPurpose'):
        """"""
        self .purpose =purpose 

    def to_dict (self ):
        return {
        '_':'CanPurchasePremiumRequest',
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xb6\x9e\xc1\x9f',
        self .purpose ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _purpose =reader .tgread_object ()
        return cls (purpose =_purpose )

class CheckGiftCodeRequest (TLRequest ):
    CONSTRUCTOR_ID =0x8e51b4c1 
    SUBCLASS_OF_ID =0x5b2997e8 

    def __init__ (self ,slug :str ):
        """"""
        self .slug =slug 

    def to_dict (self ):
        return {
        '_':'CheckGiftCodeRequest',
        'slug':self .slug 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc1\xb4Q\x8e',
        self .serialize_bytes (self .slug ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _slug =reader .tgread_string ()
        return cls (slug =_slug )

class ClearSavedInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xd83d70c1 
    SUBCLASS_OF_ID =0xf5b399ac 

    def __init__ (self ,credentials :Optional [bool ]=None ,info :Optional [bool ]=None ):
        """"""
        self .credentials =credentials 
        self .info =info 

    def to_dict (self ):
        return {
        '_':'ClearSavedInfoRequest',
        'credentials':self .credentials ,
        'info':self .info 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xc1p=\xd8',
        struct .pack ('<I',(0 if self .credentials is None or self .credentials is False else 1 )|(0 if self .info is None or self .info is False else 2 )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _credentials =bool (flags &1 )
        _info =bool (flags &2 )
        return cls (credentials =_credentials ,info =_info )

class ExportInvoiceRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf91b065 
    SUBCLASS_OF_ID =0x36105432 

    def __init__ (self ,invoice_media :'TypeInputMedia'):
        """"""
        self .invoice_media =invoice_media 

    async def resolve (self ,client ,utils ):
        self .invoice_media =utils .get_input_media (self .invoice_media )

    def to_dict (self ):
        return {
        '_':'ExportInvoiceRequest',
        'invoice_media':self .invoice_media .to_dict ()if isinstance (self .invoice_media ,TLObject )else self .invoice_media 
        }

    def _bytes (self ):
        return b''.join ((
        b'e\xb0\x91\x0f',
        self .invoice_media ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _invoice_media =reader .tgread_object ()
        return cls (invoice_media =_invoice_media )

class GetBankCardDataRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2e79d779 
    SUBCLASS_OF_ID =0x8c6dd68b 

    def __init__ (self ,number :str ):
        """"""
        self .number =number 

    def to_dict (self ):
        return {
        '_':'GetBankCardDataRequest',
        'number':self .number 
        }

    def _bytes (self ):
        return b''.join ((
        b'y\xd7y.',
        self .serialize_bytes (self .number ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _number =reader .tgread_string ()
        return cls (number =_number )

class GetGiveawayInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xf4239425 
    SUBCLASS_OF_ID =0x96a377bd 

    def __init__ (self ,peer :'TypeInputPeer',msg_id :int ):
        """"""
        self .peer =peer 
        self .msg_id =msg_id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetGiveawayInfoRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'msg_id':self .msg_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'%\x94#\xf4',
        self .peer ._bytes (),
        struct .pack ('<i',self .msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _msg_id =reader .read_int ()
        return cls (peer =_peer ,msg_id =_msg_id )

class GetPaymentFormRequest (TLRequest ):
    CONSTRUCTOR_ID =0x37148dbb 
    SUBCLASS_OF_ID =0xa0483f19 

    def __init__ (self ,invoice :'TypeInputInvoice',theme_params :Optional ['TypeDataJSON']=None ):
        """"""
        self .invoice =invoice 
        self .theme_params =theme_params 

    def to_dict (self ):
        return {
        '_':'GetPaymentFormRequest',
        'invoice':self .invoice .to_dict ()if isinstance (self .invoice ,TLObject )else self .invoice ,
        'theme_params':self .theme_params .to_dict ()if isinstance (self .theme_params ,TLObject )else self .theme_params 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xbb\x8d\x147',
        struct .pack ('<I',(0 if self .theme_params is None or self .theme_params is False else 1 )),
        self .invoice ._bytes (),
        b''if self .theme_params is None or self .theme_params is False else (self .theme_params ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _invoice =reader .tgread_object ()
        if flags &1 :
            _theme_params =reader .tgread_object ()
        else :
            _theme_params =None 
        return cls (invoice =_invoice ,theme_params =_theme_params )

class GetPaymentReceiptRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2478d1cc 
    SUBCLASS_OF_ID =0x590093c9 

    def __init__ (self ,peer :'TypeInputPeer',msg_id :int ):
        """"""
        self .peer =peer 
        self .msg_id =msg_id 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'GetPaymentReceiptRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'msg_id':self .msg_id 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xcc\xd1x$',
        self .peer ._bytes (),
        struct .pack ('<i',self .msg_id ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _msg_id =reader .read_int ()
        return cls (peer =_peer ,msg_id =_msg_id )

class GetPremiumGiftCodeOptionsRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2757ba54 
    SUBCLASS_OF_ID =0xaa92583 

    def __init__ (self ,boost_peer :Optional ['TypeInputPeer']=None ):
        """"""
        self .boost_peer =boost_peer 

    async def resolve (self ,client ,utils ):
        if self .boost_peer :
            self .boost_peer =utils .get_input_peer (await client .get_input_entity (self .boost_peer ))

    def to_dict (self ):
        return {
        '_':'GetPremiumGiftCodeOptionsRequest',
        'boost_peer':self .boost_peer .to_dict ()if isinstance (self .boost_peer ,TLObject )else self .boost_peer 
        }

    def _bytes (self ):
        return b''.join ((
        b"T\xbaW'",
        struct .pack ('<I',(0 if self .boost_peer is None or self .boost_peer is False else 1 )),
        b''if self .boost_peer is None or self .boost_peer is False else (self .boost_peer ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _boost_peer =reader .tgread_object ()
        else :
            _boost_peer =None 
        return cls (boost_peer =_boost_peer )

class GetSavedInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0x227d824b 
    SUBCLASS_OF_ID =0xad3cf146 

    def to_dict (self ):
        return {
        '_':'GetSavedInfoRequest'
        }

    def _bytes (self ):
        return b''.join ((
        b'K\x82}"',
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        return cls ()

class LaunchPrepaidGiveawayRequest (TLRequest ):
    CONSTRUCTOR_ID =0x5ff58f20 
    SUBCLASS_OF_ID =0x8af52aac 

    def __init__ (self ,peer :'TypeInputPeer',giveaway_id :int ,purpose :'TypeInputStorePaymentPurpose'):
        """"""
        self .peer =peer 
        self .giveaway_id =giveaway_id 
        self .purpose =purpose 

    async def resolve (self ,client ,utils ):
        self .peer =utils .get_input_peer (await client .get_input_entity (self .peer ))

    def to_dict (self ):
        return {
        '_':'LaunchPrepaidGiveawayRequest',
        'peer':self .peer .to_dict ()if isinstance (self .peer ,TLObject )else self .peer ,
        'giveaway_id':self .giveaway_id ,
        'purpose':self .purpose .to_dict ()if isinstance (self .purpose ,TLObject )else self .purpose 
        }

    def _bytes (self ):
        return b''.join ((
        b' \x8f\xf5_',
        self .peer ._bytes (),
        struct .pack ('<q',self .giveaway_id ),
        self .purpose ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _peer =reader .tgread_object ()
        _giveaway_id =reader .read_long ()
        _purpose =reader .tgread_object ()
        return cls (peer =_peer ,giveaway_id =_giveaway_id ,purpose =_purpose )

class SendPaymentFormRequest (TLRequest ):
    CONSTRUCTOR_ID =0x2d03522f 
    SUBCLASS_OF_ID =0x8ae16a9d 

    def __init__ (self ,form_id :int ,invoice :'TypeInputInvoice',credentials :'TypeInputPaymentCredentials',requested_info_id :Optional [str ]=None ,shipping_option_id :Optional [str ]=None ,tip_amount :Optional [int ]=None ):
        """"""
        self .form_id =form_id 
        self .invoice =invoice 
        self .credentials =credentials 
        self .requested_info_id =requested_info_id 
        self .shipping_option_id =shipping_option_id 
        self .tip_amount =tip_amount 

    def to_dict (self ):
        return {
        '_':'SendPaymentFormRequest',
        'form_id':self .form_id ,
        'invoice':self .invoice .to_dict ()if isinstance (self .invoice ,TLObject )else self .invoice ,
        'credentials':self .credentials .to_dict ()if isinstance (self .credentials ,TLObject )else self .credentials ,
        'requested_info_id':self .requested_info_id ,
        'shipping_option_id':self .shipping_option_id ,
        'tip_amount':self .tip_amount 
        }

    def _bytes (self ):
        return b''.join ((
        b'/R\x03-',
        struct .pack ('<I',(0 if self .requested_info_id is None or self .requested_info_id is False else 1 )|(0 if self .shipping_option_id is None or self .shipping_option_id is False else 2 )|(0 if self .tip_amount is None or self .tip_amount is False else 4 )),
        struct .pack ('<q',self .form_id ),
        self .invoice ._bytes (),
        b''if self .requested_info_id is None or self .requested_info_id is False else (self .serialize_bytes (self .requested_info_id )),
        b''if self .shipping_option_id is None or self .shipping_option_id is False else (self .serialize_bytes (self .shipping_option_id )),
        self .credentials ._bytes (),
        b''if self .tip_amount is None or self .tip_amount is False else (struct .pack ('<q',self .tip_amount )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _form_id =reader .read_long ()
        _invoice =reader .tgread_object ()
        if flags &1 :
            _requested_info_id =reader .tgread_string ()
        else :
            _requested_info_id =None 
        if flags &2 :
            _shipping_option_id =reader .tgread_string ()
        else :
            _shipping_option_id =None 
        _credentials =reader .tgread_object ()
        if flags &4 :
            _tip_amount =reader .read_long ()
        else :
            _tip_amount =None 
        return cls (form_id =_form_id ,invoice =_invoice ,credentials =_credentials ,requested_info_id =_requested_info_id ,shipping_option_id =_shipping_option_id ,tip_amount =_tip_amount )

class ValidateRequestedInfoRequest (TLRequest ):
    CONSTRUCTOR_ID =0xb6c8f12b 
    SUBCLASS_OF_ID =0x8f8044b7 

    def __init__ (self ,invoice :'TypeInputInvoice',info :'TypePaymentRequestedInfo',save :Optional [bool ]=None ):
        """"""
        self .invoice =invoice 
        self .info =info 
        self .save =save 

    def to_dict (self ):
        return {
        '_':'ValidateRequestedInfoRequest',
        'invoice':self .invoice .to_dict ()if isinstance (self .invoice ,TLObject )else self .invoice ,
        'info':self .info .to_dict ()if isinstance (self .info ,TLObject )else self .info ,
        'save':self .save 
        }

    def _bytes (self ):
        return b''.join ((
        b'+\xf1\xc8\xb6',
        struct .pack ('<I',(0 if self .save is None or self .save is False else 1 )),
        self .invoice ._bytes (),
        self .info ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _save =bool (flags &1 )
        _invoice =reader .tgread_object ()
        _info =reader .tgread_object ()
        return cls (invoice =_invoice ,info =_info ,save =_save )

