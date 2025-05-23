""""""
from ...tl .tlobject import TLObject 
from typing import Optional ,List ,Union ,TYPE_CHECKING 
import os 
import struct 
from datetime import datetime 
if TYPE_CHECKING :
    from ...tl .types import TypeBankCardOpenUrl ,TypeChat ,TypeDataJSON ,TypeInvoice ,TypePaymentFormMethod ,TypePaymentRequestedInfo ,TypePaymentSavedCredentials ,TypePeer ,TypeShippingOption ,TypeUpdates ,TypeUser ,TypeWebDocument 

class BankCardData (TLObject ):
    CONSTRUCTOR_ID =0x3e24e573 
    SUBCLASS_OF_ID =0x8c6dd68b 

    def __init__ (self ,title :str ,open_urls :List ['TypeBankCardOpenUrl']):
        """"""
        self .title =title 
        self .open_urls =open_urls 

    def to_dict (self ):
        return {
        '_':'BankCardData',
        'title':self .title ,
        'open_urls':[]if self .open_urls is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .open_urls ]
        }

    def _bytes (self ):
        return b''.join ((
        b's\xe5$>',
        self .serialize_bytes (self .title ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .open_urls )),b''.join (x ._bytes ()for x in self .open_urls ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _title =reader .tgread_string ()
        reader .read_int ()
        _open_urls =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _open_urls .append (_x )

        return cls (title =_title ,open_urls =_open_urls )

class CheckedGiftCode (TLObject ):
    CONSTRUCTOR_ID =0xb722f158 
    SUBCLASS_OF_ID =0x5b2997e8 

    def __init__ (self ,from_id :'TypePeer',date :Optional [datetime ],months :int ,chats :List ['TypeChat'],users :List ['TypeUser'],via_giveaway :Optional [bool ]=None ,giveaway_msg_id :Optional [int ]=None ,to_id :Optional [int ]=None ,used_date :Optional [datetime ]=None ):
        """"""
        self .from_id =from_id 
        self .date =date 
        self .months =months 
        self .chats =chats 
        self .users =users 
        self .via_giveaway =via_giveaway 
        self .giveaway_msg_id =giveaway_msg_id 
        self .to_id =to_id 
        self .used_date =used_date 

    def to_dict (self ):
        return {
        '_':'CheckedGiftCode',
        'from_id':self .from_id .to_dict ()if isinstance (self .from_id ,TLObject )else self .from_id ,
        'date':self .date ,
        'months':self .months ,
        'chats':[]if self .chats is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .chats ],
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'via_giveaway':self .via_giveaway ,
        'giveaway_msg_id':self .giveaway_msg_id ,
        'to_id':self .to_id ,
        'used_date':self .used_date 
        }

    def _bytes (self ):
        return b''.join ((
        b'X\xf1"\xb7',
        struct .pack ('<I',(0 if self .via_giveaway is None or self .via_giveaway is False else 4 )|(0 if self .giveaway_msg_id is None or self .giveaway_msg_id is False else 8 )|(0 if self .to_id is None or self .to_id is False else 1 )|(0 if self .used_date is None or self .used_date is False else 2 )),
        self .from_id ._bytes (),
        b''if self .giveaway_msg_id is None or self .giveaway_msg_id is False else (struct .pack ('<i',self .giveaway_msg_id )),
        b''if self .to_id is None or self .to_id is False else (struct .pack ('<q',self .to_id )),
        self .serialize_datetime (self .date ),
        struct .pack ('<i',self .months ),
        b''if self .used_date is None or self .used_date is False else (self .serialize_datetime (self .used_date )),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .chats )),b''.join (x ._bytes ()for x in self .chats ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _via_giveaway =bool (flags &4 )
        _from_id =reader .tgread_object ()
        if flags &8 :
            _giveaway_msg_id =reader .read_int ()
        else :
            _giveaway_msg_id =None 
        if flags &1 :
            _to_id =reader .read_long ()
        else :
            _to_id =None 
        _date =reader .tgread_date ()
        _months =reader .read_int ()
        if flags &2 :
            _used_date =reader .tgread_date ()
        else :
            _used_date =None 
        reader .read_int ()
        _chats =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _chats .append (_x )

        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (from_id =_from_id ,date =_date ,months =_months ,chats =_chats ,users =_users ,via_giveaway =_via_giveaway ,giveaway_msg_id =_giveaway_msg_id ,to_id =_to_id ,used_date =_used_date )

class ExportedInvoice (TLObject ):
    CONSTRUCTOR_ID =0xaed0cbd9 
    SUBCLASS_OF_ID =0x36105432 

    def __init__ (self ,url :str ):
        """"""
        self .url =url 

    def to_dict (self ):
        return {
        '_':'ExportedInvoice',
        'url':self .url 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xd9\xcb\xd0\xae',
        self .serialize_bytes (self .url ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _url =reader .tgread_string ()
        return cls (url =_url )

class GiveawayInfo (TLObject ):
    CONSTRUCTOR_ID =0x4367daa0 
    SUBCLASS_OF_ID =0x96a377bd 

    def __init__ (self ,start_date :Optional [datetime ],participating :Optional [bool ]=None ,preparing_results :Optional [bool ]=None ,joined_too_early_date :Optional [datetime ]=None ,admin_disallowed_chat_id :Optional [int ]=None ,disallowed_country :Optional [str ]=None ):
        """"""
        self .start_date =start_date 
        self .participating =participating 
        self .preparing_results =preparing_results 
        self .joined_too_early_date =joined_too_early_date 
        self .admin_disallowed_chat_id =admin_disallowed_chat_id 
        self .disallowed_country =disallowed_country 

    def to_dict (self ):
        return {
        '_':'GiveawayInfo',
        'start_date':self .start_date ,
        'participating':self .participating ,
        'preparing_results':self .preparing_results ,
        'joined_too_early_date':self .joined_too_early_date ,
        'admin_disallowed_chat_id':self .admin_disallowed_chat_id ,
        'disallowed_country':self .disallowed_country 
        }

    def _bytes (self ):
        return b''.join ((
        b'\xa0\xdagC',
        struct .pack ('<I',(0 if self .participating is None or self .participating is False else 1 )|(0 if self .preparing_results is None or self .preparing_results is False else 8 )|(0 if self .joined_too_early_date is None or self .joined_too_early_date is False else 2 )|(0 if self .admin_disallowed_chat_id is None or self .admin_disallowed_chat_id is False else 4 )|(0 if self .disallowed_country is None or self .disallowed_country is False else 16 )),
        self .serialize_datetime (self .start_date ),
        b''if self .joined_too_early_date is None or self .joined_too_early_date is False else (self .serialize_datetime (self .joined_too_early_date )),
        b''if self .admin_disallowed_chat_id is None or self .admin_disallowed_chat_id is False else (struct .pack ('<q',self .admin_disallowed_chat_id )),
        b''if self .disallowed_country is None or self .disallowed_country is False else (self .serialize_bytes (self .disallowed_country )),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _participating =bool (flags &1 )
        _preparing_results =bool (flags &8 )
        _start_date =reader .tgread_date ()
        if flags &2 :
            _joined_too_early_date =reader .tgread_date ()
        else :
            _joined_too_early_date =None 
        if flags &4 :
            _admin_disallowed_chat_id =reader .read_long ()
        else :
            _admin_disallowed_chat_id =None 
        if flags &16 :
            _disallowed_country =reader .tgread_string ()
        else :
            _disallowed_country =None 
        return cls (start_date =_start_date ,participating =_participating ,preparing_results =_preparing_results ,joined_too_early_date =_joined_too_early_date ,admin_disallowed_chat_id =_admin_disallowed_chat_id ,disallowed_country =_disallowed_country )

class GiveawayInfoResults (TLObject ):
    CONSTRUCTOR_ID =0xcd5570 
    SUBCLASS_OF_ID =0x96a377bd 

    def __init__ (self ,start_date :Optional [datetime ],finish_date :Optional [datetime ],winners_count :int ,activated_count :int ,winner :Optional [bool ]=None ,refunded :Optional [bool ]=None ,gift_code_slug :Optional [str ]=None ):
        """"""
        self .start_date =start_date 
        self .finish_date =finish_date 
        self .winners_count =winners_count 
        self .activated_count =activated_count 
        self .winner =winner 
        self .refunded =refunded 
        self .gift_code_slug =gift_code_slug 

    def to_dict (self ):
        return {
        '_':'GiveawayInfoResults',
        'start_date':self .start_date ,
        'finish_date':self .finish_date ,
        'winners_count':self .winners_count ,
        'activated_count':self .activated_count ,
        'winner':self .winner ,
        'refunded':self .refunded ,
        'gift_code_slug':self .gift_code_slug 
        }

    def _bytes (self ):
        assert ((self .winner or self .winner is not None )and (self .gift_code_slug or self .gift_code_slug is not None ))or ((self .winner is None or self .winner is False )and (self .gift_code_slug is None or self .gift_code_slug is False )),'winner, gift_code_slug parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'pU\xcd\x00',
        struct .pack ('<I',(0 if self .winner is None or self .winner is False else 1 )|(0 if self .refunded is None or self .refunded is False else 2 )|(0 if self .gift_code_slug is None or self .gift_code_slug is False else 1 )),
        self .serialize_datetime (self .start_date ),
        b''if self .gift_code_slug is None or self .gift_code_slug is False else (self .serialize_bytes (self .gift_code_slug )),
        self .serialize_datetime (self .finish_date ),
        struct .pack ('<i',self .winners_count ),
        struct .pack ('<i',self .activated_count ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _winner =bool (flags &1 )
        _refunded =bool (flags &2 )
        _start_date =reader .tgread_date ()
        if flags &1 :
            _gift_code_slug =reader .tgread_string ()
        else :
            _gift_code_slug =None 
        _finish_date =reader .tgread_date ()
        _winners_count =reader .read_int ()
        _activated_count =reader .read_int ()
        return cls (start_date =_start_date ,finish_date =_finish_date ,winners_count =_winners_count ,activated_count =_activated_count ,winner =_winner ,refunded =_refunded ,gift_code_slug =_gift_code_slug )

class PaymentForm (TLObject ):
    CONSTRUCTOR_ID =0xa0058751 
    SUBCLASS_OF_ID =0xa0483f19 

    def __init__ (self ,form_id :int ,bot_id :int ,title :str ,description :str ,invoice :'TypeInvoice',provider_id :int ,url :str ,users :List ['TypeUser'],can_save_credentials :Optional [bool ]=None ,password_missing :Optional [bool ]=None ,photo :Optional ['TypeWebDocument']=None ,native_provider :Optional [str ]=None ,native_params :Optional ['TypeDataJSON']=None ,additional_methods :Optional [List ['TypePaymentFormMethod']]=None ,saved_info :Optional ['TypePaymentRequestedInfo']=None ,saved_credentials :Optional [List ['TypePaymentSavedCredentials']]=None ):
        """"""
        self .form_id =form_id 
        self .bot_id =bot_id 
        self .title =title 
        self .description =description 
        self .invoice =invoice 
        self .provider_id =provider_id 
        self .url =url 
        self .users =users 
        self .can_save_credentials =can_save_credentials 
        self .password_missing =password_missing 
        self .photo =photo 
        self .native_provider =native_provider 
        self .native_params =native_params 
        self .additional_methods =additional_methods 
        self .saved_info =saved_info 
        self .saved_credentials =saved_credentials 

    def to_dict (self ):
        return {
        '_':'PaymentForm',
        'form_id':self .form_id ,
        'bot_id':self .bot_id ,
        'title':self .title ,
        'description':self .description ,
        'invoice':self .invoice .to_dict ()if isinstance (self .invoice ,TLObject )else self .invoice ,
        'provider_id':self .provider_id ,
        'url':self .url ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'can_save_credentials':self .can_save_credentials ,
        'password_missing':self .password_missing ,
        'photo':self .photo .to_dict ()if isinstance (self .photo ,TLObject )else self .photo ,
        'native_provider':self .native_provider ,
        'native_params':self .native_params .to_dict ()if isinstance (self .native_params ,TLObject )else self .native_params ,
        'additional_methods':[]if self .additional_methods is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .additional_methods ],
        'saved_info':self .saved_info .to_dict ()if isinstance (self .saved_info ,TLObject )else self .saved_info ,
        'saved_credentials':[]if self .saved_credentials is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .saved_credentials ]
        }

    def _bytes (self ):
        assert ((self .native_provider or self .native_provider is not None )and (self .native_params or self .native_params is not None ))or ((self .native_provider is None or self .native_provider is False )and (self .native_params is None or self .native_params is False )),'native_provider, native_params parameters must all be False-y (like None) or all me True-y'
        return b''.join ((
        b'Q\x87\x05\xa0',
        struct .pack ('<I',(0 if self .can_save_credentials is None or self .can_save_credentials is False else 4 )|(0 if self .password_missing is None or self .password_missing is False else 8 )|(0 if self .photo is None or self .photo is False else 32 )|(0 if self .native_provider is None or self .native_provider is False else 16 )|(0 if self .native_params is None or self .native_params is False else 16 )|(0 if self .additional_methods is None or self .additional_methods is False else 64 )|(0 if self .saved_info is None or self .saved_info is False else 1 )|(0 if self .saved_credentials is None or self .saved_credentials is False else 2 )),
        struct .pack ('<q',self .form_id ),
        struct .pack ('<q',self .bot_id ),
        self .serialize_bytes (self .title ),
        self .serialize_bytes (self .description ),
        b''if self .photo is None or self .photo is False else (self .photo ._bytes ()),
        self .invoice ._bytes (),
        struct .pack ('<q',self .provider_id ),
        self .serialize_bytes (self .url ),
        b''if self .native_provider is None or self .native_provider is False else (self .serialize_bytes (self .native_provider )),
        b''if self .native_params is None or self .native_params is False else (self .native_params ._bytes ()),
        b''if self .additional_methods is None or self .additional_methods is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .additional_methods )),b''.join (x ._bytes ()for x in self .additional_methods ))),
        b''if self .saved_info is None or self .saved_info is False else (self .saved_info ._bytes ()),
        b''if self .saved_credentials is None or self .saved_credentials is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .saved_credentials )),b''.join (x ._bytes ()for x in self .saved_credentials ))),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _can_save_credentials =bool (flags &4 )
        _password_missing =bool (flags &8 )
        _form_id =reader .read_long ()
        _bot_id =reader .read_long ()
        _title =reader .tgread_string ()
        _description =reader .tgread_string ()
        if flags &32 :
            _photo =reader .tgread_object ()
        else :
            _photo =None 
        _invoice =reader .tgread_object ()
        _provider_id =reader .read_long ()
        _url =reader .tgread_string ()
        if flags &16 :
            _native_provider =reader .tgread_string ()
        else :
            _native_provider =None 
        if flags &16 :
            _native_params =reader .tgread_object ()
        else :
            _native_params =None 
        if flags &64 :
            reader .read_int ()
            _additional_methods =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _additional_methods .append (_x )

        else :
            _additional_methods =None 
        if flags &1 :
            _saved_info =reader .tgread_object ()
        else :
            _saved_info =None 
        if flags &2 :
            reader .read_int ()
            _saved_credentials =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _saved_credentials .append (_x )

        else :
            _saved_credentials =None 
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (form_id =_form_id ,bot_id =_bot_id ,title =_title ,description =_description ,invoice =_invoice ,provider_id =_provider_id ,url =_url ,users =_users ,can_save_credentials =_can_save_credentials ,password_missing =_password_missing ,photo =_photo ,native_provider =_native_provider ,native_params =_native_params ,additional_methods =_additional_methods ,saved_info =_saved_info ,saved_credentials =_saved_credentials )

class PaymentReceipt (TLObject ):
    CONSTRUCTOR_ID =0x70c4fe03 
    SUBCLASS_OF_ID =0x590093c9 

    def __init__ (self ,date :Optional [datetime ],bot_id :int ,provider_id :int ,title :str ,description :str ,invoice :'TypeInvoice',currency :str ,total_amount :int ,credentials_title :str ,users :List ['TypeUser'],photo :Optional ['TypeWebDocument']=None ,info :Optional ['TypePaymentRequestedInfo']=None ,shipping :Optional ['TypeShippingOption']=None ,tip_amount :Optional [int ]=None ):
        """"""
        self .date =date 
        self .bot_id =bot_id 
        self .provider_id =provider_id 
        self .title =title 
        self .description =description 
        self .invoice =invoice 
        self .currency =currency 
        self .total_amount =total_amount 
        self .credentials_title =credentials_title 
        self .users =users 
        self .photo =photo 
        self .info =info 
        self .shipping =shipping 
        self .tip_amount =tip_amount 

    def to_dict (self ):
        return {
        '_':'PaymentReceipt',
        'date':self .date ,
        'bot_id':self .bot_id ,
        'provider_id':self .provider_id ,
        'title':self .title ,
        'description':self .description ,
        'invoice':self .invoice .to_dict ()if isinstance (self .invoice ,TLObject )else self .invoice ,
        'currency':self .currency ,
        'total_amount':self .total_amount ,
        'credentials_title':self .credentials_title ,
        'users':[]if self .users is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .users ],
        'photo':self .photo .to_dict ()if isinstance (self .photo ,TLObject )else self .photo ,
        'info':self .info .to_dict ()if isinstance (self .info ,TLObject )else self .info ,
        'shipping':self .shipping .to_dict ()if isinstance (self .shipping ,TLObject )else self .shipping ,
        'tip_amount':self .tip_amount 
        }

    def _bytes (self ):
        return b''.join ((
        b'\x03\xfe\xc4p',
        struct .pack ('<I',(0 if self .photo is None or self .photo is False else 4 )|(0 if self .info is None or self .info is False else 1 )|(0 if self .shipping is None or self .shipping is False else 2 )|(0 if self .tip_amount is None or self .tip_amount is False else 8 )),
        self .serialize_datetime (self .date ),
        struct .pack ('<q',self .bot_id ),
        struct .pack ('<q',self .provider_id ),
        self .serialize_bytes (self .title ),
        self .serialize_bytes (self .description ),
        b''if self .photo is None or self .photo is False else (self .photo ._bytes ()),
        self .invoice ._bytes (),
        b''if self .info is None or self .info is False else (self .info ._bytes ()),
        b''if self .shipping is None or self .shipping is False else (self .shipping ._bytes ()),
        b''if self .tip_amount is None or self .tip_amount is False else (struct .pack ('<q',self .tip_amount )),
        self .serialize_bytes (self .currency ),
        struct .pack ('<q',self .total_amount ),
        self .serialize_bytes (self .credentials_title ),
        b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .users )),b''.join (x ._bytes ()for x in self .users ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _date =reader .tgread_date ()
        _bot_id =reader .read_long ()
        _provider_id =reader .read_long ()
        _title =reader .tgread_string ()
        _description =reader .tgread_string ()
        if flags &4 :
            _photo =reader .tgread_object ()
        else :
            _photo =None 
        _invoice =reader .tgread_object ()
        if flags &1 :
            _info =reader .tgread_object ()
        else :
            _info =None 
        if flags &2 :
            _shipping =reader .tgread_object ()
        else :
            _shipping =None 
        if flags &8 :
            _tip_amount =reader .read_long ()
        else :
            _tip_amount =None 
        _currency =reader .tgread_string ()
        _total_amount =reader .read_long ()
        _credentials_title =reader .tgread_string ()
        reader .read_int ()
        _users =[]
        for _ in range (reader .read_int ()):
            _x =reader .tgread_object ()
            _users .append (_x )

        return cls (date =_date ,bot_id =_bot_id ,provider_id =_provider_id ,title =_title ,description =_description ,invoice =_invoice ,currency =_currency ,total_amount =_total_amount ,credentials_title =_credentials_title ,users =_users ,photo =_photo ,info =_info ,shipping =_shipping ,tip_amount =_tip_amount )

class PaymentResult (TLObject ):
    CONSTRUCTOR_ID =0x4e5f810d 
    SUBCLASS_OF_ID =0x8ae16a9d 

    def __init__ (self ,updates :'TypeUpdates'):
        """"""
        self .updates =updates 

    def to_dict (self ):
        return {
        '_':'PaymentResult',
        'updates':self .updates .to_dict ()if isinstance (self .updates ,TLObject )else self .updates 
        }

    def _bytes (self ):
        return b''.join ((
        b'\r\x81_N',
        self .updates ._bytes (),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _updates =reader .tgread_object ()
        return cls (updates =_updates )

class PaymentVerificationNeeded (TLObject ):
    CONSTRUCTOR_ID =0xd8411139 
    SUBCLASS_OF_ID =0x8ae16a9d 

    def __init__ (self ,url :str ):
        """"""
        self .url =url 

    def to_dict (self ):
        return {
        '_':'PaymentVerificationNeeded',
        'url':self .url 
        }

    def _bytes (self ):
        return b''.join ((
        b'9\x11A\xd8',
        self .serialize_bytes (self .url ),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        _url =reader .tgread_string ()
        return cls (url =_url )

class SavedInfo (TLObject ):
    CONSTRUCTOR_ID =0xfb8fe43c 
    SUBCLASS_OF_ID =0xad3cf146 

    def __init__ (self ,has_saved_credentials :Optional [bool ]=None ,saved_info :Optional ['TypePaymentRequestedInfo']=None ):
        """"""
        self .has_saved_credentials =has_saved_credentials 
        self .saved_info =saved_info 

    def to_dict (self ):
        return {
        '_':'SavedInfo',
        'has_saved_credentials':self .has_saved_credentials ,
        'saved_info':self .saved_info .to_dict ()if isinstance (self .saved_info ,TLObject )else self .saved_info 
        }

    def _bytes (self ):
        return b''.join ((
        b'<\xe4\x8f\xfb',
        struct .pack ('<I',(0 if self .has_saved_credentials is None or self .has_saved_credentials is False else 2 )|(0 if self .saved_info is None or self .saved_info is False else 1 )),
        b''if self .saved_info is None or self .saved_info is False else (self .saved_info ._bytes ()),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        _has_saved_credentials =bool (flags &2 )
        if flags &1 :
            _saved_info =reader .tgread_object ()
        else :
            _saved_info =None 
        return cls (has_saved_credentials =_has_saved_credentials ,saved_info =_saved_info )

class ValidatedRequestedInfo (TLObject ):
    CONSTRUCTOR_ID =0xd1451883 
    SUBCLASS_OF_ID =0x8f8044b7 

    def __init__ (self ,id :Optional [str ]=None ,shipping_options :Optional [List ['TypeShippingOption']]=None ):
        """"""
        self .id =id 
        self .shipping_options =shipping_options 

    def to_dict (self ):
        return {
        '_':'ValidatedRequestedInfo',
        'id':self .id ,
        'shipping_options':[]if self .shipping_options is None else [x .to_dict ()if isinstance (x ,TLObject )else x for x in self .shipping_options ]
        }

    def _bytes (self ):
        return b''.join ((
        b'\x83\x18E\xd1',
        struct .pack ('<I',(0 if self .id is None or self .id is False else 1 )|(0 if self .shipping_options is None or self .shipping_options is False else 2 )),
        b''if self .id is None or self .id is False else (self .serialize_bytes (self .id )),
        b''if self .shipping_options is None or self .shipping_options is False else b''.join ((b'\x15\xc4\xb5\x1c',struct .pack ('<i',len (self .shipping_options )),b''.join (x ._bytes ()for x in self .shipping_options ))),
        ))

    @classmethod 
    def from_reader (cls ,reader ):
        flags =reader .read_int ()

        if flags &1 :
            _id =reader .tgread_string ()
        else :
            _id =None 
        if flags &2 :
            reader .read_int ()
            _shipping_options =[]
            for _ in range (reader .read_int ()):
                _x =reader .tgread_object ()
                _shipping_options .append (_x )

        else :
            _shipping_options =None 
        return cls (id =_id ,shipping_options =_shipping_options )

