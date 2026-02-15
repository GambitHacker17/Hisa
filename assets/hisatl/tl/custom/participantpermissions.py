from ..import types 

def _admin_prop (field_name ,doc ):
    """"""
    def fget (self ):
        if not self .is_admin :
            return False 
        if self .is_chat :
            return True 

        return getattr (self .participant .admin_rights ,field_name )

    return {'fget':fget ,'doc':doc }

class ParticipantPermissions :
    """"""
    def __init__ (self ,participant ,chat :bool ):
        self .participant =participant 
        self .is_chat =chat 

    @property 
    def is_admin (self ):
        """"""
        return self .is_creator or isinstance (self .participant ,(
        types .ChannelParticipantAdmin ,
        types .ChatParticipantAdmin 
        ))

    @property 
    def is_creator (self ):
        """"""
        return isinstance (self .participant ,(
        types .ChannelParticipantCreator ,
        types .ChatParticipantCreator 
        ))

    @property 
    def has_default_permissions (self ):
        """"""
        return isinstance (self .participant ,(
        types .ChannelParticipant ,
        types .ChatParticipant ,
        types .ChannelParticipantSelf 
        ))

    @property 
    def is_banned (self ):
        """"""
        return isinstance (self .participant ,types .ChannelParticipantBanned )

    @property 
    def has_left (self ):
        """"""
        return isinstance (self .participant ,types .ChannelParticipantLeft )

    @property 
    def add_admins (self ):
        """"""
        if not self .is_admin :
            return False 

        if self .is_chat :
            return self .is_creator 

        return self .participant .admin_rights .add_admins 

    ban_users =property (**_admin_prop ('ban_users',""""""))

    pin_messages =property (**_admin_prop ('pin_messages',""""""))

    invite_users =property (**_admin_prop ('invite_users',""""""))

    delete_messages =property (**_admin_prop ('delete_messages',""""""))

    edit_messages =property (**_admin_prop ('edit_messages',""""""))

    post_messages =property (**_admin_prop ('post_messages',""""""))

    change_info =property (**_admin_prop ('change_info',""""""))

    anonymous =property (**_admin_prop ('anonymous',""""""))

    manage_call =property (**_admin_prop ('manage_call',""""""))

    manage_topics =property (**_admin_prop ('manage_topics',""""""))
