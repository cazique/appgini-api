from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .membership_user import MembershipUser


from pydantic import BaseModel
from typing import Optional


class AppginiCsvImportJobBase(BaseModel):
    id: str
    memberID: str
    config: Optional[str] = None
    insert_ts: Optional[int] = None
    last_update_ts: Optional[int] = None
    total: Optional[int] = None
    done: Optional[int] = None


class AppginiCsvImportJobCreate(AppginiCsvImportJobBase):
    memberID: str
    config: Optional[str] = None
    insert_ts: Optional[int] = None
    last_update_ts: Optional[int] = None
    total: Optional[int] = None
    done: Optional[int] = None


class AppginiCsvImportJobUpdate(BaseModel):
    memberID: Optional[str] = None
    config: Optional[str] = None
    insert_ts: Optional[int] = None
    last_update_ts: Optional[int] = None
    total: Optional[int] = None
    done: Optional[int] = None


class AppginiCsvImportJob(AppginiCsvImportJobBase):
    user: Optional['MembershipUser'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
