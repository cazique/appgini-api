from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser

class AppginiQueryLogEntry(Base):
    __tablename__ = "appgini_query_log"

    # Added dummy PK because DDL does not specify one.
    id = Column(Integer, primary_key=True, autoincrement=True)

    datetime = Column(DateTime, nullable=False, server_default=func.now())
    statement = Column(Text)
    duration = Column(Numeric(10, 2), default=0.00)
    error = Column(Text)
    memberID = Column(String(200), ForeignKey('membership_users.memberID'), index=True, nullable=True)
    uri = Column(String(200))

    # Relationship
    # Assuming memberID in this log table refers to the main user identifier in membership_users
    user = relationship("MembershipUser") # No back_populates needed if MembershipUser doesn't list query logs

    def __repr__(self):
        return f"<AppginiQueryLogEntry id={getattr(self, 'id', 'N/A')} memberID='{getattr(self, 'memberID', 'N/A')}'>"
