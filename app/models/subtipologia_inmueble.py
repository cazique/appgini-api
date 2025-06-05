from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tipologia_inmueble import TipologiaInmueble
    from .inmueble import Inmueble

class SubtipologiaInmueble(Base):
    __tablename__ = "subtipologias_inmueble"

    subtipologia_id = Column(Integer, primary_key=True, autoincrement=True)
    tipologia_id = Column(Integer, ForeignKey('tipologias_inmueble.tipologia_id'), nullable=False, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))

    # Relationships
    tipologia = relationship("TipologiaInmueble", back_populates="subtipologias")
    inmuebles = relationship("Inmueble", back_populates="subtipologia")

    def __repr__(self):
        return f"<SubtipologiaInmueble subtipologia_id={getattr(self, 'subtipologia_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
