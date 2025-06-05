from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser
    from .membership_grouppermission import MembershipGrouppermission
    from .membership_userrecord import MembershipUserrecord
    from .appgini_messages_group_permission import AppginiMessagesGroupPermission

class MembershipGroup(Base):
    __tablename__ = "membership_groups"

    groupID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    allowSignup = Column(Boolean, default=False) # DDL default NULL, but usually 0 or 1
    needsApproval = Column(Boolean, default=False) # DDL default NULL
    allowCSVImport = Column(Boolean, nullable=False, default=False) # DDL default 0

    # Relationships
    users = relationship("MembershipUser", back_populates="group")
    permissions = relationship("MembershipGrouppermission", back_populates="group", cascade="all, delete-orphan")
    user_records_via_group = relationship("MembershipUserrecord", back_populates="group_details", cascade="all, delete-orphan")
    message_group_permission = relationship("AppginiMessagesGroupPermission", uselist=False, back_populates="group")

    def __repr__(self):
        return f"<MembershipGroup groupID={getattr(self, 'groupID', 'N/A')} name='{getattr(self, 'name', 'N/A')}'>"
