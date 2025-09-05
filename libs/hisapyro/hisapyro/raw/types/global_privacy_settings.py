
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class GlobalPrivacySettings (TLObject ):
    """"""

    __slots__ :List [str ]=["archive_and_mute_new_noncontact_peers"]

    ID =0xbea2f424 
    QUALNAME ="types.GlobalPrivacySettings"

    def __init__ (self ,*,archive_and_mute_new_noncontact_peers :Optional [bool ]=None )->None :
        self .archive_and_mute_new_noncontact_peers =archive_and_mute_new_noncontact_peers 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"GlobalPrivacySettings":

        flags =Int .read (b )

        archive_and_mute_new_noncontact_peers =Bool .read (b )if flags &(1 <<0 )else None 
        return GlobalPrivacySettings (archive_and_mute_new_noncontact_peers =archive_and_mute_new_noncontact_peers )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .archive_and_mute_new_noncontact_peers is not None else 0 
        b .write (Int (flags ))

        if self .archive_and_mute_new_noncontact_peers is not None :
            b .write (Bool (self .archive_and_mute_new_noncontact_peers ))

        return b .getvalue ()
