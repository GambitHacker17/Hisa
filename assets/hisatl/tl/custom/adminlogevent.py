from ...tl import types 
from ...utils import get_input_peer 

class AdminLogEvent :
    """"""
    def __init__ (self ,original ,entities ):
        self .original =original 
        self .entities =entities 
        self .user =entities [original .user_id ]
        self .input_user =get_input_peer (self .user )

    @property 
    def id (self ):
        """"""
        return self .original .id 

    @property 
    def date (self ):
        """"""
        return self .original .date 

    @property 
    def user_id (self ):
        """"""
        return self .original .user_id 

    @property 
    def action (self ):
        """"""
        return self .original .action 

    @property 
    def old (self ):
        """"""
        ori =self .original .action 
        if isinstance (ori ,(
        types .ChannelAdminLogEventActionChangeAbout ,
        types .ChannelAdminLogEventActionChangeTitle ,
        types .ChannelAdminLogEventActionChangeUsername ,
        types .ChannelAdminLogEventActionChangeLocation ,
        types .ChannelAdminLogEventActionChangeHistoryTTL ,
        )):
            return ori .prev_value 
        elif isinstance (ori ,types .ChannelAdminLogEventActionChangePhoto ):
            return ori .prev_photo 
        elif isinstance (ori ,types .ChannelAdminLogEventActionChangeStickerSet ):
            return ori .prev_stickerset 
        elif isinstance (ori ,types .ChannelAdminLogEventActionEditMessage ):
            return ori .prev_message 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionParticipantToggleAdmin ,
        types .ChannelAdminLogEventActionParticipantToggleBan 
        )):
            return ori .prev_participant 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionToggleInvites ,
        types .ChannelAdminLogEventActionTogglePreHistoryHidden ,
        types .ChannelAdminLogEventActionToggleSignatures 
        )):
            return not ori .new_value 
        elif isinstance (ori ,types .ChannelAdminLogEventActionDeleteMessage ):
            return ori .message 
        elif isinstance (ori ,types .ChannelAdminLogEventActionDefaultBannedRights ):
            return ori .prev_banned_rights 
        elif isinstance (ori ,types .ChannelAdminLogEventActionDiscardGroupCall ):
            return ori .call 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionExportedInviteDelete ,
        types .ChannelAdminLogEventActionExportedInviteRevoke ,
        types .ChannelAdminLogEventActionParticipantJoinByInvite ,
        )):
            return ori .invite 
        elif isinstance (ori ,types .ChannelAdminLogEventActionExportedInviteEdit ):
            return ori .prev_invite 

    @property 
    def new (self ):
        """"""
        ori =self .original .action 
        if isinstance (ori ,(
        types .ChannelAdminLogEventActionChangeAbout ,
        types .ChannelAdminLogEventActionChangeTitle ,
        types .ChannelAdminLogEventActionChangeUsername ,
        types .ChannelAdminLogEventActionToggleInvites ,
        types .ChannelAdminLogEventActionTogglePreHistoryHidden ,
        types .ChannelAdminLogEventActionToggleSignatures ,
        types .ChannelAdminLogEventActionChangeLocation ,
        types .ChannelAdminLogEventActionChangeHistoryTTL ,
        )):
            return ori .new_value 
        elif isinstance (ori ,types .ChannelAdminLogEventActionChangePhoto ):
            return ori .new_photo 
        elif isinstance (ori ,types .ChannelAdminLogEventActionChangeStickerSet ):
            return ori .new_stickerset 
        elif isinstance (ori ,types .ChannelAdminLogEventActionEditMessage ):
            return ori .new_message 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionParticipantToggleAdmin ,
        types .ChannelAdminLogEventActionParticipantToggleBan 
        )):
            return ori .new_participant 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionParticipantInvite ,
        types .ChannelAdminLogEventActionParticipantVolume ,
        )):
            return ori .participant 
        elif isinstance (ori ,types .ChannelAdminLogEventActionDefaultBannedRights ):
            return ori .new_banned_rights 
        elif isinstance (ori ,types .ChannelAdminLogEventActionStopPoll ):
            return ori .message 
        elif isinstance (ori ,types .ChannelAdminLogEventActionStartGroupCall ):
            return ori .call 
        elif isinstance (ori ,(
        types .ChannelAdminLogEventActionParticipantMute ,
        types .ChannelAdminLogEventActionParticipantUnmute ,
        )):
            return ori .participant 
        elif isinstance (ori ,types .ChannelAdminLogEventActionToggleGroupCallSetting ):
            return ori .join_muted 
        elif isinstance (ori ,types .ChannelAdminLogEventActionExportedInviteEdit ):
            return ori .new_invite 

    @property 
    def changed_about (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeAbout )

    @property 
    def changed_title (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeTitle )

    @property 
    def changed_username (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeUsername )

    @property 
    def changed_photo (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangePhoto )

    @property 
    def changed_sticker_set (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeStickerSet )

    @property 
    def changed_message (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionEditMessage )

    @property 
    def deleted_message (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionDeleteMessage )

    @property 
    def changed_admin (self ):
        """"""
        return isinstance (
        self .original .action ,
        types .ChannelAdminLogEventActionParticipantToggleAdmin )

    @property 
    def changed_restrictions (self ):
        """"""
        return isinstance (
        self .original .action ,
        types .ChannelAdminLogEventActionParticipantToggleBan )

    @property 
    def changed_invites (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionToggleInvites )

    @property 
    def changed_location (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeLocation )

    @property 
    def joined (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantJoin )

    @property 
    def joined_invite (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantInvite )

    @property 
    def left (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantLeave )

    @property 
    def changed_hide_history (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionTogglePreHistoryHidden )

    @property 
    def changed_signatures (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionToggleSignatures )

    @property 
    def changed_pin (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionUpdatePinned )

    @property 
    def changed_default_banned_rights (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionDefaultBannedRights )

    @property 
    def stopped_poll (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionStopPoll )

    @property 
    def started_group_call (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionStartGroupCall )

    @property 
    def discarded_group_call (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionDiscardGroupCall )

    @property 
    def user_muted (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantMute )

    @property 
    def user_unmutted (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantUnmute )

    @property 
    def changed_call_settings (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionToggleGroupCallSetting )

    @property 
    def changed_history_ttl (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionChangeHistoryTTL )

    @property 
    def deleted_exported_invite (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionExportedInviteDelete )

    @property 
    def edited_exported_invite (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionExportedInviteEdit )

    @property 
    def revoked_exported_invite (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionExportedInviteRevoke )

    @property 
    def joined_by_invite (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantJoinByInvite )

    @property 
    def changed_user_volume (self ):
        """"""
        return isinstance (self .original .action ,
        types .ChannelAdminLogEventActionParticipantVolume )

    def __str__ (self ):
        return str (self .original )

    def stringify (self ):
        return self .original .stringify ()
