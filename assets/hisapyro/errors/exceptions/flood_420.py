
from ..rpc_error import RPCError 

class Flood (RPCError ):
    """"""
    CODE =420 
    """"""
    NAME =__doc__ 

class TwoFaConfirmWait (Flood ):
    """"""
    ID ="2FA_CONFIRM_WAIT_X"
    """"""
    MESSAGE =__doc__ 

class FloodTestPhoneWait (Flood ):
    """"""
    ID ="FLOOD_TEST_PHONE_WAIT_X"
    """"""
    MESSAGE =__doc__ 

class FloodWait (Flood ):
    """"""
    ID ="FLOOD_WAIT_X"
    """"""
    MESSAGE =__doc__ 

class SlowmodeWait (Flood ):
    """"""
    ID ="SLOWMODE_WAIT_X"
    """"""
    MESSAGE =__doc__ 

class TakeoutInitDelay (Flood ):
    """"""
    ID ="TAKEOUT_INIT_DELAY_X"
    """"""
    MESSAGE =__doc__ 

