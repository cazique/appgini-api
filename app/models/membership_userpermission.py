from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser

class MembershipUserpermission(Base):
    __tablename__ = "membership_userpermissions"

    permissionID = Column(Integer, primary_key=True, autoincrement=True)
    memberID = Column(String(100), ForeignKey('membership_users.memberID'), nullable=False, index=True)
    tableName = Column(String(100))
    allowInsert = Column(Boolean, nullable=False, default=False) # DDL default 0
    allowView = Column(Boolean, nullable=False, default=False)   # DDL default 0 - AppGini uses 0,1,2,3 for view levels (None, Own, Group, All)
                                                                # For a boolean, this would mean "has some view access" vs "no view access".
                                                                # If granular levels are needed, this should be Integer. For now, keeping Boolean.
    allowEdit = Column(Boolean, nullable=False, default=False)   # DDL default 0
    allowDelete = Column(Boolean, nullable=False, default=False) # DDL default 0

    # Relationships
    user = relationship("MembershipUser", back_populates="user_permissions")

    def __repr__(self):
        return f"<MembershipUserpermission permissionID={getattr(self, 'permissionID', 'N/A')} memberID='{getattr(self, 'memberID', 'N/A')}' table='{getattr(self, 'tableName', 'N/A')}'>"
