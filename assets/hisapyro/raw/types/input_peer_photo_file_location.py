
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class InputPeerPhotoFileLocation (TLObject ):
    """"""

    __slots__ :List [str ]=["peer","photo_id","big"]

    ID =0x37257e99 
    QUALNAME ="types.InputPeerPhotoFileLocation"

    def __init__ (self ,*,peer :"raw.base.InputPeer",photo_id :int ,big :Optional [bool ]=None )->None :
        self .peer =peer 
        self .photo_id =photo_id 
        self .big =big 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"InputPeerPhotoFileLocation":

        flags =Int .read (b )

        big =True if flags &(1 <<0 )else False 
        peer =TLObject .read (b )

        photo_id =Long .read (b )

        return InputPeerPhotoFileLocation (peer =peer ,photo_id =photo_id ,big =big )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .big else 0 
        b .write (Int (flags ))

        b .write (self .peer .write ())

        b .write (Long (self .photo_id ))

        return b .getvalue ()
