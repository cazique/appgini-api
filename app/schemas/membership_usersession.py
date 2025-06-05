from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_user import MembershipUser


from pydantic import BaseModel
from typing import Optional


class MembershipUsersessionBase(BaseModel):
    memberID: str
    token: str
    agent: str
    expiry_ts: int


class MembershipUsersessionCreate(MembershipUsersessionBase):
    expiry_ts: int


class MembershipUsersessionUpdate(BaseModel):
    expiry_ts: Optional[int] = None


class MembershipUsersession(MembershipUsersessionBase):
    user: Optional['MembershipUser'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
