from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_group import MembershipGroup


from pydantic import BaseModel
from typing import Optional


class AppginiMessagesGroupPermissionBase(BaseModel):
    groupID: int
    hasAccess: Optional[bool] = None
    allowedRecipientGroupIDs: Optional[str] = None
    canSendGroupMessage: Optional[bool] = None
    canSendGlobalMessage: Optional[bool] = None
    maxRecipients: Optional[int] = None


class AppginiMessagesGroupPermissionCreate(AppginiMessagesGroupPermissionBase):
    hasAccess: Optional[bool] = None
    allowedRecipientGroupIDs: Optional[str] = None
    canSendGroupMessage: Optional[bool] = None
    canSendGlobalMessage: Optional[bool] = None
    maxRecipients: Optional[int] = None


class AppginiMessagesGroupPermissionUpdate(BaseModel):
    hasAccess: Optional[bool] = None
    allowedRecipientGroupIDs: Optional[str] = None
    canSendGroupMessage: Optional[bool] = None
    canSendGlobalMessage: Optional[bool] = None
    maxRecipients: Optional[int] = None


class AppginiMessagesGroupPermission(AppginiMessagesGroupPermissionBase):
    group: Optional['MembershipGroup'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
