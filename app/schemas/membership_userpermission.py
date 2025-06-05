from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_user import MembershipUser


from pydantic import BaseModel
from typing import Optional


class MembershipUserpermissionBase(BaseModel):
    permissionID: int
    memberID: str
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipUserpermissionCreate(MembershipUserpermissionBase):
    memberID: str
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipUserpermissionUpdate(BaseModel):
    memberID: Optional[str] = None
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipUserpermission(MembershipUserpermissionBase):
    user: Optional['MembershipUser'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
