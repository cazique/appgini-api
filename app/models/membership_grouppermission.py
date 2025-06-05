from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_group import MembershipGroup

class MembershipGrouppermission(Base):
    __tablename__ = "membership_grouppermissions"

    permissionID = Column(Integer, primary_key=True, autoincrement=True)
    # DDL: groupID int(10) UNSIGNED DEFAULT NULL
    # Making it nullable=True based on DDL, though FKs to PKs are usually not nullable.
    # This implies groupID might not always be set, or 0 might be used for 'no group' if it were not for NULL.
    groupID = Column(Integer, ForeignKey('membership_groups.groupID'), index=True, nullable=True)
    tableName = Column(String(100))
    allowInsert = Column(Boolean, nullable=False, default=False) # DDL default 0
    allowView = Column(Boolean, nullable=False, default=False)   # DDL default 0 (view levels often 0-3)
    allowEdit = Column(Boolean, nullable=False, default=False)   # DDL default 0
    allowDelete = Column(Boolean, nullable=False, default=False) # DDL default 0

    # Relationships
    group = relationship("MembershipGroup", back_populates="permissions")

    def __repr__(self):
        return f"<MembershipGrouppermission permissionID={getattr(self, 'permissionID', 'N/A')} groupID='{getattr(self, 'groupID', 'N/A')}' table='{getattr(self, 'tableName', 'N/A')}'>"
