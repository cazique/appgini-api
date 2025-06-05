from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_group import MembershipGroup
    from .membership_userpermission import MembershipUserpermission
    from .membership_userrecord import MembershipUserrecord
    from .appgini_csv_import_job import AppginiCsvImportJob
    # from .appgini_query_log_entry import AppginiQueryLogEntry
    # from .membership_usersession import MembershipUsersession

class MembershipUser(Base):
    __tablename__ = "membership_users"

    memberID = Column(String(100), primary_key=True)
    passMD5 = Column(String(255))
    email = Column(String(100), unique=True, index=True) # Added index
    signupDate = Column(Date)
    groupID = Column(Integer, ForeignKey('membership_groups.groupID'), index=True)
    isBanned = Column(Boolean, default=False) # DDL: tinyint(4)
    isApproved = Column(Boolean, default=True) # DDL: tinyint(4)
    custom1 = Column(Text)
    custom2 = Column(Text)
    custom3 = Column(Text)
    custom4 = Column(Text)
    comments = Column(Text)
    pass_reset_key = Column(String(100))
    pass_reset_expiry = Column(Integer) # DDL: int(10) UNSIGNED (timestamp)
    flags = Column(Text)
    allowCSVImport = Column(Boolean, nullable=False, default=False) # DDL: tinyint(4)
    data = Column(Text) # DDL: longtext

    # Relationships
    group = relationship("MembershipGroup", back_populates="users")
    user_permissions = relationship("MembershipUserpermission", back_populates="user", cascade="all, delete-orphan")
    user_records = relationship("MembershipUserrecord", back_populates="user", cascade="all, delete-orphan")
    csv_import_jobs = relationship("AppginiCsvImportJob", back_populates="user", cascade="all, delete-orphan")

    # Relationships to AppginiQueryLogEntry and MembershipUsersession are not typically needed on the User side,
    # but can be added if required for specific query patterns.
    # query_log_entries = relationship("AppginiQueryLogEntry", back_populates="user")
    # sessions = relationship("MembershipUsersession", back_populates="user")


    def __repr__(self):
        return f"<MembershipUser memberID='{getattr(self, 'memberID', 'N/A')}' email='{getattr(self, 'email', 'N/A')}'>"
