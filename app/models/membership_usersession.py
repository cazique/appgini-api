from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser

class MembershipUsersession(Base):
    __tablename__ = "membership_usersessions"

    # Composite primary key based on DDL's UNIQUE KEY
    memberID = Column(String(100), ForeignKey('membership_users.memberID'), primary_key=True)
    token = Column(String(100), primary_key=True)
    agent = Column(String(100), primary_key=True)

    expiry_ts = Column(Integer, nullable=False, index=True) # DDL: int(10) UNSIGNED (timestamp)

    # Relationship
    # The DDL for membership_users doesn't have a `sessions` backref by default from AppGini.
    # If added to MembershipUser: sessions = relationship("MembershipUsersession", back_populates="user")
    user = relationship("MembershipUser") # Many sessions can belong to one user.

    def __repr__(self):
        return f"<MembershipUsersession memberID='{getattr(self, 'memberID', 'N/A')}' token='{getattr(self, 'token', 'N/A')}'>"
