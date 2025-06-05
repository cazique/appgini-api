from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_group import MembershipGroup
    from .membership_user import MembershipUser


from pydantic import BaseModel
from typing import Optional


class MembershipUserrecordBase(BaseModel):
    recID: int
    tableName: Optional[str] = None
    pkValue: Optional[str] = None
    memberID: Optional[str] = None
    dateAdded: Optional[int] = None
    dateUpdated: Optional[int] = None
    groupID: Optional[int] = None


class MembershipUserrecordCreate(MembershipUserrecordBase):
    tableName: Optional[str] = None
    pkValue: Optional[str] = None
    memberID: Optional[str] = None
    dateAdded: Optional[int] = None
    dateUpdated: Optional[int] = None
    groupID: Optional[int] = None


class MembershipUserrecordUpdate(BaseModel):
    tableName: Optional[str] = None
    pkValue: Optional[str] = None
    memberID: Optional[str] = None
    dateAdded: Optional[int] = None
    dateUpdated: Optional[int] = None
    groupID: Optional[int] = None


class MembershipUserrecord(MembershipUserrecordBase):
    user: Optional['MembershipUser'] = None
    group_details: Optional['MembershipGroup'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
