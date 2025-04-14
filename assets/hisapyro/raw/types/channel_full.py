from io import BytesIO
from hisapyro.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hisapyro.raw.core import TLObject
from hisapyro import raw
from typing import List, Optional, Any
class ChannelFull(TLObject):  
    __slots__: List[str] = ["id", "about", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "chat_photo", "notify_settings", "bot_info", "pts", "can_view_participants", "can_set_username", "can_set_stickers", "hidden_prehistory", "can_set_location", "has_scheduled", "can_view_stats", "blocked", "can_delete_channel", "antispam", "participants_hidden", "translations_disabled", "participants_count", "admins_count", "kicked_count", "banned_count", "online_count", "exported_invite", "migrated_from_chat_id", "migrated_from_max_id", "pinned_msg_id", "stickerset", "available_min_id", "folder_id", "linked_chat_id", "location", "slowmode_seconds", "slowmode_next_send_date", "stats_dc", "call", "ttl_period", "pending_suggestions", "groupcall_default_join_as", "theme_emoticon", "requests_pending", "recent_requesters", "default_send_as", "available_reactions"]
    ID = 0xf2355507
    QUALNAME = "types.ChannelFull"
    def __init__(self, *, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, chat_photo: "raw.base.Photo", notify_settings: "raw.base.PeerNotifySettings", bot_info: List["raw.base.BotInfo"], pts: int, can_view_participants: Optional[bool] = None, can_set_username: Optional[bool] = None, can_set_stickers: Optional[bool] = None, hidden_prehistory: Optional[bool] = None, can_set_location: Optional[bool] = None, has_scheduled: Optional[bool] = None, can_view_stats: Optional[bool] = None, blocked: Optional[bool] = None, can_delete_channel: Optional[bool] = None, antispam: Optional[bool] = None, participants_hidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, participants_count: Optional[int] = None, admins_count: Optional[int] = None, kicked_count: Optional[int] = None, banned_count: Optional[int] = None, online_count: Optional[int] = None, exported_invite: "raw.base.ExportedChatInvite" = None, migrated_from_chat_id: Optional[int] = None, migrated_from_max_id: Optional[int] = None, pinned_msg_id: Optional[int] = None, stickerset: "raw.base.StickerSet" = None, available_min_id: Optional[int] = None, folder_id: Optional[int] = None, linked_chat_id: Optional[int] = None, location: "raw.base.ChannelLocation" = None, slowmode_seconds: Optional[int] = None, slowmode_next_send_date: Optional[int] = None, stats_dc: Optional[int] = None, call: "raw.base.InputGroupCall" = None, ttl_period: Optional[int] = None, pending_suggestions: Optional[List[str]] = None, groupcall_default_join_as: "raw.base.Peer" = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, default_send_as: "raw.base.Peer" = None, available_reactions: "raw.base.ChatReactions" = None) -> None:
        self.id = id  
        self.about = about  
        self.read_inbox_max_id = read_inbox_max_id  
        self.read_outbox_max_id = read_outbox_max_id  
        self.unread_count = unread_count  
        self.chat_photo = chat_photo  
        self.notify_settings = notify_settings  
        self.bot_info = bot_info  
        self.pts = pts  
        self.can_view_participants = can_view_participants  
        self.can_set_username = can_set_username  
        self.can_set_stickers = can_set_stickers  
        self.hidden_prehistory = hidden_prehistory  
        self.can_set_location = can_set_location  
        self.has_scheduled = has_scheduled  
        self.can_view_stats = can_view_stats  
        self.blocked = blocked  
        self.can_delete_channel = can_delete_channel  
        self.antispam = antispam  
        self.participants_hidden = participants_hidden  
        self.translations_disabled = translations_disabled  
        self.participants_count = participants_count  
        self.admins_count = admins_count  
        self.kicked_count = kicked_count  
        self.banned_count = banned_count  
        self.online_count = online_count  
        self.exported_invite = exported_invite  
        self.migrated_from_chat_id = migrated_from_chat_id  
        self.migrated_from_max_id = migrated_from_max_id  
        self.pinned_msg_id = pinned_msg_id  
        self.stickerset = stickerset  
        self.available_min_id = available_min_id  
        self.folder_id = folder_id  
        self.linked_chat_id = linked_chat_id  
        self.location = location  
        self.slowmode_seconds = slowmode_seconds  
        self.slowmode_next_send_date = slowmode_next_send_date  
        self.stats_dc = stats_dc  
        self.call = call  
        self.ttl_period = ttl_period  
        self.pending_suggestions = pending_suggestions  
        self.groupcall_default_join_as = groupcall_default_join_as  
        self.theme_emoticon = theme_emoticon  
        self.requests_pending = requests_pending  
        self.recent_requesters = recent_requesters  
        self.default_send_as = default_send_as  
        self.available_reactions = available_reactions  
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelFull":
        flags = Int.read(b)
        can_view_participants = True if flags & (1 << 3) else False
        can_set_username = True if flags & (1 << 6) else False
        can_set_stickers = True if flags & (1 << 7) else False
        hidden_prehistory = True if flags & (1 << 10) else False
        can_set_location = True if flags & (1 << 16) else False
        has_scheduled = True if flags & (1 << 19) else False
        can_view_stats = True if flags & (1 << 20) else False
        blocked = True if flags & (1 << 22) else False
        flags2 = Int.read(b)
        can_delete_channel = True if flags2 & (1 << 0) else False
        antispam = True if flags2 & (1 << 1) else False
        participants_hidden = True if flags2 & (1 << 2) else False
        translations_disabled = True if flags2 & (1 << 3) else False
        id = Long.read(b)
        about = String.read(b)
        participants_count = Int.read(b) if flags & (1 << 0) else None
        admins_count = Int.read(b) if flags & (1 << 1) else None
        kicked_count = Int.read(b) if flags & (1 << 2) else None
        banned_count = Int.read(b) if flags & (1 << 2) else None
        online_count = Int.read(b) if flags & (1 << 13) else None
        read_inbox_max_id = Int.read(b)
        read_outbox_max_id = Int.read(b)
        unread_count = Int.read(b)
        chat_photo = TLObject.read(b)
        notify_settings = TLObject.read(b)
        exported_invite = TLObject.read(b) if flags & (1 << 23) else None
        bot_info = TLObject.read(b)
        migrated_from_chat_id = Long.read(b) if flags & (1 << 4) else None
        migrated_from_max_id = Int.read(b) if flags & (1 << 4) else None
        pinned_msg_id = Int.read(b) if flags & (1 << 5) else None
        stickerset = TLObject.read(b) if flags & (1 << 8) else None
        available_min_id = Int.read(b) if flags & (1 << 9) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        linked_chat_id = Long.read(b) if flags & (1 << 14) else None
        location = TLObject.read(b) if flags & (1 << 15) else None
        slowmode_seconds = Int.read(b) if flags & (1 << 17) else None
        slowmode_next_send_date = Int.read(b) if flags & (1 << 18) else None
        stats_dc = Int.read(b) if flags & (1 << 12) else None
        pts = Int.read(b)
        call = TLObject.read(b) if flags & (1 << 21) else None
        ttl_period = Int.read(b) if flags & (1 << 24) else None
        pending_suggestions = TLObject.read(b, String) if flags & (1 << 25) else []
        groupcall_default_join_as = TLObject.read(b) if flags & (1 << 26) else None
        theme_emoticon = String.read(b) if flags & (1 << 27) else None
        requests_pending = Int.read(b) if flags & (1 << 28) else None
        recent_requesters = TLObject.read(b, Long) if flags & (1 << 28) else []
        default_send_as = TLObject.read(b) if flags & (1 << 29) else None
        available_reactions = TLObject.read(b) if flags & (1 << 30) else None
        return ChannelFull(id=id, about=about, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, bot_info=bot_info, pts=pts, can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, exported_invite=exported_invite, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions)
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        flags = 0
        flags |= (1 << 3) if self.can_view_participants else 0
        flags |= (1 << 6) if self.can_set_username else 0
        flags |= (1 << 7) if self.can_set_stickers else 0
        flags |= (1 << 10) if self.hidden_prehistory else 0
        flags |= (1 << 16) if self.can_set_location else 0
        flags |= (1 << 19) if self.has_scheduled else 0
        flags |= (1 << 20) if self.can_view_stats else 0
        flags |= (1 << 22) if self.blocked else 0
        flags |= (1 << 0) if self.participants_count is not None else 0
        flags |= (1 << 1) if self.admins_count is not None else 0
        flags |= (1 << 2) if self.kicked_count is not None else 0
        flags |= (1 << 2) if self.banned_count is not None else 0
        flags |= (1 << 13) if self.online_count is not None else 0
        flags |= (1 << 23) if self.exported_invite is not None else 0
        flags |= (1 << 4) if self.migrated_from_chat_id is not None else 0
        flags |= (1 << 4) if self.migrated_from_max_id is not None else 0
        flags |= (1 << 5) if self.pinned_msg_id is not None else 0
        flags |= (1 << 8) if self.stickerset is not None else 0
        flags |= (1 << 9) if self.available_min_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.linked_chat_id is not None else 0
        flags |= (1 << 15) if self.location is not None else 0
        flags |= (1 << 17) if self.slowmode_seconds is not None else 0
        flags |= (1 << 18) if self.slowmode_next_send_date is not None else 0
        flags |= (1 << 12) if self.stats_dc is not None else 0
        flags |= (1 << 21) if self.call is not None else 0
        flags |= (1 << 24) if self.ttl_period is not None else 0
        flags |= (1 << 25) if self.pending_suggestions else 0
        flags |= (1 << 26) if self.groupcall_default_join_as is not None else 0
        flags |= (1 << 27) if self.theme_emoticon is not None else 0
        flags |= (1 << 28) if self.requests_pending is not None else 0
        flags |= (1 << 28) if self.recent_requesters else 0
        flags |= (1 << 29) if self.default_send_as is not None else 0
        flags |= (1 << 30) if self.available_reactions is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 0) if self.can_delete_channel else 0
        flags2 |= (1 << 1) if self.antispam else 0
        flags2 |= (1 << 2) if self.participants_hidden else 0
        flags2 |= (1 << 3) if self.translations_disabled else 0
        b.write(Int(flags2))
        b.write(Long(self.id))
        b.write(String(self.about))
        if self.participants_count is not None:
            b.write(Int(self.participants_count))
        if self.admins_count is not None:
            b.write(Int(self.admins_count))
        if self.kicked_count is not None:
            b.write(Int(self.kicked_count))
        if self.banned_count is not None:
            b.write(Int(self.banned_count))
        if self.online_count is not None:
            b.write(Int(self.online_count))
        b.write(Int(self.read_inbox_max_id))
        b.write(Int(self.read_outbox_max_id))
        b.write(Int(self.unread_count))
        b.write(self.chat_photo.write())
        b.write(self.notify_settings.write())
        if self.exported_invite is not None:
            b.write(self.exported_invite.write())
        b.write(Vector(self.bot_info))
        if self.migrated_from_chat_id is not None:
            b.write(Long(self.migrated_from_chat_id))
        if self.migrated_from_max_id is not None:
            b.write(Int(self.migrated_from_max_id))
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        if self.stickerset is not None:
            b.write(self.stickerset.write())
        if self.available_min_id is not None:
            b.write(Int(self.available_min_id))
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        if self.linked_chat_id is not None:
            b.write(Long(self.linked_chat_id))
        if self.location is not None:
            b.write(self.location.write())
        if self.slowmode_seconds is not None:
            b.write(Int(self.slowmode_seconds))
        if self.slowmode_next_send_date is not None:
            b.write(Int(self.slowmode_next_send_date))
        if self.stats_dc is not None:
            b.write(Int(self.stats_dc))
        b.write(Int(self.pts))
        if self.call is not None:
            b.write(self.call.write())
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        if self.pending_suggestions is not None:
            b.write(Vector(self.pending_suggestions, String))
        if self.groupcall_default_join_as is not None:
            b.write(self.groupcall_default_join_as.write())
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        if self.requests_pending is not None:
            b.write(Int(self.requests_pending))
        if self.recent_requesters is not None:
            b.write(Vector(self.recent_requesters, Long))
        if self.default_send_as is not None:
            b.write(self.default_send_as.write())
        if self.available_reactions is not None:
            b.write(self.available_reactions.write())
        return b.getvalue()