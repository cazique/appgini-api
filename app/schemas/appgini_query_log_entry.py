from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_user import MembershipUser


from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class AppginiQueryLogEntryBase(BaseModel):
    id: int
    datetime: Optional[datetime] = None
    statement: Optional[str] = None
    duration: Optional[Decimal] = None
    error: Optional[str] = None
    memberID: Optional[str] = None
    uri: Optional[str] = None


class AppginiQueryLogEntryCreate(AppginiQueryLogEntryBase):
    datetime: Optional[datetime] = None
    statement: Optional[str] = None
    duration: Optional[Decimal] = None
    error: Optional[str] = None
    memberID: Optional[str] = None
    uri: Optional[str] = None


class AppginiQueryLogEntryUpdate(BaseModel):
    datetime: Optional[datetime] = None
    statement: Optional[str] = None
    duration: Optional[Decimal] = None
    error: Optional[str] = None
    memberID: Optional[str] = None
    uri: Optional[str] = None


class AppginiQueryLogEntry(AppginiQueryLogEntryBase):
    user: Optional['MembershipUser'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
