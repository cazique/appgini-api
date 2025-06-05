from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .zona import Zona

class Subzona(Base):
    __tablename__ = "subzonas"

    subzona_id = Column(Integer, primary_key=True, autoincrement=True)
    zona_id = Column(Integer, ForeignKey('zonas.zona_id'), nullable=False, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))

    # Relationships
    zona = relationship("Zona", back_populates="subzonas")

    def __repr__(self):
        return f"<Subzona subzona_id={getattr(self, 'subzona_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
