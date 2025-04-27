
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class TranslateText (TLObject ):
    """"""

    __slots__ :List [str ]=["to_lang","peer","id","text"]

    ID =0x63183030 
    QUALNAME ="functions.messages.TranslateText"

    def __init__ (self ,*,to_lang :str ,peer :"raw.base.InputPeer"=None ,id :Optional [List [int ]]=None ,text :Optional [List ["raw.base.TextWithEntities"]]=None )->None :
        self .to_lang =to_lang 
        self .peer =peer 
        self .id =id 
        self .text =text 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"TranslateText":

        flags =Int .read (b )

        peer =TLObject .read (b )if flags &(1 <<0 )else None 

        id =TLObject .read (b ,Int )if flags &(1 <<0 )else []

        text =TLObject .read (b )if flags &(1 <<1 )else []

        to_lang =String .read (b )

        return TranslateText (to_lang =to_lang ,peer =peer ,id =id ,text =text )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<0 )if self .peer is not None else 0 
        flags |=(1 <<0 )if self .id else 0 
        flags |=(1 <<1 )if self .text else 0 
        b .write (Int (flags ))

        if self .peer is not None :
            b .write (self .peer .write ())

        if self .id is not None :
            b .write (Vector (self .id ,Int ))

        if self .text is not None :
            b .write (Vector (self .text ))

        b .write (String (self .to_lang ))

        return b .getvalue ()
