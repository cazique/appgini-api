from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subzona import Subzona
    from .inmueble import Inmueble

class Zona(Base):
    __tablename__ = "zonas"

    zona_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    localidad = Column(String(50), nullable=False)
    provincia = Column(String(50), nullable=False)
    descripcion = Column(String(200))

    # Relationships
    subzonas = relationship("Subzona", back_populates="zona", cascade="all, delete-orphan")
    inmuebles = relationship("Inmueble", back_populates="zona")

    def __repr__(self):
        return f"<Zona zona_id={getattr(self, 'zona_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
