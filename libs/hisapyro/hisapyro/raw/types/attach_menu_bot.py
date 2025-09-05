
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class AttachMenuBot (TLObject ):
    """"""

    __slots__ :List [str ]=["bot_id","short_name","peer_types","icons","inactive","has_settings","request_write_access"]

    ID =0xc8aa2cd2 
    QUALNAME ="types.AttachMenuBot"

    def __init__ (self ,*,bot_id :int ,short_name :str ,peer_types :List ["raw.base.AttachMenuPeerType"],icons :List ["raw.base.AttachMenuBotIcon"],inactive :Optional [bool ]=None ,has_settings :Optional [bool ]=None ,request_write_access :Optional [bool ]=None )->None :
        self .bot_id =bot_id 
        self .short_name =short_name 
        self .peer_types =peer_types 
        self .icons =icons 
        self .inactive =inactive 
        self .has_settings =has_settings 
        self .request_write_access =request_write_access 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"AttachMenuBot":

        flags =Int .read (b )

        inactive =True if flags &(1 <<0 )else False 
        has_settings =True if flags &(1 <<1 )else False 
        request_write_access =True if flags &(1 <<2 )else False 
        bot_id =Long .read (b )

        short_name =String .read (b )

        peer_types =TLObject .read (b )

        icons =TLObject .read (b )

        return AttachMenuBot (bot_id =bot_id ,short_name =short_name ,peer_types =peer_types ,icons =icons ,inactive =inactive ,has_settings =has_settings ,request_write_access =request_write_access )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .inactive else 0 
        flags |=(1 <<1 )if self .has_settings else 0 
        flags |=(1 <<2 )if self .request_write_access else 0 
        b .write (Int (flags ))

        b .write (Long (self .bot_id ))

        b .write (String (self .short_name ))

        b .write (Vector (self .peer_types ))

        b .write (Vector (self .icons ))

        return b .getvalue ()
