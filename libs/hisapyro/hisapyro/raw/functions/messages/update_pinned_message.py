
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class UpdatePinnedMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","id","silent","unpin","pm_oneside"]

    ID =0xd2aaf7ec 
    QUALNAME ="functions.messages.UpdatePinnedMessage"

    def __init__ (self ,*,peer :"raw.base.InputPeer",id :int ,silent :Optional [bool ]=None ,unpin :Optional [bool ]=None ,pm_oneside :Optional [bool ]=None )->None :
        self .peer =peer 
        self .id =id 
        self .silent =silent 
        self .unpin =unpin 
        self .pm_oneside =pm_oneside 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"UpdatePinnedMessage":

        flags =Int .read (b )

        silent =True if flags &(1 <<0 )else False 
        unpin =True if flags &(1 <<1 )else False 
        pm_oneside =True if flags &(1 <<2 )else False 
        peer =TLObject .read (b )

        id =Int .read (b )

        return UpdatePinnedMessage (peer =peer ,id =id ,silent =silent ,unpin =unpin ,pm_oneside =pm_oneside )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .silent else 0 
        flags |=(1 <<1 )if self .unpin else 0 
        flags |=(1 <<2 )if self .pm_oneside else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Int (self .id ))

        return b .getvalue ()
