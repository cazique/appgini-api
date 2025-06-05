from pydantic import BaseModel
from typing import Optional


from pydantic import BaseModel
from typing import Optional


class MembershipCacheEntryBase(BaseModel):
    request: str
    request_ts: Optional[int] = None
    response: Optional[str] = None


class MembershipCacheEntryCreate(MembershipCacheEntryBase):
    request_ts: Optional[int] = None
    response: Optional[str] = None


class MembershipCacheEntryUpdate(BaseModel):
    request_ts: Optional[int] = None
    response: Optional[str] = None


class MembershipCacheEntry(MembershipCacheEntryBase):
    class Config:
        from_attributes = True  # Pydantic V2 setting
