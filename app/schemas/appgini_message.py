from datetime import datetime
from pydantic import BaseModel
from typing import Optional


from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AppginiMessageBase(BaseModel):
    id: int
    originalId: Optional[int] = None
    createdTS: int
    draft: Optional[bool] = None
    sentTS: Optional[int] = None
    seenTS: Optional[int] = None
    inReplyTo: Optional[int] = None
    sender: str
    owner: Optional[str] = None
    recipients: Optional[str] = None
    subject: str
    message: Optional[str] = None
    markedUnread: Optional[bool] = None
    starred: Optional[bool] = None
    updateDT: Optional[datetime] = None


class AppginiMessageCreate(AppginiMessageBase):
    originalId: Optional[int] = None
    createdTS: int
    draft: Optional[bool] = None
    sentTS: Optional[int] = None
    seenTS: Optional[int] = None
    inReplyTo: Optional[int] = None
    sender: str
    owner: Optional[str] = None
    recipients: Optional[str] = None
    subject: str
    message: Optional[str] = None
    markedUnread: Optional[bool] = None
    starred: Optional[bool] = None
    updateDT: Optional[datetime] = None


class AppginiMessageUpdate(BaseModel):
    originalId: Optional[int] = None
    createdTS: Optional[int] = None
    draft: Optional[bool] = None
    sentTS: Optional[int] = None
    seenTS: Optional[int] = None
    inReplyTo: Optional[int] = None
    sender: Optional[str] = None
    owner: Optional[str] = None
    recipients: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    markedUnread: Optional[bool] = None
    starred: Optional[bool] = None
    updateDT: Optional[datetime] = None


class AppginiMessage(AppginiMessageBase):
    class Config:
        from_attributes = True  # Pydantic V2 setting
