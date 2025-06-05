from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actividad import Actividad

class TipoActividad(Base):
    __tablename__ = "tipos_actividad"

    tipo_actividad_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    requiere_resultado = Column(Boolean, default=False)

    # Relationships
    actividades = relationship("Actividad", back_populates="tipo_actividad")

    def __repr__(self):
        return f"<TipoActividad tipo_actividad_id={getattr(self, 'tipo_actividad_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
