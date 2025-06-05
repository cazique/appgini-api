from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .membership_group import MembershipGroup # Corrected: singular

class AppginiMessagesGroupPermission(Base):
    __tablename__ = "appgini_messages_group_permissions"

    groupID = Column(Integer, ForeignKey('membership_groups.groupID'), primary_key=True)
    hasAccess = Column(Boolean, nullable=False, default=False) # DDL default 0
    allowedRecipientGroupIDs = Column(Text)
    canSendGroupMessage = Column(Boolean, nullable=False, default=False) # DDL default 0
    canSendGlobalMessage = Column(Boolean, nullable=False, default=False) # DDL default 0
    maxRecipients = Column(Integer, default=1) # DDL default 1

    # Relationships
    group = relationship("MembershipGroup", back_populates="message_group_permission")

    def __repr__(self):
        return f"<AppginiMessagesGroupPermission groupID={getattr(self, 'groupID', 'N/A')}>"
