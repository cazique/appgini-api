from sqlalchemy import Column, Integer, String, ForeignKey # DDL has BIGINT for recID, dateAdded, dateUpdated
# from sqlalchemy.dialects.mysql import BIGINT # If specific BIGINT is needed
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser
    from .membership_group import MembershipGroup

class MembershipUserrecord(Base):
    __tablename__ = "membership_userrecords"

    recID = Column(Integer, primary_key=True, autoincrement=True) # DDL: BIGINT UNSIGNED. Using Integer for now.
    tableName = Column(String(100), index=True)
    pkValue = Column(String(255), index=True)
    memberID = Column(String(100), ForeignKey('membership_users.memberID'), index=True)
    dateAdded = Column(Integer) # DDL: BIGINT UNSIGNED (timestamp)
    dateUpdated = Column(Integer) # DDL: BIGINT UNSIGNED (timestamp)
    groupID = Column(Integer, ForeignKey('membership_groups.groupID'), index=True)

    # Relationships
    user = relationship("MembershipUser", back_populates="user_records")
    group_details = relationship("MembershipGroup", back_populates="user_records_via_group")

    def __repr__(self):
        return f"<MembershipUserrecord recID={getattr(self, 'recID', 'N/A')} table='{getattr(self, 'tableName', 'N/A')}' pkValue='{getattr(self, 'pkValue', 'N/A')}'>"
