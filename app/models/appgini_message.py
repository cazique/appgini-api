from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, func # Added BigInteger potentially
# from sqlalchemy.dialects.mysql import BIGINT # If BigInteger is needed and mapped for other DBs
from sqlalchemy.orm import relationship
from .database import Base
# from .membership_users import MembershipUser # For sender/owner relationships

class AppginiMessage(Base):
    __tablename__ = "appgini_messages"

    # DDL: id bigint(20) unsigned - Using Integer, consider BigInteger if necessary
    id = Column(Integer, primary_key=True, autoincrement=True)
    originalId = Column(Integer) # DDL: bigint(20) UNSIGNED
    createdTS = Column(Integer, nullable=False) # DDL: int(10) UNSIGNED
    draft = Column(Boolean, nullable=False, default=True)
    sentTS = Column(Integer) # DDL: int(10) UNSIGNED
    seenTS = Column(Integer) # DDL: int(10) UNSIGNED
    inReplyTo = Column(Integer) # DDL: bigint(20) UNSIGNED
    sender = Column(String(200), nullable=False) # Potential FK to MembershipUser.memberID
    owner = Column(String(200)) # Potential FK to MembershipUser.memberID
    recipients = Column(Text)
    subject = Column(String(100), nullable=False)
    message = Column(Text)
    markedUnread = Column(Boolean, nullable=False, default=True)
    starred = Column(Boolean, nullable=False, default=False)
    updateDT = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    # Potential relationships (if sender/owner are mapped to MembershipUser)
    # sender_user = relationship("MembershipUser", foreign_keys=[sender], primaryjoin="AppginiMessage.sender == MembershipUser.memberID", backref="sent_messages")
    # owner_user = relationship("MembershipUser", foreign_keys=[owner], primaryjoin="AppginiMessage.owner == MembershipUser.memberID", backref="owned_messages")

    # Self-referential relationships for threads
    # original_message = relationship("AppginiMessage", remote_side=[id], foreign_keys=[originalId], backref="thread_replies")
    # reply_to_message = relationship("AppginiMessage", remote_side=[id], foreign_keys=[inReplyTo], backref="message_replies")


    def __repr__(self):
        return f"<AppginiMessage id={getattr(self, 'id', 'N/A')} subject='{getattr(self, 'subject', 'N/A')}'>"
