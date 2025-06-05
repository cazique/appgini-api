from sqlalchemy import Column, String, Text, Integer # Integer for request_ts
from .database import Base

class MembershipCacheEntry(Base):
    __tablename__ = "membership_cache"

    request = Column(String(100), primary_key=True)
    request_ts = Column(Integer)
    response = Column(Text)

    def __repr__(self):
        return f"<MembershipCacheEntry request='{getattr(self, 'request', 'N/A')}'>"
