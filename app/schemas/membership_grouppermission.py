from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_group import MembershipGroup


from pydantic import BaseModel
from typing import Optional


class MembershipGrouppermissionBase(BaseModel):
    permissionID: int
    groupID: Optional[int] = None
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipGrouppermissionCreate(MembershipGrouppermissionBase):
    groupID: Optional[int] = None
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipGrouppermissionUpdate(BaseModel):
    groupID: Optional[int] = None
    tableName: Optional[str] = None
    allowInsert: Optional[bool] = None
    allowView: Optional[bool] = None
    allowEdit: Optional[bool] = None
    allowDelete: Optional[bool] = None


class MembershipGrouppermission(MembershipGrouppermissionBase):
    group: Optional['MembershipGroup'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
