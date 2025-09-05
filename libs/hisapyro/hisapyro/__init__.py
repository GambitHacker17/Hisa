
__version__ ="1.0.0"
__license__ ="GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ ="Copyright (C) 2025 MartyyyK"

from concurrent .futures .thread import ThreadPoolExecutor 

class StopTransmission (Exception ):
    pass 

class StopPropagation (StopAsyncIteration ):
    pass 

class ContinuePropagation (StopAsyncIteration ):
    pass 

from .import raw ,types ,filters ,handlers ,emoji ,enums 
from .client import Client 
from .sync import idle ,compose 

crypto_executor =ThreadPoolExecutor (1 ,thread_name_prefix ="CryptoWorker")
