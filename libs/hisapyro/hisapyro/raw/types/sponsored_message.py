
from io import BytesIO 

from hisapyro .raw .core .primitives import Int ,Long ,Int128 ,Int256 ,Bool ,Bytes ,String ,Double ,Vector 
from hisapyro .raw .core import TLObject 
from hisapyro import raw 
from typing import List ,Optional ,Any 

class SponsoredMessage (TLObject ):
    """"""

    __slots__ :List [str ]=["random_id","message","recommended","show_peer_photo","from_id","chat_invite","chat_invite_hash","channel_post","start_param","entities","sponsor_info","additional_info"]

    ID =0xfc25b828 
    QUALNAME ="types.SponsoredMessage"

    def __init__ (self ,*,random_id :bytes ,message :str ,recommended :Optional [bool ]=None ,show_peer_photo :Optional [bool ]=None ,from_id :"raw.base.Peer"=None ,chat_invite :"raw.base.ChatInvite"=None ,chat_invite_hash :Optional [str ]=None ,channel_post :Optional [int ]=None ,start_param :Optional [str ]=None ,entities :Optional [List ["raw.base.MessageEntity"]]=None ,sponsor_info :Optional [str ]=None ,additional_info :Optional [str ]=None )->None :
        self .random_id =random_id 
        self .message =message 
        self .recommended =recommended 
        self .show_peer_photo =show_peer_photo 
        self .from_id =from_id 
        self .chat_invite =chat_invite 
        self .chat_invite_hash =chat_invite_hash 
        self .channel_post =channel_post 
        self .start_param =start_param 
        self .entities =entities 
        self .sponsor_info =sponsor_info 
        self .additional_info =additional_info 

    @staticmethod 
    def read (b :BytesIO ,*args :Any )->"SponsoredMessage":

        flags =Int .read (b )

        recommended =True if flags &(1 <<5 )else False 
        show_peer_photo =True if flags &(1 <<6 )else False 
        random_id =Bytes .read (b )

        from_id =TLObject .read (b )if flags &(1 <<3 )else None 

        chat_invite =TLObject .read (b )if flags &(1 <<4 )else None 

        chat_invite_hash =String .read (b )if flags &(1 <<4 )else None 
        channel_post =Int .read (b )if flags &(1 <<2 )else None 
        start_param =String .read (b )if flags &(1 <<0 )else None 
        message =String .read (b )

        entities =TLObject .read (b )if flags &(1 <<1 )else []

        sponsor_info =String .read (b )if flags &(1 <<7 )else None 
        additional_info =String .read (b )if flags &(1 <<8 )else None 
        return SponsoredMessage (random_id =random_id ,message =message ,recommended =recommended ,show_peer_photo =show_peer_photo ,from_id =from_id ,chat_invite =chat_invite ,chat_invite_hash =chat_invite_hash ,channel_post =channel_post ,start_param =start_param ,entities =entities ,sponsor_info =sponsor_info ,additional_info =additional_info )

    def write (self ,*args )->bytes :
        b =BytesIO ()
        b .write (Int (self .ID ,False ))

        flags =0 
        flags |=(1 <<5 )if self .recommended else 0 
        flags |=(1 <<6 )if self .show_peer_photo else 0 
        flags |=(1 <<3 )if self .from_id is not None else 0 
        flags |=(1 <<4 )if self .chat_invite is not None else 0 
        flags |=(1 <<4 )if self .chat_invite_hash is not None else 0 
        flags |=(1 <<2 )if self .channel_post is not None else 0 
        flags |=(1 <<0 )if self .start_param is not None else 0 
        flags |=(1 <<1 )if self .entities else 0 
        flags |=(1 <<7 )if self .sponsor_info is not None else 0 
        flags |=(1 <<8 )if self .additional_info is not None else 0 
        b .write (Int (flags ))

        b .write (Bytes (self .random_id ))

        if self .from_id is not None :
            b .write (self .from_id .write ())

        if self .chat_invite is not None :
            b .write (self .chat_invite .write ())

        if self .chat_invite_hash is not None :
            b .write (String (self .chat_invite_hash ))

        if self .channel_post is not None :
            b .write (Int (self .channel_post ))

        if self .start_param is not None :
            b .write (String (self .start_param ))

        b .write (String (self .message ))

        if self .entities is not None :
            b .write (Vector (self .entities ))

        if self .sponsor_info is not None :
            b .write (String (self .sponsor_info ))

        if self .additional_info is not None :
            b .write (String (self .additional_info ))

        return b .getvalue ()
