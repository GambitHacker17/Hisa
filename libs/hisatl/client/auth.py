import getpass 
import inspect 
import os 
import sys 
import typing 
import warnings 

from ..import utils ,helpers ,errors ,password as pwd_mod 
from ..tl import types ,functions ,custom 
from .._updates import SessionState 

if typing .TYPE_CHECKING :
    from .telegramclient import TelegramClient 

class AuthMethods :

    def start (
    self :'TelegramClient',
    phone :typing .Callable [[],str ]=lambda :input ('Please enter your phone (or bot token): '),
    password :typing .Callable [[],str ]=lambda :getpass .getpass ('Please enter your password: '),
    *,
    bot_token :str =None ,
    force_sms :bool =False ,
    code_callback :typing .Callable [[],typing .Union [str ,int ]]=None ,
    first_name :str ='New User',
    last_name :str ='',
    max_attempts :int =3 )->'TelegramClient':
        """"""
        if code_callback is None :
            def code_callback ():
                return input ('Please enter the code you received: ')
        elif not callable (code_callback ):
            raise ValueError (
            'The code_callback parameter needs to be a callable '
            'function that returns the code you received by Telegram.'
            )

        if not phone and not bot_token :
            raise ValueError ('No phone number or bot token provided.')

        if phone and bot_token and not callable (phone ):
            raise ValueError ('Both a phone and a bot token provided, '
            'must only provide one of either')

        coro =self ._start (
        phone =phone ,
        password =password ,
        bot_token =bot_token ,
        force_sms =force_sms ,
        code_callback =code_callback ,
        first_name =first_name ,
        last_name =last_name ,
        max_attempts =max_attempts 
        )
        return (
        coro if self .loop .is_running ()
        else self .loop .run_until_complete (coro )
        )

    async def _start (
    self :'TelegramClient',phone ,password ,bot_token ,force_sms ,
    code_callback ,first_name ,last_name ,max_attempts ):
        if not self .is_connected ():
            await self .connect ()

        me =await self .get_me ()
        if me is not None :

            if bot_token :

                if bot_token [:bot_token .find (':')]!=str (me .id ):
                    warnings .warn (
                    'the session already had an authorized user so it did '
                    'not login to the bot account using the provided '
                    'bot_token (it may not be using the user you expect)'
                    )
            elif phone and not callable (phone )and utils .parse_phone (phone )!=me .phone :
                warnings .warn (
                'the session already had an authorized user so it did '
                'not login to the user account using the provided '
                'phone (it may not be using the user you expect)'
                )

            return self 

        if not bot_token :

            while callable (phone ):
                value =phone ()
                if inspect .isawaitable (value ):
                    value =await value 

                if ':'in value :

                    bot_token =value 
                    break 

                phone =utils .parse_phone (value )or phone 

        if bot_token :
            await self .sign_in (bot_token =bot_token )
            return self 

        me =None 
        attempts =0 
        two_step_detected =False 

        await self .send_code_request (phone ,force_sms =force_sms )
        while attempts <max_attempts :
            try :
                value =code_callback ()
                if inspect .isawaitable (value ):
                    value =await value 

                if not value :
                    raise errors .PhoneCodeEmptyError (request =None )

                me =await self .sign_in (phone ,code =value )
                break 
            except errors .SessionPasswordNeededError :
                two_step_detected =True 
                break 
            except (errors .PhoneCodeEmptyError ,
            errors .PhoneCodeExpiredError ,
            errors .PhoneCodeHashEmptyError ,
            errors .PhoneCodeInvalidError ):
                print ('Invalid code. Please try again.',file =sys .stderr )

            attempts +=1 
        else :
            raise RuntimeError (
            '{} consecutive sign-in attempts failed. Aborting'
            .format (max_attempts )
            )

        if two_step_detected :
            if not password :
                raise ValueError (
                "Two-step verification is enabled for this account. "
                "Please provide the 'password' argument to 'start()'."
                )

            if callable (password ):
                for _ in range (max_attempts ):
                    try :
                        value =password ()
                        if inspect .isawaitable (value ):
                            value =await value 

                        me =await self .sign_in (phone =phone ,password =value )
                        break 
                    except errors .PasswordHashInvalidError :
                        print ('Invalid password. Please try again',
                        file =sys .stderr )
                else :
                    raise errors .PasswordHashInvalidError (request =None )
            else :
                me =await self .sign_in (phone =phone ,password =password )

        signed ,name ='Signed in successfully as ',utils .get_display_name (me )
        tos ='; remember to not break the ToS or you will risk an account ban!'
        try :
            print (signed ,name ,tos ,sep ='')
        except UnicodeEncodeError :

            print (signed ,name .encode ('utf-8',errors ='ignore')
            .decode ('ascii',errors ='ignore'),tos ,sep ='')

        return self 

    def _parse_phone_and_hash (self ,phone ,phone_hash ):
        """"""
        phone =utils .parse_phone (phone )or self ._phone 
        if not phone :
            raise ValueError (
            'Please make sure to call send_code_request first.'
            )

        phone_hash =phone_hash or self ._phone_code_hash .get (phone ,None )
        if not phone_hash :
            raise ValueError ('You also need to provide a phone_code_hash.')

        return phone ,phone_hash 

    async def sign_in (
    self :'TelegramClient',
    phone :str =None ,
    code :typing .Union [str ,int ]=None ,
    *,
    password :str =None ,
    bot_token :str =None ,
    phone_code_hash :str =None ,
    email_code :str =None )->'typing.Union[types.User, types.auth.SentCode]':
        """"""
        me =await self .get_me ()
        if me :
            return me 

        if phone and not code and not password and not email_code :
            return await self .send_code_request (phone )
        elif code or email_code :
            phone ,phone_code_hash =self ._parse_phone_and_hash (phone ,phone_code_hash )

            request =functions .auth .SignInRequest (
            phone_number =phone ,
            phone_code_hash =phone_code_hash ,
            phone_code =str (code ),
            email_verification =(
            types .EmailVerificationCode (email_code )if email_code else None 
            ),
            )
        elif password :
            pwd =await self (functions .account .GetPasswordRequest ())
            request =functions .auth .CheckPasswordRequest (
            pwd_mod .compute_check (pwd ,password )
            )
        elif bot_token :
            request =functions .auth .ImportBotAuthorizationRequest (
            flags =0 ,bot_auth_token =bot_token ,
            api_id =self .api_id ,api_hash =self .api_hash 
            )
        else :
            raise ValueError (
            'You must provide a phone and a code the first time, '
            'and a password only if an RPCError was raised before.'
            )

        result =await self (request )
        if isinstance (result ,types .auth .AuthorizationSignUpRequired ):

            self ._tos =result .terms_of_service 
            raise errors .PhoneNumberUnoccupiedError (request =request )

        return await self ._on_login (result .user )

    async def send_email_code (
    self :"TelegramClient",
    email :str ,
    purpose :str ,
    )->"types.account.SentEmailCode":
        """"""
        if purpose =="setup":
            purpose =types .EmailVerifyPurposeLoginSetup ()
        elif purpose =="login_change":
            purpose =types .EmailVerifyPurposeLoginChange ()
        elif purpose =="passport":
            purpose =types .EmailVerifyPurposePassport ()
        else :
            raise ValueError (
            "`purpose` must be either 'setup', 'login_change' or 'passport'"
            )

        return await self (functions .account .SendVerifyEmailCodeRequest (purpose ,email ))

    async def verify_email (
    self :"TelegramClient",
    purpose :str ,
    code :str ,
    ):
        """"""
        if purpose =="setup":
            purpose =types .EmailVerifyPurposeLoginSetup ()
        elif purpose =="login_change":
            purpose =types .EmailVerifyPurposeLoginChange ()
        elif purpose =="passport":
            purpose =types .EmailVerifyPurposePassport ()
        else :
            raise ValueError (
            "`purpose` must be either 'setup', 'login_change' or 'passport'"
            )

        return await self (
        functions .account .VerifyEmailRequest (
        purpose ,
        types .EmailVerificationCode (code ),
        )
        )

    async def sign_up (
    self :'TelegramClient',
    code :typing .Union [str ,int ],
    first_name :str ,
    last_name :str ='',
    *,
    phone :str =None ,
    phone_code_hash :str =None )->'types.User':
        """"""
        raise ValueError ('Third-party applications cannot sign up for Telegram')

    async def _on_login (self ,user ):
        """"""
        self ._bot =bool (user .bot )
        self ._self_input_peer =utils .get_input_peer (user ,allow_self =False )
        self ._authorized =True 

        state =await self (functions .updates .GetStateRequest ())
        self ._message_box .load (SessionState (0 ,0 ,0 ,state .pts ,state .qts ,int (state .date .timestamp ()),state .seq ,0 ),[])

        return user 

    async def send_code_request (
    self :'TelegramClient',
    phone :str ,
    *,
    force_sms :bool =False ,
    _retry_count :int =0 )->'types.auth.SentCode':
        """"""
        if force_sms :
            warnings .warn ('force_sms has been deprecated and no longer works')
            force_sms =False 

        result =None 
        phone =utils .parse_phone (phone )or self ._phone 
        phone_hash =self ._phone_code_hash .get (phone )

        if not phone_hash :
            try :
                result =await self (functions .auth .SendCodeRequest (
                phone ,self .api_id ,self .api_hash ,types .CodeSettings ()))
            except errors .AuthRestartError :
                if _retry_count >2 :
                    raise 
                return await self .send_code_request (
                phone ,force_sms =force_sms ,_retry_count =_retry_count +1 )

            if isinstance (result ,types .auth .SentCodeSuccess ):
                raise RuntimeError ('logged in right after sending the code')

            if isinstance (result .type ,types .auth .SentCodeTypeSms ):
                force_sms =False 

            if result .phone_code_hash :
                self ._phone_code_hash [phone ]=phone_hash =result .phone_code_hash 
        else :
            force_sms =True 

        self ._phone =phone 

        if force_sms :
            try :
                result =await self (
                functions .auth .ResendCodeRequest (phone ,phone_hash ))
            except errors .PhoneCodeExpiredError :
                if _retry_count >2 :
                    raise 
                self ._phone_code_hash .pop (phone ,None )
                self ._log [__name__ ].info (
                "Phone code expired in ResendCodeRequest, requesting a new code"
                )
                return await self .send_code_request (
                phone ,force_sms =False ,_retry_count =_retry_count +1 )

            if isinstance (result ,types .auth .SentCodeSuccess ):
                raise RuntimeError ('logged in right after resending the code')

            self ._phone_code_hash [phone ]=result .phone_code_hash 

        return result 

    async def qr_login (self :'TelegramClient',ignored_ids :typing .List [int ]=None )->custom .QRLogin :
        """"""
        qr_login =custom .QRLogin (self ,ignored_ids or [])
        await qr_login .recreate ()
        return qr_login 

    async def log_out (self :'TelegramClient')->bool :
        """"""
        try :
            await self (functions .auth .LogOutRequest ())
        except errors .RPCError :
            return False 

        self ._bot =None 
        self ._self_input_peer =None 
        self ._authorized =False 

        await self .disconnect ()
        self .session .delete ()
        self .session =None 
        return True 

    async def edit_2fa (
    self :'TelegramClient',
    current_password :str =None ,
    new_password :str =None ,
    *,
    hint :str ='',
    email :str =None ,
    email_code_callback :typing .Callable [[int ],str ]=None )->bool :
        """"""
        if new_password is None and current_password is None :
            return False 

        if email and not callable (email_code_callback ):
            raise ValueError ('email present without email_code_callback')

        pwd =await self (functions .account .GetPasswordRequest ())
        pwd .new_algo .salt1 +=os .urandom (32 )
        assert isinstance (pwd ,types .account .Password )
        if not pwd .has_password and current_password :
            current_password =None 

        if current_password :
            password =pwd_mod .compute_check (pwd ,current_password )
        else :
            password =types .InputCheckPasswordEmpty ()

        if new_password :
            new_password_hash =pwd_mod .compute_digest (
            pwd .new_algo ,new_password )
        else :
            new_password_hash =b''

        try :
            await self (functions .account .UpdatePasswordSettingsRequest (
            password =password ,
            new_settings =types .account .PasswordInputSettings (
            new_algo =pwd .new_algo ,
            new_password_hash =new_password_hash ,
            hint =hint ,
            email =email ,
            new_secure_settings =None 
            )
            ))
        except errors .EmailUnconfirmedError as e :
            code =email_code_callback (e .code_length )
            if inspect .isawaitable (code ):
                code =await code 

            code =str (code )
            await self (functions .account .ConfirmPasswordEmailRequest (code ))

        return True 

    async def __aenter__ (self ):
        return await self .start ()

    async def __aexit__ (self ,*args ):
        await self .disconnect ()

    __enter__ =helpers ._sync_enter 
    __exit__ =helpers ._sync_exit 

