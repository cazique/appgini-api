from sqlalchemy import Column, String, Text
from .database import Base

class AppginiMessagesSetting(Base):
    __tablename__ = "appgini_messages_settings"

    key = Column(String(100), primary_key=True)
    value = Column(Text)

    def __repr__(self):
        return f"<AppginiMessagesSetting key='{getattr(self, 'key', 'N/A')}' value='{getattr(self, 'value', 'N/A')[:50]}...'>"
