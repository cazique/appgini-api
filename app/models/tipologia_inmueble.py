from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subtipologia_inmueble import SubtipologiaInmueble
    from .inmueble import Inmueble

class TipologiaInmueble(Base):
    __tablename__ = "tipologias_inmueble"

    tipologia_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))

    # Relationships
    subtipologias = relationship("SubtipologiaInmueble", back_populates="tipologia", cascade="all, delete-orphan")
    inmuebles = relationship("Inmueble", back_populates="tipologia")

    def __repr__(self):
        return f"<TipologiaInmueble tipologia_id={getattr(self, 'tipologia_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
