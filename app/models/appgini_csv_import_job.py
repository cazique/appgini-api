from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .membership_user import MembershipUser

class AppginiCsvImportJob(Base):
    __tablename__ = "appgini_csv_import_jobs"

    id = Column(String(40), primary_key=True)
    memberID = Column(String(100), ForeignKey('membership_users.memberID'), nullable=False, index=True)
    config = Column(Text)
    insert_ts = Column(Integer)
    last_update_ts = Column(Integer)
    total = Column(Integer, default=99999999) # DDL has '99999999'
    done = Column(Integer, default=0) # DDL has '0'

    # Relationships
    user = relationship("MembershipUser", back_populates="csv_import_jobs")

    def __repr__(self):
        return f"<AppginiCsvImportJob id='{getattr(self, 'id', 'N/A')}' memberID='{getattr(self, 'memberID', 'N/A')}'>"
