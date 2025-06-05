from datetime import date
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .appgini_csv_import_job import AppginiCsvImportJob
    from .membership_group import MembershipGroup
    from .membership_userpermission import MembershipUserpermission
    from .membership_userrecord import MembershipUserrecord


from datetime import date
from pydantic import BaseModel
from typing import List
from typing import Optional


class MembershipUserBase(BaseModel):
    memberID: str
    passMD5: Optional[str] = None
    email: Optional[str] = None
    signupDate: Optional[date] = None
    groupID: Optional[int] = None
    isBanned: Optional[bool] = None
    isApproved: Optional[bool] = None
    custom1: Optional[str] = None
    custom2: Optional[str] = None
    custom3: Optional[str] = None
    custom4: Optional[str] = None
    comments: Optional[str] = None
    pass_reset_key: Optional[str] = None
    pass_reset_expiry: Optional[int] = None
    flags: Optional[str] = None
    allowCSVImport: Optional[bool] = None
    data: Optional[str] = None


class MembershipUserCreate(MembershipUserBase):
    passMD5: Optional[str] = None
    email: Optional[str] = None
    signupDate: Optional[date] = None
    groupID: Optional[int] = None
    isBanned: Optional[bool] = None
    isApproved: Optional[bool] = None
    custom1: Optional[str] = None
    custom2: Optional[str] = None
    custom3: Optional[str] = None
    custom4: Optional[str] = None
    comments: Optional[str] = None
    pass_reset_key: Optional[str] = None
    pass_reset_expiry: Optional[int] = None
    flags: Optional[str] = None
    allowCSVImport: Optional[bool] = None
    data: Optional[str] = None


class MembershipUserUpdate(BaseModel):
    passMD5: Optional[str] = None
    email: Optional[str] = None
    signupDate: Optional[date] = None
    groupID: Optional[int] = None
    isBanned: Optional[bool] = None
    isApproved: Optional[bool] = None
    custom1: Optional[str] = None
    custom2: Optional[str] = None
    custom3: Optional[str] = None
    custom4: Optional[str] = None
    comments: Optional[str] = None
    pass_reset_key: Optional[str] = None
    pass_reset_expiry: Optional[int] = None
    flags: Optional[str] = None
    allowCSVImport: Optional[bool] = None
    data: Optional[str] = None


class MembershipUser(MembershipUserBase):
    group: Optional['MembershipGroup'] = None
    user_permissions: Optional[List['MembershipUserpermission']] = None
    user_records: Optional[List['MembershipUserrecord']] = None
    csv_import_jobs: Optional[List['AppginiCsvImportJob']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
