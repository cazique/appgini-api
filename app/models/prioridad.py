from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actividad import Actividad

class Prioridad(Base):
    __tablename__ = "prioridades"

    prioridad_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    orden = Column(Integer, default=0)
    color = Column(String(7), default='#000000')

    # Relationships
    actividades = relationship("Actividad", back_populates="prioridad")

    def __repr__(self):
        return f"<Prioridad prioridad_id={getattr(self, 'prioridad_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
