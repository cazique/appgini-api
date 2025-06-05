from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .appgini_messages_group_permission import AppginiMessagesGroupPermission
    from .membership_grouppermission import MembershipGrouppermission
    from .membership_user import MembershipUser
    from .membership_userrecord import MembershipUserrecord


from pydantic import BaseModel
from typing import List
from typing import Optional


class MembershipGroupBase(BaseModel):
    groupID: int
    name: str
    description: Optional[str] = None
    allowSignup: Optional[bool] = None
    needsApproval: Optional[bool] = None
    allowCSVImport: Optional[bool] = None


class MembershipGroupCreate(MembershipGroupBase):
    name: str
    description: Optional[str] = None
    allowSignup: Optional[bool] = None
    needsApproval: Optional[bool] = None
    allowCSVImport: Optional[bool] = None


class MembershipGroupUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    allowSignup: Optional[bool] = None
    needsApproval: Optional[bool] = None
    allowCSVImport: Optional[bool] = None


class MembershipGroup(MembershipGroupBase):
    users: Optional[List['MembershipUser']] = None
    permissions: Optional[List['MembershipGrouppermission']] = None
    user_records_via_group: Optional[List['MembershipUserrecord']] = None
    message_group_permission: Optional['AppginiMessagesGroupPermission'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
