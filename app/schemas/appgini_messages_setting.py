from pydantic import BaseModel
from typing import Optional


from pydantic import BaseModel
from typing import Optional


class AppginiMessagesSettingBase(BaseModel):
    key: str
    value: Optional[str] = None


class AppginiMessagesSettingCreate(AppginiMessagesSettingBase):
    value: Optional[str] = None


class AppginiMessagesSettingUpdate(BaseModel):
    value: Optional[str] = None


class AppginiMessagesSetting(AppginiMessagesSettingBase):
    class Config:
        from_attributes = True  # Pydantic V2 setting
